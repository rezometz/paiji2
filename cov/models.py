# -*- coding: UTF-8 -*-

from django.db import models
from django.core.validators import *
from django.forms import ModelForm
from django.utils import timezone
from datetime import timedelta

# Create your models here.
class Covoiturage(models.Model):
	"""model for Covoiturage"""

	# TODO poster and poster_email should be replaced by a FK to paiji user
	poster = models.CharField(
		max_length=50,
		blank=False,)
	poster_email = models.EmailField(
		blank=False,)

	ANNONCE_TYPE = (
        (0, 'Propose'),
        (1, 'Cherche'),
    )
	annonce_type = models.IntegerField(choices=ANNONCE_TYPE, blank=False)

	# itinerary = models.CharField(
	# 	max_length=50,
	# 	help_text="Please specify your itinerary as Metz-Paris-Compiegne (without accent) etc...",
	# 	validators=[
 #            RegexValidator(
 #                r'^(([^\W\d]|[u+0100-u+0127])+-([^\W\d]|[u+0100-u+0127])+)+$',
 #                'Please specify your itinerary as Metz-Paris-Compiegne(without accent) etc...',
 #                'Invalid itinerary'
 #            ),
 #            MinLengthValidator(3),
 #        ],)

	# n_places = models.IntegerField(
	# 	validators=[
	# 		MinValueValidator(1),
	# 		MaxValueValidator(50),
	# 	],)

	good_until = models.DateTimeField(
		'offer will be canceled on this date',
		default = timezone.now()+timedelta(days=3))

	# price_per_trip = models.IntegerField(
	# 	blank = True,
	# 	null = True,
	# 	help_text = 'leave blank for price on request',
	# 	validators=[
	# 		MinValueValidator(1),
	# 	],)

	notes = models.CharField(
		max_length=150)

	def __unicode__(self):
		rep = self.poster
		rep += ' propose ' if self.ANNONCE_TYPE == 0 else ' cherche '
		rep += self.notes
		return rep

	def future(self):
		return timezone.now() < self.good_until

class CovoiturageForm(ModelForm):
	class Meta:
		model = Covoiturage
		fields = [
		'poster',
		'poster_email',
		'annonce_type',
		'good_until',
		# 'itinerary',
		# 'dept_datetime',
		# 'ret_datetime',
		# 'n_places',
		# 'price_per_trip',
		'notes']
