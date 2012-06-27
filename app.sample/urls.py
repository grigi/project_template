# Urls for app '{{ app_name }}'
from django.conf.urls import patterns, include, url

urlpatterns = patterns('{{ app_name }}.views',
    # Examples:
    url(r'^$', 'home', name='home'),

)

