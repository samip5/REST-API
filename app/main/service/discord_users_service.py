from app.main.model.discord_users import Discord_Users
from app.main import db
from flask import jsonify


def get_all(user_id):
    query = db.session.query(Discord_Users.permission_granted, Discord_Users.joined_at,
                             Discord_Users.permission_granted_update, Discord_Users.permission_revoked)\
        .filter(Discord_Users.user_id == user_id).one()
    return jsonify(status='success', data=query)


def get_permission_granted(user_id):
    query = db.session.query(Discord_Users.permission_granted) \
        .filter(Discord_Users.user_id == user_id) \
        .one()
    return jsonify(status='success', data=query)


def get_joined_at(user_id):
    query = db.session.query(Discord_Users.joined_at) \
        .filter(Discord_Users.user_id == user_id) \
        .one()
    return jsonify(status='success', data=query)


def get_permission_granted_update(user_id):
    query = db.session.query(Discord_Users.permission_granted_update) \
        .filter(Discord_Users.user_id == user_id) \
        .one()
    return jsonify(status='success', data=query)


def get_permission_revoked(user_id):
    query = db.session.query(Discord_Users.permission_revoked) \
        .filter(Discord_Users.user_id == user_id) \
        .one()
    return jsonify(status='success', data=query)


def update_permission_revoked(user_id, value):
    with db.engine.begin() as connection:
        connection.execute(f'UPDATE discord_users SET "permission_revoked" = %s WHERE "user_id" = %s',
                           value, user_id)
        return {'status': 'success'}, 200


def update_permission_granted(user_id, value):
    with db.engine.begin() as connection:
        connection.execute(f'UPDATE discord_users SET "permission_granted_update" = %s WHERE "user_id" = %s',
                           value, user_id)
    return {'status': 'success'}, 200


def insert_new_user(user_id, joined_at, now):
    with db.engine.begin() as connection:
        connection.execute(f'INSERT INTO discord_users(user_id, joined_at, permission_granted) '
                           f'values (%s, %s, %s)', user_id, joined_at, now)
    return {'status': 'success'}, 200

