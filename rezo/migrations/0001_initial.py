# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import modular_blocks.fields
import django.contrib.auth.models
import django.utils.timezone
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ecole',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('nom', models.TextField(db_column='nomEcole')),
                ('description', models.TextField(db_column='descriptionEcole')),
                ('rezotable', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'ecoles',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Equipement',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('ip', models.CharField(max_length=15)),
                ('dns', models.TextField()),
                ('dnsrez', models.TextField()),
                ('etat', models.CharField(max_length=14)),
                ('timestampenregistrement', models.IntegerField(db_column='timestampEnregistrement')),
                ('timestampdesactivationdefinitive', models.IntegerField(db_column='timestampDesactivationDefinitive')),
                ('type_equip', models.CharField(max_length=16, db_column='typeEquipement', blank=True)),
            ],
            options={
                'db_table': 'equipements',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Macs',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('address', models.CharField(max_length=17, db_column='mac')),
                ('description', models.TextField()),
                ('etat', models.CharField(max_length=14)),
                ('timestamplasttimeup', models.IntegerField(db_column='timestampLastTimeUp')),
            ],
            options={
                'db_table': 'macs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Paiements',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('rezoteur_id', models.IntegerField()),
                ('timestamp', models.IntegerField()),
                ('moyenpaiement', models.CharField(max_length=7, db_column='moyenPaiement')),
                ('banque_id', models.IntegerField()),
                ('chknumero', models.IntegerField(db_column='chkNumero')),
                ('trezpointage', models.IntegerField(db_column='trezPointage')),
                ('commentaires', models.TextField()),
            ],
            options={
                'db_table': 'paiements',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PaiementsVentilations',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('montant', models.DecimalField(max_digits=10, decimal_places=2)),
                ('prixunitaire', models.DecimalField(decimal_places=2, max_digits=10, db_column='prixUnitaire')),
                ('affectation', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'paiements_ventilations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Topologies',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('rezoswitch_id', models.IntegerField()),
                ('port', models.IntegerField()),
                ('type', models.CharField(max_length=7)),
                ('nom', models.CharField(max_length=50)),
                ('idswitchconnecte', models.IntegerField(db_column='idSwitchConnecte')),
                ('equipement_id', models.IntegerField()),
            ],
            options={
                'db_table': 'topologies',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('precisionecole', models.TextField(db_column='precisionEcole')),
                ('nom', models.TextField()),
                ('prenom', models.TextField()),
                ('email', models.TextField()),
                ('emailverifie', models.TextField(db_column='emailVerifie')),
                ('borne_id', models.IntegerField()),
                ('timestamprezotage', models.IntegerField(db_column='timestampRezotage')),
                ('rezoteur_id', models.IntegerField()),
                ('autorisationdecouvert', models.IntegerField(db_column='autorisationDecouvert')),
                ('raisondecouvert', models.TextField(db_column='raisonDecouvert')),
                ('etat', models.CharField(max_length=14)),
                ('typeutilisateur', models.CharField(max_length=11, db_column='typeUtilisateur')),
            ],
            options={
                'db_table': 'utilisateurs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, verbose_name='username')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('sidebar_left', modular_blocks.fields.ListTextField(null=True, blank=True)),
                ('sidebar_right', modular_blocks.fields.ListTextField(null=True, blank=True)),
                ('id_rezo', models.PositiveIntegerField(default=0, null=True)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'ordering': ('username',),
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AccountRecovery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_rezo', models.PositiveIntegerField()),
                ('date', models.DateTimeField()),
                ('code', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Quotas',
            fields=[
                ('utilisateur', models.OneToOneField(related_name='quotas', primary_key=True, db_column='id', serialize=False, to='rezo.Utilisateur')),
                ('restant_veille_in', models.BigIntegerField()),
                ('restant_veille_out', models.BigIntegerField()),
                ('conso_in', models.BigIntegerField()),
                ('conso_out', models.BigIntegerField()),
                ('web_in', models.BigIntegerField()),
                ('web_out', models.BigIntegerField()),
                ('warning', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'quotas',
                'managed': False,
            },
        ),
    ]
