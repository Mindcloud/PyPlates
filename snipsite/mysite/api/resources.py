from django.contrib.auth.models import User
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.validation import Validation
from tastypie import fields
from tastypie.cache import SimpleCache
from tastypie.resources import ModelResource
from mysite.models import Snippet
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie.authorization import Authorization

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        cache = SimpleCache()
        #authentication = BasicAuthentication()
        authorization = Authorization()

class SnippetResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')
	
    class Meta:
        queryset = Snippet.objects.all()
        #list_allowed_methods = ['get', 'post']
        #detail_allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'snippet'
        authorization = Authorization()
        filtering = {
            "title": ALL,
            "user": ('exact', 'startswith'),
        }
