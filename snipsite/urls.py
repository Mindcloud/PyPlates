from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()
import settings
from tastypie.api import Api
from mysite.api.resources import *
from mysite.views import snippets, user, taglist

v1_api = Api(api_name='v1')
v1_api.register(SnippetResource())
v1_api.register(UserResource())
v1_api.register(LanguageResource())

urlpatterns = patterns('',
    url(r'^$', snippets.snippet_list, name='snippet_list'),
    url(r'^(?P<snippet_id>\d+)/$', snippets.snippet_detail, name = 'snippet_detail'),
    url(r'^add/$', snippets.edit_snippet, name='snippet_add'),
    url(r'^(?P<snippet_id>\d+)/edit/$', snippets.edit_snippet, name='snippet_edit'),
    url(r'^accounts/logout/', 'django.contrib.auth.views.logout'),
    url(r'^accounts/login/', 'django.contrib.auth.views.login'),
    (r'^search/', include('haystack.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^api/', include(v1_api.urls)),
    url(r'^tags/', taglist.top_tags, name='top_tags'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)

