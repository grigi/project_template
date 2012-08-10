# Django settings for {{ project_name }} project.
from os.path import abspath, dirname, normpath, join
from datetime import timedelta
import {{ project_name }}

DEBUG = False

# Optional support
# Change the following to True and uncomment its counterparts in both setup.py and requirements.txt
HAS_compressor = False
HAS_haml = False
HAS_celery = False
HAS_south = False


ADMINS = (
     #('Name', 'e@mail.com'),
)

MANAGERS = ADMINS

PROJECT_ROOT = dirname(normpath(abspath({{ project_name }}.__file__ + '/../')))

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Africa/Johannesburg'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-za'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    normpath(join(PROJECT_ROOT, '{{ project_name }}/static')),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '{{ secret_key }}'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = '{{ project_name }}.urls'

TEMPLATE_DIRS = [
    normpath(join(PROJECT_ROOT, '{{ project_name }}/templates')),
]

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Useful template tags:
    'django.contrib.humanize',

    # Admin panel and documentation:
    'django.contrib.admin',
    'django.contrib.admindocs',

    # Add your apps here

)

# South Configuration
if HAS_south:
    INSTALLED_APPS += (
        # Database migration helpers:
        'south',
    )

# Celery Confguration
if HAS_celery:
    INSTALLED_APPS += (
        # Asynchronous task queue:
        'djcelery',
    )
    from djcelery import setup_loader
    # See: http://celery.readthedocs.org/en/latest/configuration.html#celery-task-result-expires
    CELERY_TASK_RESULT_EXPIRES = timedelta(minutes=30)
    # See: http://celery.github.com/celery/django/
    setup_loader()

if HAS_haml:
    TEMPLATE_LOADERS = (
        # djaml must load first, else standard Django template loaders will try to process HAML
        'djaml.loaders.DjamlFilesystemLoader',
        'djaml.loaders.DjamlAppDirectoriesLoader',
    ) + TEMPLATE_LOADERS


if HAS_compressor:
    INSTALLED_APPS += (
        # Django-Compressor:
        'compressor',
    )

    STATICFILES_FINDERS += (
        'compressor.finders.CompressorFinder',
    )

    # This configures any extra content types inside compress tags, and will automaticaly
    # precompile it for you.
    #
    # These assume you have coffeescript and less installed with nodejs npm command
    # Note: less installed using ruby doesn't work as well.
    COMPRESS_PRECOMPILERS = (
        ('text/coffeescript', 'coffee --compile --stdio'),
        ('text/less', 'lessc {infile} {outfile}'),
    )

