from django import forms
from django.contrib import auth

from .models import AccountRecovery

class ConfirmForm(forms.Form):
    pass

class UserCreationForm(auth.forms.UserCreationForm):
    class Meta:
        model = auth.get_user_model()
        fields = ()

class UserAuthenticationForm(auth.forms.AuthenticationForm):
    pass
