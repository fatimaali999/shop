from app import create_app, db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
import os
from app.checkout import checkout_routes
from dotenv import load_dotenv
from config import Config

load_dotenv()

def create_app():
    app = Flask(__name__)
    

     # Register the blueprint
     app.register_blueprint(checkout_routes)
     
     # Load configuration from environment variables
     app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL,' 'postgresql://myuser:password@localhost:5432/shopease_db
')
     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
     app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
     app.config['STRIPE_SECRET_KEY'] = os.getenv('STRIPE_SECRET_KEY')
     
     
     # Initialize the database and JWT manager
     db = SQLAlchemy(app)
     jwt = JWTManager(app)i
     migrate = Migrate(app, db)

     return app
     
     
     if __name__ == '__main__':
         app = create_app()
         app.run(debug=True)
