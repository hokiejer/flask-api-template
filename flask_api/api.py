from flask import Flask, jsonify, request, Response
from flask_restx import Api, Resource
from functools import wraps

app = Flask(__name__)
api = Api(app, doc='/swagger/') # Sets the URL for the Swagger documentation

# Simple in-memory database for demonstration
data = {"message": "Hello, World!"}

def check_auth(username, password):
    """
    Check if the provided username and password are valid.

    Args:
        username (str): The username to be checked.
        password (str): The password to be checked.

    Returns:
        bool: True if the username and password are valid, False otherwise.
    """
    return username == 'admin' and password == 'secret'

def requires_auth(f):
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
        if not auth or not check_auth(auth.username, auth.password):
            return Response(
                'Could not verify your access level for that URL.\n'
                'You have to login with proper credentials', 401,
                {'WWW-Authenticate': 'Basic realm="Login Required"'}
            )
        return f(*args, **kwargs)
    return decorated

@app.route('/data', methods=['GET'])
class MyEndpoint(Resource):
    def get_data():
        """
        Retrieve the data from the in-memory database.

        Returns:
            flask.Response: The JSON response containing the data.
        """
        return jsonify(data)

@app.route('/data', methods=['POST'])
class MyEndpoint(Resource):
    def update_data():
        """
        Update the data in the in-memory database.

        Returns:
            flask.Response: The JSON response containing the updated data.
        """
        new_data = request.json
        data.update(new_data)
        return jsonify(data), 200

if __name__ == '__main__':
    app.run(debug=True)
