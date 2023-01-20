from datetime import datetime
from cafe_app.extensions import db


class Table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    table_number = db.Column(db.Integer, unique=True)
    position = db.Column(db.String(80))
    table_spacing = db.Column(db.Integer)
    reserved = db.relationship("Reserved", backref=db.backref("table"))

    def __init__(self, table_number: int, position: str, table_spacing: int):
        self.table_number = table_number
        self.position = position
        self.table_spacing = table_spacing

    def __repr__(self):
        return f'{self.__class__.__name__}({self.id}, {self.table_spacing}-Seater)'


class Reserved(db.Model):
    Reserved_Time_Default = datetime.now()

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=Reserved_Time_Default)
    time = db.Column(db.Time)
    table_id = db.Column(db.Integer, db.ForeignKey("table.id"))
    
    def __init__(self, table_id, date=Reserved_Time_Default, time=None):
        self.date = date
        self.time = time
        self.table_id = table_id
