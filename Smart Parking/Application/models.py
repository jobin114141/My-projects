from email.policy import default
from flask_login import UserMixin
from sqlalchemy.sql import func
from . import db



class admin(db.Model,UserMixin):
     id=db.Column(db.Integer,primary_key=True)
     password=db.Column(db.String(100))
     username=db.Column(db.Integer)

class priceChart(db.Model,UserMixin):
     id=db.Column(db.Integer,primary_key=True)
     time=db.Column(db.String(5))
     price=db.Column(db.String(5))


class slot(db.Model,UserMixin):
    slot_id=db.Column(db.Integer,primary_key=True)
    carNumber=db.Column(db.String(10),db.ForeignKey('car.carNumber'))
    Status=db.column(db.Integer)

class car(db.Model,UserMixin):
    carNumber=db.Column(db.String,primary_key=True)
    Ph=db.Column(db.String)




class payment(db.Model,UserMixin):
    Tid=db.Column(db.Integer,primary_key=True)
    carNumber=db.Column(db.String(10),db.ForeignKey('car.carNumber'))
    time=db.Column(db.String(5))
    payed=db.Column(db.String(5))
    pcancellation=db.Column(db.String(5))

