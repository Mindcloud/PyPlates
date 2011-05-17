"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.http import HttpRequest
from django.test import TestCase
try:
    import json
except ImportError:
    import simplejson as json


class ViewsTestCase(TestCase):
    def test_gets(self):
        resp = self.client.get('/api/v1/', data={'format': 'json'})
        self.assertEqual(resp.status_code, 200)
        print resp.status_code
        deserialized = json.loads(resp.content)
        print deserialized
        #self.assertEqual(len(deserialized), 2)
        #self.assertEqual(deserialized['notes'], {'list_endpoint': '/api/v1/notes/', 'schema': '/api/v1/notes/schema/'})
