"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template,request
from FlaskWebProject1 import app

import formatter
from gpiozero import LED
from datetime import datetime
from numpy import append

isif1=True
isif2=True
isif3=True
isif4=True
isif5=True
isif6=True
isif7=True
isif8=True

led = LED(14)
beep=LED(15)
fan= LED(18)

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )
@app.route('/led/on')
def led_on():
    if(isif1):
        isif1=False
        led.on()
        print("python ok")
    else:
        isif1=True
        led.off()


@app.route('/beep/on')
def beep_on():
    if(isif2):
        isif2=False
        beep.on()
    else:
        isif2=True
        beep.off()

@app.route('/fan/on')
def fan_on():
    if(isif3):
        isif3=False
        fan.on()
    else:
        isif3=True
        fan.off()


def contact():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Do Something':
            print("ok")
            pass # do something
        elif request.form['submit_button'] == 'Do Something Else':
            print("not ok")
            pass # do something else
        else:
            print("no")
            pass # unknown
    elif request.method == 'GET':
        return render_template('index.html', form=formatter)

    
@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )


