#import load cell library
import loadcell as lc
import RPi.GPIO as GPIO
import lcd  #import lcd library
import kpad_new as kpad	 #import keypad library
import time
import os
import math
import datetime
import sys
import json
import urllib.request
import requests
import constants

def takePicture():
    lcd.clear()
    lcd.string("Taking picture...", LINE_1)
    if os.path.exists('/dev/video0'):
        #create image file name with current date
        imgName = "image-"+ datetime.datetime.now().isoformat()+str(constants.USER_ID)+".jpg"
        #imagepath = "/home/pi/ghfarm/images/%s" %imgName
        imagepath = "/Desktop/BE project/data/%s" % imgName
        #capture image and save in images directory. if image file does not exists in folder then retake the image
        while os.path.isfile(imagepath) == False:
            os.system("fswebcam -r 640x480 -S 10 --no-banner %s" %imagepath)
        return True, imgName
    else:	#if camera is not attached display error message
        lcd.clear()
        lcd.string("      FAILED", LINE_1)
        lcd.string("No camera attached", LINE_2)
        time.sleep(2)
        return False, "NoCamera"