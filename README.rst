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
* django-celery (commented out by default)
* south (commented out by default)
* admin



To create project:
------------------
django-admin.py startproject --template=https://github.com/grigi/project_template/zipball/master --extension="py,in,conf" --name="deployment.txt,local_settings.py.sample" foo
cd foo
chmod +x manage.py
chmod +x app_create.sh

Please change the README file, as this is this is the templates README.
If you delete the README file, update the long_description parameter to
 either point to the new README file, or comment it out.

Now just run:
./manage.py syncdb
./manage.py migrate  # only if you enabled south
./manage.py runserver



To add app:
-----------
./app_create.sh bar

And follow directions.

It automatically adds serving static/foo/ content under static/foo/
It automatically adds the templates to be processed.


