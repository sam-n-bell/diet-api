from flask import Blueprint, Response, jsonify
from dietapi.users.models import UserModel, UserJwtModel

users = Blueprint('users', __name__)

@users.route('/users', methods=['GET'])
def test_route():
    return jsonify([{'message': 'hello'}])