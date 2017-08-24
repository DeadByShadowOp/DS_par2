
from django import template
register = template.Library()


@register.filter(name='get_total_price')
def get_total_price(obj):
    return obj.get_total_price()


@register.filter(name='get_extras')
def get_extras(obj):
    return obj.get_extras()
