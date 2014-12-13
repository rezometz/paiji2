# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AccountRecovery'
        db.create_table(u'rezo_accountrecovery', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('id_rezo', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal(u'rezo', ['AccountRecovery'])

        # Adding model 'User'
        db.create_table(u'rezo_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('id_rezo', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'rezo', ['User'])


    def backwards(self, orm):
        # Deleting model 'AccountRecovery'
        db.delete_table(u'rezo_accountrecovery')

        # Deleting model 'User'
        db.delete_table(u'rezo_user')


    models = {
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
            'typeequipement': ('django.db.models.fields.CharField', [], {'max_length': '16', 'db_column': "u'typeEquipement'", 'blank': 'True'}),
            'utilisateur': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'equipements'", 'db_column': "u'utilisateur_id'", 'to': u"orm['rezo.Utilisateur']"})
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_rezo': ('django.db.models.fields.PositiveIntegerField', [], {})
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