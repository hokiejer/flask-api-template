import unittest
from flask_testing import TestCase
from flask_api.api import app
from flask_api.data import Data
import base64
import os

def setUpModule():
    os.environ['FLASK_API_AUTH_TYPE'] = 'API_KEY'
    Data.global_dictionary = {"message": "Hello, World!"}

class TestAPIAuthAPIKey(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def get_auth_header_api_key(self, api_key):
        return {'x-api-key': api_key}
    
    def test_get_data(self):
        headers = self.get_auth_header_api_key('0123456789ABCDEF')
        response = self.client.get('/data', headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Hello, World!"})

    def test_update_data(self):
        headers = self.get_auth_header_api_key('0123456789ABCDEF')
        response = self.client.post('/data', json={"message": "Hello, GitHub Copilot"}, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Hello, GitHub Copilot"})

    def test_get_data_unauthorized(self):
        response = self.client.get('/data')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data, b'Could not verify your access level for that URL.\nYou have to provide a valid API key')

    def test_update_data_unauthorized(self):
        response = self.client.post('/data', json={"message": "Hello, GitHub Copilot"})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data, b'Could not verify your access level for that URL.\nYou have to provide a valid API key')

    def test_get_data_wrong_credentials(self):
        headers = self.get_auth_header_api_key('wrong')
        response = self.client.get('/data', headers=headers)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data, b'Could not verify your access level for that URL.\nYou have to provide a valid API key')

    def test_update_data_wrong_credentials(self):
        headers = self.get_auth_header_api_key('wrong')
        response = self.client.post('/data', json={"message": "Hello, GitHub Copilot"}, headers=headers)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data, b'Could not verify your access level for that URL.\nYou have to provide a valid API key')

    def test_get_data_wrong_username(self):
        headers = self.get_auth_header_api_key('admin')
        response = self.client.get('/data', headers=headers)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data, b'Could not verify your access level for that URL.\nYou have to provide a valid API key')

    def test_update_data_wrong_username(self):
        headers = self.get_auth_header_api_key('admin')
        response = self.client.post('/data', json={"message": "Hello, GitHub Copilot"}, headers=headers)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data, b'Could not verify your access level for that URL.\nYou have to provide a valid API key')

    def test_get_data_wrong_password(self):
        headers = self.get_auth_header_api_key('wrong')
        response = self.client.get('/data', headers=headers)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data, b'Could not verify your access level for that URL.\nYou have to provide a valid API key')

    def test_update_data_wrong_password(self):
        headers = self.get_auth_header_api_key('wrong')
        response = self.client.post('/data', json={"message": "Hello, GitHub Copilot"}, headers=headers)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data, b'Could not verify your access level for that URL.\nYou have to provide a valid API key')
            
    if __name__ == '__main__':
        unittest.main()
