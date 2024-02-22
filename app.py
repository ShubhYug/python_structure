from flask_babel import Babel, _
from flask import session, request
from config.config import db
from database.models.models import Members_Info
from flask_migrate import Migrate
from flask_login import LoginManager
from modules.v1.auth.routes.urls import auth_bp
from modules.v1.profile.routes.urls import user_bp
from http import HTTPStatus
from middleware import responseHandler
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



def protected_route():
    try:
        # Get CSRF token from request headers or body
        csrf_token = request.headers.get('X-CSRF-Token')  # Example: CSRF token included in headers
        # csrf_token = request.form.get('csrf_token')  # Example: CSRF token included in request body

        # Validate CSRF token
        if 'csrf_token' in session and csrf_token == session['csrf_token']:
            # CSRF token is valid
            return responseHandler.response_handler("SUCCESS", HTTPStatus.OK)
        else:
            # CSRF token is missing or invalid
            return responseHandler.response_handler("INVALID_CSRF_TOKEN", HTTPStatus.UNAUTHORIZED)
    except Exception as e:
        return responseHandler.response_handler(str(e), HTTPStatus.INTERNAL_SERVER_ERROR)



@login_manager.user_loader
def load_user(user_id):
    # return Members_Info.query.get(int(user_id))
    return db.session.get(Members_Info, int(user_id))

swagger.setup_swagger_ui(app)

if __name__ == '__main__':
     
    app.run(debug=True, host='192.168.1.119')
