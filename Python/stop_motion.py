#stop_motion
import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (1024,768)
camera.framerate = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

camera.start_preview()

frame = 1

while True:
    try:
        if GPIO.input(17):
            camera.capture('/home/pi/Documents/Engineering_4_Notebook/Python/Pics/animation/frame%03d.jpg' % frame)
            frame += 1
            print("Took a picture.")
            sleep(3)
            
    except KeyboardInterrupt:
        camera.stop_preview()
        camera.close()
        break
