from wtforms import StringField, IntegerField, EmailField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Regexp, EqualTo, ValidationError
from flask_wtf import FlaskForm
from cafe_app.user.models import User
from flask_login import current_user
from cafe_app.core.validation import is_phone_valid, is_name_valid


class RegistrationForm(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired(),
                                                  Length(3, 50, 'Firstname must be between 3 and 50 characters long.')])
    lname = StringField('Last Name', validators=[DataRequired(),
                                                 Length(3, 50, 'Lastname must be between 3 and 50 characters long.')])
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     EqualTo('re_password',
                                                             'password must be equal to Repeat Password.')])
    re_password = PasswordField('Repeat Password', validators=[DataRequired()])
    agree_term = BooleanField(validators=[DataRequired()])

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Tish email already exists')

    def validate_fname(self, fname):
        if data := fname.data:
            if not is_name_valid(data):
                raise ValidationError("The First Name is not valid")

    def validate_lname(self, lname):
        if data := lname.data:
            if not is_name_valid(data):
                raise ValidationError("The Last Name is not valid")


class LogInForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')


class UpDate(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(),
                                            Regexp('^[\w\.\_]+\@([\w\.\_]+)\.[\w]{2,4}$', 0, 'The email is not valid')])
    address = StringField('address')
    phone_number = StringField('Phone number')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Tish email already exists')

    def validate_phone_number(self, phone_number):
        if data := phone_number.data:
            if not is_phone_valid(data):
                raise ValidationError("This phone is not valid")

    def validate_fname(self, fname):
        if data := fname.data:
            if not is_name_valid(data):
                raise ValidationError("The First Name is not valid")

    def validate_lname(self, lname):
        if data := lname.data:
            if not is_name_valid(data):
                raise ValidationError("The Last Name is not valid")
