# -*- utf-8 -*-
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.core.urlresolvers import reverse
from django import forms
import os

class MessageIcon(models.Model):

    name = models.CharField(max_length=30, verbose_name='nom')
    filename = models.CharField(max_length=100, verbose_name='nom du fichier')
    
    def url(self):
        #return settings.STATIC_URL + 'forum/icons/' + self.filename
        return 'forum/icons/' + self.filename

    def __unicode__(self):
        return self.name
        

class Message(models.Model):

    title = models.CharField(
        'titre',
        max_length=200,
    )

    text = models.TextField(
        'texte'
    )

    pub_date = models.DateTimeField(
        'date de publication',
        default=timezone.now
    )

    readers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='read_messages',
        null=True,
        blank=True,
    )

    question = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='answers',
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='auteur',
        related_name='auteur',
    )

    icon = models.ForeignKey(
        MessageIcon,
        default=None,
        verbose_name='icone',
    )

    def is_topic(self):
        return self.question == None
    is_topic.boolean = True

    def is_leaf(self):
        return self.answers.count() == 0
    is_leaf.boolean = True

    def answers_nb(self):
        return self.answers.count()

    def childs_nb(self):
        nb = 0
        for answer in self.answers.all():
            nb += answer.childs_nb()
        return nb + self.answers.count()

    def childs_depth(self):
        if self.answers.count() == 0:
            return 0
        else:
            return 1 + max(
                [ i.childs_depth() for i in self.answers.all() ]
            )

    def level(self):
        if self.question == None:
            return 0
        else:
            return 1 + self.question.level()

    def topic(self):
        if self.question == None:
            return self
        else:
            return self.question.topic()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('forum:message', kwargs={'pk': self.pk})
