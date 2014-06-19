from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from .views import (
    MessageCreateView, MessageListView,
    GroupView,
)
from .feeds import LatestEntriesFeed

urlpatterns = [
    url(  # Add a message
        r'add$',
        login_required(MessageCreateView.as_view()),
        name="newsfeed-add",
    ),
    url(  # Group view
        r'(?P<slug>[\w-]+)/dashboard$',
        GroupView.as_view(),
        name="workgroup-view",
    ),

    # Feeds
    url(
        r'^feeds/latest$',
        LatestEntriesFeed(),
        name="feed-latest",
    ),
]
