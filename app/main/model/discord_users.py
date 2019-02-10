from app.main import db


class Discord_Users(db.Model):
    __tablename__ = 'discord_users'
    uid = db.Column(db.Integer, nullable=False, autoincrement=True)
    user_id = db.Column(db.BigInteger, nullable=False, primary_key=True)
    joined_at = db.Column(db.TIMESTAMP(3), nullable=False)
    permission_granted = db.Column(db.TIMESTAMP(3))
    permission_revoked = db.Column(db.TIMESTAMP(3), nullable=True)
    permission_granted_update = db.Column(db.TIMESTAMP(3), nullable=True)

    def __init__(self, uid, user_id, joined_at, permission_granted, permission_revoked, permission_granted_update):
        self.uid = uid
        self.user_id = user_id
        self.joined_at = joined_at
        self.permission_granted = permission_granted
        self.permission_revoked = permission_revoked
        self.permission_granted_update = permission_granted_update
