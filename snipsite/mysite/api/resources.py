from django.contrib.auth.models import User
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.validation import Validation
from tastypie import fields
from tastypie.cache import SimpleCache
from tastypie.resources import ModelResource
from mysite.models import Snippet

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'auth/user'
        cache = SimpleCache()
        authentication = BasicAuthentication()
        authorization = DjangoAuthorization()

class SnippetResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'author')
	
    class Meta:
        queryset = Snippet.objects.all()
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put']

