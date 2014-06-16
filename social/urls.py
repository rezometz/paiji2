from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from .views import MessageCreateView

urlpatterns = patterns('',
    url(
        r'add$',
        login_required(MessageCreateView.as_view()),
        name="newsfeed-add",
    ),
)
