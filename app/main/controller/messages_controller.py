from flask import request
from flask_restplus import Resource, reqparse
from ..util.dto import MessagesDto

from ..service.messages_service import get_messages, post_message

api = MessagesDto.api
_message = MessagesDto.message

parser = reqparse.RequestParser()
parser.add_argument('Authorization', required=True, type=str, location='headers', help='Token')


@api.route('/')
class MessagesResource(Resource):
    @api.doc('Users Messages', responses={200: 'Accepted', 204: 'No Content'})
    @api.param('user_id', 'The user identifier')
    @api.expect(parser)
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
    @api.expect(parser, _message, validate=True)
    def post(self):
        server_id = request.json.get('server_id')
        channel_id = request.json.get('channel_id')
        message_id = request.json.get('message_id')
        message_date = request.json.get('message_date')
        person_name = request.json.get('person_name')
        message_text = request.json.get('message_text')
        user_id = request.json.get('user_id')
        """Saves a new message to database"""
        return post_message(server_id, channel_id, message_id, message_date, person_name, message_text, user_id)

