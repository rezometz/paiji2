from django import template
from django.conf import settings

from ..fetcher import MettisFetcher


register = template.Library()


@register.inclusion_tag(
    'mettis/next_stops.html',
)
def next_stops_display():
    m = MettisFetcher()
    stops = []
    for stop in settings.METTIS_STOPS:
        stops.append({
            'line': stop[0],
            'head': stop[1],
            'stop': stop[2],
            'time': m.next_bus(stop[3], stop[4], stop[5]),
        })
    return {
        'stops': stops,
    }

