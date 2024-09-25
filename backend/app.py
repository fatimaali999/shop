from app import create_app, db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
import os


app = Flask(__name__)

app = create_app()

# Load configuration from environment variables
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

# Initialize the database and JWT manager
db = SQLAlchemy(app)
jwt = JWTManager(app)


if __name__ == '__main__':
    app.run(debug=True)
