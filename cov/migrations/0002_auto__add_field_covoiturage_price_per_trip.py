# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Covoiturage.price_per_trip'
        db.add_column(u'cov_covoiturage', 'price_per_trip',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Covoiturage.price_per_trip'
        db.delete_column(u'cov_covoiturage', 'price_per_trip')


    models = {
        u'cov.covoiturage': {
            'Meta': {'object_name': 'Covoiturage'},
            'annonce_type': ('django.db.models.fields.IntegerField', [], {}),
            'dept_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'itinerary': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'n_places': ('django.db.models.fields.IntegerField', [], {}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'poster': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'poster_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'price_per_trip': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ret_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['cov']