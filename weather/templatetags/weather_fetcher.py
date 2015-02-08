import urllib
import django.utils.simplejson as json
from datetime import date


class WeatherFetcher(object):
    """fetch Weather information from openweathermap API"""
    def __init__(self, lang, format, city):
        super(WeatherFetcher, self).__init__()
        self.lang = lang
        self.format = format
        self.city = city

        self.currentWeatherUrl = (
            "http://api.openweathermap.org/data/2.5/weather"
            "?q={city}&mode={mode}&lang={lang}&units=metric&type=like"
        ).format(city=self.city, mode=self.format, lang=self.lang)
        self.forcastWeatherUrl = (
            "http://api.openweathermap.org/data/2.5/forecast/daily"
            "?q={city}&mode={mode}&lang={lang}&units=metric&cnt=4&type=like"
        ).format(city=self.city, mode=self.format, lang=self.lang)

        # FIXME : The mapper should explains to which
        # weather corresponds each letter
        self.icon_mapper = {
            '01': 'day-sunny',
            '02': 'day-cloudy',
            '03': 'cloud',
            '04': 'cloudy',
            '09': 'showers',
            '10': 'rain',
            '11': 'lightning',
            '13': 'snow',
            '50': 'fog',
        }

    def fetchJson(self, url):
        return json.loads(urllib.urlopen(url).read())

    def fetchWeather(self):
        try:
            current = self.fetchJson(self.currentWeatherUrl)
            forcast = self.fetchJson(self.forcastWeatherUrl)
        except:
            return None

        list_weather = []

        temperature = {
            'current': current['main']['temp'],
            'forcast': forcast['list'],
        }
        current_description = [current['weather'][0]['description']]
        forcast_description = [
            w['weather'][0]['description'] for w in forcast['list']
        ]
        description = current_description + forcast_description

        icons = [self.icon_mapper[w['weather'][0]['icon'][:2]]
                for x in forcast['list']]

        for x in xrange(4):
            list_weather.append({
                'timestamp': date.fromtimestamp(forcast['list'][x]['dt']),
                'icon': icons[x],
                'min': temperature['forcast'][x]['temp']['min'],
                'max': temperature['forcast'][x]['temp']['max'],
                'desc': description[x],
                })
            list_weather[0]['current'] = current['main']['temp']
        return {
                'city': current['name'],
                'list_weather': list_weather,
                }
