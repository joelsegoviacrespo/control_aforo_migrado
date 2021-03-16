import imutils
import cv2,os,urllib.request
import numpy as np
from django.conf import settings
import random 
import time
from imutils.video import VideoStream
from imutils.video import FPS
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from django.shortcuts import render
from django.http import StreamingHttpResponse
import http
import threading
from threading import Thread
#import ffmpeg
import pafy
from objectsDetector.camera import objectsDetector
import time

class LiveWebCam(object):
    def __init__(self):
        url = 'https://www.youtube.com/watch?v=1cq9mUblW_A'
        

       #vPafy = pafy.new(url)
        
        #play = vPafy.getbest(preftype="webm")
        #self.video = cv2.VideoCapture(play.url)
        #self.video = cv2.VideoCapture(0+ cv2.CAP_DSHOW)
        #self.video = cv2.VideoCapture('http://211.248.20.173:8080/cam_1.cgi')
        #self.video = cv2.VideoCapture('http://210.249.39.236/mjpg/video.mjpg')
       
        
        self.video = cv2.VideoCapture('http://channel.softwaremediafactory.com:8082/canales/Barcelona720p.m3u8')
        #time.sleep(1)
        #self.video = cv2.VideoCapture("https://meraki-eu-central-1-singularity-production.s3.eu-central-1.amazonaws.com/sp/vc/665406844944033398/665406844943991420/2021/03/09/15/_1615191506_1615192106.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJT4Y6MIN4RDUITNQ%2F20210314%2Feu-central-1%2Fs3%2Faws4_request&X-Amz-Date=20210314T231444Z&X-Amz-Expires=604799&X-Amz-SignedHeaders=host&X-Amz-Signature=db92fe5516da85b55d76fb6a14aff3379dede1ca754e224439ec74b813a6e507")
        #self.video.set(cv2.CAP_PROP_POS_MSEC, 0)
        #time.sleep(1)
        self.thread = Thread(target=self.update, args=())
        self.thread.daemon = True
        self.thread.start()
        
        #(self.status, self.frame)=self.video.read()
       

        
        
    def __del__(self):
        cv2.destroyAllWindows()
        

    def get_frame(self):
        done = False
        #if self.status:
            #success,imgNp = self.video.read()
            #(self.status, self.frame)=self.video.read()
            #self.video = cv2.VideoCapture(0+ cv2.CAP_DSHOW)
            #self.video = cv2.VideoCapture('http://211.248.20.173:8080/cam_1.cgi')
            
        self.video = cv2.VideoCapture('http://channel.softwaremediafactory.com:8082/canales/Barcelona720p.m3u8')
            
            #time.sleep(1)
        #self.video = cv2.VideoCapture("https://meraki-eu-central-1-singularity-production.s3.eu-central-1.amazonaws.com/sp/vc/665406844944033398/665406844943991420/2021/03/09/15/_1615191506_1615192106.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJT4Y6MIN4RDUITNQ%2F20210314%2Feu-central-1%2Fs3%2Faws4_request&X-Amz-Date=20210314T231444Z&X-Amz-Expires=604799&X-Amz-SignedHeaders=host&X-Amz-Signature=db92fe5516da85b55d76fb6a14aff3379dede1ca754e224439ec74b813a6e507")
       # self.video.set(cv2.CAP_PROP_POS_FRAMES, 5)
            #self.video.set(cv2.CAP_PROP_POS_MSEC, 0)
            #time.sleep(1)
            #self.video = cv2.VideoCapture('http://210.249.39.236/mjpg/video.mjpg')
        while(done == False):
            try:
                (self.status, self.frame)=self.video.read()
                resize = cv2.resize(self.frame, (550, 335), interpolation = cv2.INTER_LINEAR)
                done = True
            except Exception as e:
                done = False
                #print(str(e)) 

            
            #ret, jpeg = cv2.imencode('.jpg', resize)
            
            #(objects,info) = objectsDetector.objectsdetector(self.frame)
            
            #mask =  maskDetector.maskdetector(self.frame)
            #gender = genderDetector.genderdetector(self.frame)
            #ret, jpeg = cv2.imencode('.jpg', jpeg)
        return resize
    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()
