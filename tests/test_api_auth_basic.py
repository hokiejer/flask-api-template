import pytest
from tests.test_fixtures import test_client_basic as test_client
from tests.test_helpers import get_auth_header_basic
import base64
import os

# Tests
def test_get_data(test_client):
    headers = get_auth_header_basic('admin', 'secret')
    response = test_client.get('/data', headers=headers)
    assert response.status_code == 200
    assert response.json == {"message": "Hello, World!"}

def test_update_data(test_client):
    headers = get_auth_header_basic('admin', 'secret')
    response = test_client.post('/data', json={"message": "Hello, GitHub Copilot"}, headers=headers)
    assert response.status_code == 200
    assert response.json == {"message": "Hello, GitHub Copilot"}

def test_get_data_unauthorized(test_client):
    response = test_client.get('/data')
    assert response.status_code == 401
    assert response.data == b'Could not verify your access level for that URL.\nYou have to login with proper credentials'

def test_update_data_unauthorized(test_client):
    response = test_client.post('/data', json={"message": "Hello, GitHub Copilot"})
    assert response.status_code == 401
    assert response.data == b'Could not verify your access level for that URL.\nYou have to login with proper credentials'

def test_get_data_wrong_credentials(test_client):
    headers = get_auth_header_basic('admin', 'wrong')
    response = test_client.get('/data', headers=headers)
    assert response.status_code == 401
    assert response.data == b'Could not verify your access level for that URL.\nYou have to login with proper credentials'

def test_update_data_wrong_credentials(test_client):
    headers = get_auth_header_basic('admin', 'wrong')
    response = test_client.post('/data', json={"message": "Hello, GitHub Copilot"}, headers=headers)
    assert response.status_code == 401
    assert response.data == b'Could not verify your access level for that URL.\nYou have to login with proper credentials'

def test_get_data_wrong_username(test_client):
    headers = get_auth_header_basic('wrong', 'secret')
    response = test_client.get('/data', headers=headers)
    assert response.status_code == 401
    assert response.data == b'Could not verify your access level for that URL.\nYou have to login with proper credentials'

def test_update_data_wrong_username(test_client):
    headers = get_auth_header_basic('wrong', 'secret')
    response = test_client.post('/data', json={"message": "Hello, GitHub Copilot"}, headers=headers)
    assert response.status_code == 401
    assert response.data == b'Could not verify your access level for that URL.\nYou have to login with proper credentials'

def test_get_data_wrong_password(test_client):
    headers = get_auth_header_basic('admin', 'wrong')
    response = test_client.get('/data', headers=headers)
    assert response.status_code == 401
    assert response.data == b'Could not verify your access level for that URL.\nYou have to login with proper credentials'

def test_update_data_wrong_password(test_client):
    headers = get_auth_header_basic('admin', 'wrong')
    response = test_client.post('/data', json={"message": "Hello, GitHub Copilot"}, headers=headers)
    assert response.status_code == 401
    assert response.data == b'Could not verify your access level for that URL.\nYou have to login with proper credentials'
