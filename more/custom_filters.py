# custom_filters.py

from django import template

register = template.Library()

@register.filter
def append_to_list(list, item):
    list.append(item)
    return list
