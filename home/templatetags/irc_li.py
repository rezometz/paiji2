from django import template
from django.conf import settings

register = template.Library()


@register.inclusion_tag('home/irc_li.html', takes_context=True)
def irc_li(context):
    if hasattr(settings, 'IRC'):
        irc = settings.IRC
    else:
        irc = None
    return {
        'user': context['request'].user,
        'irc': irc,
    }
