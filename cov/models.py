# -*- coding: UTF-8 -*-

from django.db import models
# from django.core.validators import *
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth import get_user_model

# Create your models here.
class Covoiturage(models.Model):
	"""model for Covoiturage"""

	poster = models.ForeignKey(
        get_user_model(),
        related_name='covs',
    )

	ANNONCE_TYPE = (
        (0, 'Propose'),
        (1, 'Cherche'),
    )
	annonce_type = models.IntegerField(choices=ANNONCE_TYPE, blank=False)

	good_until = models.DateTimeField(
		'Annonce reste valable jusqu`à la date ci-dessous',
		default = timezone.now()+timedelta(days=3))

	posted_at = models.DateTimeField(
        'Posted at',
    )

	notes = models.CharField(
		max_length=150)

	def __unicode__(self):
		rep = self.poster.first_name + self.poster.last_name
		rep += ' propose ' if self.ANNONCE_TYPE == 0 else ' cherche '
		rep += self.notes
		return rep

	def isGood(self):
		return self.good_until > timezone.now()

	def save(self, *args, **kwargs):
		if self.pk is None:
			self.posted_at = timezone.now()

		super(Covoiturage, self).save(*args, **kwargs)

	class Meta:
		ordering = ('-posted_at', )
