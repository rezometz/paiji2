import re
import urllib

from bs4 import BeautifulSoup

from django.core.cache import cache
from django.utils.timezone import now, localtime

class MettisFetcher(object):
    url = 'http://lemet.fr/src/page_editions_horaires_iframe_build.php'
    params = '?ligne={ligne}&head={head}&arret={arret}'
    
    def make_url(self, ligne, head, arret):
        return self.url + self.params.format(
            ligne=ligne,
            head=head,
            arret=arret,
        )
    
    def get_schedule(self, ligne, head, arret):
        url = self.make_url(ligne, head, arret)
        content = BeautifulSoup(urllib.urlopen(url).read())

        schedule = content.find('', {'id': 'horaires'})

        week = schedule.find('', {'class': 'un'})
        saturday = schedule.find('', {'class': 'deux'})
        sunday = schedule.find('', {'class': 'trois'})

        return {
            'week': [x for x in self.extract_schedule(week)],
            'saturday': [x for x in self.extract_schedule(saturday)],
            'sunday': [x for x in self.extract_schedule(sunday)],
        }

    def extract_schedule(self, timetable):
        for row in timetable.findAll('tr'):
            cells = row.findAll('td')
            hour = cells[0].get_text().strip()
            hour = int(re.search('(\d+)', hour).group(0))
            for cell in cells[1:]:
                minutes = cell.get_text().strip()
                if minutes != '':
                    if minutes == '1 toutes les 10 minutes':
                        for x in range(0, 60, 10):
                            yield {
                                'hour': hour,
                                'minutes': x,
                                'approximated': True,
                            }
                    else:
                        yield {
                            'hour': hour,
                            'minutes': int(minutes),
                            'approximated': False,
                        }

            
    def next_bus(self, ligne, head, arret):
        key = 'mettis_{ligne}_{head}_{arret}'.format(
            ligne=ligne, head=head, arret=arret,
        )
        data = cache.get(key)
        if data is None:
            data = self.get_schedule(ligne, head, arret)
            cache.set(key, data, 1 * 24 * 60 * 60)


        date = localtime(now())
        weekday = date.weekday()
        if weekday <= 4:
            timetable = data['week']
        elif weekday == 5:
            timetable = data['saturday']
        elif weekday == 6:
            timetable = data['sunday']

        schedule = timetable[0]
        for time in timetable[1:]:
            if date.hour >= schedule['hour'] and date.minute >= schedule['minutes'] \
                and date.hour <= time['hour'] and date.minute <= time['minutes']:
                schedule = time
                break
            schedule = time

        if schedule is None:
            schedule = timetable[0]

        return date.replace(hour=schedule['hour'], minute=schedule['minutes'])
