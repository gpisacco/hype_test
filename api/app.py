# -*- coding: utf-8 -*-

from flask import Flask, request
from flask_restful import  Api
from rest import Users, Providers, Vehicles

app = Flask(__name__)
api = Api(app)

api.add_resource(Users, '/users/<int:user_id>', '/users')
api.add_resource(Providers, '/providers/<int:prov_id>', '/providers')
api.add_resource(Vehicles, '/vehicles/<int:veh_id>', '/vehicles')


if __name__ == '__main__':
    app.run()
