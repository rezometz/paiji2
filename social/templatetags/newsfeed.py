from django import template
from ..models import Message

register = template.Library()

@register.inclusion_tag('social/newsfeed_block.html', takes_context=True)
def display_newsfeed(context, nb):
	return {
        'messages' : Message.objects.all().order_by('-pubDate')[:nb],
        'request': context['request'],
    }
