from wtforms import StringField, EmailField, TextAreaField
from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm


class ContactForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired("This first_name field is required."),
                                                       Length(3, 50,
                                                              'Firstname must be between 3 and 50 characters long.')])
    last_name = StringField('Last Name', validators=[DataRequired("This last_name field is required."),
                                                     Length(3, 50,
                                                            'Lastname must be between 3 and 50 characters long.')])
    email = EmailField('Email', validators=[DataRequired("This email field is required.")])
    phone = StringField('Phone', validators=[DataRequired("This Phone field is required."),
                                             Length(11, 11, 'Your Phone Number should be 11 characters.')])
    message = TextAreaField("Message", validators=[DataRequired("This Message field is required.")])
    # agree_chaptcha = BooleanField('Captcha', validators=[DataRequired("please send capthcer button.")])
