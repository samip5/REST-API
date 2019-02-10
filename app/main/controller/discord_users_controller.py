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

