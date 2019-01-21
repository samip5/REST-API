from flask import request
from flask_restful import Resource
from model import db, Messages, MessagesSchema
from sqlalchemy import func

messages_schema = MessagesSchema(many=True)
message_schema = MessagesSchema()


class MessageResource(Resource):
    def get(self):
        value = request.args.get('user_id')
        if value is not None:
            messages = Messages.query.filter(Messages.user_id == value)
            messages = messages_schema.dump(messages).data
            return {'status': 'success', 'data': messages}, 200
        else:
            messages = Messages.query.all()
            messages = message_schema.dump(messages).data
            return {'status': 'success', 'data': messages}, 200


class CountMessages(Resource):
    def get(self):
        value = request.args.get('user_id')
        if value is not None:
            count = db.session.query(func.count(Messages.message_id)).filter(Messages.user_id == value).one()
            return {'status': 'success', 'data': count}, 200
        else:
            return {'status': 'failed', 'data': 'This is not how it works'}, 400

class CountMessagesByChannel(Resource):
    def get(self):
        value = request.args.get('user_id')
        if value is not None:
            count = db.session.query()
