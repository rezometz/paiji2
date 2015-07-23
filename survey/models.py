from django.db import models
from django.utils.translation import ugettext as _
from django.utils.timezone import now
from django.contrib.auth import get_user_model

from HTMLParser import HTMLParser


class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)


def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


class PollManager(models.Manager):
    def current(self):
        try:
            return self.filter(
                beginning__lt=now(),
                end__gt=now(),
            ).annotate(
                votes_count=models.Count('choices__votes')
            )[0]
        except IndexError:
            return self.annotate(
                votes_count=models.Count('choices__votes')
            ).latest()


class Poll(models.Model):

    class Meta:
        verbose_name = _('poll')
        verbose_name_plural = _('polls')
        get_latest_by = 'end'
        ordering = ('-end', )

    title = models.CharField(
        _('title'),
        max_length=255,
    )
    beginning = models.DateTimeField(
        _('beginning'),
        default=now,
    )
    end = models.DateTimeField(
        _('end'),
    )

    objects = PollManager()

    def __unicode__(self):
        return self.title

    def vote_for(self, user):
        try:
            return self.choices.get(votes__user=user)
        except Choice.DoesNotExist:
            return None
    vote_for.short_description = _('vote for ?')


class Choice(models.Model):
    
    class Meta:
        verbose_name = _('choice')
        verbose_name_plural = _('choices')

    poll = models.ForeignKey(
        Poll,
        verbose_name=_('poll'),
        related_name='choices',
    )

    value = models.CharField(
        _('value'),
        max_length=255,
    )

    def __unicode__(self):
        return self.value

    def stripped_value(self):
        return strip_tags(self.value)


class Vote(models.Model):

    class Meta:
        verbose_name = _('vote')
        verbose_name_plural = _('votes')
        unique_together = (
            ('user', 'choice', ),
        )

    choice = models.ForeignKey(
        Choice,
        verbose_name=_('choice'),
        related_name='votes',
    )

    user = models.ForeignKey(
        get_user_model(),
        verbose_name=_('user'),
        related_name='votes',
    )

