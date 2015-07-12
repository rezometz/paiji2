# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Bannissements'
        db.create_table(u'bannissements', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('utilisateur_id', self.gf('django.db.models.fields.IntegerField')()),
            ('rezoteur_id', self.gf('django.db.models.fields.IntegerField')()),
            ('timestampdebut', self.gf('django.db.models.fields.IntegerField')(db_column=u'timestampDebut')),
            ('timestampfin', self.gf('django.db.models.fields.IntegerField')(db_column=u'timestampFin')),
            ('typeraison', self.gf('django.db.models.fields.CharField')(max_length=10, db_column=u'typeRaison')),
            ('raison', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'rezo', ['Bannissements'])

        # Adding model 'Banques'
        db.create_table(u'banques', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'rezo', ['Banques'])

        # Adding model 'Blocs'
        db.create_table(u'blocs', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.TextField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('ipdebut', self.gf('django.db.models.fields.CharField')(max_length=15, db_column=u'ipDebut')),
            ('ipfin', self.gf('django.db.models.fields.CharField')(max_length=15, db_column=u'ipFin')),
            ('alloueesparpaijiadmin', self.gf('django.db.models.fields.CharField')(max_length=1, db_column=u'alloueesParPaijiAdmin')),
        ))
        db.send_create_signal(u'rezo', ['Blocs'])

        # Adding model 'Documents'
        db.create_table(u'documents', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('nomdocument', self.gf('django.db.models.fields.TextField')(db_column=u'nomDocument')),
            ('descriptiondocument', self.gf('django.db.models.fields.TextField')(db_column=u'descriptionDocument')),
        ))
        db.send_create_signal(u'rezo', ['Documents'])

        # Adding model 'DocumentsEcoles'
        db.create_table(u'documents_ecoles', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('document_id', self.gf('django.db.models.fields.IntegerField')()),
            ('ecole_id', self.gf('django.db.models.fields.IntegerField')()),
            ('commentaires', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'rezo', ['DocumentsEcoles'])

        # Adding model 'DocumentsUtilisateurs'
        db.create_table(u'documents_utilisateurs', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('document_id', self.gf('django.db.models.fields.IntegerField')()),
            ('utilisateur_id', self.gf('django.db.models.fields.IntegerField')()),
            ('rezoteur_id', self.gf('django.db.models.fields.IntegerField')()),
            ('timestamp', self.gf('django.db.models.fields.IntegerField')()),
            ('secrpointage', self.gf('django.db.models.fields.IntegerField')(db_column=u'secrPointage')),
        ))
        db.send_create_signal(u'rezo', ['DocumentsUtilisateurs'])

        # Adding model 'Ecole'
        db.create_table(u'ecoles', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.TextField')(db_column=u'nomEcole')),
            ('description', self.gf('django.db.models.fields.TextField')(db_column=u'descriptionEcole')),
            ('rezotable', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'rezo', ['Ecole'])

        # Adding model 'Utilisateur'
        db.create_table(u'utilisateurs', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('ecole', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rezo.Ecole'])),
            ('precisionecole', self.gf('django.db.models.fields.TextField')(db_column=u'precisionEcole')),
            ('nom', self.gf('django.db.models.fields.TextField')()),
            ('prenom', self.gf('django.db.models.fields.TextField')()),
            ('topology_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.TextField')()),
            ('emailverifie', self.gf('django.db.models.fields.TextField')(db_column=u'emailVerifie')),
            ('borne_id', self.gf('django.db.models.fields.IntegerField')()),
            ('timestamprezotage', self.gf('django.db.models.fields.IntegerField')(db_column=u'timestampRezotage')),
            ('rezoteur_id', self.gf('django.db.models.fields.IntegerField')()),
            ('autorisationdecouvert', self.gf('django.db.models.fields.IntegerField')(db_column=u'autorisationDecouvert')),
            ('raisondecouvert', self.gf('django.db.models.fields.TextField')(db_column=u'raisonDecouvert')),
            ('etat', self.gf('django.db.models.fields.CharField')(max_length=14)),
            ('typeutilisateur', self.gf('django.db.models.fields.CharField')(max_length=11, db_column=u'typeUtilisateur')),
        ))
        db.send_create_signal(u'rezo', ['Utilisateur'])

        # Adding model 'Quotas'
        db.create_table(u'quotas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('utilisateur', self.gf('django.db.models.fields.related.OneToOneField')(related_name=u'quotas', unique=True, to=orm['rezo.Utilisateur'])),
            ('restant_veille_in', self.gf('django.db.models.fields.BigIntegerField')()),
            ('restant_veille_out', self.gf('django.db.models.fields.BigIntegerField')()),
            ('conso_in', self.gf('django.db.models.fields.BigIntegerField')()),
            ('conso_out', self.gf('django.db.models.fields.BigIntegerField')()),
            ('web_in', self.gf('django.db.models.fields.BigIntegerField')()),
            ('web_out', self.gf('django.db.models.fields.BigIntegerField')()),
            ('warning', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'rezo', ['Quotas'])

        # Adding model 'Equipement'
        db.create_table(u'equipements', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('utilisateur', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'equipements', db_column=u'utilisateur_id', to=orm['rezo.Utilisateur'])),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('dns', self.gf('django.db.models.fields.TextField')()),
            ('dnsrez', self.gf('django.db.models.fields.TextField')()),
            ('etat', self.gf('django.db.models.fields.CharField')(max_length=14)),
            ('timestampenregistrement', self.gf('django.db.models.fields.IntegerField')(db_column=u'timestampEnregistrement')),
            ('timestampdesactivationdefinitive', self.gf('django.db.models.fields.IntegerField')(db_column=u'timestampDesactivationDefinitive')),
            ('type_equip', self.gf('django.db.models.fields.CharField')(max_length=16, db_column=u'typeEquipement', blank=True)),
        ))
        db.send_create_signal(u'rezo', ['Equipement'])

        # Adding model 'Macs'
        db.create_table(u'macs', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=17, db_column=u'mac')),
            ('equipement', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'mac', db_column=u'equipement_id', to=orm['rezo.Equipement'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('etat', self.gf('django.db.models.fields.CharField')(max_length=14)),
            ('timestamplasttimeup', self.gf('django.db.models.fields.IntegerField')(db_column=u'timestampLastTimeUp')),
        ))
        db.send_create_signal(u'rezo', ['Macs'])

        # Adding model 'AccountRecovery'
        db.create_table(u'rezo_accountrecovery', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('id_rezo', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal(u'rezo', ['AccountRecovery'])

        # Adding model 'Paiements'
        db.create_table(u'paiements', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'paiements', db_column=u'utilisateur_id', to=orm['rezo.Utilisateur'])),
            ('rezoteur_id', self.gf('django.db.models.fields.IntegerField')()),
            ('timestamp', self.gf('django.db.models.fields.IntegerField')()),
            ('moyenpaiement', self.gf('django.db.models.fields.CharField')(max_length=7, db_column=u'moyenPaiement')),
            ('banque_id', self.gf('django.db.models.fields.IntegerField')()),
            ('chknumero', self.gf('django.db.models.fields.IntegerField')(db_column=u'chkNumero')),
            ('trezpointage', self.gf('django.db.models.fields.IntegerField')(db_column=u'trezPointage')),
            ('commentaires', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'rezo', ['Paiements'])

        # Adding model 'PaiementsVentilations'
        db.create_table(u'paiements_ventilations', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('paiement_id', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'paiements_ventilations', db_column=u'paiement_id', to=orm['rezo.Paiements'])),
            ('montant', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('prixunitaire', self.gf('django.db.models.fields.DecimalField')(db_column=u'prixUnitaire', decimal_places=2, max_digits=10)),
            ('affectation', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'rezo', ['PaiementsVentilations'])

        # Adding model 'User'
        db.create_table(u'rezo_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('is_staff', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('sidebar_left', self.gf('modular_blocks.fields.ListTextField')()),
            ('sidebar_right', self.gf('modular_blocks.fields.ListTextField')()),
            ('id_rezo', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, null=True)),
        ))
        db.send_create_signal(u'rezo', ['User'])

        # Adding M2M table for field groups on 'User'
        m2m_table_name = db.shorten_name(u'rezo_user_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'rezo.user'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'group_id'])

        # Adding M2M table for field user_permissions on 'User'
        m2m_table_name = db.shorten_name(u'rezo_user_user_permissions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'rezo.user'], null=False)),
            ('permission', models.ForeignKey(orm[u'auth.permission'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'permission_id'])


    def backwards(self, orm):
        # Deleting model 'Bannissements'
        db.delete_table(u'bannissements')

        # Deleting model 'Banques'
        db.delete_table(u'banques')

        # Deleting model 'Blocs'
        db.delete_table(u'blocs')

        # Deleting model 'Documents'
        db.delete_table(u'documents')

        # Deleting model 'DocumentsEcoles'
        db.delete_table(u'documents_ecoles')

        # Deleting model 'DocumentsUtilisateurs'
        db.delete_table(u'documents_utilisateurs')

        # Deleting model 'Ecole'
        db.delete_table(u'ecoles')

        # Deleting model 'Utilisateur'
        db.delete_table(u'utilisateurs')

        # Deleting model 'Quotas'
        db.delete_table(u'quotas')

        # Deleting model 'Equipement'
        db.delete_table(u'equipements')

        # Deleting model 'Macs'
        db.delete_table(u'macs')

        # Deleting model 'AccountRecovery'
        db.delete_table(u'rezo_accountrecovery')

        # Deleting model 'Paiements'
        db.delete_table(u'paiements')

        # Deleting model 'PaiementsVentilations'
        db.delete_table(u'paiements_ventilations')

        # Deleting model 'User'
        db.delete_table(u'rezo_user')

        # Removing M2M table for field groups on 'User'
        db.delete_table(db.shorten_name(u'rezo_user_groups'))

        # Removing M2M table for field user_permissions on 'User'
        db.delete_table(db.shorten_name(u'rezo_user_user_permissions'))


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
        u'rezo.bannissements': {
            'Meta': {'object_name': 'Bannissements', 'db_table': "u'bannissements'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'raison': ('django.db.models.fields.TextField', [], {}),
            'rezoteur_id': ('django.db.models.fields.IntegerField', [], {}),
            'timestampdebut': ('django.db.models.fields.IntegerField', [], {'db_column': "u'timestampDebut'"}),
            'timestampfin': ('django.db.models.fields.IntegerField', [], {'db_column': "u'timestampFin'"}),
            'typeraison': ('django.db.models.fields.CharField', [], {'max_length': '10', 'db_column': "u'typeRaison'"}),
            'utilisateur_id': ('django.db.models.fields.IntegerField', [], {})
        },
        u'rezo.banques': {
            'Meta': {'object_name': 'Banques', 'db_table': "u'banques'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.TextField', [], {})
        },
        u'rezo.blocs': {
            'Meta': {'object_name': 'Blocs', 'db_table': "u'blocs'"},
            'alloueesparpaijiadmin': ('django.db.models.fields.CharField', [], {'max_length': '1', 'db_column': "u'alloueesParPaijiAdmin'"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'ipdebut': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_column': "u'ipDebut'"}),
            'ipfin': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_column': "u'ipFin'"}),
            'nom': ('django.db.models.fields.TextField', [], {})
        },
        u'rezo.documents': {
            'Meta': {'object_name': 'Documents', 'db_table': "u'documents'"},
            'descriptiondocument': ('django.db.models.fields.TextField', [], {'db_column': "u'descriptionDocument'"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nomdocument': ('django.db.models.fields.TextField', [], {'db_column': "u'nomDocument'"})
        },
        u'rezo.documentsecoles': {
            'Meta': {'object_name': 'DocumentsEcoles', 'db_table': "u'documents_ecoles'"},
            'commentaires': ('django.db.models.fields.TextField', [], {}),
            'document_id': ('django.db.models.fields.IntegerField', [], {}),
            'ecole_id': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        u'rezo.documentsutilisateurs': {
            'Meta': {'object_name': 'DocumentsUtilisateurs', 'db_table': "u'documents_utilisateurs'"},
            'document_id': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'rezoteur_id': ('django.db.models.fields.IntegerField', [], {}),
            'secrpointage': ('django.db.models.fields.IntegerField', [], {'db_column': "u'secrPointage'"}),
            'timestamp': ('django.db.models.fields.IntegerField', [], {}),
            'utilisateur_id': ('django.db.models.fields.IntegerField', [], {})
        },
        u'rezo.ecole': {
            'Meta': {'object_name': 'Ecole', 'db_table': "u'ecoles'"},
            'description': ('django.db.models.fields.TextField', [], {'db_column': "u'descriptionEcole'"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.TextField', [], {'db_column': "u'nomEcole'"}),
            'rezotable': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'rezo.equipement': {
            'Meta': {'object_name': 'Equipement', 'db_table': "u'equipements'"},
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
            'Meta': {'object_name': 'Macs', 'db_table': "u'macs'"},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '17', 'db_column': "u'mac'"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'equipement': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'mac'", 'db_column': "u'equipement_id'", 'to': u"orm['rezo.Equipement']"}),
            'etat': ('django.db.models.fields.CharField', [], {'max_length': '14'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'timestamplasttimeup': ('django.db.models.fields.IntegerField', [], {'db_column': "u'timestampLastTimeUp'"})
        },
        u'rezo.paiements': {
            'Meta': {'object_name': 'Paiements', 'db_table': "u'paiements'"},
            'banque_id': ('django.db.models.fields.IntegerField', [], {}),
            'chknumero': ('django.db.models.fields.IntegerField', [], {'db_column': "u'chkNumero'"}),
            'commentaires': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'moyenpaiement': ('django.db.models.fields.CharField', [], {'max_length': '7', 'db_column': "u'moyenPaiement'"}),
            'rezoteur_id': ('django.db.models.fields.IntegerField', [], {}),
            'timestamp': ('django.db.models.fields.IntegerField', [], {}),
            'trezpointage': ('django.db.models.fields.IntegerField', [], {'db_column': "u'trezPointage'"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'paiements'", 'db_column': "u'utilisateur_id'", 'to': u"orm['rezo.Utilisateur']"})
        },
        u'rezo.paiementsventilations': {
            'Meta': {'object_name': 'PaiementsVentilations', 'db_table': "u'paiements_ventilations'"},
            'affectation': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'montant': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'paiement_id': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'paiements_ventilations'", 'db_column': "u'paiement_id'", 'to': u"orm['rezo.Paiements']"}),
            'prixunitaire': ('django.db.models.fields.DecimalField', [], {'db_column': "u'prixUnitaire'", 'decimal_places': '2', 'max_digits': '10'})
        },
        u'rezo.quotas': {
            'Meta': {'object_name': 'Quotas', 'db_table': "u'quotas'"},
            'conso_in': ('django.db.models.fields.BigIntegerField', [], {}),
            'conso_out': ('django.db.models.fields.BigIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'restant_veille_in': ('django.db.models.fields.BigIntegerField', [], {}),
            'restant_veille_out': ('django.db.models.fields.BigIntegerField', [], {}),
            'utilisateur': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "u'quotas'", 'unique': 'True', 'to': u"orm['rezo.Utilisateur']"}),
            'warning': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'web_in': ('django.db.models.fields.BigIntegerField', [], {}),
            'web_out': ('django.db.models.fields.BigIntegerField', [], {})
        },
        u'rezo.user': {
            'Meta': {'ordering': "(u'username',)", 'object_name': 'User'},
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
        u'rezo.utilisateur': {
            'Meta': {'object_name': 'Utilisateur', 'db_table': "u'utilisateurs'"},
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