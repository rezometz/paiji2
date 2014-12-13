# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PostType'
        db.create_table(u'social_posttype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'social', ['PostType'])

        # Adding model 'GroupCategory'
        db.create_table(u'social_groupcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'social', ['GroupCategory'])

        # Adding model 'Group'
        db.create_table(u'social_group', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['social.GroupCategory'])),
            ('createdOn', self.gf('django.db.models.fields.DateTimeField')()),
            ('deletedOn', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True)),
            ('newsfeed', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'social', ['Group'])

        # Adding model 'Bureau'
        db.create_table(u'social_bureau', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('createdDate', self.gf('django.db.models.fields.DateTimeField')()),
            ('endDate', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['social.Group'])),
        ))
        db.send_create_signal(u'social', ['Bureau'])

        # Adding model 'Post'
        db.create_table(u'social_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('utilisateur', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rezo.User'])),
            ('bureau', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['social.Bureau'])),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('postType', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['social.PostType'])),
        ))
        db.send_create_signal(u'social', ['Post'])

        # Adding unique constraint on 'Post', fields ['bureau', 'postType']
        db.create_unique(u'social_post', ['bureau_id', 'postType_id'])

        # Adding model 'Message'
        db.create_table(u'social_message', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pubDate', self.gf('django.db.models.fields.DateTimeField')()),
            ('title', self.gf('django.db.models.fields.TextField')(max_length=140)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['social.Group'])),
            ('importance', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'social', ['Message'])


    def backwards(self, orm):
        # Removing unique constraint on 'Post', fields ['bureau', 'postType']
        db.delete_unique(u'social_post', ['bureau_id', 'postType_id'])

        # Deleting model 'PostType'
        db.delete_table(u'social_posttype')

        # Deleting model 'GroupCategory'
        db.delete_table(u'social_groupcategory')

        # Deleting model 'Group'
        db.delete_table(u'social_group')

        # Deleting model 'Bureau'
        db.delete_table(u'social_bureau')

        # Deleting model 'Post'
        db.delete_table(u'social_post')

        # Deleting model 'Message'
        db.delete_table(u'social_message')


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
            'sidebar_left': ('modular_blocks.fields.ListTextField', [], {}),
            'sidebar_right': ('modular_blocks.fields.ListTextField', [], {}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'social.bureau': {
            'Meta': {'ordering': "('group__type', 'group__name', '-createdDate')", 'object_name': 'Bureau'},
            'createdDate': ('django.db.models.fields.DateTimeField', [], {}),
            'endDate': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['social.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'social.group': {
            'Meta': {'object_name': 'Group'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['social.GroupCategory']"}),
            'createdOn': ('django.db.models.fields.DateTimeField', [], {}),
            'deletedOn': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'newsfeed': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'social.groupcategory': {
            'Meta': {'object_name': 'GroupCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'social.message': {
            'Meta': {'ordering': "('group__name', '-pubDate')", 'object_name': 'Message'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['social.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'importance': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pubDate': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.TextField', [], {'max_length': '140'})
        },
        u'social.post': {
            'Meta': {'unique_together': "(('bureau', 'postType'),)", 'object_name': 'Post'},
            'bureau': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['social.Bureau']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'postType': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['social.PostType']"}),
            'utilisateur': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rezo.User']"})
        },
        u'social.posttype': {
            'Meta': {'object_name': 'PostType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['social']