from flask import request, jsonify, json

from app.main.model.api_users import User
from flask_jwt_extended import get_jwt_identity, current_user, create_refresh_token, create_access_token, get_raw_jwt
from datetime import timedelta
from app.main import jwt, db
from app.main.util.blacklist_helpers import (
    is_token_revoked, add_token_to_database, get_user_tokens,
    revoke_token, unrevoke_token,
    prune_database
)
from app.main.util.exceptions import TokenNotFound
from app.main.config import Config


class Auth:

    @staticmethod
    def login_user(data):
        user = None
        try:
            # fetch the user data
            user = User.query.filter_by(username=data.get('username')).first()
        except Exception as e:
            print(e)

        if user is None:
            try:
                user = User.query.filter_by(email=data.get('username')).first()
            except Exception as e:
                print(e)

        if user and user.check_password(data.get('password')):
            #test_data = json.dumps(data)
            #print(test_data)
            access_token = create_access_token(identity=data['username'], fresh=True)
            refresh_token = create_refresh_token(identity=data['username'], expires_delta=timedelta(hours=1))
            response_object = {
                'status': 'success',
                'message': 'Successfully logged in.',
                'authorization': {
                    'access-token': access_token,
                    'refresh-token': refresh_token
                }
            }
            return response_object, 200

    @staticmethod
    def get_logged_in_user():
        response_object = {
            'status': 'success',
            'logged_in_as': current_user
        }
        return response_object, 200

    @staticmethod
    def get_tokens():
        user_identity = get_jwt_identity()
        all_tokens = get_user_tokens(user_identity)
        ret = [token.to_dict() for token in all_tokens]
        response_object = {
            'status': 'success',
            'data': jsonify(ret)
        }
        return response_object, 200

    @staticmethod
    def refresh_token():
        # Do the same thing that we did in the login endpoint here
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        add_token_to_database(access_token, Config.JWT_IDENTITY_CLAIM)
        return jsonify({'access_token': access_token}), 201

    @staticmethod
    def modify_token(token_id):
        # Get and verify the desired revoked status from the body
        json_data = request.get_json(silent=True)
        if not json_data:
            return jsonify({"msg": "Missing 'revoke' in body"}), 400
        revoke = json_data.get('revoke', None)
        if revoke is None:
            return jsonify({"msg": "Missing 'revoke' in body"}), 400
        if not isinstance(revoke, bool):
            return jsonify({"msg": "'revoke' must be a boolean"}), 400

        # Revoke or unrevoke the token based on what was passed to this function
        user_identity = get_jwt_identity()
        try:
            if revoke:
                revoke_token(token_id, user_identity)
                return jsonify({'msg': 'Token revoked'}), 200
            else:
                unrevoke_token(token_id, user_identity)
                return jsonify({'msg': 'Token unrevoked'}), 200
        except TokenNotFound:
            return jsonify({'msg': 'The specified token was not found'}), 404

    # Define our callback function to check if a token has been revoked or not
    @jwt.token_in_blacklist_loader
    def check_if_token_revoked(decoded_token):
        return is_token_revoked(decoded_token)
