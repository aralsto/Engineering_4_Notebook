#camera_test03
from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (1024,768)

camera.start_preview()
camera.start_recording('/home/pi/Documents/Engineering_4_Notebook/Python/Pics/video.h264')
sleep(10)
camera.stop_recording()
camera.stop_preview()
camera.close()
