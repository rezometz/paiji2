from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from social.views import MessageListView

urlpatterns = patterns('',
    url(r'^$',
    	login_required(MessageListView.as_view()),
    	name='index'
    ),
    url(
        r'^(?P<page>\d+)?$',
        login_required(MessageListView.as_view()),
        name="index",
    ),
)
