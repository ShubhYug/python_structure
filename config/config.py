from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_babel import Babel
from app_name import app


# app = Flask(__name__, template_folder='templates')
user = "root"
pin = ""
host = '127.0.0.1'
db_name = "running_app"


app.config['STATIC_FOLDER'] = 'static'
app.config['STATIC_URL_PATH'] = '/static'
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{user}:{pin}@{host}/{db_name}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['WTF_CSRF_ENABLED'] = False  # Disable CSRF for API

# Change localization language heare  -- ['en', 'fr', 'es']
app.config['BABEL_DEFAULT_LOCALE'] = 'en'  # Set default language

# Serve the 'media' directory at the '/public/media' URL prefix
app.static_folder =  './media'
UPLOAD_FOLDER = './static/media'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)