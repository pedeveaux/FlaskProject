from sqlalchemy.orm import backref, relationship
from application import db, bcrypt


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, unique=True, nullable=False)
    hashed_password = db.Column(db.String(60), nullable=False)

    def is_correct_password(self, plaintext_password: str):
        return bcrypt.check_password_hash(self.hashed_password, plaintext_password)

    def __init__(self, email, plaintext_password: str):
        self.email = email
        self.hashed_password = bcrypt.generate_password_hash(plaintext_password).decode(
            "utf-8"
        )

    def set_password(self, plaintext_password):
        self.hashed_password = bcrypt.generate_password_hash(plaintext_password).decode(
            "utf-8"
        )


class Permission(db.Model):

    __tablename__ = "permissions"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    permision_name = db.Column(db.String, unique=True, nullable=False)

    def __init__(self, permission_name) -> None:
        self.permision_name = permission_name


class UserPermission(db.Model):
    __tablename__ = "userpermissions"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    permission_id = db.Column(db.Integer, db.ForeignKey("permissions.id"))
    users = relationship("User", backref=backref("users", uselist=False))
    permissions = relationship("Permission", backref=backref("permissions", uselist=False))
