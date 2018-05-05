#!/usr/bin/env python

############################################################
# This code uses to demonstrate the capbility for 
# using sensor to read the temp and humidity using Raspberry.
############################################################

import time
import Adafruit_DHT
import sys
import requests
import json


period = 60 ## Sensor data reporting period (1 minute)
pin = 4 ## Assuming the DHT11 sensor is connected to GPIO pin number 4

def run():
  while True:
    ### Assume 
    humidity, temperature = Adafruit_DHT.read_retry( Adafruit_DHT.DHT11, pin )
    if humidity is not None and temperature is not None:
        print "Temp={0:f}*C  Humidity={1:f}%".format(temperature, humidity)
        try:
          ### print "In try block"
            data = {'humidity':humidity,'temperature':temperature}
            json_data = json.dumps(data)
            ## r = requests.post('http://192.168.0.8:1880/payload',json_data)
        except Exception as e:
          ## Process exception here
          print "Error= " + str(e)
    else:
        print "Failed to get reading. Try again!"

    #Sleep some time
    time.sleep( period )

run()
