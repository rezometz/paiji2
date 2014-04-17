# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'User.sidebar_left'
        db.add_column(u'rezo_user', 'sidebar_left',
                      self.gf('modulable_app.fields.ListTextField')(default='infoconcert:weather'),
                      keep_default=False)

        # Adding field 'User.sidebar_right'
        db.add_column(u'rezo_user', 'sidebar_right',
                      self.gf('modulable_app.fields.ListTextField')(default='calendar:cov:bulletin-board'),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'User.sidebar_left'
        db.delete_column(u'rezo_user', 'sidebar_left')

        # Deleting field 'User.sidebar_right'
        db.delete_column(u'rezo_user', 'sidebar_right')


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
        u'rezo.accountrecovery': {
            'Meta': {'object_name': 'AccountRecovery'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_rezo': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'rezo.ecole': {
            'Meta': {'object_name': 'Ecole', 'db_table': "u'ecoles'", 'managed': 'False'},
            'description': ('django.db.models.fields.TextField', [], {'db_column': "u'descriptionEcole'"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.TextField', [], {'db_column': "u'nomEcole'"}),
            'rezotable': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'rezo.equipement': {
            'Meta': {'object_name': 'Equipement', 'db_table': "u'equipements'", 'managed': 'False'},
            'dns': ('django.db.models.fields.TextField', [], {}),
            'dnsrez': ('django.db.models.fields.TextField', [], {}),
            'etat': ('django.db.models.fields.CharField', [], {'max_length': '14'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'timestampdesactivationdefinitive': ('django.db.models.fields.IntegerField', [], {'db_column': "u'timestampDesactivationDefinitive'"}),
            'timestampenregistrement': ('django.db.models.fields.IntegerField', [], {'db_column': "u'timestampEnregistrement'"}),
            'type_equip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'db_column': "u'typeEquipement'", 'blank': 'True'}),
            'utilisateur': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'equipements'", 'db_column': "u'utilisateur_id'", 'to': u"orm['rezo.Utilisateur']"})
        },
        u'rezo.macs': {
            'Meta': {'object_name': 'Macs', 'db_table': "u'macs'", 'managed': 'False'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '17', 'db_column': "u'mac'"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'equipement': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'mac'", 'db_column': "u'equipement_id'", 'to': u"orm['rezo.Equipement']"}),
            'etat': ('django.db.models.fields.CharField', [], {'max_length': '14'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'timestamplasttimeup': ('django.db.models.fields.IntegerField', [], {'db_column': "u'timestampLastTimeUp'"})
        },
        u'rezo.quotas': {
            'Meta': {'object_name': 'Quotas', 'db_table': "u'quotas'", 'managed': 'False'},
            'conso_in': ('django.db.models.fields.BigIntegerField', [], {}),
            'conso_out': ('django.db.models.fields.BigIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'restant_veille_in': ('django.db.models.fields.BigIntegerField', [], {}),
            'restant_veille_out': ('django.db.models.fields.BigIntegerField', [], {}),
            'utilsateur': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "u'quotas'", 'unique': 'True', 'primary_key': True, 'db_column': "u'id'", 'to': u"orm['rezo.Utilisateur']"}),
            'warning': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'web_in': ('django.db.models.fields.BigIntegerField', [], {}),
            'web_out': ('django.db.models.fields.BigIntegerField', [], {})
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
            'sidebar_left': ('modulable_app.fields.ListTextField', [], {}),
            'sidebar_right': ('modulable_app.fields.ListTextField', [], {}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'rezo.utilisateur': {
            'Meta': {'object_name': 'Utilisateur', 'db_table': "u'utilisateurs'", 'managed': 'False'},
            'autorisationdecouvert': ('django.db.models.fields.IntegerField', [], {'db_column': "u'autorisationDecouvert'"}),
            'borne_id': ('django.db.models.fields.IntegerField', [], {}),
            'ecole': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rezo.Ecole']"}),
            'email': ('django.db.models.fields.TextField', [], {}),
            'emailverifie': ('django.db.models.fields.TextField', [], {'db_column': "u'emailVerifie'"}),
            'etat': ('django.db.models.fields.CharField', [], {'max_length': '14'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.TextField', [], {}),
            'precisionecole': ('django.db.models.fields.TextField', [], {'db_column': "u'precisionEcole'"}),
            'prenom': ('django.db.models.fields.TextField', [], {}),
            'raisondecouvert': ('django.db.models.fields.TextField', [], {'db_column': "u'raisonDecouvert'"}),
            'rezoteur_id': ('django.db.models.fields.IntegerField', [], {}),
            'timestamprezotage': ('django.db.models.fields.IntegerField', [], {'db_column': "u'timestampRezotage'"}),
            'topology_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'typeutilisateur': ('django.db.models.fields.CharField', [], {'max_length': '11', 'db_column': "u'typeUtilisateur'"})
        }
    }

    complete_apps = ['rezo']