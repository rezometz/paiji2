from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from .views import *
from .feeds import LatestEntriesFeed

urlpatterns = [
    # Message
    url(
        r'add$',
        login_required(MessageCreateView.as_view()),
        name="newsfeed-add",
    ),
    url(
        r'edit/(?P<pk>[0-9]+)/$',
        login_required(MessageEditView.as_view()),
        name="newsfeed-edit",
    ),
    url(
        r'delete/(?P<pk>[0-9]+)/$',
        login_required(MessageDeleteView.as_view()),
        name="newsfeed-delete",
    ),
    url(
        r'^comment/(?P<on_message>[0-9]+)/$',
        login_required(CommentCreateView.as_view()),
        name="comment-add"
    ),

    # Group
    url(
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
