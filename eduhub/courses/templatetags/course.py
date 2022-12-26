from django import template

# custom filter to get the model name for each type of content item
register = template.Library()

@register.filter
def model_name(obj):
    try:
        return obj._meta.model_name
    except AttributeError:
        return None