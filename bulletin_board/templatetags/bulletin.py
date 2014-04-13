from django import template

from ..models import Note


register = template.Library()


@register.inclusion_tag(
    'bulletin_board/bulletin_board_short.html',
    takes_context=True,
)
def display_bulletin_board(context, nb):
    return {
        'request': context['request'],
        'notes': Note.objects.select_related('author').all()[:nb],
    }
