from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()
import settings
from tastypie.api import Api
from mysite.api.resources import *
from mysite.views import snippets, taglist, lists, user

v1_api = Api(api_name='v1')
v1_api.register(SnippetResource())
v1_api.register(UserResource())
v1_api.register(LanguageResource())

urlpatterns = patterns('',
    url(r'^$', snippets.snippet_list, name='snippet_list'),
    url(r'^(?P<snippet_id>\d+)/$', snippets.snippet_detail, name = 'snippet_detail'),
    url(r'^add/$', snippets.edit_snippet, name='snippet_add'),
    url(r'^(?P<snippet_id>\d+)/edit/$', snippets.edit_snippet, name='snippet_edit'),
    #url(r'^accounts/logout/', 'django.contrib.auth.views.logout'),
    #url(r'^accounts/login/', 'django.contrib.auth.views.login'),
    #url(r'^accounts/new/', user.create_user),
    url(r'^accounts/', include('registration.urls')),
    url(r'^search/$', include('haystack.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
    url(r'^tags/', taglist.top_tags, name='top_tags'),
    url(r'^(?P<slug>[-\w]+)/$', snippets.matches_tag, name='mysite_snippet_matches_tag'),
    url(r'^users/$', lists.top_users, name='mysite_top_users'),
    url(r'^users/(?P<username>[-\w]+)/$', snippets.user_snippets, name='mysite_user_snippets'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)

