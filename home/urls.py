from django.conf.urls import patterns, url

from social.views import MessageListView

urlpatterns = patterns('',
    url(r'^$',
    	MessageListView.as_view(),
    	name='index'
    ),
    url(
        r'^(?P<page>\d+)?$',
        MessageListView.as_view(),
        name="index",
    ),
)
