import builtins
import json
import datetime
import string

from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib import messages
from django.urls import reverse
from django.conf import settings
from jinja2 import Environment


STANDARD_MODULE_CONTEXT = {
    'datetime': datetime,
    'json': json,
    'string': string,
}

DJANGO_CONTEXT = {
    'static': staticfiles_storage.url,
    'url': reverse,
    'get_messages': messages.get_messages,
}


def environment(**options):
    env = Environment(**options)
    env.globals.update(vars(builtins))
    env.globals.update(DJANGO_CONTEXT)
    env.globals.update(STANDARD_MODULE_CONTEXT)
    env.globals['changelog_hash'] = settings.CHANGELOG_HASH
    return env