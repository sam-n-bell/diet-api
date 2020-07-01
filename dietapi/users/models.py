from dietapi import db, ma
from datetime import datetime
from citext import CIText
from sqlalchemy.dialects.postgresql import UUID
import uuid

# https://stackoverflow.com/a/49398042/7858114 UUID
class UserModel(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    email = db.Column(CIText(), unique=True, nullable=False)
    password = db.Column(CIText(), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    first_name = db.Column(CIText(), nullable=False)
    last_name = db.Column(CIText(), nullable=False)
    jwts = db.relationship('UserJwt', backref="user", lazy=True)

    def __repr__(self):
        return f'User(user_id: {self.user_id}, email: {self.email}, password: {self.password}, date_created: {self.date_created}, first_name: {self.first_name}, last_name: {self.last_name})'

class UserJwtModel(db.Model):
    __tablename__ = 'user_jwts'
    user_jwt_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('users.user_id'), nullable=False)
    jwt = db.Column(CIText(), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'UserJwt(jwt_id: {self.user_jwt_id}, jwt: {self.jwt}, date_created: {self.date_created}, user_id: {self.user_id})'
