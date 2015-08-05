# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        db.rename_table('survey_poll', 'paiji2_survey_poll')
        db.rename_table('survey_vote', 'paiji2_survey_vote')
        db.rename_table('survey_choice', 'paiji2_survey_choice')

    def backwards(self, orm):
        db.rename_table('paiji2_survey_poll', 'survey_poll')
        db.rename_table('paiji2_survey_vote', 'survey_vote')
        db.rename_table('paiji2_survey_choice', 'survey_choice')

    models = {

    }

    complete_apps = ['home']
