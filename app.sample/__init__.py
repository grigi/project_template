# __init__ for app '{{ app_name }}'
from django.conf import settings
import os
import inspect

APP_ROOT = os.path.dirname(os.path.normpath(inspect.getfile(inspect.currentframe())))

settings.TEMPLATE_DIRS.append('%s/templates' % APP_ROOT)

