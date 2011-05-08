from django.template.defaultfilters import slugify
from django.utils import simplejson as json
from django.views.generic.list_detail import object_list, object_detail
from mysite.models import Snippet, Language, Category
from django.db.models import Q
from django.contrib.auth.decorators import login_required

def snippet_list(request, queryset=None, **kwargs):
    if queryset is None:
        queryset = Snippet.objects.all()
    return object_list(
        request,
        queryset=queryset,
        paginate_by=20,
        **kwargs)

def snippet_detail(request, snippet_id):
    return object_detail(
        request,
        queryset=Snippet.objects.all(),
        object_id=snippet_id)

def search(request):
    query = request.GET.get('q')
    snippet_qs = Snippet.objects.none()
    if query:
        snippet_qs = Snippet.objects.filter(
            Q(title__icontains=query) |
            Q(tags__in=[query]) |
            Q(author__username__iexact=query)
        ).distinct().order_by('-rating_score', '-pub_date')
    return snippet_list(
        request,
        queryset=snippet_qs,
        template_name='search/search.html',
        extra_context={'query':query})

