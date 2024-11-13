import RPi.GPIO as GPIO
import time

# Pin definitions
IN1 = 17  # GPIO pin connected to IN1
IN2 = 18  # GPIO pin connected to IN2
ENA = 13  # GPIO pin connected to ENA (use a PWM-capable pin)

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)

# Set up PWM on the ENA pin
pwm = GPIO.PWM(ENA, 1000)  # 1kHz frequency
pwm.start(100)  # Start at 100% duty cycle for full speed

def motor_forward():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    print("Motor should be running forward")

def motor_backward():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    print("Motor should be running backward")

def motor_stop():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    print("Motor should be stopped")

try:
    motor_forward()
    time.sleep(2)
    
    motor_backward()
    time.sleep(2)

    motor_stop()

except KeyboardInterrupt:
    print("Test interrupted by user")

finally:
    pwm.stop()
    GPIO.cleanup()
