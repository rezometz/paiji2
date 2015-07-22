from django.conf.urls import patterns, url

from django.contrib.auth.decorators import login_required

from .views import *


urlpatterns = patterns('',
    url(
        r'^board$',
        login_required(NoteListView.as_view()),
        name="bulletin-board",
    ),
    url(
        r'board/add$',
        login_required(NoteCreateView.as_view()),
        name="bulletin-add",
    ),
    url(
        r'board/edit/(?P<pk>[0-9]+)/$',
        login_required(NoteEditView.as_view()),
        name="bulletin-edit",
    ),
    url(
        r'board/delete/(?P<pk>[0-9]+)/$',
        login_required(NoteDeleteView.as_view()),
        name="bulletin-delete",
    ),
)
