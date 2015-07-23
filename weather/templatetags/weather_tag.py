from django import template
from .weather_fetcher import WeatherFetcher
from django.core.cache import get_cache
from django.conf import settings
from django.utils.translation import get_language


register = template.Library()


@register.inclusion_tag('weather/weather_block.html')
def get_weather():
    cache = get_cache('default')
    weather = cache.get(settings.KEY_CACHE_WEATHER)
    if weather is None:
        try:
            wf = WeatherFetcher(get_language(), 'json', 'Metz')
        except:
            try:
                wf = WeatherFetcher(settings.LANGUAGE_CODE, 'json', 'Metz')
            except:
                wf = WeatherFetcher('en', 'json', 'Metz')
        weather = wf.fetchWeather()
        # Cache weather info for 10 min
        cache.set(settings.KEY_CACHE_WEATHER, weather, 60*10)

    return {
        'weather': weather,
    }
