from flask import request
from flask_restplus import Resource
from ..util.dto import MessagesDto

from ..service.messages_service import get_messages, post_message

api = MessagesDto.api


@api.route('')
class MessagesResource(Resource):
    @api.doc('Users Messages', responses={200: 'Accepted', 204: 'No Content'})
    @api.param('user_id', 'The user identifier')
    def get(self):
        """Get's users messages"""
        value = request.args.get('user_id')
        if value is not None:
            return get_messages(value)
        else:
            return {'status': 'failed', 'message': 'This is not supported.'}, 400


@api.route('/post')
class PostMessage(Resource):
    @api.doc('Post a new message')
    @api.param('server_id', 'Messages server ID')
    @api.param('channel_id', 'Messages channel ID')
    @api.param('message_id', 'Messages own ID')
    @api.param('message_date', 'Messages datetime in UTC from Discord')
    @api.param('person_name', 'Discord users display_name')
    @api.param('message_text', 'The message itself')
    @api.param('user_id', 'The user identifier')
    def post(self):
        server_id = request.args.get('server_id')
        channel_id = request.args.get('channel_id')
        message_id = request.args.get('message_id')
        message_date = request.args.get('message_date')
        person_name = request.args.get('person_name')
        message_text = request.args.get('message_text')
        user_id = request.args.get('user_id')
        """Saves a new message to database"""
        return post_message(server_id, channel_id, message_id, message_date, person_name, message_text, user_id)

