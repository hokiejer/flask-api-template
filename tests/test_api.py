import unittest
from flask_testing import TestCase
from flask_api.api import app
import base64

class TestAPI(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def get_basic_auth_header(self, username, password):
        credentials = base64.b64encode(f"{username}:{password}".encode()).decode('utf-8')
        return {'Authorization': f'Basic {credentials}'}

    def test_get_data(self):
        headers = self.get_basic_auth_header('admin', 'secret')
        response = self.client.get('/data', headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Hello, World!"})

    def test_update_data(self):
        headers = self.get_basic_auth_header('admin', 'secret')
        response = self.client.post('/data', json={"message": "Hello, GitHub Copilot"}, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Hello, GitHub Copilot"})

    def test_get_data_unauthorized(self):
        response = self.client.get('/data')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data, b'Could not verify your access level for that URL.\nYou have to login with proper credentials')
        
if __name__ == '__main__':
    unittest.main()
