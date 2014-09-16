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


    for stop_setting in settings.METTIS_STOPS:
        next_stops = m.next_bus_stops(
                stop_setting['line'], stop_setting['direction'], stop_setting['from_stop'],
                stops_number=3,
            )
        error = None
        if not next_stops:
            error = 'Not available'
        stops.append({
            'line': stop_setting['line'],
            'direction': stop_setting['direction'],
            'from_stop': stop_setting['from_stop'],
            'next_stops': next_stops,
            'error': error
        })
    return {
        'stops': stops,
        'url': m.make_url(stop_setting['url_1'], stop_setting['url_2'], stop_setting['url_3']),
    }
