import base64
import requests
import os

# Run the following command from the terminal to set the environment variable:
#
# export FLASK_API_AUTH_TYPE=API_KEY

def get_api_key_header(api_key):
    return {'x-api-key': f'{api_key}'}

def make_api_call():
    url = 'http://127.0.0.1:5000/data'
    headers = get_api_key_header('0123456789ABCDEF')
    response = requests.get(url, headers=headers)
    return response.json()

data = make_api_call()
print(data)