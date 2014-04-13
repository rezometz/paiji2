from django import template
from cov import models
from django.utils import timezone

register = template.Library()

@register.inclusion_tag('cov/cov_block.html', takes_context=True)
def get_cov(context):
	list_cov = models.Covoiturage.objects.all().filter(good_until__gte=timezone.now()).order_by('good_until')[:5]
	ctx_data = {
        'cov' : list_cov,
        'request': context['request'],
    }
	return ctx_data
