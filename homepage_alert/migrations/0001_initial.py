# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=60, verbose_name='Titre')),
                ('description', models.TextField(verbose_name='Description')),
                ('type', models.SmallIntegerField(verbose_name='Type', choices=[(0, 'Information+'), (1, 'Information'), (2, 'Attention'), (3, 'Attention+')])),
                ('posted_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date de l\u2019alerte')),
                ('end_date', models.DateTimeField(verbose_name='Date de fin')),
            ],
        ),
    ]
