from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user,login_user
from . import db
import requests
import datetime
from .models import car
views = Blueprint('views', __name__)

@views.route('/',methods=['GET','POST'])                   
def home():      
    if request.method=='POST':
        vno=request.form.get('vnumber')
        phone=request.form.get('number')
        car_obj=car(carNumber=vno,Ph=phone)       
        db.session.add(car_obj)
        db.session.commit()   
        return render_template('cards.html')                     
    return render_template('index.html')

@views.route('/price',methods=['GET','POST'])   
def price():                                #price page
    return render_template('price.html')

@views.route('/cards')                       
def card(): 
    x = requests.get('http://192.168.128.208:80/')
    sensorDict=type(eval(x.text))      
    #free slots areyan 
    return render_template('cards.html',data=sensorDict)

@views.route('/payment')
def payment():                                #payment page
    return render_template('payment.html')

@views.route('/tst')
def tst():                                #home page
    return render_template('TST.html')





