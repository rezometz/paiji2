from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now
from django.contrib.auth import get_user_model


class PollManager(models.Manager):
    def current(self):
        try:
            return self.filter(
                beginning__lt=now(),
                end__gt=now(),
            )[0]
        except IndexError:
            return self.latest()


class Poll(models.Model):
    title = models.CharField(
        _('Title'),
        max_length=255,
    )
    beginning = models.DateTimeField(
        _('Beginning'),
        default=now,
    )
    end = models.DateTimeField(
        _('End'),
    )

    objects = PollManager()

    def __unicode__(self):
        return self.title

    def vote_for(self, user):
        try:
            return self.choices.get(votes__user=user)
        except Choice.DoesNotExist:
            return None

    class Meta:
        get_latest_by = 'end'


class Choice(models.Model):
    poll = models.ForeignKey(
        Poll,
        verbose_name=_('Poll'),
        related_name='choices',
    )
    value = models.CharField(
        _('Value'),
        max_length=255,
    )

    def __unicode__(self):
        return self.value


class Vote(models.Model):
    choice = models.ForeignKey(
        Choice,
        verbose_name=_('Choice'),
        related_name='votes',
    )
    user = models.ForeignKey(
        get_user_model(),
        verbose_name=_('User'),
        related_name='votes',
    )

    class Meta:
        unique_together = (
            ('user', 'choice', ),
        )
