import re

from django import template
# from django.utils.html import escape
from django.utils.safestring import mark_safe


register = template.Library()


# TODO: this function is not clean, are you trying to write PHP guys?
@register.filter
def readmore(txt, showwords=15):
    # TODO should be an external javascript function
    readmore_showscript = (
        """this.parentNode.style.display='none';"""
        """this.parentNode.parentNode.getElementsByClassName('more')[0]"""
        """.style.display='inline';"""
        """return false;"""
    )
    words = re.split(r' ', txt)

    # wrap the more part
    if len(words) > showwords:
        words.insert(showwords, '<span class="more" style="display:none;">')
        words.append('</span>')

        # insert the readmore part
        dots = '<span class="readmore">... <a href="#" onclick="'
        words.insert(showwords, dots)
        words.insert(showwords+1, readmore_showscript)
        words.insert(showwords+2, '">read more</a>')
        words.insert(showwords+3, '</span>')

    # TODO SECURITY: actually that's not safe at all..
    return mark_safe(' '.join(words))
