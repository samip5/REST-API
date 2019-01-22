from flask import request
from flask_restful import Resource
from model import db, Messages, MessagesSchema, Channels, ChannelsSchema
from sqlalchemy import func

messages_schema = MessagesSchema(many=True)
message_schema = MessagesSchema()

channel_schema = ChannelsSchema()

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
            #thing = db.session.execute('select count(*) cnt, channel_name from discord_messages dm '
            #                           'inner join discord_channels dc on dm.channel_id = dc.channel_id '
            #                           'where user_id = $1 group by channel_name', value).one()
            count = (db.session.query(func.count(Messages.message_id), Channels.channel_name)
                     .join(Channels)
                     .filter(Channels.channel_id == Messages.channel_id, Messages.user_id == value)
                     .group_by(Channels.channel_name)
                     .all())

            return {'status': 'success', 'data': count}, 200
        else:
            return {'status': 'failed', 'data': 'This is not how it works'}, 400
