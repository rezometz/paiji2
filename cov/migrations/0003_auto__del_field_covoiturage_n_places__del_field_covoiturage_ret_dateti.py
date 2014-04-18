# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Covoiturage.n_places'
        db.delete_column(u'cov_covoiturage', 'n_places')

        # Deleting field 'Covoiturage.ret_datetime'
        db.delete_column(u'cov_covoiturage', 'ret_datetime')

        # Deleting field 'Covoiturage.dept_datetime'
        db.delete_column(u'cov_covoiturage', 'dept_datetime')

        # Deleting field 'Covoiturage.price_per_trip'
        db.delete_column(u'cov_covoiturage', 'price_per_trip')

        # Deleting field 'Covoiturage.itinerary'
        db.delete_column(u'cov_covoiturage', 'itinerary')

        # Adding field 'Covoiturage.good_until'
        db.add_column(u'cov_covoiturage', 'good_until',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 4, 15, 0, 0)),
                      keep_default=False)


        # Changing field 'Covoiturage.notes'
        db.alter_column(u'cov_covoiturage', 'notes', self.gf('django.db.models.fields.CharField')(max_length=150))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Covoiturage.n_places'
        raise RuntimeError("Cannot reverse this migration. 'Covoiturage.n_places' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Covoiturage.n_places'
        db.add_column(u'cov_covoiturage', 'n_places',
                      self.gf('django.db.models.fields.IntegerField')(),
                      keep_default=False)

        # Adding field 'Covoiturage.ret_datetime'
        db.add_column(u'cov_covoiturage', 'ret_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Covoiturage.dept_datetime'
        raise RuntimeError("Cannot reverse this migration. 'Covoiturage.dept_datetime' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Covoiturage.dept_datetime'
        db.add_column(u'cov_covoiturage', 'dept_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(),
                      keep_default=False)

        # Adding field 'Covoiturage.price_per_trip'
        db.add_column(u'cov_covoiturage', 'price_per_trip',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Covoiturage.itinerary'
        raise RuntimeError("Cannot reverse this migration. 'Covoiturage.itinerary' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Covoiturage.itinerary'
        db.add_column(u'cov_covoiturage', 'itinerary',
                      self.gf('django.db.models.fields.CharField')(max_length=50),
                      keep_default=False)

        # Deleting field 'Covoiturage.good_until'
        db.delete_column(u'cov_covoiturage', 'good_until')


        # Changing field 'Covoiturage.notes'
        db.alter_column(u'cov_covoiturage', 'notes', self.gf('django.db.models.fields.CharField')(max_length=50))

    models = {
        u'cov.covoiturage': {
            'Meta': {'object_name': 'Covoiturage'},
            'annonce_type': ('django.db.models.fields.IntegerField', [], {}),
            'good_until': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 4, 15, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'poster': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'poster_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'})
        }
    }

    complete_apps = ['cov']