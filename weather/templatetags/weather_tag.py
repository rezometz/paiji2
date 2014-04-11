from django import template
from .weather_fetcher import WeatherFetcher


register = template.Library()

@register.inclusion_tag('weather/weather_block.html')
def get_weather():
    wf = WeatherFetcher('fr', 'json', 'Metz')

    weather = wf.fetchWeather()

    ctx_data = {'weather' : weather}
    return ctx_data