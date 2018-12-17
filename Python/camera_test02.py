#camera_test02
from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (1024,768)
camera.framerate = 24

camera.start_preview()
c = 0
for e in camera.IMAGE_EFFECTS:
    camera.image_effect = e
    camera.annotate_text = 'Effect: ' + e
    sleep(5)
    if c < 5:
        camera.capture('/home/pi/Documents/Engineering_4_Notebook/Python/Pics/%s.jpg' % e)
    c += 1
camera.stop_preview()
camera.close()
