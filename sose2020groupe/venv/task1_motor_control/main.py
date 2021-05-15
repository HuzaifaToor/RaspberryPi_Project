import time
from motor_controller import MotorController

motor_controller = MotorController()

for x in range(5):
  if not motor_controller.is_working():
    motor_controller.start_motor()
    x=int(input("Please Enter 1 to continue, anything else to exit"))
    if x==1:
      time.sleep(5)
    else:
      motor_controller.stop_motor()
