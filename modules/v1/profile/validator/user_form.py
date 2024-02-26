from flask_wtf import FlaskForm
import wtforms as wtf
from flask_wtf.file import FileAllowed, FileRequired
from wtforms.validators import ValidationError, DataRequired, EqualTo, Length, Regexp

def validate_file_size(form, field):
    max_size = 10 * 1024 * 1024  # 10 MB
    if field.data and len(field.data.read()) > max_size:
        raise ValidationError('File size must be less than 10 MB.')


# Custom validator for file size
def validate_file_size(form, field):
    max_size = 10 * 1024 * 1024  # 10 MB
    if field.data and len(field.data.read()) > max_size:
        raise ValidationError('File size must be less than 10 MB.')

class UpdateProfileForm(FlaskForm):
    firstname = wtf.StringField('First Name', validators=[DataRequired(message='PLS_ENTER_FNAME'), Length(min=2, max=100, message='FNAME_MIM_2CHAR')])
    lastname = wtf.StringField('Last Name', validators=[DataRequired(message='PLS_ENTER_LNAME'), Length(min=2, max=100, message='LNAME_MIM_2CHAR')])
    dob = wtf.DateField('Date of Birth', validators=[DataRequired(message='PLEASE_ENTER_DOB')], format='%Y-%m-%d')
    gender = wtf.StringField('Gender', validators=[DataRequired(message='SELECT_GENTER')])
    height = wtf.StringField('Height', validators=[Regexp('^\d+$', message='DIGITS_ONLY') , DataRequired(message='ENTER_HEIGHT'),Length(min=2, max=3, message='HEIGHT_IN_DIGITS')])
    weight = wtf.StringField('Weight', validators=[DataRequired(message='ENTER_WEIGHT') , Regexp('^\d+$', message='DIGITS_ONLY'),Length(min=2, max=3, message='WEIGHT_IN_DIGITS')])
    country = wtf.StringField('Country', validators=[DataRequired(message='ENTRY_COUNTRY'), Length(max=50, message='ENTRY_COUNTRY') , Regexp('^[A-Za-z]+$', message='CONTAIN_CHAR')])
    state = wtf.StringField('State', validators=[DataRequired(message='ENTRY_STATE'), Length(max=50, message='STATE_MAX50') , Regexp('^[A-Za-z]+$', message='CONTAIN_CHAR')])
    city = wtf.StringField('City', validators=[DataRequired(message='ENTRY_CITY'), Length(max=50, message='CITY_MAX50') , Regexp('^[A-Za-z]+$', message='CONTAIN_CHAR')])
    pincode = wtf.StringField('Pincode', validators=[DataRequired(message='ENTRY_PINCODE'), Length(max=15, message='PINCODE_MAX15')])
    
    # Profile Information
    profile = wtf.FileField('Profile', validators=[
        FileAllowed(['jpg', 'jpeg', 'png', 'gif'], message='IMAGE_FORMATE'),
        validate_file_size,  # Custom validator for file size
    ])
    group = wtf.StringField('Group', validators=[DataRequired()])




