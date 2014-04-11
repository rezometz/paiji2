from django.conf.urls import patterns, url

from .views import AccountClaimView


urlpatterns = patterns('',
    url(r'^account/claim', AccountClaimView.as_view(), name="account-claim"),
)
