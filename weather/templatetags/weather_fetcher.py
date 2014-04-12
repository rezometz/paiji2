import urllib
import django.utils.simplejson as json
from datetime import date

# Create your models here.
class WeatherFetcher(object):
    """fetch Weather information from openweathermap API"""
    def __init__(self, lang, format, city):
        super(WeatherFetcher, self).__init__()
        self.lang = lang
        self.format = format
        self.city = city

        self.currentWeatherUrl = "http://api.openweathermap.org/data/2.5/weather?q="+self.city+"&mode="+self.format+"&lang="+self.lang+"&units=metric&type=like"
        self.forcastWeatherUrl = "http://api.openweathermap.org/data/2.5/forecast/daily?q="+self.city+"&mode="+self.format+"&lang="+self.lang+"&units=metric&cnt=4&type=like"

        self.icon_mapper = {'01':'B', '02':'H', '03':'N', '04':'Y', '09':'Q', '10':'R', '11':'6', '13':
        '#', '50':'M'}

    def fetchJson(self, url):
        u = urllib.FancyURLopener(None)

        usock = u.open(url)
        rawdata = usock.read()
        usock.close()
        return json.loads(rawdata)

    def fetchWeather(self):
        current = self.fetchJson(self.currentWeatherUrl)
        forcast = self.fetchJson(self.forcastWeatherUrl)

        list_weather = []

        temperature = {'current' : current['main']['temp'], 'forcast' : forcast['list']}
        description = [current['weather'][0]['description']] + [w['weather'][0]['description'] for w in forcast['list']]
        icons = [self.icon_mapper[ w['weather'][0]['icon'][:-1] ] for w in forcast['list']]

        for x in xrange(4):
            list_weather.append({'timestamp':date.fromtimestamp(forcast['list'][x]['dt']), 'icon':icons[x], 'min':temperature['forcast'][x]['temp']['min'], 'max':temperature['forcast'][x]['temp']['max'], 'desc':description[x]})
        list_weather[0]['current'] = current['main']['temp']

        weather = {'city' : current['name'], 'list_weather' : list_weather}
        return weather