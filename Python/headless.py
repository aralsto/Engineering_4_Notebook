#Headless
#GPIO Pins -I2C
#imports
import time

import Adafruit_LSM303
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

#setting up OLED
RST = 24
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3D)

disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image)

font = ImageFont.load_default()

#initializing accelerometer and its variables
lsm303 = Adafruit_LSM303.LSM303()
accelInitialized = None
accelInitCount = 0
accelInitSum = 0
accelConst = 0

#data set
data = []

#main loop
while True:
    #getting accelerometer data
    accel, mag = lsm303.read()
    accel_x, accel_y, accel_z = accel

    #calibrating to earth's gravity
    if not accelInitialized:
        draw.text((0,0), 'Calibrating,', font=font, fill=255)
        draw.text((0,10), 'hold still.', font=font, fill=255)
        disp.image(image)
        disp.display()
        
        accel_x, accel_y, accel_z = accel
        accelInitCount += 1
        accelInitSum += accel_z
        if accelInitCount == 50:
            accelInitialized = True
            accelConst = 9.81/(accelInitSum/50)
        
    #normal function
    else:
        accel_x = round((accel_x*accelConst),3)
        accel_y = round((accel_y*accelConst),3)
        accel_z = round((accel_z*accelConst),3)
        
        #display accelerometer data
        draw.rectangle((0,0,width,height), outline=0, fill=0)

        #draw.text((0,0), 'X accel: '+str(accel_x), font=font, fill=255)
        #draw.text((0,10), 'Y accel: '+str(accel_y), font=font, fill=255)
        #draw.text((0,20), 'Z accel: '+str(accel_z), font=font, fill=255)
        
        if len(data) >= 118:
            data.pop(0)
        
        data.append(accel_y)
        
        for i in range(0,len(data)):
            draw.point(((i+5),(32+int(data[i]/0.4))), fill=255)

        draw.text((0,20), 'Y Acceleration '+str(accel_z), font=font, fill=255)
        disp.image(image)
        disp.display()
