from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.views import (
    logout,
    password_reset_confirm,
    password_change,
)
from .forms import EmailValidationOnForgotPassword

from .views import (
    AccountClaimView,
    AccountClaimConfirmView,
    SignInView,
    RezoAccountView,
    UserDetailView,
)


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
        login_required(RezoAccountView.as_view()),
        name="account",
    ),

    url(
        r'^logout$',
        login_required(
            logout
        ),
        {
            'next_page': reverse_lazy('index'),
        },
        name="logout",
    ),

    url(
        r'^password/lost$',
        'django.contrib.auth.views.password_reset',
        {
            'post_reset_redirect': reverse_lazy('password_reset_done'),
            'template_name': 'rezo/user/password_reset.html',
            'password_reset_form': EmailValidationOnForgotPassword
        },
        name="password-reset",
    ),

    url(
        r'^password/reset/done$',
        generic.TemplateView.as_view(
            template_name='rezo/user/password_reset_done.html'
            ),
        name="password_reset_done",
    ),

    url(
        r'^password/reset/confirm/(?P<uidb64>[\w\d]+)/(?P<token>[\d\w-]+)$',
        password_reset_confirm,
        {
        'template_name': 'rezo/user/password_reset_confirm.html',
        'post_reset_redirect': reverse_lazy('sign-in'),
        },
        name="password_reset_confirm",
    ),

    url(r'password/change$',
        login_required(
            password_change
            ),
        {
        'template_name': 'rezo/user/password_change.html',
        'post_change_redirect': reverse_lazy('account'),
        },
        name="password-change",
    ),

    url(
        r'^(?P<username>[\w-]+)/profile$',
        UserDetailView.as_view(),
        name='user-profile',
    ),
)
