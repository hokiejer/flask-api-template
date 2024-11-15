import base64
import requests
import os

# Run the following command from the terminal to set the environment variable:
#
# export FLASK_API_AUTH_TYPE=BASIC

def get_basic_auth_header(username, password):
    credentials = base64.b64encode(f"{username}:{password}".encode()).decode('utf-8')
    return {'Authorization': f'Basic {credentials}'}

def make_api_call():
    url = 'http://127.0.0.1:5000/data'
    headers = get_basic_auth_header('admin', 'secret')
    response = requests.get(url, headers=headers)
    return response.json()

data = make_api_call()
print(data)