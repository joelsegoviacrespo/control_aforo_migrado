from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from imutils.video import VideoStream
import imutils
import cv2,os,urllib.request
import numpy as np
from django.conf import settings
from imutils.video import VideoStream
from imutils.video import FPS
import numpy as np
import argparse
import imutils
import time
import cv2
#from settings import objectconfidence_threshold,objectsNet
import json 
from datetime import datetime

#import options.settings as st
from .settings import maskconfidence_threshold, faceNet,maskNet
#import settings
print("AAAAAAAAAAAAAAAAAAAAAA",maskconfidence_threshold)

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
	"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
	"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	"sofa", "train", "tvmonitor"]
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))
active= True
label= None



class maskDetector(object):
    def __init__(self):
        pass

    def maskdetector(frame,th,sm):
   
        (h, w) = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(frame, 1.0, (400, 400),
    		(104.0, 177.0, 123.0)) #224
        
    
    
        faceNet.setInput(blob)
        detections = faceNet.forward()
    
    

        faces = []
        locs = []
        preds = []
        informacion =[]
        deteccionInfo = {};a = True
        deteccionInfo ={"label": "none" }
        for i in range(0, detections.shape[2]):
            now = datetime.now()
            dt_string = now.strftime("%d.%m.%Y %H:%M:%S,%f")
                
                
            dt_obj = datetime.strptime(dt_string,'%d.%m.%Y %H:%M:%S,%f')
            millisec = dt_obj.timestamp() * 1000
            confidence = detections[0, 0, i, 2]

            if confidence > maskconfidence_threshold:# 0.5
   
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")
    
    		
                (startX, startY) = (max(0, startX), max(0, startY))
                (endX, endY) = (min(w - 1, endX), min(h - 1, endY))
    
    
                face = frame[startY:endY, startX:endX]
                face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
                face = cv2.resize(face, (224, 224))
                face = img_to_array(face)
                face = preprocess_input(face)
                
    
    
                faces.append(face)
                locs.append((startX, startY, endX, endY))

    
  
        if len(faces) > 0:



                faces = np.array(faces, dtype="float32")
                preds = maskNet.predict(faces, batch_size=32)
                for (box, pred) in zip(locs, preds):
                    now = datetime.now()
                    dt_string = now.strftime("%d.%m.%Y %H:%M:%S,%f")
                
                
                    dt_obj = datetime.strptime(dt_string,
                           '%d.%m.%Y %H:%M:%S,%f')
                    millisec = dt_obj.timestamp() * 1000
	
                    (startX, startY, endX, endY) = box
                    (mask, withoutMask) = pred

		
                    label = "Mask" if mask > withoutMask else "No Mask"
                    color = (0, 255, 0) if label == "Mask" else (0, 0, 255)
                    templabel=label
		
                    label = "{}: {:.2f}%".format(label, max(mask, withoutMask) * 100)

	
                    cv2.putText(frame, label, (startX, startY - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
                    cv2.rectangle(frame, (startX, startY), (endX, endY), color, 2)
                    #deteccionInfo ={"label": templabel,"prediction": (max(mask, withoutMask) * 100), "pos":((startX, startY), (endX, endY)), "date":dt_string, "timestamp":millisec  }
                    deteccionInfo ={"label": templabel }
                    informacion.append(deteccionInfo)
                    ret, jpeg = cv2.imencode('.jpg', frame)
                    a = False
        if a == True :
            ret, jpeg = cv2.imencode('.jpg', frame)
        else: 
             pass
		#return 
        return jpeg.tobytes(),deteccionInfo 
            
    
        