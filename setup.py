import os
from setuptools import setup, find_packages

# This is to disable the 'black magic' surrounding versioned repositories... Terrible!
from setuptools.command import sdist
del sdist.finders[:]

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='{{ project_name }}',
    version = '0.1',
    description='Project for {{ project_name }}',
    long_description=read('README.rst'),
    author='',
    author_email='',
    url='',
    zip_safe = False,

    # Dependencies
    install_requires = [
        'django >=1.4, <1.5',
        'django-compressor >=1.1',
        # Jinja2 & Hamlpy 
        #'coffin >=0.3.6',
        #'Jinja2 >=2.6',
        #'jinja2-hamlpy',

        #'python-memcached >= 1.47',
        #'django-celery >=2.5, <2.6',
        #'south >=0.7, <0.8',
    ],
    dependency_links = [
	# For example, this project would be something like:
        # 'git+ssh://git@github.com/USERNAME/{{ project_name }}.git@master#egg={{ project_name }}-0.1',
    ],

    # Packages
    packages = find_packages(),
    include_package_data = True,

    # Scripts
    scripts = [
       '{{ project_name }}/wsgi_prod.py',
    ],
)

