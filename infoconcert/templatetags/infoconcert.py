import itertools

from django import template

from ..fetcher import InfoConcertFetcher


register = template.Library()

@register.inclusion_tag('infoconcert/block.html')
def next_concerts(nb=5, filter_free=False):
	return {
        'events': itertools.islice(InfoConcertFetcher().get_events(filter_free=filter_free), 0, nb),
    }
