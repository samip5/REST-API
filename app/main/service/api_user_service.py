import uuid
import datetime

from app.main import db
from app.main.model.api_users import User
from flask_jwt_extended import create_access_token, create_refresh_token


def save_new_user(data):
    user = User.query.filter_by(email=data['username']).first()
    if not user:
        new_user = User(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            username=data['username'],
            password=data['password'],
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_user)
        return generate_token(new_user)
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def generate_token(user):
    access_token = create_access_token(identity=user.username)
    refresh_token = create_refresh_token(identity=user.username, expires_delta=datetime.timedelta(days=30))

    try:
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'access-token': access_token,
            'refresh-token': refresh_token
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def get_all_users():
    return User.query.all()


def get_a_user(public_id):
    return User.query.filter_by(public_id=public_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
