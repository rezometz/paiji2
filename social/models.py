from django.db import models

from django.utils import timezone
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse

from backbone_calendar.models import Calendar

# Create your models here.

class PostType(models.Model):
    # President, Vice-President, Respo Com etc
    description = models.CharField(max_length = 50, blank=False)

    def __unicode__(self):
        return self.description

# group de type assos/club/listeBDE/listePipo etc
class GroupCategory(models.Model):
    name = models.CharField(max_length = 50, unique = True)

    def __unicode__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length = 50, unique = True, blank = False)
    slug = models.SlugField()
    category = models.ForeignKey(GroupCategory, null=False)

    createdOn = models.DateTimeField(null = False, blank = False)
    deletedOn = models.DateTimeField(null = True, blank = True)

    logo = models.ImageField(upload_to = 'groups/logo', null=True)
    newsfeed = models.URLField(blank = True)

    calendar = models.OneToOneField(Calendar, related_name='group', null=True)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.createdOn = timezone.now()
        super(Group, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('workgroup-view', kwargs={
            'slug': self.slug,
        })

    def __unicode__(self):
        return self.name

class Bureau(models.Model):
    # debut de mandat
    createdDate = models.DateTimeField(null = False)
    # fin du mandat null si mandat en cours
    endDate = models.DateTimeField(null = True, blank=True)

    group = models.ForeignKey(Group, blank=False, related_name='bureaus')

    def currentBureauExist(self):
        if self.endDate == None:
            return Bureau.objects.filter(group=self.group, endDate=None).count() > 0
        return False

    def is_current(self):
        return self.endDate is not None

    def clean(self):
        if self.currentBureauExist():
            raise ValidationError('Another current Bureau exists already, update its endDate before setting a new Bureau')

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.createdDate = timezone.now()
        super(Bureau, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.group.name

    class Meta:
        ordering = ('group__category', 'group__name', '-createdDate')

class Post(models.Model):
    utilisateur = models.ForeignKey(get_user_model(), related_name='post')

    bureau = models.ForeignKey(Bureau, related_name='members')

    description = models.TextField(blank=True)

    postType = models.ForeignKey(PostType, null=False)

    class Meta:
        unique_together = ('bureau', 'postType',)

class Message(models.Model):
    author = models.ForeignKey(
        get_user_model(),
        related_name='message',
    )

    pubDate = models.DateTimeField(null = False)
    title = models.CharField(max_length=140, blank=False)
    content = models.TextField(blank=False)

    IMPORTANCE_LEVEL = (
        (0, 'Normal'),
        (1, 'Priority'),
    )

    group = models.ForeignKey(Group)

    importance = models.IntegerField(choices = IMPORTANCE_LEVEL,
                                     blank = False,
                                     default = 0)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.pubDate = timezone.now()
        super(Message, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('group__name', '-pubDate', )


class Comment(models.Model):
    author = models.ForeignKey(
            get_user_model(),
            related_name='comment'
        )
    message = models.ForeignKey(
            Message,
            related_name='comment'
        )

    pubDate = models.DateTimeField(null=False)
    content = models.CharField(max_length=140, blank=False)
    class Meta:
        ordering = ('message', '-pubDate', )
