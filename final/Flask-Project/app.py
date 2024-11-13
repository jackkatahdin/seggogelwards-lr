from flask import Flask, render_template
import RPi.GPIO as GPIO
from gpiozero import Motor

app = Flask(__name__)

motorFR = Motor(14, 15, 13)
motorFL = Motor(17, 27, 12)
motorBR = Motor(24, 25, 18)
motorBL = Motor(7, 8, 19)

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
