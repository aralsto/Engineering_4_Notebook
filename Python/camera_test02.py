#camera_test02
from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (1024,768)
camera.framerate = 24

camera.start_preview()

for i in range(1,9):
    camera.annotate_text = 'Effect: ' + str(i)
    sleep(2)
camera.stop_preview()
camera.close()
    
