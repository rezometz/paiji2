# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Comment'
        db.create_table(u'social_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(related_name='comment', to=orm['rezo.User'])),
            ('message', self.gf('django.db.models.fields.related.ForeignKey')(related_name='comment', to=orm['social.Message'])),
            ('pubDate', self.gf('django.db.models.fields.DateTimeField')()),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=140)),
        ))
        db.send_create_signal(u'social', ['Comment'])


    def backwards(self, orm):
        # Deleting model 'Comment'
        db.delete_table(u'social_comment')


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
        u'backbone_calendar.calendar': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Calendar'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '30'})
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
            'Meta': {'ordering': "('group__category', 'group__name', '-createdDate')", 'object_name': 'Bureau'},
            'createdDate': ('django.db.models.fields.DateTimeField', [], {}),
            'endDate': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'bureaus'", 'to': u"orm['social.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'social.comment': {
            'Meta': {'ordering': "('message', '-pubDate')", 'object_name': 'Comment'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comment'", 'to': u"orm['rezo.User']"}),
            'content': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comment'", 'to': u"orm['social.Message']"}),
            'pubDate': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'social.group': {
            'Meta': {'object_name': 'Group'},
            'calendar': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'group'", 'unique': 'True', 'null': 'True', 'to': u"orm['backbone_calendar.Calendar']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['social.GroupCategory']"}),
            'createdOn': ('django.db.models.fields.DateTimeField', [], {}),
            'deletedOn': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'newsfeed': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        u'social.groupcategory': {
            'Meta': {'object_name': 'GroupCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'social.message': {
            'Meta': {'ordering': "('group__name', '-pubDate')", 'object_name': 'Message'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'message'", 'to': u"orm['rezo.User']"}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['social.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'importance': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pubDate': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        },
        u'social.post': {
            'Meta': {'unique_together': "(('bureau', 'postType'),)", 'object_name': 'Post'},
            'bureau': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['social.Bureau']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'postType': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['social.PostType']"}),
            'utilisateur': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'post'", 'to': u"orm['rezo.User']"})
        },
        u'social.posttype': {
            'Meta': {'object_name': 'PostType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['social']