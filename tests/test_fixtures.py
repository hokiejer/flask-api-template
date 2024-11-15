import pytest
import os
from flask_api.api import app
from flask_api.data import Data

@pytest.fixture()
def test_client_basic():
    # Set environment variable for API auth type
    os.environ['FLASK_API_AUTH_TYPE'] = 'BASIC'
    Data.global_dictionary = {"message": "Hello, World!"}
    
    # Configure and initialize Flask test client
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture()
def test_client_api_key():
    # Set environment variable for API auth type
    os.environ['FLASK_API_AUTH_TYPE'] = 'API_KEY'
    Data.global_dictionary = {"message": "Hello, World!"}
    
    # Configure and initialize Flask test client
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client