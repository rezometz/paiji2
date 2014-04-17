from modular_blocks import ModuleApp, TemplateTagBlock, modules


class WeatherModule(ModuleApp):
    app_name = 'weather'
    name = 'weather'
    urls = None
    templatetag_blocks = [
        TemplateTagBlock(
            name='weather',
            library='weather_tag',
            tag='get_weather',
            cache_time=30 * 60,
        ),
    ]
modules.register(WeatherModule)
