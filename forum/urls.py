from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    url(
        r'^$',
        login_required(views.TopicListView.as_view()),
        name='topic-list',
    ),
    url(
        r'^recent/$',
        login_required(views.NewMessagesView.as_view()),
        name='recent-list',
    ),
    url(
        r'^unread/$',
        login_required(views.UnreadMessagesView.as_view()),
        name='unread',
    ),
    url(
        '^message/(?P<pk>[0-9]+)$',
        login_required(views.TopicView.as_view()),
        name='message',
    ),
    url(
        '^message/(?P<pk>[0-9]+)/answer$',
        login_required(views.AnswerCreate.as_view()),
        name='answer',
    ),
    url(
        '^new$',
        login_required(views.AnswerCreate.as_view()),
        name='new',
    ),
]
