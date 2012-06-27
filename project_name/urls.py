from os.path import dirname,normpath,abspath
from django.conf.urls import patterns, include, url
from django.conf import settings

# See: https://docs.djangoproject.com/en/dev/ref/contrib/admin/#hooking-adminsite-instances-into-your-urlconf
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Admin panel and documentation
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Examples
    # url(r'^app/', include('app.urls')),

)

# Serve static files only if DEBUG=True
# See: https://docs.djangoproject.com/en/dev/howto/static-files/
if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()

