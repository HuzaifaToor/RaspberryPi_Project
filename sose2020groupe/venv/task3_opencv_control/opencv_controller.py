import cv2
import numpy as np
import sys
#x1, y1, w1, h1 = 0
x1, y1, w1, h1 = [0, 0, 0, 0]
x, y, w, h = [0, 0, 0, 0]

class OpenCVController(object):

    def __init__(self):
        self.in_zone = False
        print('OpenCV controller initiated')
        x1, y1, w1, h1 = [0, 0, 0, 0]
        x, y, w, h = [0, 0, 0, 0]


    def get_frame(self, camera):
        self.in_zone = False
        frame = camera.get_frame()

        #cv2.imshow('Camera Output', frame)
        #cv2.waitKey(0)
        #############################
        #Red Lower range
        hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        '''lower_red = np.array([0,120,70])
        upper_red = np.array([10,255,255])
        mask1 = cv2.inRange(hsvFrame, lower_red, upper_red)
        #Red upper range
        lower_red = np.array([170,120,70])
        upper_red = np.array([180,255,255])
        mask2 = cv2.inRange(hsvFrame,lower_red,upper_red)
        red_mask = mask1 + mask2'''
        lower_red = np.array([161, 155, 84],np.uint8)
        upper_red = np.array([179, 255, 255],np.uint8)
        red_mask = cv2.inRange(hsvFrame, lower_red, upper_red)
        #Blue color Range
        blue_lower=np.array([100,150,0],np.uint8)
        blue_upper=np.array([140,255,255],np.uint8)
        blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)
	# to detect only that particular color 
        kernal = np.ones((5, 5), "uint8")
        # For red color
        red_mask = cv2.dilate(red_mask, kernal)
        res_red = cv2.bitwise_and(frame, frame, mask = red_mask)
        # for blue color
        blue_mask = cv2.dilate(blue_mask, kernal)
        res_blue = cv2.bitwise_and(frame, frame, mask = blue_mask)
        
        ####################### Red area detection ######################

        contours, hierarchy = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if(area > 3000):
                x, y, w, h = cv2.boundingRect(contour)
                imageFrame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.putText(imageFrame, "Red Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255))

            '''elif (area > 3000):
                x, y, w, h = cv2.boundingRect(contour)
                imageFrame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv2.putText(imageFrame, "Blue Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0))
                self.in_zone = True 
                print("Overlapping ")'''

        ########################### Blue area detection ########################################

        contours, hierarchy = cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if(area > 5000):
                x1, y1, w1, h1 = cv2.boundingRect(contour)

                imageFrame = cv2.rectangle(frame, (x1, y1), (x1 + w1, y1 + h1), (255, 0, 0), 2)
                cv2.putText(imageFrame, "Blue Colour", (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0))
                
        
        try:
            if (x < (x1+w1) and (x+w) > x1):
                self.in_zone = True
                print("Overlapping ")
        except:
            self.in_zone = False
            print("No Overlapping\n")
        #############################
        # ...
        print('Monitoring\n')
        #print("Type before openCV ", type(frame))
        #print("dtype before opneCV ", frame.dtype)
        
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        #yield (b'--frame\r\n'
                #b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result
        #print("Type after openCV ", type(frame))
        #print("dtype after opneCV ", frame.dtype)
        return frame

    def is_in_zone(self):
        return self.in_zone


    def stopCamera(self):
        quit()
