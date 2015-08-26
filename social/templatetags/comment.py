from django import template

from ..models import Comment  # , Message
from ..forms import CommentForm


register = template.Library()


@register.inclusion_tag(
    'social/comment_area.html',
    takes_context=True,
)
def display_comment_area(context, on_message, nb=5):
    comments = Comment.objects.select_related('author').filter(
        message=on_message
    ).order_by('pubDate')[:nb]

    return {
        'request': context['request'],
        'comments': comments,
        'on_message': on_message,
        'form': CommentForm(),
    }
