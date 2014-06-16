from django import template
from django.db.models import Count
from django.utils.translation import ugettext_lazy as _

from graphos.renderers import morris
from graphos.sources.model import ModelDataSource

from ..models import Poll
from ..forms import SurveyVoteForm


register = template.Library()

@register.inclusion_tag(
    'survey/chart.html',
    takes_context=True,
)
def display_poll_chart(context, poll):
    print poll
    choices = poll.choices.annotate(nb_votes=Count('votes__user'))
    data_source = ModelDataSource(choices, fields=['value', 'nb_votes'])
    chart = morris.DonutChart(data_source, width=250, height=250, options={
        'title': _('Votes'),
    })
    return {
        'chart': chart,
    }
    

@register.inclusion_tag(
    'survey/form.html',
    takes_context=True,
)
def display_survey_form(context):
    poll = Poll.objects.current()
    vote = poll.vote_for(context['request'].user)
    if vote != None:
        return {
            'has_voted': True,
            'poll': poll,
        }
    else:
        return {
            'has_voted': False,
            'form': SurveyVoteForm(poll=poll),
            'poll': poll,
        }
