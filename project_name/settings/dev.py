# Django Dev settings for {{ project_name }} project.

from os.path import normpath, join
from .common import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG
# This makes runserver send exceptions to the console
# DEBUG_PROPAGATE_EXCEPTIONS = DEBUG

# Test if django-nose is available
try:
    import django_nose
    HAS_nose = True
    try:
        import pinocchio
        import nose_cov
        HAS_noseaddons = True
    except ImportError:
        HAS_noseaddons = False
except ImportError:
    HAS_nose = False

# Test if devserver is available
try:
    import devserver
    HAS_devserver = True
except ImportError:
    HAS_devserver = False


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': normpath(join(PROJECT_ROOT, 'default.db')),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}


# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = '{{ project_name }}.wsgi_dev.application'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = normpath(join(PROJECT_ROOT, 'static_root'))

# Some commonly set django-compressor options
#COMPRESS_ENABLED = True
#COMPRESS_OFFLINE = True
# Typlically you would uncomment these when using compress_enabled in development:
#COMPRESS_CSS_FILTERS = []
#COMPRESS_JS_FILTERS = []

# This configures any extra content types inside compress tags, and will automaticaly
# precompile it for you.
#
# These assume you have coffeescript and less installed with nodejs npm command
# Note: less installed using ruby doesn't work as well.
#COMPRESS_PRECOMPILERS = (
#    ('text/coffeescript', 'coffee --compile --stdio'),
#    ('text/less', 'lessc {infile} {outfile}'),
#)

INSTALLED_APPS += (
    # Any dev-only apps to include
)

# Configuring optional devserver
if HAS_devserver:
    INSTALLED_APPS += (
        # django-devserver documentation: https://github.com/dcramer/django-devserver
        'devserver',
    )

# Configuring optional nose & addons
if HAS_nose:
    INSTALLED_APPS += (
        # django-nose testing framework: http://nose.readthedocs.org/ 
        'django_nose',
    )

    # Nose configuration
    TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
    if HAS_noseaddons:
        # Do test coverage + spec output in colour
        NOSE_ARGS = ['--with-cov','--cov-report=term-missing','--with-spec','--spec-color']

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Django Cacheing
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

# Celery
'''
# See: http://docs.celeryq.org/en/latest/configuration.html#celery-always-eager
CELERY_ALWAYS_EAGER = True
# Tests run in-queue
TEST_RUNNER = 'djcelery.contrib.test_runner.CeleryTestSuiteRunner'
'''

