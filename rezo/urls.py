from django.conf.urls import patterns, url

from .views import AccountClaimView, AccountClaimConfirmView, \
    SignInView


urlpatterns = patterns('',
    url(
        r'^account/claim$',
        AccountClaimView.as_view(),
        name="account-claim"
    ),

    url(
        r'^account/claim/(?P<email>\S+)/(?P<code>\w+)$',
        AccountClaimConfirmView.as_view(),
        name="account-claim-confirm"
    ),

    url(
        r'^sign-in$',
        SignInView.as_view(),
        name="sign-in",
    ),

)
