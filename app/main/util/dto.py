from flask_restplus import Namespace, fields


class ApiUserDto:
    api = Namespace('api_user', description='api user related operations')
    user = api.model('api_users', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })


class TestingDto:
    api = Namespace('tests', description='Testing operations')


class ChannelsDto:
    api = Namespace('channels', description='Channel related operations')
    channel = api.model('channels', {
        'channel_id': fields.Integer(required=True, description="Channel's ID"),
        'channel_name': fields.String(required=False)
    })


class ProfilesDto:
    api = Namespace('profiles', description='Profiles related operations')
    profile = api.model('profiles', {
        'userid': fields.Integer(required=True, description='User Discord ID'),
        'settingsid': fields.String(required=True, description='Settings ID of the profile'),
        'settingsvalue': fields.String(required=False, description='Settings value')
    })


class MessagesDto:
    api = Namespace('messages', description='Messages related operations')
    message = api.model('messages', {
        'server_id': fields.Integer(required=True, description='The server ID the message is from'),
        'channel_id': fields.Integer(required=True, description='The channel ID the message is from'),
        'message_id': fields.Integer(required=True, description='The message ID of the message'),
        'message_date': fields.DateTime(required=True, description="The message's datetime, as in "
                                                                   "when it was sent in Discord"),
        'person_name': fields.String(required=True, description="The user's name in Discord who sent the message"),
        'message_text': fields.String(required=True, description='The message content itself.'),
        'user_id': fields.Integer(required=True, description="The user's unique id in Discord")
    })


class UsersDto:
    api = Namespace('users', description='Users related operations')
    user = api.model('users', {
        'userID': fields.Integer(required=True, description="User's unique ID on Discord"),
        'Roles': fields.String(required=False, description="User's roles")
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })
