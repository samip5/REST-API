from marshmallow import fields
from app.main import db, ma


class Profile(db.Model):
    __tablename__ = 'users_profile'
    userid = db.Column(db.BigInteger, primary_key=True)
    permissionsid = db.Column(db.Integer, nullable=True)
    settingsid = db.Column(db.Integer, primary_key=True)
    settingsvalue = db.Column(db.VARCHAR(255), nullable=True)
    permissionsvalue = db.Column(db.VARCHAR())
    notify_consent = db.Column(db.Boolean, default=False, nullable=True)

    def __init__(self, userid, permisisonsid, settingsid, settingsvalue, permissionsvalue, notify_consent):
        self.userid = userid
        self.permissionsid = permisisonsid
        self.settingsid = settingsid
        self.settingsvalue = settingsvalue
        self.permissionsvalue = permissionsvalue
        self.notify_consent = notify_consent


class ProfileSchema(ma.Schema):
    userid = fields.Integer()
    permissionsid = fields.Integer()
    settingsid = fields.Integer()
    settingsvalue = fields.String()
    permissionsvalue = fields.String()
    notify_consent = fields.Boolean()
