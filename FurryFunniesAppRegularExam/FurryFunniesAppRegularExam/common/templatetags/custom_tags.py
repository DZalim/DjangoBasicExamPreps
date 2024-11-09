from django import template

from FurryFunniesAppRegularExam.common.helpers import get_author_obj

register = template.Library()


@register.simple_tag
def get_author():
    return get_author_obj()
