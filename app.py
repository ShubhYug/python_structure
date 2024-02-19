from flask_swagger_ui import get_swaggerui_blueprint
from flask import send_from_directory
from flask_babel import Babel, _
from config.config import db
from database.models.models import Members_Info
from flask_migrate import Migrate
from flask_login import LoginManager, login_required, AnonymousUserMixin, current_user
from modules.v1.auth.routes.urls import auth_bp
from modules.v1.profile.routes.urls import user_bp
from http import HTTPStatus
from middleware import responseHandler
from flask import request
from app_name import app
from api_doc import swagger


babel = Babel(app)
# # Define supported languages
LANGUAGES = ['en', 'es', 'fr']
def get_locale():
    return request.accept_languages.best_match(LANGUAGES)

# pybabel compile -d translations
# Initialize Babel with the locale selector function
babel = Babel(app, locale_selector=get_locale)


# Create a Blueprint object
# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(user_bp)


# Initialize Flask-Migrate
migrate = Migrate(app, db)

login_manager = LoginManager(app)


@login_manager.unauthorized_handler
def unauthorized():
    return responseHandler.response_handler("SESSION_EXPIRED",HTTPStatus.UNAUTHORIZED)


@app.route('/protected')
@login_required
def protected():
    # Check if the current user is not an anonymous user
    if not isinstance(current_user, AnonymousUserMixin):
        user_id = current_user.id
        # Proceed with accessing user-specific data
        return responseHandler.response_handler("User ID", HTTPStatus.OK, user_id)
    else:
        return responseHandler.response_handler("SESSION_EXPIRED",HTTPStatus.SERVICE_UNAVAILABLE)
    

@login_manager.user_loader
def load_user(user_id):
    # return Members_Info.query.get(int(user_id))
    return db.session.get(Members_Info, int(user_id))

swagger.setup_swagger_ui(app)


if __name__ == '__main__':
     
    app.run(debug=True, host='192.168.1.119')
