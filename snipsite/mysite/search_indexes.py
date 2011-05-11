import datetime
from haystack.indexes import *
from haystack import site
from mysite.models import Snippet

class SnippetIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    title = CharField(model_attr='title')
    user = CharField(model_attr='user')
    pub_date = DateTimeField(model_attr='pub_date')

    def index_queryset(self):
        return Snippet.objects.filter()



site.register(Snippet, SnippetIndex)

