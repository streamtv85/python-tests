import unittest
import requests
# import xmltodict
from yaml import load


# using cookie-based auth
class BaseApiTest(unittest.TestCase):
    def setUp(self):
        self.settings = load(open('settings.yml').read())
        self.base_url = self.settings['base_url']
        params = {
            'login': self.settings['credentials']['login'],
            'password': self.settings['credentials']['password']
        }
        url = self.base_url + '/user/login'
        resp = requests.post(url, data=params)
        self.cookies = resp.cookies

    def create_issue(self):
        params = {
            'project': self.settings['project'],
            'summary': ' Test summary 2 created by robot',
            'description': 'Robots are working'
        }
        resp = requests.put(self.url, data=params, cookies=self.cookies)
        self.assertEquals(resp.status_code, 201)
        issue_id = resp.headers['location'].split('/')[-1]
        return issue_id
