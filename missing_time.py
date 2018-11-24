import numpy as np
import cv2
from tkinter import messagebox
import time
import threading

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

class Inception:
    def __init__(self):
        self.first_time = True
        self.start_time = 0
        self.new_time = 0
        self.missing_time = 10
    def begin_clock(self,new_time):
        self.new_time = new_time
        if self.first_time:
            self.start_time = time.time()
            self.diff = self.start_time - self.new_time
            self.first_time = False
        else:
            self.diff = self.new_time - self.start_time

        if self.diff > self.missing_time:
            self.notify()
            
    def notify(self):
        print("Person is missing for more than 10 sec")

    def reset_time(self):
        self.first_time = True
        self.start_time = 0
        self.new_time = 0
        
        
    

def beginprocess():
    
    cap = cv2.VideoCapture(0)
    bro = Inception()
    while True:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        if len(faces) == 0:
            current_time = time.time()
            bro.begin_clock(current_time)
        else:
            bro.reset_time()
            
            
            
        
        
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
        cv2.imshow('img',img)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()        

beginprocess()
