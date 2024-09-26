from app import create_app, db
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
import os
from your_database_module import check_db_connection
from config import Config


# Initialize the database and JWT manager
db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    
    # Load configuration from environment variables
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    
    # Initialize the database and JWT manager
    db.init_app(app)
    jwt.init_app(app)
    
    # Create all database tables
    with app.app_context():
        db.create_all()

    return app

app = create_app()

@app.route('/status', methods=['GET'])
def status():
    try:
        # Check your database connection here
        check_db_connection()  # Implement this function to validate your DB connection
        return jsonify({"status": "running", "db": "connected"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
