#!/usr/bin/python3
import os
import time
from sense_hat import SenseHat
import datetime
from time import sleep

filePath = "/home/pi/Desktop/weather_station_pictures/Data_from_SenseHat/SenseHat_Data.txt"

sense = SenseHat()
e = [0, 0, 0]
blank = [
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e
]
sense.set_pixels(blank)
print("Starting SenseHat weather script")

while True:
    # Prints datetime
    now = datetime.datetime.now()
    timeNow = now.strftime("%a %m-%d-%Y @ %H:%M:%S")
    print(timeNow)
    print("Getting data from SenseHat...")
    # Tries to get SenseHat data
    try:
        # Get SenseHat data values
        temp = sense.get_temperature_from_pressure()
        humid = sense.get_humidity()
        press = sense.get_pressure()
        
        # Round SenseHat values
        tempC = round(temp, 2)
        tempF = round(1.8 * (temp) + 32, 2)
        humidR = round(humid, 2)
        pressR = round(press, 2)
        
        # Prints the values of temperature and humidity from SenseHat
        print("temp " + u"\u00B0" + "C = {:.2f}".format(tempC))
        print("temp " + u"\u00B0" + "F = {:.2f}".format(tempF))
        print("humid = {:.2f}".format(humidR))
        print("press = {:.2f}".format(pressR))
        print("SenseHat data retreved successfully.\n")
        print("Inputting data into SenseHat_Data.txt")
        try:
            f = open(filePath, "a")
            f.write(timeNow +"\ntemp " + u"\u00B0" + "C = {:.2f}".format(tempC) + "\ntemp " + u"\u00B0" + "F = {:.2f}".format(tempF) +
                    "\nhumidity = {:.2f}".format(humidR) + "\npressure = {:.2f}".format(pressR) +
                    "\n------------------------------\n\n")
            f.close()
            print("Successfully entered data into SenseHat_Data.txt\n")
        except:
            print("Something went wrong. Unable to open SenseHat_Data.txt\n")
    except:
        print("An error occurred. Unable to get data from SenseHat\n")
    sleep(60)
