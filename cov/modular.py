from django.conf.urls import url, include

from modular_blocks import ModuleApp, TemplateTagBlock, modules


class CovModule(ModuleApp):
    app_name = 'cov'
    name = 'cov'
    urls = url(r'^cov/', include('cov.urls'))
    templatetag_blocks = [
        TemplateTagBlock(
            name='cov',
            library='cov_tag',
            tag='get_cov',
            cache_time=60,
            kwargs={
                'nb': 5,
            }
        ),
    ]
modules.register(CovModule)
