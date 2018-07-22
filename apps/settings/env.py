from .base import *  # NOQA

BOOLS = {'True': True, 'False': False, 'true': True, 'false': False, '1': True, '0': False}

DEBUG = BOOLS[os.environ.get('DJANGO_DEBUG', 'False')]

# HTTP
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', '*').split(',')
SESSION_COOKIE_SECURE = BOOLS[os.environ.get('DJANGO_SESSION_COOKIE_SECURE', 'False')]
CSRF_COOKIE_SECURE = BOOLS[os.environ.get('DJANGO_SESSION_COOKIE_SECURE', 'False')]


# Database
DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DJANGO_DATABASES__default__ENGINE'),
        'NAME': os.environ.get('DJANGO_DATABASES__default__NAME'),
        'USER': os.environ.get('DJANGO_DATABASES__default__USER'),
        'PASSWORD': os.environ.get('DJANGO_DATABASES__default__PASSWORD'),
        'HOST': os.environ.get('DJANGO_DATABASES__default__HOST'),
        'PORT': os.environ.get('DJANGO_DATABASES__default__PORT'),
    }
}


# Time
LANGUAGE_CODE = os.environ.get('DJANGO_LANGUAGE_CODE', 'en-us')
TIME_ZONE = os.environ.get('DJANGO_TIME_ZONE', 'UTC')
USE_I18N = BOOLS[os.environ.get('DJANGO_USE_I18N', 'True')]
USE_L10N = BOOLS[os.environ.get('DJANGO_USE_L10N', 'True')]
USE_TZ = BOOLS[os.environ.get('DJANGO_USE_TZ', 'True')]


# Management
ADMINS = [
    (os.environ[f'DJANGO_ADMINS__{i}__name'], os.environ[f'DJANGO_ADMINS__{i}__email'])
    for i in range(10)
    if f'DJANGO_ADMINS__{i}__name' in os.environ and f'DJANGO_ADMINS__{i}__email' in os.environ
]


## EMail
EMAIL_BACKEND = os.environ.get('DJANGO_EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')
EMAIL_HOST = os.environ.get('DJANGO_EMAIL_HOST', 'localhost')
EMAIL_USE_TLS = BOOLS[os.environ.get('DJANGO_EMAIL_USE_TLS', 'True')]
EMAIL_HOST_USER = os.environ.get('DJANGO_EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('DJANGO_EMAIL_HOST_PASSWORD')
EMAIL_PORT = os.environ.get('DJANGO_EMAIL_PORT', 587)


# Logging
if os.environ.get('RAVEN_CONFIG__dsn'):
    # https://raven.readthedocs.io/en/stable/integrations/django.html
    # import raven
    INSTALLED_APPS += ['raven.contrib.django.raven_compat']
    RAVEN_CONFIG = {
        'dsn': os.environ['RAVEN_CONFIG__dsn'],
        'release': os.environ.get('RAVEN_CONFIG__release', 'master'),
        #'release': raven.fetch_git_sha(PROJ_DIR),
    }
    LOGGING['handlers']['sentry'] = {
        'level': 'WARNING',
        'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
    }
    LOGGING['root']['handlers'].append('sentry')


# Caching
CACHES = {
    'default': {
        'BACKEND': os.environ.get('DJANGO_CACHES__default__BACKEND', 'django.core.cache.backends.locmem.LocMemCache'),
        'LOCATION': os.environ.get('DJANGO_CACHES__default__LOCATION'),
        'OPTIONS': {
            'CLIENT_CLASS': os.environ.get('DJANGO_CACHES__default__OPTIONS__CLIENT_CLASS'),
        },
    },
}

# MISC
TIMESTAMP_FORMAT = os.environ.get('TIMESTAMP_FORMAT', TIMESTAMP_FORMAT)
