from django.db import models
from django.core.validators import *

# Create your models here.
class Covoiturage(models.Model):
	"""model for Covoiturage"""
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
		validators=[
            RegexValidator(
                r'\w+-\w+',
                'Please specify your itinerary as Metz-Paris-Compiegne etc...',
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
		validators=[
			MinValueValidator(1),
		],)

	notes = models.CharField(
		max_length=50,
		blank=True)

	def __unicode__(self):
		rep = self.poster
		rep += ' propose ' if self.ANNONCE_TYPE == 0 else ' cherche '
		rep += str(self.dept_datetime)
		rep += ' for ' + str(self.n_places) + ' places'
		return rep
