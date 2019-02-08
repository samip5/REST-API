from flask import request
from flask_restplus import Resource
from models import db, Messages, MessagesSchema, Channels, ChannelsSchema
from sqlalchemy import func

messages_schema = MessagesSchema(many=True)
message_schema = MessagesSchema()

channel_schema = ChannelsSchema()


class MessageResource(Resource):
    """Hello there"""
    def get(self):
        """Request type is GET."""
        value = request.args.get('user_id')
        if value is not None:
            messages = Messages.query.filter(Messages.user_id == value)
            messages = messages_schema.dump(messages).data
            return {'status': 'success', 'data': messages}, 200
        else:
            return {'status': 'failed', 'message': 'This is not supported.'}, 400

    def post(self):
        """Request type is POST."""
        server_id = request.args.get('server_id')
        channel_id = request.args.get('channel_id')
        message_id = request.args.get('message_id')
        message_date = request.args.get('message_date')
        person_name = request.args.get('person_name')
        message_text = request.args.get('message_text')
        user_id = request.args.get('user_id')
        if server_id is not None:
            if channel_id is not None:
                if message_id is not None:
                    if message_date is not None:
                        if person_name is not None:
                            if message_text is not None:
                                if user_id is not None:
                                    db.session.add(Messages(server_id=server_id,
                                                            channel_id=channel_id,
                                                            message_id=message_id,
                                                            message_date=message_date,
                                                            person_name=person_name,
                                                            message_text=message_text,
                                                            user_id=user_id))
                                    db.session.commit()
                                    return {'status': 'success'}, 200
                                    # result =
                                else:
                                    return {'status': 'failed', 'message': 'You failed to give me user_id.'}, 400
                            else:
                                return {'status': 'failed', 'message': 'You failed to give me message_text.'}, 400
                        else:
                            return {'status': 'failed', 'message': 'You failed to give me person_name.'}, 400
                    else:
                        return {'status': 'failed', 'message': 'You failed to give me message_date.'}, 400
                else:
                    return {'status': 'failed', 'message': 'You failed to give me message_id.'}, 400
            else:
                return {'status': 'failed', 'message': 'You failed to give me channel_id.'}, 400
        else:
            return {'status': 'failed', 'message': 'You failed to give me server_id.'}, 400


class CountMessages(Resource):
    def get(self):
        """Request type is GET."""
        value = request.args.get('user_id')
        if value is not None:
            count = db.session.query(func.count(Messages.message_id)).filter(Messages.user_id == value).one()
            return {'status': 'success', 'data': count}, 200
        else:
            return {'status': 'failed', 'message': 'This is not how it works'}, 400


class CountMessagesByChannel(Resource):
    def get(self):
        """Request type is GET."""
        # We require the user_id to be passed to the API endpoint,# otherwise we wont output anything execpt a error.
        value = request.args.get('user_id')
        if value is not None:
            count = (db.session.query(func.count(Messages.message_id), Channels.channel_name)
                     .join(Channels)
                     .filter(Channels.channel_id == Messages.channel_id, Messages.user_id == value)
                     .group_by(Channels.channel_name)
                     .all())
            return {'status': 'success', 'data': count}, 200
        else:
            return {'status': 'failed', 'data': 'This is not how it works'}, 400
