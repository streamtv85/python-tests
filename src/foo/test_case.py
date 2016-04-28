import unittest
import requests
import xmltodict

from foo.base_test import BaseApiTest


# using basic auth
class TestGetIssue(BaseApiTest):
    def setUp(self):
        super(TestGetIssue, self).setUp()
        self.url = self.base_url + '/issue/'
        self.creds = ('root', 'c11desp@ce')

    def test_get_issue(self):
        url = self.base_url + '/issue/' + 'API-51'
        response = requests.get(url, auth=self.creds)
        self.assertEquals(response.status_code, 200)
        r_dict = xmltodict.parse(response.text)
        self.assertEqual(r_dict['issue']['@id'], 'API-51')

    def test_get_invalid_issue(self):
        url = self.base_url + '/issue/' + 'API-1212'
        response = requests.get(url, auth=self.creds)
        self.assertEquals(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
