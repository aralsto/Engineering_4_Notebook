#gpio Pins - Python
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

for i in range(0,10):
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(22, GPIO.LOW)
    sleep(1)
    
    GPIO.output(17, GPIO.LOW)
    GPIO.output(22, GPIO.HIGH)
    sleep(1)
    
GPIO.output(22, GPIO.LOW)
    
     
