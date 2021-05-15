#from fake_rpi_gpio.gpio import GPIO # For testing in PC
import RPi.GPIO as GPIO # For testing in Raspberry Pi
import time
import numpy as np

class SensorController:

  def __init__(self):
    self.PIN_TRIGGER = 18 # do not change
    self.PIN_ECHO = 24 # do not change
    #self.distance = None
    self.distance = 500
    #set GPIO direction (IN / OUT)
    print('Sensor controller initiated')
    print("Waiting For sensor to settle")
    #GPIO.setwarnings(False)

  def track_rod(self):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.PIN_TRIGGER, GPIO.OUT)
    GPIO.setup(self.PIN_ECHO, GPIO.IN)
    #######################
    # set Trigger to LOW
    GPIO.output(self.PIN_TRIGGER, False)
    time.sleep(0.5)

    dist_array = np.array([])

    for i in range(50):
      #GPIO.output(self.PIN_TRIGGER, False)
      #time.sleep(0.005)
      GPIO.output(self.PIN_TRIGGER, True)
      # set Trigger after 0.01ms to LOW
      time.sleep(0.00001)
      GPIO.output(self.PIN_TRIGGER, False)

      StartTime = time.time()
      StopTime = time.time()

      # save StartTime
      while GPIO.input(self.PIN_ECHO) == 0:
          StartTime = time.time()

      # save time of arrival
      while GPIO.input(self.PIN_ECHO) == 1:
          StopTime = time.time()

      # time difference between start and arrival
      TimeElapsed = StopTime - StartTime
      distance1 = round(TimeElapsed * 17150, 2)
      #print ("Orignal_Distance" + str(distance1))
      self.distance = 100
      dist_array = np.append(dist_array, distance1)
      
      #print("STD : " + str(np.std(dist_array[-10:])))
      #print ("Orignal_Distance" + str(np.mean(dist_array)))
      #GPIO.cleanup()
      if(dist_array.size >=10):
        if(np.std(dist_array[-10:])<=0.5):
          #self.distance = np.mean(dist_array[-10:])
          self.distance = 200
          break
      if(dist_array.size == 50):
        self.distance = np.median(dist_array)
        self.distance = 300
        break


  def get_distance(self):
    return self.distance
