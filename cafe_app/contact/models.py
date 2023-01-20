from cafe_app.extensions import db
from cafe_app.core.validation import *
from sqlalchemy.orm import validates
from cafe_app.core.exceptions import NameValidationError, EmailValidationError, PhoneValidationError


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    phone = db.Column(db.Integer)
    message = db.Column(db.Text)

    def __init__(self, first_name, last_name, email, phone, message):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.message = message

    @validates('first_name')
    def valid_first_name(self, key, name):
        if not is_name_valid(name):
            raise NameValidationError
        return name

    @validates('last_name')
    def valid_last_name(self, key, name):
        if not is_name_valid(name):
            raise NameValidationError
        return name

    @validates('email')
    def valid_email(self, key, email):
        if not is_email_valid(email):
            raise EmailValidationError
        return email

    @validates('phone')
    def valid_phone(self, key, phone):
        if not is_phone_valid(phone):
            raise PhoneValidationError
        return phone

    def __repr__(self):
        return f'{self.__class__.__name__}({self.first_name} {self.last_name},{self.email}, {self.phone})'
