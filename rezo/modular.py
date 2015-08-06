from django.conf.urls import url, include

from modular_blocks import ModuleApp, TemplateTagBlock, modules

from . import urls


class RezoModule(ModuleApp):
    app_name = 'rezo'
    name = 'account-information'
    urls = url(r'rezo/', include(urls))
    templatetag_blocks = [
        TemplateTagBlock(
            name='rezo-account',
            library='rezo',
            tag='display_rezo_account_information',
            cache_time=60,
        ),
    ]


modules.register(RezoModule)
