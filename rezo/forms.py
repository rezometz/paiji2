from django import forms
from django.contrib import auth

from .models import AccountRecovery

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
