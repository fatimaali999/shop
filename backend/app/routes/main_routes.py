from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models import Product, CartItem


main_routes = Blueprint('main_routes', __name__)


@main_routes.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Welcome to ShopEase API!"}), 200

# Get products route
@main_routes.route('/products', methods=['GET'])
def get_products():
    category = request.args.get('category')
    if category:
        products = Product.query.filter_by(category=category).all()
    else:
        products = Product.query.all()

    product_list = [{"id": p.id, "name": p.name, "description": p.description, "price": p.price, "image_url": p.image_url, "category": p.category} for p in products]
    return jsonify(product_list), 200

# Add product route (admin only)
@main_routes.route('/admin/products', methods=['POST'])
@jwt_required()
def add_product():
    user_identity = get_jwt_identity()
    if not user_identity['is_admin']:
        return jsonify({"message": "Access denied. Admins only."}), 403

    data = request.json
    new_product = Product(
        name=data['name'],
        description=data['description'],
        price=data['price'],
        image_url=data.get('image_url'),
        category=data['category']
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify({"message": "Product added successfully"}), 201

# Add to cart route
@main_routes.route('/cart', methods=['POST'])
@jwt_required()
def add_to_cart():
    user_identity = get_jwt_identity()
    data = request.json
    user_id = user_identity['id']
    new_cart_item = CartItem(user_id=user_id, product_id=data['product_id'], quantity=data['quantity'])
    db.session.add(new_cart_item)
    db.session.commit()
    return jsonify({"message": "Item added to cart"}), 201
