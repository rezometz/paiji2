from django import template
from cov import models
from django.utils import timezone

register = template.Library()

@register.inclusion_tag('cov/cov_block.html')
def get_cov():
	list_cov = models.Covoiturage.objects.all().filter(dept_datetime__gte=timezone.now()).order_by('dept_datetime')[:5]
	ctx_data = {'cov' : list_cov}
	return ctx_data
