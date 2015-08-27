from django import template
from django.conf import settings
from django.core.urlresolvers import reverse

register = template.Library()


@register.simple_tag
def profile_url(user):
    try:
        return settings.PROFILE_URL(user)
    except:
        return reverse(
            'user-profile',
            kwargs={
                'username': user.username,
            },
        )
