from marshmallow import fields
from app.main import db, ma


class Users(db.Model):
    __tablename__ = 'Users'
    uid = db.Column(db.Integer, primary_key=True)
    UserID = db.Column(db.BigInteger, nullable=False)
    Roles = db.Column(db.JSON, nullable=False)

    def __init__(self, uid, UserID, Roles):
        self.uid = uid
        self.UserID = UserID
        self.Roles = Roles


class UsersSchema(ma.Schema):
    uid = fields.Integer()
    UserID = fields.String()
    Roles = fields.Field()
