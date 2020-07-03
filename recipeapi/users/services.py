from recipeapi.users.models import User, UserJwt
from recipeapi import db, bcrypt
from recipeapi.users.utils import serialize_one
from flask_jwt_extended import create_access_token
from datetime import datetime, timedelta


def find_user_by_email(email):
    user = User.query.filter(User.email == email).one_or_none()
    if user:
        user = user.__dict__
    return user

def save_new_user(user_dict):
    user_dict['password'] = bcrypt.generate_password_hash(user_dict.get('password'), 10).decode('utf8')
    user = User(email=user_dict.get('email'), password=user_dict.get('password'), first_name=user_dict.get('first_name'), last_name=user_dict.get('last_name'))
    db.session.add(user)
    db.session.commit()

def save_new_user_jwt(jwt, user_id):
    user_jwt = UserJwt(user_id=user_id, jwt=jwt)
    db.session.add(user_jwt)
    db.session.commit()

def compare_login_password(login_password, stored_password):
    return bcrypt.check_password_hash(stored_password, login_password)

def generate_jwt(user):
    return create_access_token(identity=serialize_one(user), expires_delta=timedelta(days=2))
