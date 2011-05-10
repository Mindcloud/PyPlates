from django import forms
from django.contrib import admin

from mysite.models import Language, Snippet, Category, PYTHON_VERSIONS

class SnippetForm(forms.ModelForm):
    class Meta:
         model = Snippet
         exclude = ('user', 'rating_score',)

