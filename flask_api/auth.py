from flask import Flask, jsonify, request, Response
from flask_restx import Api, Resource, fields
from functools import wraps
import os

def requires_auth(f):
    """
    Decorator for routes that require authentication.  This will decide on the authentication
    method based on the FLASK_API_AUTH_TYPE environment variable.

    Args:
        f (function): The function to be decorated.

    Returns:
        function: The decorated function.
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_mode = os.environ.get('FLASK_API_AUTH_TYPE', 'BASIC')
        if auth_mode == 'BASIC':
            auth = request.authorization
            if not auth or not check_auth_basic(auth.username, auth.password):
                return Response(
                    'Could not verify your access level for that URL.\n'
                    'You have to login with proper credentials', 401,
                    {'WWW-Authenticate': 'Basic realm="Login Required"'}
                )
            return f(*args, **kwargs)
        
        elif auth_mode == 'API_KEY':
            api_key = request.headers.get('x-api-key')
            if not api_key or not check_auth_api_key(api_key):
                return Response(
                    'Could not verify your access level for that URL.\n'
                    'You have to provide a valid API key', 401,
                    {'WWW-Authenticate': 'Basic realm="Login Required"'}
                )
            return f(*args, **kwargs)
        
    return decorated


        




### BASIC Authentication

def check_auth_basic(username, password):
    """
    Check if the provided username and password are valid.

    Args:
        username (str): The username to be checked.
        password (str): The password to be checked.

    Returns:
        bool: True if the username and password are valid, False otherwise.
    """
    return username == 'admin' and password == 'secret'

def requires_auth_basic(f):
    """
    Decorator for routes that require authentication.

    Args:
        f (function): The function to be decorated.

    Returns:
        function: The decorated function.
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth_basic(auth.username, auth.password):
            return Response(
                'Could not verify your access level for that URL.\n'
                'You have to login with proper credentials', 401,
                {'WWW-Authenticate': 'Basic realm="Login Required"'}
            )
        return f(*args, **kwargs)
    return decorated

### API KEY Authentication

def check_auth_api_key(api_key):
    """
    Check if the provided API key is valid.

    Args:
        api_key (str): The API key to be checked.

    Returns:
        bool: True if the API key is valid, False otherwise.
    """
    return api_key == '0123456789ABCDEF'

def requires_auth_api_key(f):
    """
    Decorator for routes that require authentication.

    Args:
        f (function): The function to be decorated.

    Returns:
        function: The decorated function.
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        api_key = request.headers.get('x-api-key')
        if not api_key or not check_auth_api_key(api_key):
            return Response(
                'Could not verify your access level for that URL.\n'
                'You have to provide a valid API key', 401
            )
        return f(*args, **kwargs)
    return decorated

