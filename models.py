from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
import config

from passlib.apps import custom_app_context as pwd_context


ma = Marshmallow()
db = SQLAlchemy()


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


class Channels(db.Model):
    __tablename__ = 'discord_channels'
    channel_id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    channel_name = db.Column(db.VARCHAR, nullable=False)

    def __init__(self, channel_id, channel_name):
        self.channel_id = channel_id
        self.channel_name = channel_name


class Profile(db.Model):
    __tablename__ = 'Users_Profile'
    userid = db.Column(db.BigInteger, primary_key=True)
    settingsid = db.Column(db.Integer, primary_key=True)
    settingsvalue = db.Column(db.VARCHAR(255), nullable=True)

    def __init__(self, userid, settingsid, settingsvalue):
        self.userid = userid
        self.settingsid = settingsid
        self.settingsvalue = settingsvalue


class Users(db.Model):
    __tablename__ = 'Users'
    uid = db.Column(db.Integer, primary_key=True)
    UserID = db.Column(db.BigInteger, nullable=False)
    Roles = db.Column(db.JSON, nullable=False)

    def __init__(self, uid, UserID, Roles):
        self.uid = uid
        self.UserID = UserID
        self.Roles = Roles


class MessagesSchema(ma.Schema):
    discord_message_id = fields.Integer()
    server_id = fields.Integer()
    channel_id = fields.Integer()
    message_id = fields.Integer()
    message_date = fields.DateTime()
    person_name = fields.Field()
    message_text = fields.Field()
    user_id = fields.Integer()


class ChannelsSchema(ma.Schema):
    channel_id = fields.Integer()
    channel_name = fields.String()


class ProfileSchema(ma.Schema):
    uid = fields.Integer()
    UserID = fields.String()
    Roles = fields.Field()
