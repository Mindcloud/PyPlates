from django import forms
from django.contrib import admin
from mysite.models import Language, Snippet, PYTHON_VERSIONS
from django.forms import ModelForm, Textarea

class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        exclude = ('user', 'rating_score',)
        #fields = ('title', 'language', 'description', 'code', 'python_version')
        widgets = {
            'description': Textarea(attrs={'cols': 80, 'rows': 10}),
            'code': Textarea(attrs={'cols': 80, 'rows': 20}),
        }


