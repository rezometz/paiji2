from django import template


register = template.Library()


@register.inclusion_tag(
    'rezo/user/summary.html',
    takes_context=True,
)
def display_rezo_account_information(context):
    return {
        'request': context['request'],
    }
