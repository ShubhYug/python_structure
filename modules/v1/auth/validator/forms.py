from flask_wtf import FlaskForm
import wtforms as wtf
# from wtforms import ValidationError
from flask_wtf.file import FileAllowed, FileRequired
from wtforms import StringField, PasswordField, validators
from wtforms.validators import ValidationError, DataRequired, EqualTo, Length

def validate_file_size(form, field):
    max_size = 10 * 1024 * 1024  # 10 MB
    if field.data and len(field.data.read()) > max_size:
        raise ValidationError('File size must be less than 10 MB.')



# class RegistrationForm(FlaskForm):
#     # Personal Information
#     # firstname = StringField('First Name', validators=[DataRequired(message="Please enter your first name."), Length(min=2, max=100, message="First name must be at least 2 characters long.")])

#     firstname = wtf.StringField('First Name', validators=[wtf.validators.DataRequired(message='PLS_ENTER_FNAME'), wtf.validators.Length(min=2,max=100,message='FNAME_MIM_2CHAR')])
#     lastname = wtf.StringField('Last Name', validators=[wtf.validators.DataRequired(message='PLS_ENTER_LNAME'), wtf.validators.Length(min=2,max=100, message='LNAME_MIM_2CHAR')])
#     email = wtf.StringField('Email', [wtf.validators.Email(message='EMAIL_INVALID')])
#     contact = wtf.StringField('Contact', [wtf.validators.Length(min=7, max=15, message='CONTECT_MIM7_MAX15')])
#     dob = wtf.DateField('Date of Birth', validators=[wtf.validators.DataRequired(message='PLEASE_ENTER_DOB')], format='%Y-%m-%d')
#     gender = wtf.SelectField('Gender', choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], validators=[wtf.validators.DataRequired(message='SELECT_GENTER')])

#     # Physical Information
#     # height = wtf.FloatField('Height', validators=[DataRequired(message="ENTER_HEIGHT"),Length(min=1, max=3, message="HEIGHT_IN_DIGITS"),])

#     # weight = wtf.FloatField('Weight', validators=[DataRequired(message="ENTER_WEIGHT"),Length(min=1, max=3, message="WEIGHT_IN_DIGITS"),])

#     height = wtf.FloatField('Height', validators=[DataRequired(message="ENTER_HEIGHT")])

#     weight = wtf.FloatField('Weight', validators=[DataRequired(message="ENTER_WEIGHT")])

#     # Other fields...



#     # Address Information
#     country = wtf.StringField('Country', validators=[wtf.validators.DataRequired(message='ENTRY_COUNTRY'), wtf.validators.Length(max=50,message='ENTRY_COUNTRY')])
#     state = wtf.StringField('State', validators=[wtf.validators.DataRequired(message='ENTRY_STATE'), wtf.validators.Length(max=50, message='STATE_MAX50')])
#     city = wtf.StringField('City', validators=[wtf.validators.DataRequired(message='ENTRY_CITY'), wtf.validators.Length(max=50, message='CITY_MAX50')])
#     pincode = wtf.StringField('Pincode', validators=[wtf.validators.DataRequired(message='ENTRY_PINCODE'), wtf.validators.Length(max=15, message='PINCODE_MAX15')])

#     # Profile Information
#     # profile = wtf.FileField('Profile', validators=[
#     #     FileAllowed(['jpg', 'jpeg', 'png', 'gif'], message='IMAGE_FORMATE'),
#     #     DataRequired(message="UPLOAD_IMAGE"),
#     #     validate_file_size  # Custom validator for file size
#     # ])

#     # New Group Information
#     group = wtf.StringField('Group', validators=[wtf.validators.DataRequired()])

#     password = PasswordField('Password', validators=[
#         validators.DataRequired(message='ENTRY_PASS'),
#         validators.Length(min=8, message='PASSWORD_MIM8'),
#         validators.Regexp(
#             regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]+$",
#             message="RGX_PASSWORD_ERROR"
#         )
#     ])

#     confirm_password = PasswordField('Confirm Password', validators=[
#         DataRequired(message="ENTRY_CON_PASS"),
#         EqualTo('password', message="PASS_MATCH")
#     ])


# class LoginForm(FlaskForm):
#     email_or_contact = StringField('Email/Contact', validators=[DataRequired()])
#     password = PasswordField('Password', validators=[DataRequired()])



# Custom validator for file size
def validate_file_size(form, field):
    max_size = 10 * 1024 * 1024  # 10 MB
    if field.data and len(field.data.read()) > max_size:
        raise ValidationError('File size must be less than 10 MB.')

class RegistrationForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired(message='PLS_ENTER_FNAME'), Length(min=2, max=100, message='FNAME_MIM_2CHAR')])
    lastname = StringField('Last Name', validators=[DataRequired(message='PLS_ENTER_LNAME'), Length(min=2, max=100, message='LNAME_MIM_2CHAR')])
    email = StringField('Email', [validators.Email(message='EMAIL_INVALID')])
    contact = StringField('Contact', [Length(min=7, max=15, message='CONTECT_MIM7_MAX15')])
    dob = wtf.DateField('Date of Birth', validators=[DataRequired(message='PLEASE_ENTER_DOB')], format='%Y-%m-%d')
    gender = StringField('Gender', validators=[DataRequired(message='SELECT_GENTER')])
    height = wtf.FloatField('Height', validators=[DataRequired(message='ENTER_HEIGHT')])
    weight = wtf.FloatField('Weight', validators=[DataRequired(message='ENTER_WEIGHT')])
    country = StringField('Country', validators=[DataRequired(message='ENTRY_COUNTRY'), Length(max=50, message='ENTRY_COUNTRY')])
    state = StringField('State', validators=[DataRequired(message='ENTRY_STATE'), Length(max=50, message='STATE_MAX50')])
    city = StringField('City', validators=[DataRequired(message='ENTRY_CITY'), Length(max=50, message='CITY_MAX50')])
    pincode = StringField('Pincode', validators=[DataRequired(message='ENTRY_PINCODE'), Length(max=15, message='PINCODE_MAX15')])
    # Profile Information
    profile = wtf.FileField('Profile', validators=[
        FileAllowed(['jpg', 'jpeg', 'png', 'gif'], message='IMAGE_FORMATE'),
        DataRequired(message="UPLOAD_IMAGE"),
        validate_file_size,  # Custom validator for file size
    ])
    group = StringField('Group', validators=[DataRequired()])
    password = PasswordField('Password', validators=[
        DataRequired(message='ENTRY_PASS'),
        Length(min=8, message='PASSWORD_MIM8'),
        validators.Regexp(
            regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]+$",
            message="RGX_PASSWORD_ERROR"
        )
    ])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(message="ENTRY_CON_PASS"),
        EqualTo('password', message="PASS_MATCH")
    ])
