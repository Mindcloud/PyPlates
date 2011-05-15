from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count, Sum, permalink
import datetime
from pygments import formatters, highlight, lexers
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from markdown import markdown
from django import forms
from django.forms import ModelForm, Textarea
from taggit.managers import TaggableManager

PYTHON_VERSIONS = (
    (3.0, '3.0'),
    (2.7, '2.7'),
    (2.6, '2.6'),
    (2.5, '2.5'),
    (0,  'Other'),
)

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
        return lexers.get_lexer_by_name("python")

class SnippetManager(models.Manager):
    def top_rated(self):
        return self.all().order_by('-rating_score')

    def top_tags(self):
        return self.model.tags.most_common().order_by('-num_times', 'name')

    def tag_match(self, tag):
        return self.filter(tags__in=[tag])

class Snippet(models.Model):
    title = models.CharField(max_length=255)
    language = models.ForeignKey(Language)
    user = models.ForeignKey(User)
    description = models.TextField()
    description_html = models.TextField(editable=False)
    code = models.TextField()
    highlighted_code = models.TextField(editable=False)
    python_version = models.FloatField(choices=PYTHON_VERSIONS, default=2.7)
    pub_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    rating_score = models.IntegerField(default=0)
    
    tags = TaggableManager()
    objects = SnippetManager()

    class Meta:
        ordering = ('-pub_date',)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.description_html = markdown(self.description, safe_mode="escape")
        self.highlighted_code = self.highlight()
        super(Snippet, self).save(*args, **kwargs)

    def entered_today(self):
        return self.pub_date.date() == datetime.date.today()

    def highlight(self): #highlight the code for the right syntax
        return highlight(self.code, PythonLexer(),HtmlFormatter())

    def get_version(self):
        return dict(PYTHON_VERSIONS)[self.python_version]

    @permalink
    def get_absolute_url(self):
        return ('snippet_detail', (), {'snippet_id': self.id})

    def get_tags(self):
        return ", ".join([tag.name for tag in self.tags.all()])
