# -*- coding: utf-8 -*-

from flask import Flask, request
from flask_restful import  Api
from rest import Users, Providers, Vehicles, UsersList, ProvidersList, VehiclesList

app = Flask(__name__)
api = Api(app)

api.add_resource(Users, '/users/<int:key_id>')
api.add_resource(UsersList, '/users')

api.add_resource(Providers, '/providers/<int:key_id>', '/providers')
api.add_resource(ProvidersList, '/providers')

api.add_resource(Vehicles, '/vehicles/<int:key_id>')
api.add_resource(VehiclesList, '/vehicles')


if __name__ == '__main__':
    app.run()
