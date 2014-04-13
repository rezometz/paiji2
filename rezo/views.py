from django.views import generic
from django.shortcuts import redirect

from django.core.mail import send_mail
from django.core.urlresolvers import reverse

from django.contrib import messages
from django.contrib.auth import get_user_model, login, authenticate

from .models import Equipement, Utilisateur, AccountRecovery
from .forms import ConfirmForm, UserCreationForm, UserAuthenticationForm


import hashlib
import uuid
from datetime import datetime

def create_hash(chain):
    hash = hashlib.sha256()
    hash.update(chain)
    return  hash.hexdigest()

class AccountClaimView(generic.FormView):
    template_name = 'rezo/claim_account.html'
    form_class = ConfirmForm
    
    def __init__(self, *args, **kwargs):
        super(AccountClaimView, self).__init__(*args, **kwargs)
        
        equipements = Equipement.objects.using('rezo').filter(
            ip='10.69.8.127', #self.request.META.get('REMOTE_ADDR'),
        ).exclude(
            utilisateur__etat='STATE_ARCHIVE',
        )

        if len(equipements) == 1:
            self.equipement = equipements[0]
            self.utilisateur = equipements[0].utilisateur
            self.email_verifie = self.utilisateur.email == self.utilisateur.emailverifie
        elif len(equipements) > 1:
            print "Too much matching"
            exit()

    def get_context_data(self, *args, **kwargs):
        cd = super(AccountClaimView, self).get_context_data(*args, **kwargs)

        cd['utilisateur'] = self.utilisateur
        cd['email_verifie'] = self.email_verifie

        return cd

    def form_valid(self, form):
        if not self.email_verifie:
            exit()

        self.uid = uuid.uuid4()
        now = datetime.now()
        self.hash = create_hash(str(self.uid) + str(now))

        AccountRecovery.objects.filter(
            email=self.utilisateur.emailverifie,
        ).delete()
        
        AccountRecovery.objects.create(
            id_rezo=self.utilisateur.pk,
            date=now,
            code=self.hash,
            email=self.utilisateur.emailverifie,
        )

        send_mail(
            '[Paiji2] Recuperation de votre compte', (
            'Veuillez suivre le lien :\n  {url}\n'
            ).format(
                url=self.request.build_absolute_uri(
                    reverse('account-claim-confirm', kwargs={
                        'code': self.hash, 
                        'email': self.utilisateur.emailverifie,
                    })
                ),
            ),
            'paiji@metz.supelec.fr',
            [self.utilisateur.emailverifie, ],
        )

        return super(AccountClaimView, self).form_valid(form)
    def get_success_url(self):
        return reverse('account-claim-confirm', kwargs={
            'code': self.hash,
            'email': self.utilisateur.emailverifie,
        })


class AccountClaimConfirmView(generic.CreateView):
    form_class = UserCreationForm
    model = get_user_model()
    template_name = 'rezo/account_claim_confirm.html'

    def get_form(self, *args, **kwargs):

        try:
            self.account = AccountRecovery.objects.get(
               code=self.kwargs.get('code'),
               email=self.kwargs.get('email'),
            )
        except AccountRecovery.DoesNotExist:
            messages.error(self.request, 'Lien de confirmation invalide')
            return redirect(reverse('claim-account'))
        

        self.utilisateur = Utilisateur.objects.using('rezo').get(
            pk=self.account.id_rezo,
        )

        return super(AccountClaimConfirmView, self).get_form(*args, **kwargs)
    
    def get_context_data(self, *args, **kwargs):
        cd = super(AccountClaimConfirmView, self).get_context_data(*args, **kwargs)

        cd['utilisateur'] = self.utilisateur

        return cd

    def form_valid(self, form):
        #response = 
        self.object = form.save(commit=False)
        
        self.object.first_name = self.utilisateur.prenom
        self.object.last_name = self.utilisateur.nom
        self.object.email = self.utilisateur.emailverifie

        self.object.id_rezo = self.utilisateur.pk

        self.object.save()

        self.account.delete()
        # TODO : assure that id_rezo is unique

        return super(AccountClaimConfirmView, self).form_valid(form)

    def get_success_url(self):
        return reverse('index')


class SignInView(generic.FormView):
    form_class = UserAuthenticationForm
    template_name = 'rezo/sign_in.html'

    def form_valid(self, form):
        login(self.request, form.get_user())

        return super(SignInView, self).form_valid(form)

    def get_success_url(self):
        return reverse('index')