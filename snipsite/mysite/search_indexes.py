from haystack.indexes import *
from haystack import site
from mysite.models import Snippet

class SnippetIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    user = CharField()
    title = CharField(model_attr='title')

site.register(Snippet, SnippetIndex)

