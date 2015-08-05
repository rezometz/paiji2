import re
import urllib2
import socket

from bs4 import BeautifulSoup

from django.core.cache import cache
from django.utils.timezone import now, localtime


def nest_list(x0, f, n):
    """
        Useful function to create a list of n elements from a given object
        x0 and a function f (tail-recursive)
        nest_list(x0, f, n) -> [x0, f(x0), f^2(x0), ..., f^(n-1)(x0)]
    """
    def nest(f, n, l):
        if n == 0:
            return l
        next = f(l[-1])
        if next is None:
            return None
        l.append(next)
        return nest(f, n-1, l)
    return nest(f, n, [x0])


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
        try:
            content = BeautifulSoup(urllib2.urlopen(url, timeout=0.5).read())
        except socket.timeout:
            print "mettis fetcher timed out"
            return None
        except urllib2.URLError:
            print "Url failed: internet connection?"
            return None

        schedule = content.find('', {'id': 'horaires'})

        if schedule is None:
            return None
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

    def find_next_stop(self, from_time):
        if self.data is None or from_time is None:
            return None
        from_time = from_time.replace(minute=from_time.minute)
        weekday = from_time.weekday()
        if weekday <= 4:
            timetable = self.data['week']
        elif weekday == 5:
            timetable = self.data['saturday']
        elif weekday == 6:
            timetable = self.data['sunday']

        schedule = timetable[0]
        for time in timetable[1:]:
            if ((from_time.hour >= schedule['hour'] and from_time.minute >= schedule['minutes']) or from_time.hour > schedule['hour']) \
                and ((from_time.hour <= time['hour'] and from_time.minute < time['minutes']) or from_time.hour < time['hour']):
                schedule = time
                break
            schedule = time

        if schedule is None:
            schedule = timetable[0]

        return from_time.replace(hour=schedule['hour'], minute=schedule['minutes'])

    def next_bus_stops(self, ligne, head, arret, stops_number=1):
        key = 'mettis_{ligne}_{head}_{arret}'.format(
            ligne=ligne, head=head, arret=arret,
        ).replace(' ', '-')
        self.data = cache.get(key)
        if self.data is None:
            self.data = self.get_schedule(ligne, head, arret)
            if self.data is None:
                return None
            else:
                cache.set(key, self.data, 1 * 24 * 60 * 60)

        return nest_list(localtime(now()), self.find_next_stop, stops_number)
