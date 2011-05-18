from django import forms
from django.template.context import RequestContext
from django.template.defaultfilters import slugify
from django.utils import simplejson as json
from django.views.generic.list_detail import object_list, object_detail
from mysite.models import Snippet, Language
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseForbidden, Http404, HttpResponse
from mysite.forms import SnippetForm
from taggit.models import Tag

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

#@login_required
def edit_snippet(request, snippet_id=None, template_name='mysite/edit_snippet.html'):
    if snippet_id:
        snippet = get_object_or_404(Snippet, pk=snippet_id)
        #if request.user.id != snippet.user.id:
        #    return HttpResponseForbidden()
    else:
        template_name = 'mysite/add_snippet.html'
        snippet = Snippet(user=request.user, language=Language.objects.get(name='Python'))
    if request.method == 'POST':
        form = SnippetForm(instance=snippet, data=request.POST)
        if form.is_valid():
            snippet = form.save()
            return HttpResponseRedirect(snippet.get_absolute_url())
    else:
        form = SnippetForm(instance=snippet)
    return render_to_response(template_name,
        {'form': form}, context_instance=RequestContext(request))


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

