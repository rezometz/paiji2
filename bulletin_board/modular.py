from django.conf.urls import url, include

from modular_blocks import ModuleApp, TemplateTagBlock, modules

from . import urls

class BulletinBoardModule(ModuleApp):
    app_name = 'bulletin_board'
    name = 'bulletin-board'
    urls = url(r'bulletin-board/', include(urls))
    templatetag_blocks = [
        TemplateTagBlock(
            name='bulletin-board',
            library='bulletin',
            tag='display_bulletin_board',
            cache_time=30 * 60,
            kwargs={
                'nb': 5,
            },
        ),
    ]
modules.register(BulletinBoardModule)
