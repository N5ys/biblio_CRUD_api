from flask import Blueprint, request, jsonify
from ..models.user import User
from ..app import session

user_routes = Blueprint('user_routes', __name__)


@user_routes.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user = User(**data)
    session.add(user)
    session.commit()
    return jsonify(user.__dict__), 201
