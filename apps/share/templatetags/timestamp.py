from django import template
from django.utils import timezone
from django.conf import settings

NOW = timezone.now()

register = template.Library()

@register.simple_tag
def timestamp(fmt=settings.TIMESTAMP_FORMAT):
    now = timezone.now() if settings.DEBUG else NOW
    return now.strftime(fmt)
