from django.db import models

from django.utils.timezone import now

from django.contrib.auth import get_user_model


class Note(models.Model):
    author = models.ForeignKey(
        get_user_model(),
        related_name='notes',
    )
    message = models.CharField(
        'Message',
        max_length=200,
    )
    posted_at = models.DateTimeField(
        'Posted at',
    )

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.posted_at = now()

        super(Note, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-posted_at', )
