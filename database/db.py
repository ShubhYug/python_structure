# from .config import app

from flask_sqlalchemy import SQLAlchemy
from app_name import app

# Create an instance of SQLAlchemy
db = SQLAlchemy(app)

# Run this file manually using CMD
# python db.py
with app.app_context():
    db.create_all()
