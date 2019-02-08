from flask import request
from flask_restful import Resource
from models import db, Discord_Users
from flask import jsonify


class UsersResource(Resource):
    def get(self):
        value = request.args.get('user_id')
        action = request.args.get('action')
        if value is not None and action == str('get_all'):
            query = db.session.query(Discord_Users.permission_granted, Discord_Users.joined_at,
                                     Discord_Users.permission_granted_update, Discord_Users.permission_revoked) \
                .filter(Discord_Users.user_id == value) \
                .one()
            return jsonify(status='success', data=query)
        elif value is not None and action == str('get_permission_granted'):
            query = db.session.query(Discord_Users.permission_granted)\
                .filter(Discord_Users.user_id == value) \
                .one()
            return jsonify(status='success', data=query)
        elif value is not None and action == str('get_joined_at'):
            query = db.session.query(Discord_Users.joined_at) \
                .filter(Discord_Users.user_id == value) \
                .one()
            return jsonify(status='success', data=query)
        elif value is not None and action == str('get_permssion_granted_update'):
            query = db.session.query(Discord_Users.permission_granted_update) \
                .filter(Discord_Users.user_id == value) \
                .one()
            return jsonify(status='success', data=query)
        elif value is not None and action == str('get_permission_revoked'):
            query = db.session.query(Discord_Users.permission_revoked) \
                .filter(Discord_Users.user_id == value) \
                .one()
            return jsonify(status='success', data=query)
        else:
            return {'status': 'failed', 'message': 'This is not how it works'}, 400

    def post(self):
        user_id = request.args.get('user_id')
        action = request.args.get('action')
        value = request.args.get('value')
        joined_at = request.args.get('joined_at')
        now = request.args.get('current_timestamp')
        if user_id is not None and action == str('update_permission_revoked') and value is not None:
            with db.engine.begin() as connection:
                connection.execute(f'UPDATE discord_users SET "permission_revoked" = %s WHERE "user_id" = %s',
                                   value, user_id)
            return {'status': 'success'}, 200
        elif user_id is not None and action == str('update_permission_granted') and value is not None:
            with db.engine.begin() as connection:
                connection.execute(f'UPDATE discord_users SET "permission_granted_update" = %s WHERE "user_id" = %s',
                                   value, user_id)
            return {'status': 'success'}, 200
        elif user_id is not None and action == str('insert_new_user') and value is not None and \
                joined_at is not None and now is not None:
            with db.engine.begin() as connection:
                connection.execute(f'INSERT INTO discord_users(user_id, joined_at, permission_granted) '
                                   f'values (%s, %s, %s)', user_id, joined_at, now)
            return {'status': 'success'}, 200
        else:
            return {'status': 'failed'}, 400


