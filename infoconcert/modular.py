from django.conf.urls import url, include

from modular_blocks import ModuleApp, TemplateTagBlock, modules


class InfoConcertModule(ModuleApp):
    app_name = 'infoconcert'
    name = 'infoconcert'
    urls = None
    templatetag_blocks = [
        TemplateTagBlock(
            name='infoconcert',
            library='infoconcert',
            tag='next_concerts',
            cache_time=30 * 60,
            kwargs={
                'nb': 5,
                'filter_free': False,
            },
        ),
    ]
modules.register(InfoConcertModule)
