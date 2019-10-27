from .base import *

import json

from django.core.exceptions import ImproperlyConfigured

# Secure Secret Key Logic

# JSON-based secrets module
with open(os.path.join(BASE_DIR, 'local-secrets.json')) as f:
    secrets = json.loads(f.read())


def get_secret(setting, secrets=secrets):
    """Get the secret variable or return explicit exception."""
    try:
        return secrets[setting]
    except KeyError:
        error_msg = 'Set the {0} environment variable'.format(setting)
        raise ImproperlyConfigured(error_msg)


# Basic Settings

SECRET_KEY = get_secret('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = ['*']

# Installed Apps

INSTALLED_APPS += [
    'core',
    'website',
]

# Databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'data', 'db.sqlite3'),
    }
}

# Static Files

STATIC_URL = '/static/'

# Email Backend

EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Login Settings

LOGIN_URL = 'core:login'
DEFAULT_PAGE = 'website:home_page'

# Google ReCaptcha

RECAPTCHA_SECRET_KEY = get_secret('RECAPTCHA_SECRET_KEY')
RECAPTCHA_SITE_KEY = get_secret('RECAPTCHA_SITE_KEY')

# 2019.09.02-DEA
