# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Covoiturage.poster_email'
        db.delete_column(u'cov_covoiturage', 'poster_email')

        # Adding field 'Covoiturage.posted_at'
        db.add_column(u'cov_covoiturage', 'posted_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 4, 13, 0, 0)),
                      keep_default=False)


        # Renaming column for 'Covoiturage.poster' to match new field type.
        db.rename_column(u'cov_covoiturage', 'poster', 'poster_id')
        # Changing field 'Covoiturage.poster'
        db.alter_column(u'cov_covoiturage', 'poster_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rezo.User']))
        # Adding index on 'Covoiturage', fields ['poster']
        db.create_index(u'cov_covoiturage', ['poster_id'])


    def backwards(self, orm):
        # Removing index on 'Covoiturage', fields ['poster']
        db.delete_index(u'cov_covoiturage', ['poster_id'])


        # User chose to not deal with backwards NULL issues for 'Covoiturage.poster_email'
        raise RuntimeError("Cannot reverse this migration. 'Covoiturage.poster_email' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Covoiturage.poster_email'
        db.add_column(u'cov_covoiturage', 'poster_email',
                      self.gf('django.db.models.fields.EmailField')(max_length=75),
                      keep_default=False)

        # Deleting field 'Covoiturage.posted_at'
        db.delete_column(u'cov_covoiturage', 'posted_at')


        # Renaming column for 'Covoiturage.poster' to match new field type.
        db.rename_column(u'cov_covoiturage', 'poster_id', 'poster')
        # Changing field 'Covoiturage.poster'
        db.alter_column(u'cov_covoiturage', 'poster', self.gf('django.db.models.fields.CharField')(max_length=50))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'cov.covoiturage': {
            'Meta': {'ordering': "('-posted_at',)", 'object_name': 'Covoiturage'},
            'annonce_type': ('django.db.models.fields.IntegerField', [], {}),
            'good_until': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 4, 16, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'posted_at': ('django.db.models.fields.DateTimeField', [], {}),
            'poster': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'covs'", 'to': u"orm['rezo.User']"})
        },
        u'rezo.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_rezo': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'null': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        }
    }

    complete_apps = ['cov']