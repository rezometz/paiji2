from django.conf.urls import url, include

from modular_blocks import ModuleApp, TemplateTagBlock, modules

from . import urls

class SurveyModule(ModuleApp):
    app_name = 'survey'
    name = 'survey'
    urls = url(r'^survey/', include(urls))
    templatetag_blocks = [
        TemplateTagBlock(
            name='survey-form',
            library='survey',
            tag='display_survey_form',
        ),
    ]


modules.register(SurveyModule)
