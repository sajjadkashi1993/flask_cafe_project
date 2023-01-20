from hashlib import sha256
from cafe_app.extensions import db, login_manager
from flask_login import UserMixin
from cafe_app.core.exceptions import NameValidationError, EmailValidationError, PhoneValidationError, \
    NormalPasswordError, CharacterValidationError
from cafe_app.core.validation import *
from sqlalchemy.orm import validates


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    # __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(80))
    l_name = db.Column(db.String(80))
    address = db.Column(db.String(250), nullable=True)
    phone_number = db.Column(db.String(10), nullable=True)
    email = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(250))
    character = db.Column(db.String(80))
    carts = db.relationship("Cart", backref=db.backref("customer"))

    def __init__(self, f_name, l_name, email, password, address=None, phone_number=None, character="user"):
        self.phone_number = phone_number
        self.email = email
        self.password = sha256(password.encode()).hexdigest()
        self.address = address
        self.f_name = f_name
        self.l_name = l_name
        self.character = character

    @validates('f_name')
    def valid_f_name(self, key, name):
        if not is_name_valid(name):
            raise NameValidationError
        return name

    @validates('l_name')
    def valid_l_name(self, key, name):
        if not is_name_valid(name):
            raise NameValidationError
        return name

    @validates('email')
    def valid_email(self, key, email):
        if not is_email_valid(email):
            raise EmailValidationError
        return email

    @validates('password')
    def valid_password(self, key, password):
        if not is_normal_pas(password):
            raise NormalPasswordError
        return password

    #
    @validates('character')
    def valid_character(self, key, character):
        if not is_character_valid(character):
            raise CharacterValidationError
        return character

    @validates('phone_number')
    def valid_phone_number(self, key, phone_number):

        if phone_number and not is_phone_valid(phone_number):
            raise PhoneValidationError
        return phone_number

    def __repr__(self):
        return f'{self.__class__.__name__}({self.f_name} {self.l_name},{self.email}, {self.phone_number})'
