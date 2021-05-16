from opencv_controller import OpenCVController
from camera import Camera
import time
import cv2
import numpy as np
import base64

opencv_controller = OpenCVController()

while True:
  frame = opencv_controller.get_frame(Camera())
  #img = cv2.resize(frame, (700, 500))
  print("Main file frame type : ", type(frame))
  #print("Main file frame dtype : ", frame.dtype)
  # Display in window
  #jpg_as_np = np.frombuffer(frame, np.uint8)
  #img = cv2.imdecode(jpg_as_np, cv2.COLOR_BGR2RGB)
  #cv2.imshow('image', frame)
  cv2.imshow('image', jpg_as_np)

  print("Is in zone: ", opencv_controller.is_in_zone())
  print("---------------------------------")
  
  cv2.waitKey(1)
  cv2.destroyAllWindows()
