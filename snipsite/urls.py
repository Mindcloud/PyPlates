from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from tastypie.api import Api
from mysite.api.resources import *

v1_api = Api(api_name='v1')
v1_api.register(SnippetResource())
v1_api.register(UserResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'snipsite.views.home', name='home'),
    # url(r'^snipsite/', include('snipsite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    (r'^api/', include(v1_api.urls)),
)
