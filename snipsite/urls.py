from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

from tastypie.api import Api
from mysite.api.resources import *
from mysite.views import snippets

v1_api = Api(api_name='v1')
v1_api.register(SnippetResource())
v1_api.register(UserResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'snipsite.views.home', name='home'),
    # url(r'^snipsite/', include('snipsite.foo.urls')),
    url(r'^$', snippets.snippet_list, name='snippet_list'),
    url(r'^(?P<snippet_id>\d+)/$', snippets.snippet_detail, name = 'snippet_detail'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    (r'^api/', include(v1_api.urls)),
)
