import urllib
import dateutil.parser
from bs4 import BeautifulSoup


class InfoConcertFetcher(object):
    url = 'https://www.infoconcert.com/ville/metz-2186/concerts.html'
    labels = {
        'Concert': 'primary',
        'Festival': 'success',
    }

    def __init__(self):
        self.content = BeautifulSoup(urllib.urlopen(self.url).read())

    def get_events(self, filter_free=False):
        for event in self.content.findAll('', {'itemtype': 'http://data-vocabulary.org/Event', }):
            etype = event.find('', {'itemprop': 'eventType'})['content']
            free = event.find('', {'class': 'btn_gratuit'}) != None
            cost = event.find('', {'class': 'lst_concert_prix'}).find('div').get_text().strip()
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
                    'url': 'http://www.infoconcert.com/' + event.find('', {'itemprop': 'url'})['href'],
                    'label': self.labels.get(etype, 'danger'),
                    'is_free': free,
                    'cost': cost,
                }
