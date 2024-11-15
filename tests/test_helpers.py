import base64

# Helper function for authorization header
def get_auth_header_api_key(api_key):
    return {'x-api-key': api_key}

# Helper function for basic auth header
def get_auth_header_basic(username, password):
    credentials = base64.b64encode(f"{username}:{password}".encode()).decode('utf-8')
    return {'Authorization': f'Basic {credentials}'}
