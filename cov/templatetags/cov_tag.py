from django import template
from ..models import Covoiturage
from django.utils import timezone

register = template.Library()

@register.inclusion_tag('cov/cov_block.html', takes_context=True)
def get_cov(context, nb):
	list_cov = Covoiturage.objects.select_related('poster').all().filter(good_until__gte=timezone.now()).order_by('good_until')[:nb]
	print list_cov
	ctx_data = {
        'cov' : list_cov,
        'request': context['request'],
    }
	return ctx_data
