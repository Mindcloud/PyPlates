from django.contrib.auth import logout, login
from django.views.generic.list_detail import object_list
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponseRedirect

from mysite.models import Snippet

def logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def top_users(request):
    return object_list(
        request,
        queryset=Snippet.objects.top_users(),
        template_name='mysite/top_users.html',
        paginate_by=20)


