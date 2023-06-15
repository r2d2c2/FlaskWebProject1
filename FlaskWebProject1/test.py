import formatter
from gpiozero import LED
from datetime import datetime
from flask import render_template,request
from numpy import append
led = LED(14)
beep=LED(15)
fan= LED(18)


@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")

def led_on():
    led.on()
    return "ok"

def beep_on():
    beep.on()
    return "ok"

def fan_on():
    print("@@@@@@@@@@@@@@@@@@@@@@@@ fan   test")
    fan.on()
    return "ok"


def contact():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Do Something':
            print("ok")
            pass # do something
        elif request.form['submit_button'] == 'Do Something Else':
            print("not ok")
            pass # do something else
        else:
            pass # unknown
    elif request.method == 'GET':
        return render_template('index.html', form=formatter)