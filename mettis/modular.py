from django.conf.urls import url, include

from modular_blocks import ModuleApp, TemplateTagBlock, modules


class MettisModule(ModuleApp):
    app_name = 'mettis'
    name = 'mettis'
    urls = None
    templatetag_blocks = [
        TemplateTagBlock(
            name='mettis-stops',
            library='mettis',
            tag='next_stops_display',
            cache_time=20,
        ),
    ]
modules.register(MettisModule)
