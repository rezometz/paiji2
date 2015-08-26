from django.conf.urls import url  # , patterns
from django.contrib.auth.decorators import login_required

from .views import (
    MessageCreateView, MessageEditView, MessageDeleteView,
    CommentCreateView,
    GroupView, GroupMembersView, GroupNewsView,
)
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
        login_required(GroupView.as_view()),
        name="workgroup-view",
    ),
    # Group Members
    url(
        r'(?P<slug>[\w-]+)/members$',
        login_required(GroupMembersView.as_view()),
        name="workgroup-members",
    ),

    # Group News
    url(
        r'(?P<slug>[\w-]+)/news$',
        login_required(GroupNewsView.as_view()),
        name="workgroup-news",
    ),

    # Feeds
    url(
        r'^feeds/latest$',
        login_required(LatestEntriesFeed()),
        name="feed-latest",
    ),
]
