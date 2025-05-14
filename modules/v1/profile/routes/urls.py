# import views.views as views # Assuming your view functions are defined in views.py
import modules.v1.profile.controller.user_controller as userview
from libraries import email
from flask import Blueprint

# Create a Blueprint object
user_bp = Blueprint('urls', __name__)
# user_bp.add_url_rule('/profile/<int:user_id>', view_func=userview.delete_user, methods=['DELETE'])
user_bp.add_url_rule('/profile', view_func=userview.delete_user, methods=['DELETE'])
user_bp.add_url_rule('/profile', view_func=userview.update_profile, methods=['PUT'])
user_bp.add_url_rule('/profile', view_func=userview.userinfo)
user_bp.add_url_rule('/mail', view_func=email.send_email)