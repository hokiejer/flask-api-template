from flask import Flask, jsonify, request, Response
from functools import wraps

app = Flask(__name__)

# Simple in-memory database for demonstration
data = {"message": "Hello, World!"}

# Authentication function
def check_auth(username, password):
    return username == 'admin' and password == 'secret'

# Decorator for routes that require authentication
def requires_auth(f):
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
@requires_auth
def get_data():
    return jsonify(data)

@app.route('/data', methods=['POST'])
@requires_auth
def update_data():
    new_data = request.json
    data.update(new_data)
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(debug=True)
