# ShopEase Backend
ShopEase is a Flask-based backend application designed to facilitate e-commerce functionalities, including user authentication, product management, and payment processing through Stripe.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Database Setup](#database-setup)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Running Tests](#running-tests)
- [License](#license)

## Features

- User signup and login functionality
- Product management (fetching products and filtering by category)
- Shopping cart functionality
- Checkout process with Stripe payment integration
- RESTful API

## Technologies

- **Flask**: Web framework for Python
- **PostgreSQL**: Relational database management system
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapping (ORM) system for Python
- **Flask-Migrate**: Database migration tool for SQLAlchemy
- **Stripe**: Payment processing platform
- **pytest**: Testing framework for Python

## Installation

To set up the backend locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd ShopEase/backend

2. Create a virtual environment:
   python3 -m venv venv

3. Activate the virtual environment:
   source venv/bin/activate
   venv\Scripts\activate

4. Install the required packages:
   pip install -r requirements.txt

## Configuration

1. Create a .env file in the root of the project and configure the following environment variables:
FLASK_APP=app.py
FLASK_ENV=development
DATABASE_URL=postgresql://<username>:<password>@localhost:5432/<database_name>
STRIPE_SECRET_KEY=your_stripe_secret_key

## Database Setup

1. Ensure PostgreSQL is installed and running on your machine.
2. Create a new PostgreSQL database:
psql -U <username>
CREATE DATABASE <database_name>;

3. Initialize the database and apply migrations:
flask db init
flask db migrate -m "Initial migration."
flask db upgrade

## Running the Application

To start the Flask development server, run:
flask run

API Endpoints

User Management
POST /signup: Register a new user.
POST /login: Authenticate a user.

Product Management
GET /products: Fetch all products.
GET /products/category/<category>: Fetch products by category.

Shopping Cart
POST /cart: Add an item to the shopping cart.

Checkout
POST /create-checkout-session: Create a checkout session with Stripe.

Success and Cancel
GET /success: Success page after payment.
GET /cancel: Cancel page if payment is aborted.

## Running Tests

python -m unittest discover -s tests


## License

This project is licensed under the MIT License. 
