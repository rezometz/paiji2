from django import template
from datetime import *

register = template.Library()

@register.simple_tag
def copyright_year():
    return datetime.now().year
