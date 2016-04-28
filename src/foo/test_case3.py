import unittest
import requests
# import xmltodict
from yaml import load
from foo.base_test import BaseApiTest


# using cookie-based auth
class TestDeleteIssue(BaseApiTest):
    def setUp(self):
        super(TestDeleteIssue, self).setUp()
        self.url = self.base_url + '/issue/'

    def test_delete_issue(self):
        issue_id = self.create_issue()

        r = requests.delete(self.url + issue_id, cookies=self.cookies)
        self.assertEquals(r.status_code, 200)

        r = requests.get(self.url + issue_id, cookies=self.cookies)
        self.assertEquals(r.status_code, 404)

    def test_delete_not_existing_issue(self):
        issue_id = 'nothing'
        r = requests.delete(self.url + issue_id, cookies=self.cookies)
        self.assertEquals(r.status_code, 404)
