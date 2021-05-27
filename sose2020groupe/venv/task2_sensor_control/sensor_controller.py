#from fake_rpi_gpio.gpio import GPIO # For testing in PC
#import RPi.GPIO as GPIO # For testing in Raspberry Pi
import time
import numpy as np
from random import randint
import sys
from time import sleep

class SensorController:

  def __init__(self):
    self.PIN_TRIGGER = 18 # do not change
    self.PIN_ECHO = 24 # do not change
    self.distance = None
    #self.distance = 500
    #set GPIO direction (IN / OUT)
    print('Sensor controller initiated')
    print("Waiting For sensor to settle")
    #GPIO.setwarnings(False)

  def track_rod(self):
    sleep(1)
    self.distance = randint(10, 30)
    #print("Distance is :", self.distance)

  def get_distance(self):
    return self.distance

  def stopSensor(self):
    sys.exit()
