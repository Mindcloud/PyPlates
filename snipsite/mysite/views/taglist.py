from taggit.models import Tag
from django.views.generic.list_detail import object_list
from mysite.models import Snippet

def top_tags(request):
    return object_list(
        request,
        queryset=Snippet.objects.top_tags(),
        template_name='mysite/tag_list.html',
        paginate_by=20)

