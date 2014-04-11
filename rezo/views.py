from django.views import generic

from .models import Equipement, Utilisateur

class AccountClaimView(generic.TemplateView):
    template_name = 'rezo/claim_account.html'

    def get_context_data(self, *args, **kwargs):
        cd = super(AccountClaimView, self).get_context_data(*args, **kwargs)

        equip = Equipement.objects.using('rezo').filter(
            ip='10.69.8.127', #self.request.META.get('REMOTE_ADDR'),
        ).exclude(
            utilisateur__etat='STATE_ARCHIVE',
        )

        if len(equip) == 1:
            cd['equipement'] = equip[0]
            cd['utilisateur'] = equip[0].utilisateur

        return cd
        
