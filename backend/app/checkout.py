import stripe
from flask import Blueprint, request, jsonify

checkout_routes = Blueprint('checkout_routes', __name__)

@checkout_routes.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        # Initialize Stripe
        stripe.api_key = app.config['STRIPE_SECRET_KEY'] 

        # Get the request data
        data = request.json
        
        # Create a new checkout session
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': data['product_name'],
                        },
                        'unit_amount': data['amount'],
                    },
                    'quantity': data['quantity'],
                },
            ],
            mode='payment',
            success_url='http://localhost:5000/success',
            cancel_url='http://localhost:5000/cancel',
        )
        
        return jsonify({'id': checkout_session.id}), 200
    except Exception as e:
        return jsonify(error=str(e)), 403

    @checkout_routes.route('/success', methods=['GET'])
def success():
    return jsonify({'message': 'Payment successful!'}), 200

@checkout_routes.route('/cancel', methods=['GET'])
def cancel():
    return jsonify({'message': 'Payment canceled.'}), 200
