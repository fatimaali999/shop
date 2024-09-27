from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token,  jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app.models import User
import logging

logging.basicConfig(level=logging.DEBUG)

user_routes = Blueprint('user_routes', __name__)

# User Signup
@user_routes.route('/signup', methods=['POST'])
def signup():
    logging.debug(f"Received data: {data}")

    data = request.json
    
    # Check if email is already registered
    if User.query.filter_by(email=data['email']).first():
        return jsonify({"message": "Email already registered."}), 400

    # Check if passwords match
    if data['password'] != data['confirm_password']:
        return jsonify({"message": "Passwords do not match."}), 400

    hashed_password = generate_password_hash(data['password'])
    new_user = User(
        email=data['email'],
        name=data['name'],
        surname=data['surname'],
        password=hashed_password
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User signed up successfully."}), 201

# User Login
@user_routes.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()
    if user and check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity={'id': user.id, 'email': user.email, 'is_admin': user.is_admin})
        return jsonify(access_token=access_token), 200
    return jsonify({"message": "Invalid credentials."}), 401

# Protected Route
@user_routes.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
