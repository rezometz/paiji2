from django import template

from ..models import Note


register = template.Library()


@register.inclusion_tag('bulletin_board/bulletin_board_short.html')
def display_bulletin_board(nb):
    return {
        'notes': Note.objects.all()[:nb],
    }
