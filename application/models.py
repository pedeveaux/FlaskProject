from sqlalchemy.orm import backref, relationship
from application import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, unique=True, nullable=False)
    hashed_password = db.Column(db.String(60), nullable=False)

    def __init__(self, email, plaintext_password: str):
        self.email = email
        


class Permission(db.Model):

    __tablename__ = "permissions"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    permision_name = db.Column(db.String, unique=True, nullable=False)


class UserPermission(db.Model):
    __tablename__ = "userpermissions"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    permission_id = db.Column(db.Integer, db.ForeignKey("permissions.id"))
    users = relationship("Users", backref=backref("users", uselist=False))
