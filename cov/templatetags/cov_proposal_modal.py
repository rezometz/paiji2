from django import template
from django.forms.models import modelformset_factory
from django.shortcuts import render_to_response

from cov.models import Covoiturage as Cov
from cov.models import CovoiturageForm as CovForm

from django.utils import timezone

register = template.Library()

@register.inclusion_tag('cov/propose_modal.html', takes_context = True)
def get_proposal_modal(context):
	request = context['request']
	print "getting REQUEST##########"
	CovFormSet = modelformset_factory(Cov, formset=CovForm)
	if request.method == 'POST':
		formset = CovFormSet(request.POST, request.FILES)
		print "getting POST##########"
		if formset.is_valid():
			print "getting VALID##########"
			formset.save()
	else:
		formset = CovFormSet()

	return {"formset": formset,}
