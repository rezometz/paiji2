# -*- coding: UTF-8 -*-

from django.db import models
# from django.core.validators import *
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext as _
from django.utils.translation import pgettext

class Covoiturage(models.Model):

    class Meta:
        verbose_name = _('carpool')
        verbose_name_plural = _('carpools')
        ordering = ('-posted_at', )

    author = models.ForeignKey(
        get_user_model(),
        verbose_name=_('author'),
        related_name='covs',
    )

    ANNONCE_TYPE = (
        (0, pgettext('1st p sg','Offer')),
        (1, pgettext('1st p sg','Search')),
    )

    annonce_type = models.IntegerField(
        _('advert type'),
        choices=ANNONCE_TYPE,
        blank=False,
    )

    good_until = models.DateTimeField(
        _('advert validity deadline'),
        default = timezone.now()+timedelta(days=3),
    )

    posted_at = models.DateTimeField(
        _('publication date'),
    )

    notes = models.CharField(
        _('description'),
        max_length=150,
    )

    def __unicode__(self):
        rep = self.author.first_name + self.author.last_name
        rep += ' '+_('offer')+' ' if self.ANNONCE_TYPE == 0 else ' '+_('search')+' '
        rep += self.notes
        return rep

    def isGood(self):
        return self.good_until > timezone.now()
    isGood.short_description = _('still current ?')

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.posted_at = timezone.now()
        super(Covoiturage, self).save(*args, **kwargs)

