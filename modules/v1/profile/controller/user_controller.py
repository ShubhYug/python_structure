from config.config import  db
from database.models.models import Members_Info
from flask import request, url_for, jsonify
from flask_babel import _
from flask_login import current_user, login_required
from middleware import  responseHandler
from http import HTTPStatus
from modules.v1.profile.validator.user_form import UpdateProfileForm
from constants.folderConstants import STATIC_FILE_PATHS

@login_required
def update_profile():
    try:
        print('inside')
        form = UpdateProfileForm()
        print('UpdateProfileForm : ',form)
        if form.validate():
            print('inside validate')
            print('user',current_user)
            data = form.data
            user_id = current_user.id
            user = db.session.get(Members_Info, user_id)

            if user:
                user.firstname = data.get('firstname', user.firstname)
                user.lastname = data.get('lastname', user.lastname)
                user.dob = data.get('dob', user.dob)
                user.gender = data.get('gender', user.gender)
                user.height = data.get('height', user.height)
                user.weight = data.get('weight', user.weight)
                user.country = data.get('country', user.country)
                user.state = data.get('state', user.state)
                user.city = data.get('city', user.city)
                user.pincode = data.get('pincode', user.pincode)
                user.group = data.get('group', user.group)

                file = request.files['profile']
                file.save(STATIC_FILE_PATHS['STATIC'] + file.filename)
                user.profile = file.filename

                db.session.commit()
                return responseHandler.response_handler("UPDATE_PROFILE", HTTPStatus.OK)
            else:
                return responseHandler.response_handler("USER_NOT_FOUND", HTTPStatus.NOT_FOUND)
        else:
            # Handle form validation errors or missing values
            errors = {}
            for field, messages in form.errors.items():
                translated_messages = [_(msg) for msg in messages]
                errors[field] = ', '.join(translated_messages)
            return jsonify({'error': errors}), HTTPStatus.BAD_REQUEST
            # return responseHandler.response_handler(errors, HTTPStatus.NOT_FOUND)
    except Exception as e:
        db.session.rollback()
        return responseHandler.response_handler(str(e), HTTPStatus.INTERNAL_SERVER_ERROR)


# @app.route('/userinfo', methods=['GET'])
@login_required
def userinfo():
    try:
        user_info = {
            'id': current_user.id,
            'Firstname': current_user.firstname,
            'Lastname': current_user.lastname,
            'Email': current_user.email,
            'Countact':current_user.contact,
            'Date Of Birth' : current_user.dob,
            'Country' : current_user.country,
            'Profile' : current_user.profile,
            'State' : current_user.state,
            'City' : current_user.city,
        }

        # Get the URL or path to the profile picture
        if current_user.profile:
            profile_url = url_for('static', filename=f'media/{current_user.profile}', _external=True)
            user_info['Profile'] = profile_url
        else:
            user_info['Profile'] = None
            
        return responseHandler.response_handler("USER_ADDED", HTTPStatus.OK, user_info)
    except Exception as e:

        return responseHandler.response_handler(str(e), HTTPStatus.INTERNAL_SERVER_ERROR)


# @app.route('/delete_user/<int:user_id>', methods=['DELETE'])
# def delete_user(user_id):
# @app.route('/delete_user', methods=['DELETE'])
@login_required
def delete_user():

    if current_user.is_authenticated:
        user_id = current_user.id
        try:
            user = Members_Info.query.get(user_id)
            if user:
                db.session.delete(user)
                db.session.commit()
                return responseHandler.response_handler("USER_DELETE",HTTPStatus.OK)
            else:
                return responseHandler.response_handler("USER_NOT_FOUND", HTTPStatus.NOT_FOUND)
        except Exception as e:
            return responseHandler.response_handler(str(e), HTTPStatus.INTERNAL_SERVER_ERROR)
    else:
        return responseHandler.response_handler("SESSION_EXPIRED",HTTPStatus.SERVICE_UNAVAILABLE)
