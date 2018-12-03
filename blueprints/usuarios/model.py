import uuid

from ext.bcrypt_password import bcrypt
from ext.db import db


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.String, primary_key=True, default=uuid.uuid4())
    username = db.Column(db.String(64), index=True, unique=True, nullable=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))

    def __repr__(self):
        return f'<User {self.username}>'

    def __init__(self, email, password, username):
        self.username = username
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode()

    def password_is_valid(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def find_all():
        return str([str(a.nome) for a in User.query.order_by(User.nome).all()])
