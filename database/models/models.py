# from .config import db
from flask_login import UserMixin
from config.config import db
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


class Members_Info(db.Model, UserMixin):
    __tablename__ = "members_info"
    id = db.Column(db.Integer, primary_key=True)
    
    # Personal Information
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    contact = db.Column(db.String(20), nullable=False, unique=True)
    dob = db.Column(db.String(10), nullable=False)  # date format like 'YYYY-MM-DD'
    gender = db.Column(db.String(10), nullable=False)

    # Physical Information
    height = db.Column(db.Float)
    weight = db.Column(db.Float)

    # Address Informatio
    country = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    pincode = db.Column(db.String(20), nullable=False) 

    # Profile Information
    profile = db.Column(db.String(255), nullable=False)

    # New Group Information
    group = db.Column(db.String(50), comment="New Group Information")

    # Password Information
    password_hash = db.Column(db.String(300), nullable=False)

    # Methods for password management
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
        # Flask-Login methods
    
    def is_active(self):
        return True  # You can implement your own logic for determining if the user is active
    
    def get_id(self):
        return str(self.id) 
    
    # Flask-Login methods
    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False