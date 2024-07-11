from django import template
from ..models import Platform

register = template.Library()

@register.simple_tag
def get_all_platforms():
    return Platform.objects.all()