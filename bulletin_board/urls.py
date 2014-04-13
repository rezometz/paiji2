from django.conf.urls import patterns, url

from .views import NoteListView


urlpatterns = patterns('',
    url(
        r'^board$',
        NoteListView.as_view(),
        name="bulletin-board",
    ),
    url(
        r'^board/(?P<page>\d+)?$',
        NoteListView.as_view(),
        name="bulletin-board",
    ),

)
