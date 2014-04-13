from django import forms
from django.contrib import auth

from .models import AccountRecovery, User

class ConfirmForm(forms.Form):
    pass

class UserCreationForm(auth.forms.UserCreationForm):
    class Meta(auth.forms.UserCreationForm.Meta):
        model = User

class UserAuthenticationForm(auth.forms.AuthenticationForm):
    pass