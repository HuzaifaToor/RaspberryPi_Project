import time
from sensor_controller import SensorController

sensor_controller = SensorController()

while True:
  sensor_controller.track_rod()
  print("Distance: ", sensor_controller.get_distance(), 'cm')
  x = int(input("Enter 1 to stop Monitorig and anything else to continue : "))
  if x == 1:
    sensor_controller.stopSensor()
  else:
    time.sleep(2)
  
