Sample instructions on how to deploy
====================================

Create Python container
=======================

For this we assume you are using a Linux host with:
 * Python >= 2.6
 * virtualenv

As root, on the server:
-----------------------
Add a System User (-r) ``{{ project_name }}``, in directory ``/opt/{{ project_name }}``::

  useradd -r -d /opt/{{ project_name }} -m -s /bin/bash {{ project_name }}

Change to the container::

  su - {{ project_name }}

As the Container User:
----------------------
Create virtualenv in user root::

  virtualenv --no-site-packages . 

Confirm or Edit that your ``~/.profile`` or ``~/.bashrc`` contains the following::

  source ~/bin/activate

Log out an back in to your session again

Do a ``which python`` to see that you are using the right version.
Result should be something like::

  ~/bin/python
  /opt/{{ project_name }}/bin/python


Deploy project
==============

In your project root:
---------------------
Build a source blob::

  python setup.py sdist

Copy the tarball ``dist/{{ project_name }}-0.1.tar.gz`` to the Python container.

As the Container User:
----------------------
Install the project::

  pip install <tarball>

If anything fails to build, resolve it manually.
Common causes are lack of a ``-dev`` package to build some library against.

Confirm or Edit that your ``~/.profile`` or ``~/.bashrc`` contains the following::

  export DJANGO_SETTINGS_MODULE="{{ project_name }}.settings.prod"

Run ``django-admin.py validate`` to confirm that your environment is set up correctly.

For static content, make sure that a static folder exists.
By default it is ``/opt/{{ project_name }}/static/`` for production.
Edit ``STATIC_ROOT`` in the settings to change it.

Now make sure it exists::

  mkdir /opt/{{ project_name }}/static/

Collect all the static content in one place, for easy serving :-)
Make sure to run this after every deployment update::

  django-admin.py collectstatic


Configuring Apache
==================

Add a configuration file in the apache config directory.
You can use the sample file in ``{{ project_name }}/apache-sample.conf`` as a base.

Please update references to ``<CNAME>`` to the cname of the vhost.

