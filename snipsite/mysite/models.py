from django.db import models
from django.contrib.auth.models import User
from django.db.models import permalink
import datetime
from pygments import formatters, highlight, lexers
from markdown import markdown
from django import forms
from django.forms import ModelForm, Textarea

PYTHON_VERSIONS = (
    (3.0, '3.0'),
    (2.7, '2.7'),
    (2.6, '2.6'),
    (2.5, '2.5'),
    (0,  'Other'),
)

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    language_code = models.CharField(max_length=50)
    mime_type = models.CharField(max_length=100)
    file_extension = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name

    @permalink
    def get_absolute_url(self):
        return ('language_detail', (), {'slug': self.slug})

    def get_lexer(self):
        return lexers.get_lexer_by_name(self.language_code)

class SnippetManager(models.Manager):
    def top_rated(self):
        return self.all().order_by('-rating_score')

class Snippet(models.Model):
    title = models.CharField(max_length=255)
    language = models.ForeignKey(Language)
    category = models.ForeignKey(Category)
    user = models.ForeignKey(User)
    description = models.TextField()
    description_html = models.TextField(editable=False)
    code = models.TextField()
    highlighted_code = models.TextField(editable=False)
    python_version = models.FloatField(choices=PYTHON_VERSIONS, default=2.7)
    pub_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    rating_score = models.IntegerField(default=0)
    
    #objects = SnippetManager()

    class Meta:
        ordering = ('-pub_date',)

    def __unicode__(self):
        return self.title

    def entered_today(self):
        return self.pub_date.date() == datetime.date.today()

    def highlight(self): #highlight the code for the right syntax
        return highlight(self.code, self.language.get_lexer(), 
                         formatters.HtmlFormatter(linenos=True))

    def get_version(self):
        return dict(PYTHON_VERSIONS)[self.python_version]

class SnippetForm(ModelForm):
    class Meta:
        model = Snippet
        fields = ('title', 'category', 'description', 'code', 'python_version')
        widgets = {
            'description': Textarea(attrs={'cols': 80, 'rows': 20}),
            'code': Textarea(attrs={'cols': 80, 'rows': 20}),
        }

