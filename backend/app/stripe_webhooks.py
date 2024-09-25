from flask import Blueprint, request, jsonify
import stripe
from app import db
from app.models import Order

stripe.api_key = Config.STRIPE_SECRET_KEY

stripe_webhooks = Blueprint('stripe_webhooks', __name__)

@stripe_webhooks.route('/stripe-webhook', methods=['POST'])
def stripe_event():
    payload = request.get_data(as_text=True)
    sig_header = request.headers.get('Stripe-Signature')
    
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, Config.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        return 'Invalid payload', 400
    except stripe.error.SignatureVerificationError as e:
        return 'Invalid signature', 400
    
    # Handle payment successful event
    if event['type'] == 'payment_intent.succeeded':
        intent = event['data']['object']
        order = Order.query.filter_by(stripe_payment_intent_id=intent['id']).first()
        if order:
            order.status = "completed"
            db.session.commit()

    return jsonify(success=True)
