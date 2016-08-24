"""
Local development and testing settings
"""
from .base_settings import *


# Debug allowed in development
DEBUG = True

ALLOWED_HOSTS = ['localhost']

# EMAIL #
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'default.db'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}


# -------------------------
# DJANGO TOOLBAR SETTINGS
# -------------------------

THIRD_PARTY_APPS += (
    'debug_toolbar',
)

MIDDLEWARE += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INSTALLED_APPS = DJANGO_CORE + THIRD_PARTY_APPS + LOCAL_APPS

INTERNAL_IPS = ('127.0.0.1',)


# ---------------------------
# END DJANGO TOOLBAR SETTINGS
# ---------------------------

