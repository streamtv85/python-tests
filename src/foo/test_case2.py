import unittest
import requests
# import xmltodict
from yaml import load

# using cookie-based auth
from foo.base_test import BaseApiTest


class TestCreateIssue(BaseApiTest):
    def setUp(self):
        super(TestCreateIssue, self).setUp()
        self.url = self.base_url + '/issue'

    def test_create_new_issue(self):
        params = {
            'project': 'API',
            'summary': ' Test summary 2 created by robot',
            'description': 'Robots are working'
        }
        resp = requests.put(self.url, data=params, cookies=self.cookies)
        self.assertEquals(resp.status_code, 201)
        issue_id = resp.headers['location'].split('/')[-1]
        print issue_id

        url_get = self.url + '/' + issue_id
        r = requests.get(url_get, cookies=self.cookies)
        self.assertEquals(r.status_code, 200)
        r_del = requests.delete(url_get, cookies=self.cookies)
        self.assertEquals(r.status_code, 200)

    def test_create_issue_incorrect_project(self):
        url = self.base_url + '/issue'
        params = {
            'project': 'IAMINVALID',
            'summary': ' Test summary 2 created by robot',
            'description': 'Robots are working'
        }
        resp = requests.put(url, data=params, cookies=self.cookies)
        self.assertEquals(resp.status_code, 403)
