# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        db.rename_table('cov_covoiturage', 'paiji2_carpooling_carpool')

    def backwards(self, orm):
        db.rename_table('paiji2_carpooling_carpool', 'cov_covoiturage')

    models = {

    }

    complete_apps = ['home']
