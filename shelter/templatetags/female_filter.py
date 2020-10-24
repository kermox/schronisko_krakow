from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name='female_filter')
@stringfilter
def female_filter(variable):
    """
    Simple function to know the gender by name ending. If name ends with 'a' - it is female's name.
    """
    return variable[-1].lower() == 'a'

