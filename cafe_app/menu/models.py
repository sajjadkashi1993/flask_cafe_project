from cafe_app.extensions import db
from sqlalchemy.orm import validates
from cafe_app.core.validation import is_int_valid, is_bool_valid
from cafe_app.core.exceptions import IntegerValidationError, BoolValidationError


class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text)
    picture_path = db.Column(db.Text, nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=True)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"))

    def __init__(self, name, price, description, category_id, picture_path, status=True):
        self.name = name
        self.price = price
        self.description = description
        self.category_id = category_id
        self.picture_path = picture_path
        self.status = status

    @validates('price')
    def valid_price(self, key, price):
        if not is_int_valid(price):
            raise IntegerValidationError
        return price

    @validates('status')
    def valid_status(self, key, status):
        if not is_bool_valid(status):
            raise BoolValidationError
        return status

    def __repr__(self):
        return f'{self.__class__.__name__}({self.id},{self.name},{self.price})'


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.Text, nullable=False)
    items = db.relationship("Menu", backref=db.backref("category"))

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return f'{self.__class__.__name__}({self.id},{self.name})'
