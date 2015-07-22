from django.db import models

from django.utils import timezone
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _

from backbone_calendar.models import Calendar


# President, Vice-President, Respo Com etc
class PostType(models.Model):

    class Meta:
        verbose_name = _('post type')
        verbose_name_plural = _('post types')

    description = models.CharField(
        _('description'),
        max_length = 50,
        blank=False,
    )

    def __unicode__(self):
        return self.description

# group de type assos/club/listeBDE/listePipo etc
class GroupCategory(models.Model):

    class Meta:
        verbose_name = _('group category')
        verbose_name_plural = _('group categories')

    name = models.CharField(
        _('name'),
        max_length = 50,
        unique = True,
    )

    def __unicode__(self):
        return self.name


class Group(models.Model):

    class Meta:
        verbose_name = _('group')
        verbose_name_plural = _('groups')

    name = models.CharField(
        _('name'),
        max_length = 50,
        unique = True,
        blank = False
    )

    slug = models.SlugField()

    category = models.ForeignKey(
        GroupCategory,
        null=False,
        verbose_name=_('category'),
    )

    createdOn = models.DateTimeField(
        _('creation date'),
        null = False,
        blank = False,
    )

    deletedOn = models.DateTimeField(
        _('deletion date'),
        null = True,
        blank = True,
    )


    logo = models.ImageField(
        _('logo'),
        upload_to = 'groups/logo',
        null=True,
    )

    newsfeed = models.URLField(
        _('newsfeed'),
        blank = True,
    )

    calendar = models.OneToOneField(
        Calendar,
        verbose_name=_('calendar'),
        related_name='group',
        null=True,
    )

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

    class Meta:
        verbose_name = _('Bureau')
        verbose_name_plural = _('Bureaux')
        ordering = ('group__category', 'group__name', '-createdDate')

    # debut de mandat
    createdDate = models.DateTimeField(
        _('tenure beginning date'),
        null = False,
    )

    # fin du mandat null si mandat en cours
    endDate = models.DateTimeField(
        _('tenure end date'),
        null = True,
        blank=True,
    )

    group = models.ForeignKey(
        Group,
        verbose_name=_('group'),
        blank=False,
        related_name='bureaus',
    )

    def currentBureauExist(self):
        if self.endDate == None:
            return Bureau.objects.filter(group=self.group, endDate=None).count() > 0
        return False
    currentBureauExist.short_description = _('Does it exist ?')

    def is_current(self):
        return self.endDate is not None
    is_current.short_description = _('Is it current ?')

    def clean(self):
        if self.currentBureauExist():
            raise ValidationError(_(\
            'Another current Bureau exists already,\
            update its tenure end date (endDate)\
            before setting a new Bureau'))

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.createdDate = timezone.now()
        super(Bureau, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.group.name


class Post(models.Model):

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')
        unique_together = ('bureau', 'postType',)

    utilisateur = models.ForeignKey(
        get_user_model(),
        verbose_name=_('user'),
        related_name='post',
    )

    bureau = models.ForeignKey(
        Bureau,
        verbose_name=_('Bureau'),
        related_name='members',
    )

    description = models.TextField(
        _('description'),
        blank=True,
    )

    postType = models.ForeignKey(
        PostType,
        verbose_name=_('post type'),
        null=False,
    )


class Message(models.Model):

    class Meta:
        verbose_name = _('message')
        verbose_name_plural = _('messages')
        ordering = ('group__name', '-pubDate', )

    author = models.ForeignKey(
        get_user_model(),
        verbose_name=_('author'),
        related_name='message',
    )

    pubDate = models.DateTimeField(
        _('publication date'),
        null = False,
    )

    title = models.CharField(
        _('title'),
        max_length=140,
        blank=False,
    )

    content = models.TextField(
        _('content'),
        blank=False,
    )

    public = models.BooleanField(
        verbose_name=_('readable by unregistered visitors'),
        default=False,
    )

    IMPORTANCE_LEVEL = (
        (0, _('Normal')),
        (1, _('Priority')),
    )

    group = models.ForeignKey(
        Group,
        verbose_name=_('group'),
    )

    importance = models.IntegerField(
        _('importance level'),
        choices = IMPORTANCE_LEVEL,
        blank = False,
        default = 0,
    )

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.pubDate = timezone.now()
        super(Message, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title


class Comment(models.Model):

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')
        ordering = ('message', '-pubDate', )

    author = models.ForeignKey(
        get_user_model(),
        verbose_name=_('author'),
        related_name='comment',
    )

    message = models.ForeignKey(
        Message,
        verbose_name=_('message'),
        related_name='comment'
    )

    pubDate = models.DateTimeField(
        _('publication date'),
        null=False,
    )

    content = models.CharField(
        _('content'),
        max_length=140,
        blank=False,
    )
