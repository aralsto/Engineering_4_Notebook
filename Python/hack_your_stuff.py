#hack your stuff
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.IN)

while True:
	if GPIO.input(22):
		GPIO.output(17, GPIO.HIGH)
	else:
		GPIO.output(17, GPIO.LOW)
