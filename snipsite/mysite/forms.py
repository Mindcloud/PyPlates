from django import forms
from django.contrib import admin
from mysite.models import Language, Snippet, Category, PYTHON_VERSIONS
from django.forms import ModelForm, Textarea


#class SnippetForm(forms.ModelForm):
#    class Meta:
#         model = Snippet
#         exclude = ('user', 'rating_score',)

class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        exclude = ('user', 'rating_score',)
        fields = ('title', 'language', 'category', 'description', 'code', 'python_version')
        widgets = {
            'description': Textarea(attrs={'cols': 80, 'rows': 20}),
            'code': Textarea(attrs={'cols': 80, 'rows': 20}),
        }


