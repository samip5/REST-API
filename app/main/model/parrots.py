from marshmallow import fields
from app.main import db, ma


class ParrotModel(db.Model):
    __tablename__ = 'parrots'
    parrot_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    user_id = db.Column(db.VARCHAR(50), nullable=False)
    message_id = db.Column(db.VARCHAR(50), nullable=False)
    message_date = db.Column(db.DateTime, nullable=False)
    person_name = db.Column(db.VARCHAR(50), nullable=False)
    message_text = db.Column(db.VARCHAR(2000), nullable=True)
    message_url = db.Column(db.VARCHAR(200), nullable=True)
    channel_id = db.Column(db.VARCHAR(50), nullable=True)

    def __init__(self, parrot_id, user_id, message_id, message_date, person_name, message_text,
                 message_url, channel_id):
        self.parrot_id = parrot_id
        self.user_id = user_id
        self.message_id = message_id
        self.message_date = message_date
        self.person_name = person_name
        self.message_text = message_text
        self.message_url = message_url
        self.channel_id = channel_id
