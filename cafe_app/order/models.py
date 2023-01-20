from datetime import datetime
from cafe_app.extensions import db
from sqlalchemy.orm import validates
from cafe_app.core.exceptions import DateValidationError, StateValidationError, OrderTypeValidationError, \
    IntegerValidationError, FloatValidationError, JSONValidationError
from cafe_app.core.validation import is_date_valid, is_state_valid, is_order_type_valid, is_int_valid, is_float_valid, \
    is_json_valid


class Order(db.Model):
    Order_Time_Default = datetime.now()

    id = db.Column(db.Integer, primary_key=True)
    order_time = db.Column(db.DateTime, nullable=False, default=Order_Time_Default)
    delivery_address = db.Column(db.Text, nullable=True)
    comment = db.Column(db.Text, nullable=True)
    state = db.Column(db.String, nullable=False)
    reserved_id = db.Column(db.Integer, db.ForeignKey("reserved.id"), nullable=True)
    receipt_id = db.Column(db.Integer, db.ForeignKey("receipt.id"), nullable=True)
    offer_id = db.Column(db.Integer, db.ForeignKey("offer.id"), nullable=True)
    order_type = db.Column(db.String(10), nullable=True)
    carts = db.relationship("Cart", backref=db.backref("order"))

    def __init__(self, delivery_address, comment, state, reserved_id, receipt_id, offer_id,
                 order_type, order_time=Order_Time_Default):
        self.order_time = order_time
        self.delivery_address = delivery_address
        self.comment = comment
        self.state = state
        self.reserved_id = reserved_id
        self.receipt_id = receipt_id
        self.offer_id = offer_id
        self.order_type = order_type

    @validates('order_time')
    def valid_order_time(self, key, date):
        if not is_date_valid(date):
            raise DateValidationError
        return date

    @validates('state')
    def valid_state(self, key, state):
        if not is_state_valid(state):
            raise StateValidationError
        return state

    @validates('order_type')
    def valid_order_type(self, key, order_type):
        if not is_order_type_valid(order_type):
            raise OrderTypeValidationError
        return order_type

    def __repr__(self):
        return f'{self.__class__.__name__}({self.order_time}, {self.state})'


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_quantity = db.Column(db.String, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey("order.id"), nullable=True)

    def __init__(self, item_quantity, customer_id, order_id=None):
        self.item_quantity = item_quantity
        self.customer_id = customer_id
        self.order_id = order_id

    @validates('item_quantity')
    def valid_item_quantity(self, key, item_quantity):
        if not is_json_valid(item_quantity):
            raise JSONValidationError
        return item_quantity

    def __repr__(self):
        return f'{self.__class__.__name__}({self.id}, {self.item_quantity} ,{self.customer_id})'


class Receipt(db.Model):
    Receipt_Time_Default = datetime.now()

    id = db.Column(db.Integer, primary_key=True)
    total_price = db.Column(db.Float, nullable=False)
    final_price = db.Column(db.Float, nullable=False)
    discount = db.Column(db.Integer, nullable=True)
    state = db.Column(db.String, nullable=True)
    receipt_time = db.Column(db.DateTime, nullable=False, default=Receipt_Time_Default)
    order = db.relationship("Order", backref=db.backref("receipt"))

    def __init__(self, total_price, discount, final_price, receipt_time=Receipt_Time_Default, state='Paid'):
        self.state = state
        self.total_price = total_price
        self.final_price = final_price
        self.receipt_time = receipt_time
        if self.total_price != self.final_price:
            self.discount = int(self.total_price) - int(self.final_price)
        else:
            self.discount = discount

    @validates('receipt_time')
    def valid_receipt_time(self, key, date):
        if not is_date_valid(date):
            raise DateValidationError
        return date

    @validates('total_price')
    def valid_total_price(self, key, price):
        if not is_float_valid(price):
            raise FloatValidationError
        return price

    @validates('final_price')
    def valid_final_price(self, key, price):
        if not is_float_valid(price):
            raise FloatValidationError
        return price

    @validates('discount')
    def valid_discount(self, key, discount):
        if not is_int_valid(discount):
            raise IntegerValidationError
        return discount
