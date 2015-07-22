from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from .views import *

urlpatterns = patterns('',
    url(
        r'^$',
        login_required(CovListView.as_view()),
        name="cov-list",
    ),
    url(
        r'add$',
        login_required(CovCreateView.as_view()),
        name="cov-add",
    ),
    url(
        r'edit/(?P<pk>[0-9]+)/$',
        login_required(CovEditView.as_view()),
        name="cov-edit",
    ),
    url(
        r'delete/(?P<pk>[0-9]+)/$',
        login_required(CovDeleteView.as_view()),
        name="cov-delete",
    ),
)
