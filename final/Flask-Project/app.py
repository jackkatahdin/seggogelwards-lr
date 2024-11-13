from flask import Flask, render_template
import RPi.GPIO as GPIO
from gpiozero import Motor

app = Flask(__name__)

motorFR = Motor(forward=14, backward=15, enable=13)
motorFL = Motor(forward=17, backward=27, enable=12)
motorBR = Motor(forward=24, backward=25, enable=18)
motorBL = Motor(forward=7, backward=8, enable=19)

@app.route("/forward_turn", methods=["POST"])
def forward_turn():
    
    motorFR.forward()
    motorFL.forward()
    motorBR.forward()
    motorBL.forward()
    return "ok"

@app.route("/stop", methods=["POST"])
def stop():
    
    motorFR.stop()
    motorFL.stop()
    motorBR.stop()
    motorBL.stop()
    return "ok"


@app.route("/backward_turn", methods=["POST"])
def backward_turn():
    
    motorFR.backward()
    motorFL.backward()
    motorBR.backward()
    motorBL.backward()
    return "ok"

@app.route("/", methods=["GET"])
def home():
    return render_template("button.html", title="Button", name="Brendan Vogel")
