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

	
        objectsNet.setInput(blob)
        detections = objectsNet.forward()
        deteccionInfo = {"label": None}
		
        

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
            
        else: 
             pass
#return 
        
        return (jpeg.tobytes(), deteccionInfo)
'''
		# grab the dimensions of the frame and then construct a blob
		# from it
		(h, w) = frame.shape[:2]
		blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300),
									 (104.0, 177.0, 123.0))

		# pass the blob through the network and obtain the face detections
		faceNet.setInput(blob)
		detections = faceNet.forward()

		# initialize our list of faces, their corresponding locations,
		# and the list of predictions from our face mask network
		faces = []
		locs = []
		preds = []

		# loop over the detections
		for i in range(0, detections.shape[2]):
			# extract the confidence (i.e., probability) associated with
			# the detection
			confidence = detections[0, 0, i, 2]

			# filter out weak detections by ensuring the confidence is
			# greater than the minimum confidence
			if confidence > 0.5:
				# compute the (x, y)-coordinates of the bounding box for
				# the object
				box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
				(startX, startY, endX, endY) = box.astype("int")

				# ensure the bounding boxes fall within the dimensions of
				# the frame
				(startX, startY) = (max(0, startX), max(0, startY))
				(endX, endY) = (min(w - 1, endX), min(h - 1, endY))

				# extract the face ROI, convert it from BGR to RGB channel
				# ordering, resize it to 224x224, and preprocess it
				face = frame[startY:endY, startX:endX]
				face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
				face = cv2.resize(face, (224, 224))
				face = img_to_array(face)
				face = preprocess_input(face)

				# add the face and bounding boxes to their respective
				# lists
				faces.append(face)
				locs.append((startX, startY, endX, endY))

		# only make a predictions if at least one face was detected
		if len(faces) > 0:
			# for faster inference we'll make batch predictions on *all*
			# faces at the same time rather than one-by-one predictions
			# in the above `for` loop
			faces = np.array(faces, dtype="float32")
			preds = maskNet.predict(faces, batch_size=32)

		# return a 2-tuple of the face locations and their corresponding
		# locations
		return (locs, preds)
'''
'''
    def get_frame(self):
		frame = self.vs.read()
		frame = imutils.resize(frame, width=650)
		frame = cv2.flip(frame, 1)
		# detect faces in the frame and determine if they are wearing a
		# face mask or not
		(locs, preds) = self.detect_and_predict_mask(frame, faceNet, maskNet)

		# loop over the detected face locations and their corresponding
		# locations
		for (box, pred) in zip(locs, preds):
			# unpack the bounding box and predictions
			(startX, startY, endX, endY) = box
			(mask, withoutMask) = pred

			# determine the class label and color we'll use to draw
			# the bounding box and text
			label = "Mask" if mask > withoutMask else "No Mask"
			color = (0, 255, 0) if label == "Mask" else (0, 0, 255)

			# include the probability in the label
			label = "{}: {:.2f}%".format(label, max(mask, withoutMask) * 100)

			# display the label and bounding box rectangle on the output
			# frame
			cv2.putText(frame, label, (startX, startY - 10),
						cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
			cv2.rectangle(frame, (startX, startY), (endX, endY), color, 2)
		ret, jpeg = cv2.imencode('.jpg', frame)
		return jpeg.tobytes()
    '''
'''
class LiveWebCam(object):
	def __init__(self):
		self.url = cv2.VideoCapture("rtsp://admin:Mumbai@123@203.192.228.175:554/")

	def __del__(self):
		cv2.destroyAllWindows()

	def get_frame(self):
		success,imgNp = self.url.read()
		resize = cv2.resize(imgNp, (640, 480), interpolation = cv2.INTER_LINEAR) 
		ret, jpeg = cv2.imencode('.jpg', resize)
		return jpeg.tobytes()
'''