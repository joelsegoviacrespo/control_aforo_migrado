from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from imutils.video import VideoStream
import imutils
import cv2,os,urllib.request
import numpy as np
from django.conf import settings
from imutils.video import FPS
import argparse
import time
import json 
from datetime import datetime

from .settings import objectconfidence_threshold, objectsNet
thesmooth= 0


global mythreshold
global mysmooth

mythreshold = objectconfidence_threshold



CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
	"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
	"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	"sofa", "train", "tvmonitor"]
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))
active= True
label= None

class objectsDetector(object):
    global mythreshold
    global mysmooth
    def __init__(self):
        pass

    def __del__(self):
        cv2.destroyAllWindows()

    def objectsdetector(frame,th,sm):
        
        mythreshold = th
        mysmooth = sm
        print ("\n ESTO SON LOS VALORES ***************",mythreshold,mysmooth)
       
        ormacion= []
        deccionInfo = None
        #cv2.imshow("frame",frame)
        el= None;a = True
        #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        (h, w) = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007843, (300, 300), 127.5)
        deteccionInfo = {'label': None}
	
        objectsNet.setInput(blob)
        detections = objectsNet.forward()
        
		
        

	# loop over the detections
        for i in np.arange(0, detections.shape[2]):
            
            
            
		# extract the confidence (i.e., probability) associated with
		# the prediction
            confidence = detections[0, 0, i, 2]

		# filter out weak detections by ensuring the `confidence` is
		# greater than the minimum confidence
            if confidence > mythreshold:
                now = datetime.now()
                dt_string = now.strftime("%d.%m.%Y %H:%M:%S,%f")
                
                
                dt_obj = datetime.strptime(dt_string,
                           '%d.%m.%Y %H:%M:%S,%f')
                millisec = dt_obj.timestamp() * 1000
          
    			# `detections`, then compute the (x, y)-coordinates of
    			# the bounding box for the object
                idx = int(detections[0, 0, i, 1])
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")
    
    			# draw the prediction on the frame
                label = "{}: {:.2f}%".format(CLASSES[idx],
				confidence * 100)
                cv2.rectangle(frame, (startX, startY), (endX, endY),COLORS[idx], 2)
                boxContainer = (label,(startX, startY), (endX, endY))
                    
                y = startY - 15 if startY - 15 > 15 else startY + 15
                cv2.putText(frame, label, (startX, y),cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)
                deteccionInfo = {"label": CLASSES[idx]}
                ret, jpeg = cv2.imencode('.jpg', frame)
                a = False
            if deteccionInfo['label'] == None: 
                deteccionInfo = {"label": "None"}
            else:
                pass	
                #deteccionInfo ={"label": CLASSES[idx],"prediction": (confidence*100), "pos":((startX, startY), (endX, endY)), "date":dt_string, "timestamp":millisec  }
                #informacion.append(deteccionInfo)

				
				
        if a == True:
            ret, jpeg = cv2.imencode('.jpg', frame)
            if deteccionInfo['label'] == None:
                deteccionInfo = {"label": "None"}
            else:
                pass	
            
        else: 
             pass
        
#return 
        
        return (jpeg.tobytes(), deteccionInfo)
