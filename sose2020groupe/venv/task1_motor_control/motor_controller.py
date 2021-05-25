from fake_rpi_gpio.gpio import GPIO # For testing in PC
#import RPi.GPIO as GPIO # For testing in Raspberry
from time import sleep
import sys
#exit()
class MotorController(object):
  
  def __init__(self):
    self.working = False

  def start_motor(self):

    self.PIN_STEP = 25 # do not change
    self.PIN_DIR = 8 # do not change
    #self.working = False
    # ...
    self.CCW = 1    # Counterclockwise Rotation
    self.SPR = 1600   # Steps per Revolution (360 / 0.225)
      
    #GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.PIN_DIR, GPIO.OUT)
    GPIO.setup(self.PIN_STEP, GPIO.OUT)
    GPIO.output(self.PIN_DIR, self.CCW)


    #GPIO.setwarnings(False)
    delay = 1/400
    counter = 50
    print('Motor started')
    self.working = True  
    for x in range(counter): 
      GPIO.output(self.PIN_STEP, GPIO.HIGH)
      sleep(delay)
      GPIO.output(self.PIN_STEP, GPIO.LOW)
      sleep(delay)
      self.working = True
          
    self.working = False
    #GPIO.cleanup()    
    #########
    #return "Motor Running"

  def stop_motor(self):
    self.working = False
    sys.exit()
    
  def is_working(self):
    return self.working


