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
 * Autmatic CSS and Javascript compression support
 * Automatic less/coffeescript compilation that works transparently on referenced files or inline scripts. (Needs node.js with less and coffeescript)
 * Optional Nose test framework with test coverage
 * Optional HAML support

It includes as default dependencies:
 * admin
 * JQuery
   http://jquery.com/
   (Version 1.7.2 bundled)
 * Bootstrap
   http://twitter.github.com/bootstrap/index.html
   (Version 2.0.4 bundled)

The following dependancies are optional in dev-mode only. It will automatically use these libraries if you have them installed:
 * django-devserver
   https://github.com/dcramer/django-devserver
 * django-nose
   http://nose.readthedocs.org/
   http://nose-plugins.jottit.com/
 * nose-cov
   https://bitbucket.org/memedough/nose-cov/overview
   (nose coverage plugin)
 * pinoccio
   http://darcs.idyll.org/~t/projects/pinocchio/doc/
   (nose spec plugin)

The following dependencies have default configuration added in a commented out state by default, for easy inclusion:
 * django-compressor
   http://django_compressor.readthedocs.org/en/latest/index.html
   * Autmatic CSS and Javascript compression support
   * Automatic less/coffeescript compilation that works transparently on referenced files or inline scripts. (Needs node.js with less and coffeescript)
 * Djaml (Optional HAML support)
   https://github.com/chartjes/djaml
 * django-celery
 * south

To setup initial virtualenv:
----------------------------

Note:
  This part can be skipped, but is a convenient (and recommended)  way of isolating your development environment, and making it closer to how you would likely deploy it on a server.

Check that virtualenv is installed::

  pip install virtualenv

First, create a new directory that will contain your virtualenv, and setup::

  mkdir fooenv
  cd fooenv
  virtualenv .
  . bin/activate

At this point you should have your virtualenv up and running.
Test that your virtualenv is running correctly::

  which python

Should be inside your current directory.

Now install django::

  pip install django

Now simulate what a ``pip install -e`` (Editable package) would do.
(You only need to do it the first time, thereafter you could just do ``pip install -e <SOURCE REPO>`` to install it the same)
::

  mkdir src
  cd src

Now install as per the 'To create project' instructions.

The rest here is to make your package available in your python path:
  Once that is done, get the path::

    pwd

  Append that path to ``lib/python2.7/site-packages/easy-install.pth`` (or equivalent) from the root of the virtualenv.

  Now your new package is available in your python path::

    python
    >>> import foo
    (No import error)
  
  If you want your app runnable from ``django-admin.py`` anywhere in the virtualenv (not just from the primary projects root) you now only need to define the ``DJANGO_SETTINGS_MODULE`` environment variable::

    DJANGO_SETTINGS_MODULE="foo.settings.dev"

  A good place to put it is in your ``bin/activate`` script:

    | ...
    |
    | # reset old environment variables
    |
    | **unset DJANGO_SETTINGS_MODULE**
    |
    | ...
    |
    | export PATH
    | 
    | **export DJANGO_SETTINGS_MODULE="ssoserver.settings.dev"**
    | 
    | # unset PYTHONHOME if set
    |
    | ...

Tip:
  If you want your virtualenv to auto-load when you cd into it follow instructions on http://www.redslider.net/2011/2011-11-22-auto-source-virtualenv-settings.html

To create project:
------------------
::

  django-admin.py startproject --template=https://github.com/grigi/project_template/zipball/master --extension="py,in,conf" --name="deployment.txt,local_settings.py.sample" foo
  cd foo
  chmod +x manage.py
  chmod +x app_create.sh

Make sure that development runtime & testing requirements are installed::

  pip install -r requirements.txt 

Please change the ``README.rst`` file, as this is this is the templates README.
If you delete the ``README.rst`` file, update the long_description parameter to
either point to the new README file, or comment it out.

Now just run::

  ./manage.py syncdb
  ./manage.py migrate  # only if you enabled south
  ./manage.py runserver

Please pay attention to the ``setup.py`` file, as this is the configuration file that would be used for deployment.

Note:
  The sample template uses ``less``, and ``coffeescript``. Please make sure that you have the following installed:
    * ``nodejs`` http://nodejs.org/ (node.js)
    * ``npm install less``
    * ``npm install coffeescript``

  The version of less that ships with ruby (if using rvm to install) is somewhat broken.

To add app:
-----------
::

  ./app_create.sh bar

And follow directions.

Note:
 * It automatically adds serving static/foo/ content under static/foo/
 * It automatically adds the templates to be processed.

To enable optional features:
----------------------------

Django-Compressor:
  To use Django-Compressor, uncomment:
   * HAS_compressor in {{ project_name }}/settings/common.py
   * ``django-compressor`` in both ``setup.py`` and ``requirements.txt``
   * Rerun::

      pip install -r requirements.txt

  This also enables you seamless ``less``, and ``coffeescript`` usage. Please make sure that you have the following installed:
   * ``nodejs`` http://nodejs.org/ (node.js)
   * ``npm install less``
   * ``npm install coffeescript``

  The version of less that ships with ruby (if using rvm to install) is somewhat broken.

