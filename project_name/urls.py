from os.path import dirname,normpath,abspath,join
from django.conf.urls import patterns, include, url
from django.http import HttpResponsePermanentRedirect
from django.conf import settings

# See: https://docs.djangoproject.com/en/dev/ref/contrib/admin/#hooking-adminsite-instances-into-your-urlconf
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Admin documentation
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Admin panel
    url(r'^admin/', include(admin.site.urls)),

    # Examples
    # (r'^$', lambda request: HttpResponsePermanentRedirect('/app/')),
    # url(r'^app/', include('app.urls')),

)

# Serve static files only if DEBUG=True
# See: https://docs.djangoproject.com/en/dev/howto/static-files/
if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    staticroot = normpath(join(settings.PROJECT_ROOT, '{{ project_name }}/static'))
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns('',
        (r'^favicon\.ico$', 'django.views.static.serve', { 'document_root': staticroot, "path":'favicon.ico' }),
        (r'^robots\.txt$', 'django.views.static.serve', { 'document_root': staticroot, "path":'robots.txt' }),
        (r'^crossdomain\.xml$', 'django.views.static.serve', { 'document_root': staticroot, "path":'crossdomain.xml' }),
    )

