from flask_restful import Resource, Api
from flask import jsonify, request
from collections import namedtuple
from flask.ext.restful import abort

from model import db


def row2dict(row):
    d = {}
    table = str(row._sa_instance_state.class_._table)
    for column in row._sa_instance_state.class_._table.columns:
        col = column.name.replace(table + '.','')
        d[col] = str(getattr(row, col))
    return d
    
class Users(Resource):
    def get(self, user_id):
        try:
            user = db.users.filter(db.users.nid == user_id).one()
            return row2dict(user)
        except Exception as e:
            abort(500, message=str(e))

    def post(self):
        try:
            data = request.json
            user = db.users.insert(**(data))
            v = db.commit()
            return row2dict(user)
        except Exception as e:
            db.rollback()
            abort(500, message=str(e))
    
    def patch(self):
        try:
            data = request.json
            user = db.users.insert(**(data))
            v = db.commit()
            return row2dict(user)
        except Exception as e:
            db.rollback()
            abort(500, message=str(e))


class Vehicles(Resource):
    def get(self, veh_id):
        try:
            user = db.objects.filter(db.objects.nid == veh_id).one()
            return row2dict(user)
        except Exception as e:
            abort(500, message=str(e))

    def post(self):
        try:
            data = request.json
            user = db.objects.insert(**(data))
            v = db.commit()
            return row2dict(user)
        except Exception as e:
            db.rollback()
            abort(500, message=str(e))
    
    def patch(self):
        try:
            data = request.json
            user = db.users.insert(**(data))
            v = db.commit()
            return row2dict(user)
        except Exception as e:
            db.rollback()
            abort(500, message=str(e))

class Locations(Resource):
    def get(self, user_id):
        try:
            user = db.users.filter(db.users.nid == user_id).one()
            return row2dict(user)
        except Exception as e:
            abort(500, message=str(e))

    def post(self):
        try:
            data = request.json
            user = db.users.insert(**(data))
            v = db.commit()
            return row2dict(user)
        except Exception as e:
            db.rollback()
            abort(500, message=str(e))
    
    def patch(self):
        try:
            data = request.json
            user = db.users.insert(**(data))
            v = db.commit()
            return row2dict(user)
        except Exception as e:
            db.rollback()
            abort(500, message=str(e))
            
class Settings(Resource):
    def get(self, user_id):
        try:
            user = db.users.filter(db.users.nid == user_id).one()
            return row2dict(user)
        except Exception as e:
            abort(500, message=str(e))

    def post(self):
        try:
            data = request.json
            user = db.users.insert(**(data))
            v = db.commit()
            return row2dict(user)
        except Exception as e:
            db.rollback()
            abort(500, message=str(e))
    
    def patch(self):
        try:
            data = request.json
            user = db.users.insert(**(data))
            v = db.commit()
            return row2dict(user)
        except Exception as e:
            db.rollback()
            abort(500, message=str(e))

class Providers(Resource):
    def get(self, prov_id):
        try:
            prov = db.providers.filter(db.providers.nid == prov_id).one()
            print prov
            return row2dict(prov)
        except Exception as e:
            abort(500, message=str(e))

    def post(self):
        try:
            data = request.json
            prov = db.providers.insert(**(data))
            v = db.commit()
            return row2dict(prov)
        except Exception as e:
            db.rollback()
            abort(500, message=str(e))
    
    def patch(self):
        try:
            data = request.json
            user = db.users.insert(**(data))
            v = db.commit()
            return row2dict(user)
        except Exception as e:
            db.rollback()
            abort(500, message=str(e))