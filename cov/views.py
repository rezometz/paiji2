# -*- coding: utf-8 -*-

from django.views import generic
from django.core.urlresolvers import reverse

from django.utils.translation import ugettext_lazy as _

from django.contrib import messages

from .models import Covoiturage as Cov


class CovListView(generic.ListView):
    model = Cov
    paginate_by = 10
    context_object_name = 'covs'
    template_name='cov/cov_list.html'

    def get_queryset(self):
        return super(CovListView, self).get_queryset().select_related(
            'poster'
        )

    def get_object(self):
        # Call the superclass
        object = super(CovListView, self).get_object()
        # Record the last accessed date
        object.label = labels.get(object.get_annonce_type_display())
        # Return the object
        return object

class CovCreateView(generic.CreateView):
    model = Cov
    fields = ('annonce_type', 'good_until', 'notes')

    def form_valid(self, form):
        cov = form.save(commit=False)
        cov.poster = self.request.user
        cov.save()

        return super(CovCreateView, self).form_valid(form)

    def get_success_url(self):
        messages.success(
            self.request, _(
            'Your request has been saved successfully :P'
        ))
        success_url = self.request.POST.get('next')
        return success_url if success_url != '' else reverse('index')


class CovEditView(generic.UpdateView):
    model = Cov
    fields = ('annonce_type', 'good_until', 'notes')

    def dispatch(self, request, *args, **kwargs):
        """ Making sure that only authors can update Covs """
        obj = self.get_object()
        if obj.poster != self.request.user:
            return redirect(obj)
        return super(CovEditView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        messages.success(
            self.request, _(
            'Your cov has been updated, '
            'it will be refreshed in a moment'
        ))
        success_url = self.request.POST.get('next')
        return success_url if success_url != '' else reverse('index')

class CovDeleteView(generic.DeleteView):
    model = Cov
    def dispatch(self, request, *args, **kwargs):
        """ Making sure that only authors can update Covs """
        obj = self.get_object()
        if obj.poster != self.request.user:
            return redirect(obj)
        return super(CovDeleteView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        messages.success(
            self.request, _(
            'Your cov has been removed, '
            'it will be refreshed in a moment'
        ))
        success_url = self.request.POST.get('next')
        return success_url if success_url != '' else reverse('index')
