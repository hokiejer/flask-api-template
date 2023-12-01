from flask import Flask, jsonify, request, Response
from flask_restx import Api, Resource, fields
from functools import wraps
from flask_api.data import Data
from flask_api import auth
import os

app = Flask(__name__)
api = Api(app, doc='/swagger/') # Sets the URL for the Swagger documentation

# Simple in-memory database for demonstration
Data.global_dictionary = {"message": "Hello, World!"}

# Define a model for your data structure
data_model = api.model('DataModel', {
    'message': fields.String(description='A message.')
})

@api.route('/data')
class DataResource(Resource):
    """
    Resource for retrieving and updating data from the in-memory database.
    """

    method_decorators = [auth.requires_auth]

    @api.doc(params={'x-api-key': 'API Key'}, responses={
        200: ('Success', data_model),
        401: 'Unauthorized'
    })
    @api.marshal_with(data_model)
    def get(self):
        """
        Retrieve the data from the in-memory database.

        Returns:
            flask.Response: The JSON response containing the data.
        """
        return Data.global_dictionary
    
    @api.doc(params={'x-api-key': 'API Key'}, responses={200: 'Success', 401: 'Unauthorized'})
    @api.expect(data_model)
    @api.marshal_with(data_model)
    def post(self):
        """
        Update the data in the in-memory database.

        Returns:
            flask.Response: The JSON response containing the updated data.
        """
        new_data = request.json
        Data.global_dictionary = new_data
        return Data.global_dictionary, 200

if __name__ == '__main__':
    # This block of code will only be executed if the script is run directly (not imported as a module)
    app.run(debug=True)  # Start the Flask application in debug mode

