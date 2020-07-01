from flask import Blueprint, Response, jsonify, request, abort, make_response
from dietapi.users.schema_validators import validate_registration_post, validate_login_post
from dietapi.marshmallow_utils import convert_errors_to_sentence
from dietapi.users.services import find_user_by_email, save_new_user, save_new_user_jwt, compare_login_password, generate_jwt
from dotenv import load_dotenv
import os
load_dotenv()

users = Blueprint('users', __name__)

@users.route('/users', methods=['GET'])
def test_route():
    return jsonify([{'message': 'hello'}])

@users.route('/register', methods=['POST'])
def register():
    user_dict = request.json
    errors = validate_registration_post(user_dict)
    if errors:
        abort(400, description=convert_errors_to_sentence(errors))

    existing = find_user_by_email(user_dict.get('email'))
    if existing:
        abort(400, description="Account already exists for this email")

    save_new_user(user_dict)

    return Response(None, 201)

@users.route('/login', methods=['POST'])
def login():
    login_dict =request.json
    errors = validate_login_post(login_dict)
    if errors:
        abort(400, description=convert_errors_to_sentence(errors))

    user = find_user_by_email(login_dict.get('email'))
    if user is None or compare_login_password(login_dict.get('password'), user.get('password')) is False:
        abort(401, description="Invalid credentials")

    jwt = generate_jwt(user)
    save_new_user_jwt(jwt, user.get('user_id'))
    domain = os.getenv("COOKIE_DOMAIN")
    resp = make_response()
    resp.set_cookie(key="DIET-API-COOKIE", value=jwt, domain=domain)

    return resp






