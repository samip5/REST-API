from marshmallow import fields
from app.main import db, ma


class Messages(db.Model):
    __tablename__ = 'discord_messages'
    discord_message_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    server_id = db.Column(db.BigInteger, nullable=False)
    channel_id = db.Column(db.Integer, db.ForeignKey('discord_channels.channel_id'), unique=True, nullable=False)
    message_id = db.Column(db.BigInteger, nullable=False)
    message_date = db.Column(db.TIMESTAMP(3), server_default=db.func.current_timestamp(), nullable=False)
    person_name = db.Column(db.VARCHAR, nullable=False)
    message_text = db.Column(db.VARCHAR(2000), nullable=True)
    user_id = db.Column(db.BigInteger, nullable=False)

    def __init__(self, server_id, channel_id, message_id, message_date, person_name, message_text, user_id):
        self.server_id = server_id
        self.channel_id = channel_id
        self.message_id = message_id
        self.message_date = message_date
        self.person_name = person_name
        self.message_text = message_text
        self.user_id = user_id


class MessagesSchema(ma.Schema):
    discord_message_id = fields.Integer()
    server_id = fields.Integer()
    channel_id = fields.Integer()
    message_id = fields.Integer()
    message_date = fields.DateTime()
    person_name = fields.Field()
    message_text = fields.Field()
    user_id = fields.Integer()
