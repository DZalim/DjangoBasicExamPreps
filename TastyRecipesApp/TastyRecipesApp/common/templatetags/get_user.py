from django import template

from TastyRecipesApp.common.helpers import get_user_obj

register = template.Library()


@register.simple_tag
def get_user():
    return get_user_obj()
