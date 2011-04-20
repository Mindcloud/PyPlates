from tastypie.resources import ModelResource
from mysite.models import Snippet


class SnippetResource(ModelResource):
    class Meta:
        queryset = Snippet.objects.all()
        allowed_methods = ['get']

