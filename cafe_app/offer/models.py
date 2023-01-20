from cafe_app.extensions import db
from sqlalchemy.orm import validates
from datetime import datetime, timedelta
from cafe_app.core.exceptions import IntegerValidationError, DateValidationError
from cafe_app.core.validation import is_int_valid, is_date_valid


class Offer(db.Model):
    Date_Default = datetime.today() + timedelta(days=30)
    Ex_Count_Default = 1
    Min_Price_Default = 0

    id = db.Column(db.Integer, primary_key=True)
    min_price = db.Column(db.Integer, nullable=False, default=Min_Price_Default)
    max_price = db.Column(db.Integer, nullable=False)
    percent = db.Column(db.Integer, nullable=False)
    offer_code = db.Column(db.String(20), nullable=False, unique=True)
    expire_time = db.Column(db.TIMESTAMP, nullable=False, default=Date_Default)
    expire_count = db.Column(db.Integer, nullable=False, default=Ex_Count_Default)
    orders = db.relationship("Order", backref=db.backref("offer"))

    def __init__(self, max_price, percent, offer_code, min_price=Min_Price_Default, expire_time=Date_Default,
                 expire_count=Ex_Count_Default):
        self.min_price = min_price
        self.max_price = max_price
        self.percent = percent
        self.offer_code = offer_code
        self.expire_time = expire_time
        self.expire_count = expire_count

    @validates('min_price')
    def valid_min_price(self, key, min_price):
        if not is_int_valid(min_price):
            raise IntegerValidationError
        return min_price

    @validates('max_price')
    def valid_max_price(self, key, max_price):
        if not is_int_valid(max_price):
            raise IntegerValidationError
        return max_price

    @validates('percent')
    def valid_percent(self, key, percent):
        if not is_int_valid(percent):
            raise IntegerValidationError
        return percent

    @validates('expire_time')
    def valid_expire_time(self, key, expire_time):
        if not is_date_valid(expire_time):
            raise DateValidationError
        return expire_time

    @validates('expire_count')
    def valid_expire_count(self, key, expire_count):
        if not is_int_valid(expire_count):
            raise IntegerValidationError
        return expire_count

    def __repr__(self):
        return f'{self.__class__.__name__}({self.offer_code}, {self.max_price}, {self.expire_time})'
