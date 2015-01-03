from django.conf.urls import patterns, url

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import (
    logout,
    password_reset,
    password_reset_confirm,
    password_change,
)

from .views import AccountClaimView, AccountClaimConfirmView, \
    SignInView, RezoAccountView


urlpatterns = patterns(
    '',  # Prefix


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

    url(
        r'^account$',
        RezoAccountView.as_view(),
        name="rezo-account",
    ),

    url(
        r'^logout$',
        login_required(
            logout
        ),
        {
            'next_page': '/',
        },
        name="logout",
    ),

)
