from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, FloatField, FileField, DateField
from flask_wtf.file import FileAllowed
from wtforms.validators import DataRequired, Length
from flask_babel import  _


class UpdateProfileForm(FlaskForm):
    # Personal Information
    firstname = StringField('First Name', validators=[DataRequired(message='PLS_ENTER_FNAME'), Length(min=2, max=100, message='FNAME_MIM_2CHAR')])
    lastname = StringField('Last Name', validators=[DataRequired(message='PLS_ENTER_LNAME'), Length(min=2, max=100, message='LNAME_MIM_2CHAR')])
    m = _('PLEASE_ENTER_DOB')
    dob = DateField('Date of Birth', format='%Y-%m-%d', validators=[DataRequired(message=m)])
    gender = SelectField('Gender', choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], validators=[DataRequired(message='SELECT_GENTER')])

    # Physical Information
    height = FloatField('Height', validators=[
        DataRequired(message="ENTER_HEIGHT"),
        Length(min=1, max=3, message="HEIGHT_IN_DIGITS"),
    ])

    weight = FloatField('Weight', validators=[
        DataRequired(message="ENTER_WEIGHT"),
        Length(min=1, max=3, message="WEIGHT_IN_DIGITS"),
    ])

    # Address Information
    country = StringField('Country', validators=[DataRequired(message='ENTRY_COUNTRY'), Length(max=50,message='COUNTRY_MAX50')])
    state = StringField('State', validators=[DataRequired(message='ENTRY_STATE'), Length(max=50, message='STATE_MAX50')])
    city = StringField('City', validators=[DataRequired(message='ENTRY_CITY'), Length(max=50, message='CITY_MAX50')])
    pincode = StringField('Pincode', validators=[DataRequired(message='ENTRY_PINCODE'), Length(max=15,message='PINCODE_MAX15')])

    # Profile Information
    profile = FileField('Profile', validators=[
        FileAllowed(['jpg', 'jpeg', 'png', 'gif'], message='IMAGE_FORMATE'),
        DataRequired(message="UPLOAD_IMAGE.")
    ])

    # New Group Information
    group = StringField('Group', validators=[DataRequired()])
