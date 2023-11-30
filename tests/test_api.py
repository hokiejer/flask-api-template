import unittest
from flask_testing import TestCase
from flask_api.api import api

class TestAPI(TestCase):
    def create_app(self):
        app = api.app
        app.config['TESTING'] = True
        return app

    def test_get_data(self):
        response = self.client.get('/data')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Hello, World!"})

    def test_update_data(self):
        response = self.client.post('/data', json={"message": "Hello, GitHub Copilot"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Hello, GitHub Copilot"})

if __name__ == '__main__':
    unittest.main()