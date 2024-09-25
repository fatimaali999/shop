from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app.models import User, Product, CartItem

main_routes = Blueprint('main_routes', __name__)

# Register user route
@main_routes.route('/register', methods=['POST'])
def register():
    data = request.json
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(email=data['email'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201

# Login user route
@main_routes.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()
    if user and check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity={'email': user.email, 'is_admin': user.is_admin})
        return jsonify(access_token=access_token), 200
    return jsonify({"message": "Invalid credentials"}), 401

# Get products route
@main_routes.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    product_list = [{"id": p.id, "name": p.name, "description": p.description, "price": p.price, "image_url": p.image_url} for p in products]
    return jsonify(product_list), 200

# Add to cart route
@main_routes.route('/cart', methods=['POST'])
@jwt_required()
def add_to_cart():
    user_identity = get_jwt_identity()
    data = request.json
    new_cart_item = CartItem(user_id=user_identity['id'], product_id=data['product_id'], quantity=data['quantity'])
    db.session.add(new_cart_item)
    db.session.commit()
    return jsonify({"message": "Item added to cart"}), 201

