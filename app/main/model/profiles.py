from marshmallow import fields
from app.main import db, ma


class Profile(db.Model):
    __tablename__ = 'Users_Profile'
    userid = db.Column(db.BigInteger, primary_key=True)
    settingsid = db.Column(db.Integer, primary_key=True)
    settingsvalue = db.Column(db.VARCHAR(255), nullable=True)

    def __init__(self, userid, settingsid, settingsvalue):
        self.userid = userid
        self.settingsid = settingsid
        self.settingsvalue = settingsvalue


class ProfileSchema(ma.Schema):
    userid = fields.Integer()
    settingsid = fields.Integer()
    settingsvalue = fields.String()
