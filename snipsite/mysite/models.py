from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Snippet(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User)
    description = models.TextField()
    description_html = models.TextField(editable=False)
    code = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
