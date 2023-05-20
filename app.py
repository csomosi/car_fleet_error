from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):

  def get(self):
    return {'hello': 'world'}

  def post(self):
    return {'hello': 'bla'}


api.add_resource(HelloWorld, '/')
