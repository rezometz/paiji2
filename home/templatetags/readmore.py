from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe

register = template.Library()

import re


@register.filter
def readmore(txt, showwords=15):
    readmore_showscript = ''.join([
        'this.parentNode.style.display=\'none\';',
        'this.parentNode.parentNode.getElementsByClassName(\'more\')[0].style.display=\'inline\';',
        'return false;',
    ])
    words = re.split(r' ', txt)

    # wrap the more part
    if len(words) > showwords:
        words.insert(showwords, '<span class="more" style="display:none;">')
        words.append('</span>')

        # insert the readmore part
        words.insert(showwords, '<span class="readmore">... <a href="#" onclick="')
        words.insert(showwords+1, readmore_showscript)
        words.insert(showwords+2, '">read more</a>')
        words.insert(showwords+3, '</span>')

        # Wrap with <p>
        #words.insert(0, '<p>')
        #words.append('</p>')

    return mark_safe(' '.join(words))
