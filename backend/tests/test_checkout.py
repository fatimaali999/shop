import unittest
from unittest.mock import patch
from app import create_app
from flask import json

class TestCheckoutRoutes(unittest.TestCase):

    def setUp(self):
        """Create a test client before each test."""
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    @patch('stripe.checkout.Session.create')
    def test_create_checkout_session(self, mock_create):
        """Test the create_checkout_session route."""
        
        # Mock the Stripe response
        mock_create.return_value = type('obj', (object,), {'id': 'test_session_id'})

        response = self.client.post('/create-checkout-session', 
                                     data=json.dumps({
                                         'product_name': 'Test Product',
                                         'amount': 2000,
                                         'quantity': 1
                                     }),
                                     content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertIn('id', response.get_json())
        self.assertEqual(response.get_json()['id'], 'test_session_id')

    def test_success_route(self):
        """Test the success route."""
        response = self.client.get('/success')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'message': 'Payment successful!'})

    def test_cancel_route(self):
        """Test the cancel route."""
        response = self.client.get('/cancel')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'message': 'Payment canceled.'})

    @patch('stripe.checkout.Session.create')
    def test_create_checkout_session_failure(self, mock_create):
        """Test failure case for create_checkout_session."""
        mock_create.side_effect = Exception('Stripe error')
        
        response = self.client.post('/create-checkout-session', 
                                     data=json.dumps({
                                         'product_name': 'Test Product',
                                         'amount': 2000,
                                         'quantity': 1
                                     }),
                                     content_type='application/json')

        self.assertEqual(response.status_code, 403)
        self.assertIn('error', response.get_json())

if __name__ == '__main__':
    unittest.main()

