from flask_restful import Resource, Api
from flask import jsonify, request

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
        print user_id
        try:
            user = db.users.filter(db.users.nid == user_id).one()
            return row2dict(user)
        except Exception as e:
            print e

    def post(self):
        try:
            data = request.json
            user = db.users.insert(data)
            v = db.commit()
            print v
            return row2dict(user)
        except Exception as e:
            print e
        