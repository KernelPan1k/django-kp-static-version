from django import template
from django.conf import settings
from django.templatetags.static import static

register = template.Library()


@register.simple_tag
def vstatic(path):
    static_path = static(path)
    is_debug = getattr(settings, 'DEBUG')

    if is_debug:
        from random import randint
        version = randint(1, 10000)
    else:
        version = getattr(settings, 'KP_STATIC_VERSION', '0.1')

    return "%s?v=%s" % (static_path, str(version))
