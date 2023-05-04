import RPi.GPIO as GPIO
import time

# GPIO Pins für Motorsteuerung
IN1 = 7
IN2 = 13
IN3 = 15
IN4 = 18

# Initialisiere GPIO Pins
GPIO.setmode(GPIO.BOARD)

# Festlegen der GPIO-Pins zu den L293D Input-Pins als Ausgang
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

try:
    while True:
        GPIO.output(IN1, GPIO.HIGH)
        GPIO.output(IN2, GPIO.LOW)
        GPIO.output(IN3, GPIO.HIGH)
        GPIO.output(IN4, GPIO.LOW)

except KeyboardInterrupt:
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    
    GPIO.cleanup()