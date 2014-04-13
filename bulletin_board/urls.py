from django.conf.urls import patterns, url

from django.contrib.auth.decorators import login_required

from .views import NoteListView, NoteCreateView


urlpatterns = patterns('',
    url(
        r'^board(/(?P<page>\d+))?$',
        NoteListView.as_view(),
        name="bulletin-board",
    ),
    url(
        r'board/add$',
        login_required(NoteCreateView.as_view()),
        name="bulletin-add",
    ),

)
