from flask import Flask, render_template, request
import RPi.GPIO as GPIO

led1 = None
led2 = None

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
	global led1
	global led2
	if request.method == "POST":
		if request.form.get("button1") == "on":
			led1 = not led1
		if request.form.get("button2") == "on":
			led2 = not led2

	if led1:
		GPIO.output(17,GPIO.HIGH)
		if led2:
			color = "purple"
		else:
			color = "red"
	else:
		GPIO.output(17,GPIO.LOW)
		if led2:
			color = "blue"
		else:
			color = "black"
	if led2:
		GPIO.output(22,GPIO.HIGH)
	else:
		GPIO.output(22,GPIO.LOW)

	return render_template("index.html", color=color)

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80)
