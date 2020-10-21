from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name='female_filter')
@stringfilter
def female_filter(variable):
    return variable[-1].lower() == 'a'

