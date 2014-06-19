from django.shortcuts import render
from django.views import generic
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages

from tinymce.widgets import TinyMCE

from models import Message, Group


class MessageListView(generic.ListView):
    model = Message
    paginate_by = 8
    context_object_name = 'news'
    template_name='home/index.html'

    def get_queryset(self):
        return super(MessageListView, self).get_queryset().order_by('-pubDate').select_related(
            'poster'
        )


class MessageCreateView(generic.CreateView):
    model = Message
    fields = ('group', 'title', 'content')
    template_name = 'social/newsfeed_form.html'

    def get_form(self, form_class):
        form = super(MessageCreateView, self).get_form(form_class)
        form.fields['group'].queryset = Group.objects.filter(bureaus__post__utilisateur=self.request.user)
        form.fields['content'].widget = TinyMCE(attrs={'cols': 80, 'rows': 20})
        return form

    def form_valid(self, form):
        message = form.save(commit=False)
        message.poster = self.request.user
        message.save()

        return super(MessageCreateView, self).form_valid(form)

    def get_success_url(self):
        messages.success(
            self.request, _(
            'Your request has been saved successfully :P'
        ))
        success_url = self.request.POST.get('next')
        return success_url if success_url != '' else reverse('index')


class GroupView(generic.DetailView):
    model = Group

