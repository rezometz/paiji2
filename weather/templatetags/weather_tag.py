from django import template
from .weather_fetcher import WeatherFetcher
from django.core.cache import get_cache

register = template.Library()

KEY_CACHE_WEATHER = 'paiji2_weather_data'

@register.inclusion_tag('weather/weather_block.html')
def get_weather():
    cache = get_cache('default')
    weather = cache.get(KEY_CACHE_WEATHER)
    if (weather is None):
        wf = WeatherFetcher('fr', 'json', 'Metz')
        weather = wf.fetchWeather()
        # Cache weather info for 25 min
        cache.set(KEY_CACHE_WEATHER, weather, 60*25)

    ctx_data = {'weather' : weather}
    return ctx_data