from django.db import models

from django.contrib import auth

from django.utils.translation import ugettext_lazy as _


class User(auth.models.User):
    id_rezo = models.PositiveIntegerField(_('ID Rezo Account'))
    validation_code = models.CharField(_('Validation code'), max_length=40)

