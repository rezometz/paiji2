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
        r'^page/(?P<page>[0-9]+)/$',
        login_required(views.TopicListView.as_view()),
        name='topic-page',
    ),
    url(
        r'^recent/$',
        login_required(views.NewMessagesView.as_view()),
        name='recent-list',
    ),
    url(
        r'^recent/page/(?P<page>[0-9]+)$',
        login_required(views.NewMessagesView.as_view()),
        name='recent-page',
    ),
    url(
        '^message/(?P<pk>[0-9]+)$',
        login_required(views.message_view),
        name='message',
    ),
    url(
        '^message/(?P<pk>[0-9]+)/answer$',
        login_required(views.AnswerCreate.as_view()),
        name='answer',
    ),
    url(
        '^topic/(?P<pk>[0-9]+)$',
        #login_required(views.TopicView.as_view()),
        login_required(views.topic_view),
        name='topic',
    ),
    url(
        '^new$',
        login_required(views.AnswerCreate.as_view()),
        name='new',
    ),
]
