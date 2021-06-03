from application import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Coumn(db.String, unique=True, nullable=False)
    hashed_password = db.Column(db.String(60), nullable=False)


class Privilege(db.Model):

    __tablename__ = "privileges"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
