from django import template
# Esta es la forma como puedes crear tus propios filtros en Django
register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)