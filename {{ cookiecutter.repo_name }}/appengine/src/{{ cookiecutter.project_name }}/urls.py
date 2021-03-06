from django.conf.urls import patterns, include, url
from django import http

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

import djappengine.sessions.urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', '{{ cookiecutter.project_name }}.views.home', name='home'),
    # url(r'^{{ cookiecutter.project_name }}/', include('{{ cookiecutter.project_name }}.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', lambda request: http.HttpResponse('Hello world!')),
    url(r'^djappengine/sessions/', include(djappengine.sessions.urls)),
)
