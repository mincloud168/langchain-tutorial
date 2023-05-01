from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class ChatResource(Resource):
    def get(self):
        return {"message": "This is a GET request from a Flask-RESTful endpoint"}

    def post(self):
        return {"message": "This is a POST request from a Flask-RESTful endpoint"}

# Register the ExampleResource with the route '/example'
api.add_resource(ChatResource, '/chat')

if __name__ == '__main__':
    app.run(debug=True)

