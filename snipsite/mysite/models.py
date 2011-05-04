from django.db import models
from django.contrib.auth.models import User
import datetime

PYTHON_VERSIONS = (
    (3.0, '3.0'),
    (2.7, '2.7'),
    (2.6, '2.6'),
    (2.5, '2.5'),
    (0,  'Other'),
)

class Snippet(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User)
    description = models.TextField()
    description_html = models.TextField(editable=False)
    code = models.TextField()
    highlighted_code = models.TextField(editable=False)
    python_version = models.FloatField(choices=PYTHON_VERSIONS, default=2.7)
    pub_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    rating_score = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.title

    def entered_today(self):
        return self.pub_date.date() == datetime.date.today()
