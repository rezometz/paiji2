from django import forms
from django.contrib import auth
from django.utils.translation import ugettext_lazy as _

from .models import User  # , AccountRecovery


class ConfirmForm(forms.Form):
    pass


class UserCreationForm(auth.forms.UserCreationForm):
    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            self.Meta.model._default_manager.get(username=username)
        except self.Meta.model.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )

    class Meta:
        model = auth.get_user_model()
        fields = ('username', )


class UserAuthenticationForm(auth.forms.AuthenticationForm):
    pass


class EmailValidationOnForgotPassword(auth.forms.PasswordResetForm):
    message = _(
        "There is no user registered with the specified email address!"
    )

    def clean_email(self):
        email = self.cleaned_data['email']
        exists_email = User.objects.filter(
            email__iexact=email,
            is_active=True,
        ).exists()
        if not exists_email:
            raise forms.ValidationError(self.message)

        return email
