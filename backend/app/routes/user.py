from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app.models import User
import logging

logging.basicConfig(level=logging.DEBUG)

user_routes = Blueprint('user_routes', __name__)

# User Signup
@user_routes.route('/signup', methods=['POST'])
def signup():
    data = request.json

    logging.debug(f"Received data: {data}")
    
    # Check if email is already registered
    if User.query.filter_by(email=data['email']).first():
        return jsonify({"message": "Email already registered."}), 400

    # Check if passwords match
    if data['password'] != data['confirm_password']:
        return jsonify({"message": "Passwords do not match."}), 400

    hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')
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
    # Attempt to parse JSON data from the request
    try:
        data = request.json
        logging.debug(f"Login attempt with data: {data}")

        # Check if email and password are provided
        if not data or 'email' not in data or 'password' not in data:
            return jsonify({"message": "Email and password are required."}), 400
        
        # Query the user by email
        user = User.query.filter_by(email=data['email']).first()
        
        if user:
            logging.debug(f"User found: {user.email}")
            # Check if the password matches the hashed password
            if check_password_hash(user.password, data['password'], method='pbkdf2:sha256'):
                access_token = create_access_token(identity={'id': user.id, 'email': user.email, 'is_admin': user.is_admin})
                return jsonify(access_token=access_token), 200
            else:
                logging.debug("Password mismatch.")
                return jsonify({"message": "Invalid credentials."}), 401
        else:
            logging.debug("User not found.")
            return jsonify({"message": "Invalid credentials."}), 401

    except Exception as e:
        logging.error(f"Error during login: {str(e)}")
        return jsonify({"message": "An error occurred. Please try again later."}), 500


@user_routes.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
