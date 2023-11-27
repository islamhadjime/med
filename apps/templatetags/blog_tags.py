from django import template
register = template.Library()
from ..models import Category

@register.simple_tag
def total_posts():
    return Category.objects.all()