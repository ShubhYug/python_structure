from config.config import  db
from database.models.models import Members_Info
from modules.v1.auth.validator.forms import RegistrationForm
from flask import request, jsonify, session, render_template, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from constants.folderConstants import STATIC_FILE_PATHS
from flask_wtf.csrf import generate_csrf
from middleware import responseHandler
from http import HTTPStatus
from sqlalchemy.exc import IntegrityError
from flask_babel import _
import random
from libraries.email import send_email


# @app.route('/login', methods=['POST'])
def login():
    try:
        data = request.form  # Assuming JSON data is sent in the request body
        email_or_contact = data.get('email_or_contact')
        password = data.get('password') 
        if not email_or_contact and not password:
            return responseHandler.response_handler("PLEASE_FEEL_ALL", HTTPStatus.BAD_REQUEST)
        # if not email_or_contact or not password:
        elif not email_or_contact:
            return responseHandler.response_handler("EMAIL_CONTACT_REQ", HTTPStatus.BAD_REQUEST)
        elif not password:
                return responseHandler.response_handler("PASS_REQUIRED", HTTPStatus.BAD_REQUEST)

        user = Members_Info.query.filter((Members_Info.email == email_or_contact) | (Members_Info.contact == email_or_contact)).first()
        if user:
            if check_password_hash(user.password_hash, password):
                # Authentication successful
                user.authenticated = True
                db.session.add(user)
                db.session.commit()
                login_user(user, remember=True) 

                csrf_token = generate_csrf()
                session['csrf_token'] = csrf_token
                data = user.id
                return responseHandler.response_handler("LOGIN_SUCCESS", HTTPStatus.OK, data)
            else:
                return responseHandler.response_handler("INVALID_PASS", HTTPStatus.UNAUTHORIZED)
        else:
            return responseHandler.response_handler("INVALID_USER_EMAIL_CONTACT", HTTPStatus.NOT_FOUND)
    except Exception as e:
        return responseHandler.response_handler(str(e), HTTPStatus.INTERNAL_SERVER_ERROR)


# @app.route('/logout')
@login_required
def logout():
    try:
        logout_user()  # Log the user out
        data = {}
        # return responseHandler.response_handler(_('Logout successfully'), HTTPStatus.OK, data)
        return responseHandler.response_handler('LOGOUT_SUCCESS', HTTPStatus.OK, data)
    except Exception as e:
        return responseHandler.response_handler(str(e), HTTPStatus.INTERNAL_SERVER_ERROR)
    
    
# @app.route('/register', methods=['POST'])
def register():

    try:
        form = RegistrationForm()

        if form.validate():
            # Check if email or contact already exists
            condition = (Members_Info.email == form.email.data) | (Members_Info.contact == form.contact.data)
            existing_user = Members_Info.query.filter(condition).first()

            if existing_user:
                return responseHandler.response_handler('EMAIL_CONTACT_EXIST', HTTPStatus.BAD_REQUEST)

            file = request.files['profile']
            file.save(STATIC_FILE_PATHS['STATIC'] + file.filename)
            file_name = file.filename

            # Generate password hash
            password_hash = generate_password_hash(form.password.data)

            new_user = Members_Info(
                firstname=form.firstname.data,
                lastname=form.lastname.data,
                email=form.email.data,
                contact=form.contact.data,
                dob=form.dob.data,
                gender=form.gender.data,
                height=form.height.data,
                weight=form.weight.data,
                country=form.country.data,
                state=form.state.data,
                city=form.city.data,
                pincode=form.pincode.data,
                profile=file_name,
                group=form.group.data,
                password_hash=password_hash,  # Set the password hash
            )

            db.session.add(new_user)
            db.session.commit()
            csrf_token = generate_csrf()
            return responseHandler.response_handler("USER_ADDED", HTTPStatus.OK, {'csrf_token': csrf_token})
        else:
            # Handle form validation errors or missing values
            errors = {}
            for field, messages in form.errors.items():
                translated_messages = [_(msg) for msg in messages]
                errors[field] = ', '.join(translated_messages)
            return jsonify({'error': errors}), HTTPStatus.BAD_REQUEST
            # return responseHandler.response_handler("VALIDATION_FAILED", HTTPStatus.BAD_REQUEST)
    
    except IntegrityError as e:
        
        return responseHandler.response_handler(e, HTTPStatus.INTERNAL_SERVER_ERROR)


# Generate 4-digit PIN
def generate_pin():
    return str(random.randint(1000, 9999))


# @app.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    if request.method == 'POST':
        email = request.form['email']
        # Check if email is valid and exists in the database
        user = Members_Info.query.filter_by(email=email).first()
        if user:
            # If email is valid, generate a PIN and send it via email
            pin = generate_pin()
            subject = 'TTS- Reset Password'
            toEmail = email

            image_url = url_for('static', filename='media/download.png', _external=True)    
            html_template = render_template('email/resetPassword.html', image_url = image_url, pin = pin)
            return send_email(toEmail, subject, html_template)
        return 'Email not registered.'
    return 'forgot_password error'


# @app.route('/verify_pin', methods=['GET', 'POST'])
def verify_pin():
    if request.method == 'POST':
        pin = request.form['pin']
        # Verify the PIN
        # Proceed with password reset if PIN is valid
        return 'PIN verified. You can now reset your password.'
    return render_template('verify_pin.html')