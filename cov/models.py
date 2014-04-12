# -*- coding: UTF-8 -*-

from django.db import models
from django.core.validators import *
from django.forms import ModelForm
from django.utils import timezone

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
	annonce_type = models.IntegerField(choices=ANNONCE_TYPE)

	itinerary = models.CharField(
		max_length=50,
		help_text="Please specify your itinerary as Metz-Paris-Compiegne (without accent) etc...",
		validators=[
            RegexValidator(
                r'^(([^\W\d]|[u+0100-u+0127])+-([^\W\d]|[u+0100-u+0127])+)+$',
                'Please specify your itinerary as Metz-Paris-Compiegne(without accent) etc...',
                'Invalid itinerary'
            ),
            MinLengthValidator(3),
        ],)

	n_places = models.IntegerField(
		validators=[
			MinValueValidator(1),
			MaxValueValidator(50),
		],)

	dept_datetime = models.DateTimeField()
	ret_datetime = models.DateTimeField(
		blank = True,
		null = True,
		)

	price_per_trip = models.IntegerField(
		blank = True,
		null = True,
		help_text = 'leave blank for price on request',
		validators=[
			MinValueValidator(1),
		],)

	notes = models.TextField(
		max_length=200,
		blank=True)

	def __unicode__(self):
		rep = self.poster
		rep += ' propose ' if self.ANNONCE_TYPE == 0 else ' cherche '
		rep += str(self.dept_datetime)
		rep += ' for ' + str(self.n_places) + ' places'
		return rep

	def future(self):
		return timezone.now() < self.dept_datetime

class CovoiturageForm(ModelForm):
	class Meta:
		model = Covoiturage
		fields = [
		'poster',
		'poster_email',
		'annonce_type',
		'itinerary',
		'dept_datetime',
		'ret_datetime',
		'n_places',
		'price_per_trip',
		'notes']
