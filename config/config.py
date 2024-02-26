# from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from app_name import app
from dotenv import load_dotenv
import os
from constants.folderConstants import STATIC_FILE_PATHS
from constants.commonConstants import URL

load_dotenv()
  
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

app.config['WTF_CSRF_ENABLED'] = False  # Disable CSRF for API
# app.config['WTF_CSRF_ENABLED'] = os.getenv('WTF_CSRF_ENABLED')  # Disable CSRF for API
app.config['BABEL_DEFAULT_LOCALE'] = URL['BABEL_DEFAULT_LOCALE']  # Set default language
# app.static_folder =  STATIC_FILE_PATHS['MEDIA']
app.config['UPLOAD_FOLDER'] = STATIC_FILE_PATHS['UPLOAD_FOLDER']

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
