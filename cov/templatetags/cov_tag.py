from django import template

register = template.Library()

@register.inclusion_tag('cov/cov_block.html')
def get_cov():
    ctx_data = {'cov' : None}
    return ctx_data