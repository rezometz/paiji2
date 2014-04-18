from django import template
from .weather_fetcher import WeatherFetcher
from django.core.cache import get_cache
from django.conf import settings

register = template.Library()

@register.inclusion_tag('weather/weather_block.html')
def get_weather():
    cache = get_cache('default')
    weather = cache.get(settings.KEY_CACHE_WEATHER)
    if (weather is None):
        wf = WeatherFetcher('fr', 'json', 'Metz')
        weather = wf.fetchWeather()
        # Cache weather info for 25 min
        cache.set(settings.KEY_CACHE_WEATHER, weather, 60*25)

    ctx_data = {'weather' : weather}
    return ctx_data
