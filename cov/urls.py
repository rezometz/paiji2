from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from .views import CovListView, CovCreateView

urlpatterns = patterns('',
    url(
        r'^$',
        CovListView.as_view(),
        name="cov-list",
    ),
    url(
        r'^(?P<page>\d+)?$',
        CovListView.as_view(),
        name="cov-list",
    ),
    url(
        r'add$',
        login_required(CovCreateView.as_view()),
        name="cov-add",
    ),

)
