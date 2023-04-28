from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(150))
    Full_Name = db.Column(db.String(150))
    phone_number = db.Column(db.Integer)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    manage_re = db.relationship('Manage')

class Manage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    incoming_stock = db.Column(db.Integer)
    outgoing_stock = db.Column(db.Integer)
    total_stock = db.Column(db.Integer)
    #date = db.Column(db.DateTime(timezone=True), default=func.now())
    date = db.Column(db.Date, default=func.date(func.now()))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))





