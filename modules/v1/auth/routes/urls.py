# import views.views as views # Assuming your view functions are defined in views.py
import modules.v1.auth.controller.auth_controller as authview
# from app import urls_bp
from flask import Blueprint

# Create a Blueprint object
auth_bp = Blueprint('auth', __name__)

# Add more URL rules as needed
# auth urls
auth_bp.add_url_rule('/register', view_func=authview.register, methods=['POST'])
auth_bp.add_url_rule('/login', view_func=authview.login, methods=['POST'])
auth_bp.add_url_rule('/logout', view_func=authview.logout)
auth_bp.add_url_rule('/reset_password', view_func=authview.reset_password, methods=['POST'])