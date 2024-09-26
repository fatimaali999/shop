from flask import Blueprint
from .main_routes import main_routes
from .user_routes import user_routes

app_routes = Blueprint('app_routes', __name__)

app_routes.register_blueprint(main_routes)
app_routes.register_blueprint(user_routes)
