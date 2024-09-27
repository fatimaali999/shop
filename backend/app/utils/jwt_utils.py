import jwt
import datetime
import os

SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'fallback_secret_key')

# Function to generate JWT
def generate_jwt(user_id):
    payload = {
        'id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30),  # Token expires in 30 mins
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

# Function to validate and decode JWT
def validate_jwt(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload  # Returns the payload if the token is valid
    except jwt.ExpiredSignatureError:
        return None  # Token has expired
    except jwt.InvalidTokenError:
        return None  # Invalid token

# Function to extract user information from the token
def get_user_id_from_jwt(token):
    payload = validate_jwt(token)
    if payload:
        return payload.get('id')
    return None
