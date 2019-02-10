from marshmallow import fields
from app.main import db, ma


class Channels(db.Model):
    __tablename__ = 'discord_channels'
    channel_id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    channel_name = db.Column(db.VARCHAR, nullable=False)

    def __init__(self, channel_id, channel_name):
        self.channel_id = channel_id
        self.channel_name = channel_name


class ChannelsSchema(ma.Schema):
    channel_id = fields.Integer()
    channel_name = fields.String()
