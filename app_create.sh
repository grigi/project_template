#!/bin/sh

if [ $# -lt "1" ]
then
    echo "Usage: $0 <appname>"
    exit 1
fi

PROJ_NAME=`cat manage.py | grep DJANGO_SETTINGS_MODULE | sed 's/^[^"]*"[^"]*"[^"]*"//' | sed 's/\..*$//'`

echo "Creating app '$1' in project '$PROJ_NAME'"

django-admin.py startapp --template=https://github.com/grigi/project_template_app/zipball/master --extension="py,html,in" $1
cat $1/MANIFEST.in >> MANIFEST.in
rm $1/MANIFEST.in
rm $1/README

echo "Add to $PROJ_NAME/urls.py"
echo "    url(r'^$1/', include('$1.urls')),"
echo
echo "Add to $PROJ_NAME/settings/common.py to the INSTALLED_APPS"
echo "    '$1',"
echo

