from django.conf.urls import patterns, include, url
from . import APP_ROOT

urlpatterns = patterns('app.views',
    # Examples:
    url(r'^$', 'home', name='home'),

) + patterns('',
    # Serve the apps static dir
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '%s/static' % APP_ROOT}),
)

