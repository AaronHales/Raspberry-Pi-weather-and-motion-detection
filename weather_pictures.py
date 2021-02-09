#!/usr/bin/python
import picam
import picamera
from datetime import datetime

motionState = False
picPath = "/home/pi/Desktop/weather_station_pictures/Pictures/"
print("Starting motion detection script")

def captureImage(currentTime, picPath):
    # Generate the picture's name
    print ("Taking picture...")
    picName = currentTime.strftime("%a %m-%d-%Y @ %H:%M:%S") + ".jpg"
    with picamera.PiCamera() as camera:
        camera.resolution = (1280, 720)
        camera.capture(picPath + picName)
    print("We have taken a picture.")
    return picName
    
def getTime():
    # Fetch the current time
    currentTime = datetime.now()
    return currentTime

while True:
    motionState = picam.motion()
    print("Motion Detected: " + str(motionState))
    if motionState:
        currentTime = getTime()
        try:
            picName = captureImage(currentTime, picPath)
            print("Saved picture.")
        except:
            print("Something went wrong. Unable to take picture.")
        
