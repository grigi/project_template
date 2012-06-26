from os.path import dirname,normpath,abspath
from django.conf.urls import patterns, include, url
from django.contrib import admin

# See: https://docs.djangoproject.com/en/dev/ref/contrib/admin/#hooking-adminsite-instances-into-your-urlconf
admin.autodiscover()

urlpatterns = patterns('',
    # Admin panel and documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^static/admin/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '%s/static/admin' % dirname(normpath(abspath(admin.__file__)))}),
    # Examples:
    # url(r'^app/', include('app.urls')),

)
