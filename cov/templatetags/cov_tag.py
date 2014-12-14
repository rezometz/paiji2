from django import template
from ..models import Covoiturage
from django.utils import timezone

register = template.Library()

@register.inclusion_tag('cov/cov_block.html', takes_context=True)
def get_cov(context, nb):
	return {
        'cov' : Covoiturage.objects.select_related('author').filter(
            good_until__gte=timezone.now()
        ).order_by('good_until')[:nb],
        'request': context['request'],
    }
