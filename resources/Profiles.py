from flask import request
from flask_restful import Resource
from models import db, Profile, ProfileSchema


class ProfilesResource(Resource):
    def get(self):
        value = request.args.get('user_id')
        if value is not None:
            query = db.session.query(Profile.settingsid, Profile.settingsvalue)\
                .filter(Profile.userid == value)\
                .all()
            return {'status': 'success', 'data': query}, 200
        else:
            return {'status': 'failed', 'message': 'This is not how it works'}, 400
