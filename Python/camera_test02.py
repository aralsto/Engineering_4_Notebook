#camera_test02
from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (1024,768)
camera.framerate = 24

keepers = ['gpen', 'hatch', 'oilpaint', 'emboss', 'negative']
camera.start_preview()

for e in camera.IMAGE_EFFECTS:
    camera.image_effect = e
    camera.annotate_text = 'Effect: ' + e
    sleep(5)
    if e in keepers:
        camera.capture('/home/pi/Documents/Engineering_4_Notebook/Python/Pics/%s.jpg' % e)

camera.stop_preview()
camera.close()
