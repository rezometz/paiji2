from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from social.views import MessageListView


urlpatterns = [
    url(
        r'^$',
        MessageListView.as_view(),
        name='index',
    ),
]
