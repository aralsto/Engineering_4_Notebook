from flask import Flask, render_template, request
import RPi.GPIO as GPIO

led1 = None

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
	global led1
	if request.method == "POST":
		if request.form.get("button1") == "on":
			led1 = not led1

	if(led1):
		GPIO.output(17,GPIO.HIGH)
	else:
		GPIO.output(17,GPIO.LOW)

	return render_template("index.html")

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80)
