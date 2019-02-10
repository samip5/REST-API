from app.main.model.messages import Messages, MessagesSchema
from app.main import db


def get_messages(user_id):
    messages = Messages.query.filter(Messages.user_id == user_id)
    messages = MessagesSchema.dump(messages).data
    return messages


def post_message(server_id, channel_id, message_id, message_date, person_name, message_text, user_id):
    db.session.add(Messages(server_id=server_id,
                            channel_id=channel_id,
                            message_id=message_id,
                            message_date=message_date,
                            person_name=person_name,
                            message_text=message_text,
                            user_id=user_id))
    db.session.commit()
    return {'status': 'success'}, 200
