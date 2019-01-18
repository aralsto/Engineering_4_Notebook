#Parent Detector
import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (1024,768)

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

running = True
while running:
    if GPIO.input(17):
        print("started")
        camera.start_recording('/home/pi/Documents/Engineering_4_Notebook/Python/Pics/detectorVideo.h264')
        sleep(10)
        camera.stop_recording()
        camera.close()
        print("stopped")
        running = False
