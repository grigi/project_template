#!/usr/bin/env python
import os
import sys
import imp

if __name__ == "__main__":
    settings_path = "{{ project_name }}.settings.dev"
    try:
        # Check for local settings.py in local directory.
        imp.find_module('local_settings')
        settings_path = "local_settings"
    except:
        # No local settings.py file
        pass
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_path)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
