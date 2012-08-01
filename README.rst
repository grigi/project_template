Project Template for a Django project
=====================================

Creates a Django Project that is structured well, is an egg (ditributable),
and works with minimal changes. Much of this work is based on rdegges/django-skel.

Features:
 * Useable with minimal configuration
 * Settings split up into core/dev/prod
 * Sample wsgi files
 * Templates are automatically added to template processor path
 * Static file management for easy deployment
 * Using html5boilerplate
 * Standard 404 and 500 templates 
 * base template
 * Sample templates inheriting the base template

It includes as default dependencies:
 * JQuery
 * admin
 * django-compressor
 * django-devserver

The following dependencies have default configuration added in a commented out state by default, for easy inclusion:
 * django-celery
 * south


To create project:
------------------
::

  django-admin.py startproject --template=https://github.com/grigi/project_template/zipball/master --extension="py,in,conf" --name="deployment.txt,local_settings.py.sample" foo
  cd foo
  chmod +x manage.py
  chmod +x app_create.sh

Make sure that development runtime requirements are installed::

  pip install requirements.txt 

Please change the ``README.rst`` file, as this is this is the templates README.
If you delete the ``README.rst`` file, update the long_description parameter to
either point to the new README file, or comment it out.

Now just run::

  ./manage.py syncdb
  ./manage.py migrate  # only if you enabled south
  ./manage.py runserver

Please pay attention to the ``setup.py`` file, as this is the configuration file that would be used for deployment.


To add app:
-----------
::

  ./app_create.sh bar

And follow directions.

Note:
 * It automatically adds serving static/foo/ content under static/foo/
 * It automatically adds the templates to be processed.

