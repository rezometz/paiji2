import urllib2
import dateutil.parser
import socket

from bs4 import BeautifulSoup


class InfoConcertFetcher(object):
    url = 'https://www.infoconcert.com/ville/metz-2186/concerts.html'
    labels = {
        'Concert': 'primary',
        'Festival': 'success',
    }

    def __init__(self):
        try:
            self.content = BeautifulSoup(urllib2.urlopen(self.url, timeout=0.5).read())
        except socket.timeout:
            print "Infoconcert timeout"
            self.content = None
        except urllib2.URLError:
            print "Infoconcert no internet access?"
            self.content = None

    def get_events(self, filter_free=False):
        for event in self.content.findAll('', {'itemtype': 'http://data-vocabulary.org/Event', }):
            etype = event.find('', {'itemprop': 'eventType'})['content']
            free = event.find('', {'class': 'btn_gratuit'}) != None
            cost = event.find('', {'class': 'price'});
            if cost is None:
                continue

            if not filter_free or free:
                yield {
                    'type': etype,
                    'summary': event.find('', {'itemprop': 'summary'}).text.strip().title(),
                    'organization': {
                        'locality': event.find('', {'itemprop': 'locality'}).text,
                        'name': event.find('', {'itemprop': 'name'}).text,
                    },
                    'date': dateutil.parser.parse(
                        event.find('', {'itemprop': 'startDate'})['datetime']
                    ),
                    'url': 'http://www.infoconcert.com/',
                    'label': self.labels.get(etype, 'danger'),
                    'is_free': free,
                    'cost': cost.get_text().strip(),
                }
