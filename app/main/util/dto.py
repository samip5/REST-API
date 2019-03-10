from flask_restplus import Namespace, fields


class ApiUserDto:
    api = Namespace('api_user', description='api user related operations')
    user = api.model('api_users', {
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password')
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
        'permissionsid': fields.Integer(required=True, description='The permissions ID'),
        'settingsid': fields.String(required=True, description='Settings ID of the profile'),
        'settingsvalue': fields.String(required=False, description='Settings value'),
        'permissionsvalue': fields.Integer(required=True, description='Integer value of the desired permission')
    })
    parrot = api.model('parrot', {
        'user_id': fields.String(required=True, description='User Discord ID'),
        'message_id': fields.String(required=True, description='Message ID from Discord'),
        'message_date': fields.DateTime(required=True, description='The UTC datetime when the message was posted '
                                                                   'from Discord'),
        'person_name': fields.String(required=True, description="User's display_name from Discord"),
        'message_text': fields.String(required=True, description='Message content itself'),
        'message_url': fields.String(required=True, description='The jump URL'),
        'channel_id': fields.String(required=True, description='The channel ID where the message was posted')
    })
    publicity_update_profile = api.model('publicity_update', {
        'userid': fields.Integer(required=True, description='User Discord ID'),
        'perm_id': fields.Integer(required=True, description='The permissions ID'),
        'settings_id': fields.Integer(required=True, description='The settings ID'),
        'perm_value': fields.Integer(required=True, description='Integer value of the desired permission')
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
        'username': fields.String(required=True, description='The username'),
        'password': fields.String(required=True, description='The user password '),
    })
