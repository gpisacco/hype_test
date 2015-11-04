# -*- coding: utf-8 -*-

from flask import Flask, request
from flask_restful import  Api
from rest import Users

app = Flask(__name__)
api = Api(app)

api.add_resource(Users, '/users/<int:user_id>', '/users')


if __name__ == '__main__':
    app.run()
