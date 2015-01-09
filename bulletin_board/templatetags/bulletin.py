from django import template

from ..models import Note
from ..forms import NoteForm

from django.core.urlresolvers import reverse

register = template.Library()


@register.inclusion_tag('bulletin_board/bulletin_board_short.html', takes_context=True)
def display_bulletin_board(context, nb=5):
	return {
        'request': context['request'],
        'notes': Note.objects.select_related('author').all()[:nb],
        'form':NoteForm(),
        'bulletin_add':reverse('bulletin-add'),
    }
