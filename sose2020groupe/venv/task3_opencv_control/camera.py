# Please note that this is a fake camera, it will just 
# yield the images 1.jpg, 2.jpg, 3.jg and 4.jpg. It is
# just for testing purposes. You should actually use the
# picamera module and implement the get_frame properly  

from time import time
import os, sys
import cv2

webcam = cv2.VideoCapture(0)

class Camera(object):
    def __init__(self):
        webcam = cv2.VideoCapture(0)
        #directory = os.path.join(os.path.dirname(__file__), 'test_frames')
        #_, self.test_frames_name = webcam.read()
        #self.test_frames_name = ['1.jpg', '2.jpg', '3.jpg', '4.jpg']
        #_, self.frames = [open(os.path.join(directory, f), 'rb').read() for f in self.test_frames_name]
        #_, self.frames = webcam.read()

    def get_frame(self):
        #random_index = int(time()) % 4
        #_, frame = webcam.read()
        #print('Frame', self.test_frames_name[random_index])
        #return self.frames[random_index]
        _, self.frames = webcam.read()
        #ret, buffer = cv2.imencode('.jpg', self.frames)
        #self.frames = buffer.tobytes()        
        return self.frames

'''from time import time
import os, sys
import cv2
import glob

class Camera(object):
    def __init__(self):
        #directory = os.path.join(os.path.dirname(__file__), 'test_frames')
        #self.test_frames_name = ['1.jpg', '2.jpg', '3.jpg', '4.jpg']
        #self.frames = [open(os.path.join(directory, f), 'rb').read() for f in self.test_frames_name]
        #self.frames = [open(os.path.join(directory, f), 'rb').read() for f in self.test_frames_name]
        #self.frames = cv2.imread("4.jpg")
        img_dir = os.path.join(os.path.dirname(__file__), 'test_frames')#"" # Enter Directory of all images  
        self.data_path = os.path.join(img_dir,'*g') 
        self.files = glob.glob(self.data_path) 
        self.data = [] 
        for f1 in self.files: 
            self.img = cv2.imread(f1) 
            self.data.append(self.img)

    def get_frame(self):
        for i in range (0,3):
            random_index = int(time()) % 4
            return self.data[random_index]
        ##random_index = int(time()) % 4
        #print('Frame', self.test_frames_name[random_index])
        #return self.frames[random_index]
        #return self.frames'''
