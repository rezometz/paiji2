# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backbone_calendar', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bureau',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('createdDate', models.DateTimeField(auto_now_add=True, verbose_name='date de d\xe9but de mandat')),
                ('endDate', models.DateTimeField(null=True, verbose_name='date de fin de mandat', blank=True)),
            ],
            options={
                'ordering': ('group__category', 'group__name', '-createdDate'),
                'verbose_name': 'Bureau',
                'verbose_name_plural': 'Bureaux',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pubDate', models.DateTimeField(verbose_name='date de publication')),
                ('content', models.CharField(max_length=140, verbose_name='corps du message')),
                ('author', models.ForeignKey(related_name='comment', verbose_name='auteur', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('message', '-pubDate'),
                'verbose_name': 'commentaire',
                'verbose_name_plural': 'commentaires',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50, verbose_name='nome')),
                ('slug', models.SlugField()),
                ('createdOn', models.DateTimeField(auto_now_add=True, verbose_name='date de cr\xe9ation')),
                ('deletedOn', models.DateTimeField(null=True, verbose_name='date de suppression', blank=True)),
                ('logo', models.ImageField(upload_to=b'groups/logo', null=True, verbose_name='logo')),
                ('newsfeed', models.URLField(verbose_name='flux de nouvelles', blank=True)),
                ('calendar', models.OneToOneField(related_name='group', null=True, verbose_name='calendrier', to='backbone_calendar.Calendar')),
            ],
            options={
                'verbose_name': 'groupe',
                'verbose_name_plural': 'groupes',
            },
        ),
        migrations.CreateModel(
            name='GroupCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50, verbose_name='nome')),
            ],
            options={
                'verbose_name': 'cat\xe9gorie de groupe',
                'verbose_name_plural': 'cat\xe9gories de groupe',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pubDate', models.DateTimeField(auto_now_add=True, verbose_name='date de publication')),
                ('title', models.CharField(max_length=140, verbose_name='titre')),
                ('content', models.TextField(verbose_name='corps du message')),
                ('public', models.BooleanField(default=False, verbose_name='visible par des visiteurs non-inscrits')),
                ('importance', models.IntegerField(default=0, verbose_name='niveau d\u2019importance', choices=[(0, 'Normal'), (1, 'Priorit\xe9')])),
                ('author', models.ForeignKey(related_name='message', verbose_name='auteur', to=settings.AUTH_USER_MODEL)),
                ('group', models.ForeignKey(verbose_name='groupe', to='social.Group')),
            ],
            options={
                'ordering': ('group__name', '-pubDate'),
                'verbose_name': 'message',
                'verbose_name_plural': 'messages',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('bureau', models.ForeignKey(related_name='members', verbose_name='Bureau', to='social.Bureau')),
            ],
            options={
                'verbose_name': 'poste',
                'verbose_name_plural': 'postes',
            },
        ),
        migrations.CreateModel(
            name='PostType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=50, verbose_name='description')),
            ],
            options={
                'verbose_name': 'type de poste',
                'verbose_name_plural': 'types de poste',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='postType',
            field=models.ForeignKey(verbose_name='type de poste', to='social.PostType'),
        ),
        migrations.AddField(
            model_name='post',
            name='utilisateur',
            field=models.ForeignKey(related_name='posts', verbose_name='utilisateur', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='group',
            name='category',
            field=models.ForeignKey(verbose_name='cat\xe9gorie', to='social.GroupCategory'),
        ),
        migrations.AddField(
            model_name='comment',
            name='message',
            field=models.ForeignKey(related_name='comment', verbose_name='message', to='social.Message'),
        ),
        migrations.AddField(
            model_name='bureau',
            name='group',
            field=models.ForeignKey(related_name='bureaus', verbose_name='groupe', to='social.Group'),
        ),
        migrations.AlterUniqueTogether(
            name='post',
            unique_together=set([('bureau', 'postType')]),
        ),
    ]
