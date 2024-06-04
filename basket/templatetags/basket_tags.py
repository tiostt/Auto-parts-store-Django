from django import template

from basket.utils import get_user_carts

register = template.Library()


@register.simple_tag()
def user_basket(request):
    return get_user_carts(request)