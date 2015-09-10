# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import modular_blocks.fields


class Migration(migrations.Migration):

    dependencies = [
        ('rezo', '0002_user_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='topbar',
            field=modular_blocks.fields.ListTextField(null=True, blank=True),
        ),
    ]
