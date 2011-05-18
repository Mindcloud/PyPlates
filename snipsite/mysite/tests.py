"""
This runs through API tests
"""

from django.http import HttpRequest
from django.test import TestCase
try:
    import json
except ImportError:
    import simplejson as json


class APITestCases(TestCase):
    def test_gets(self):
        print "running get test"
        resp = self.client.get('/api/v1/snippet/1/', data={'format': 'json'})
        self.assertEqual(resp.status_code, 200)
        #print resp.status_code
        deserialized = json.loads(resp.content)
        print deserialized
        #print len(deserialized)
        #self.assertEqual(len(deserialized), 2)
        #self.assertEqual(deserialized['notes'], {'list_endpoint': '/api/v1/notes/', 'schema': '/api/v1/notes/schema/'})

    def test_post(self):
        print "Running post test"
        request = HttpRequest()
        post_data = '{"code": "Some cool code", "description": "test snippet", "python_version": 2.7, "language": "/api/v1/language/1/", "title": "Unit Test Snippet 1", "user": "/api/v1/user/1/"}'
        request._raw_post_data = post_data
        
        resp = self.client.post('/api/v1/snippet/', data=post_data, content_type='application/json')
        print resp.content
        self.assertEqual(resp.status_code, 201)

        # make sure posted object exists
        resp = self.client.get('/api/v1/snippet/2/', data={'format': 'json'})
        self.assertEqual(resp.status_code, 200)
        obj = json.loads(resp.content)
        print resp.content
        self.assertEqual(obj['code'], 'Some cool code')
