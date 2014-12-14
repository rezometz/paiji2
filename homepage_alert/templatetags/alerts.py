from django import template

from django.utils.timezone import now

from ..models import Alert
from .. import CACHE_KEY


register = template.Library()


@register.inclusion_tag('homepage_alerts/alerts.html')
def display_alerts():
    return {
        'alerts': Alert.objects.filter(
            end_date__gte=now(),
        ).select_related('author').order_by('end_date'),
        'CACHE_KEY': CACHE_KEY,
    }
