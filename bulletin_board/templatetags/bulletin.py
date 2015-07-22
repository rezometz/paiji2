import re

from django import template
from django.core.urlresolvers import reverse

from ..models import Note
from ..forms import NoteForm


register = template.Library()


@register.inclusion_tag('bulletin_board/bulletin_board_short.html', takes_context=True)
def display_bulletin_board(context, nb=5):
    return {
        'request': context['request'],
        'notes': Note.objects.select_related('author').all()[:nb],
        'form':NoteForm(),
        'bulletin_add':reverse('bulletin-add'),
    }


@register.filter
def urlize2(text):
    url_regex = re.compile(r'((ftp|https?)://\S*)')
    def replacement(matchobj):
        return ('<a href="{link}">[link]</a>').format(
            link=matchobj.group(0),
        )
    return re.sub(url_regex, replacement, text)

