# test connection to flask server 
curl -X GET http://localhost:5000/

# GET Request to Check Database Status
curl -X GET http://localhost:5000/status

# esting User Registration (POST Request)
curl -X POST http://localhost:5000/register \
-H "Content-Type: application/json" \
-d '{"email": "testuser@example.com", "password": "yourpassword"}'

#  Testing Login (POST Request)
curl -X POST http://localhost:5000/login \
-H "Content-Type: application/json" \
-d '{"email": "testuser@example.com", "password": "yourpassword"}'

# Testing Stripe Payment (POST Request)
curl -X POST http://localhost:5000/pay \
-H "Content-Type: application/json" \
-d '{
    "amount": 5000,
    "currency": "usd",
    "source": "tok_visa",  # Replace with a valid Stripe token
    "description": "Payment for order #12345"
}'

# Testing Product Listing (GET Request)
curl -X GET http://localhost:5000/products

