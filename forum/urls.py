from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        r'^$',
        views.TopicListView.as_view(),
        name='topic-list'
    ),
    url(
        r'^page/(?P<page>[0-9]+)/$',
        views.TopicListView.as_view(),
        name='topic-page'
    ),
    url(
        r'^recent/$',
        views.NewMessagesView.as_view(),
        name='recent-list'
    ),
    url(
        r'^recent/page/(?P<page>[0-9]+)$',
        views.NewMessagesView.as_view(),
        name='recent-page'
    ),
    url(
        '^message/(?P<pk>[0-9]+)$',
        views.message_view,
        name='message'
    ),
    url(
        '^message/(?P<pk>[0-9]+)/answer$',
        views.AnswerCreate.as_view(),
        name='answer'
    ),
    url(
        '^new$',
        views.AnswerCreate.as_view(),
        name='new'
    ),
]
