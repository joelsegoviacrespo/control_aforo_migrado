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


from scipy.spatial import distance as dist
from collections import OrderedDict
import numpy as np


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

(h, w) = (None, None)



class CentroidTracker():
    def __init__(self, maxDisappeared=50):
		# initialize the next unique object ID along with two ordered
		# dictionaries used to keep track of mapping a given object
		# ID to its centroid and number of consecutive frames it has
		# been marked as "disappeared", respectively
        self.nextObjectID = 0
        self.objects = OrderedDict()
        self.disappeared = OrderedDict()

		# store the number of maximum consecutive frames a given
		# object is allowed to be marked as "disappeared" until we
		# need to deregister the object from tracking
        self.maxDisappeared = maxDisappeared
    def register(self, centroid):
       
		# when registering an object we use the next available object
		# ID to store the centroid
        self.objects[self.nextObjectID] = centroid
        self.disappeared[self.nextObjectID] = 0
        self.nextObjectID += 1
        print("in recieving this", str(centroid))

    def deregister(self, objectID):
		# to deregister an object ID we delete the object ID from
		# both of our respective dictionaries
        del self.objects[objectID]
        del self.disappeared[objectID]

    def update(self, rects):
        print("updating", str(rects))
	
        if len(rects) == 0:
		
            for objectID in list(self.disappeared.keys()):
                self.disappeared[objectID] += 1

				
                if self.disappeared[objectID] > self.maxDisappeared:
                    self.deregister(objectID)

			
            return self.objects

        inputCentroids = np.zeros((len(rects), 2), dtype="int")

		# loop over the bounding box rectangles
        for (i, (startX, startY, endX, endY)) in enumerate(rects):
			
            cX = int((startX + endX) / 2.0)
            cY = int((startY + endY) / 2.0)
            inputCentroids[i] = (cX, cY)

        if len(self.objects) == 0:
            for i in range(0, len(inputCentroids)):
                self.register(inputCentroids[i])

	
        else:
		
            objectIDs = list(self.objects.keys())
            objectCentroids = list(self.objects.values())

		
            D = dist.cdist(np.array(objectCentroids), inputCentroids)


            rows = D.min(axis=1).argsort()

			
            cols = D.argmin(axis=1)[rows]

            usedRows = set()
            usedCols = set()

            for (row, col) in zip(rows, cols):
	
                if row in usedRows or col in usedCols:
                    continue

		
                objectID = objectIDs[row]
                self.objects[objectID] = inputCentroids[col]
                self.disappeared[objectID] = 0

                usedRows.add(row)
                usedCols.add(col)

            unusedRows = set(range(0, D.shape[0])).difference(usedRows)
            unusedCols = set(range(0, D.shape[1])).difference(usedCols)

			
            if D.shape[0] >= D.shape[1]:
				# loop over the unused row indexes
                for row in unusedRows:
					
                    objectID = objectIDs[row]
                    self.disappeared[objectID] += 1

					
                    if self.disappeared[objectID] > self.maxDisappeared:
                        self.deregister(objectID)

			
            else:
                for col in unusedCols:
                    self.register(inputCentroids[col])

		# return the set of trackable objects
        return self.objects




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
        smoothxsmooth = sm * sm
        mythreshold = round(mythreshold,1)
        if mythreshold >= 0.9:
            mythreshold =0.9
        elif mythreshold <= 0.1:
            mythreshold =0.1

        mysmooth = sm
        #print ("\n ESTO SON LOS VALORES ***************",mythreshold,mysmooth)
        ct = CentroidTracker()

        
        

        rects= []
        deccionInfo = None
        #cv2.imshow("frame",frame)
        el= None;a = True
        #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        (h, w) = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007843, (300, 300), 127.5)


        if mysmooth > 1 :
            kernel = np.ones((mysmooth,mysmooth),np.float32)/smoothxsmooth
            frame = cv2.filter2D(frame,-1,kernel)

        else:
            pass



        deteccionInfo = {'label': None,"id":None}
	
        objectsNet.setInput(blob)
        detections = objectsNet.forward()
        
		
        

	# loop over the detections
        for i in np.arange(0, detections.shape[2]):
            
            
            
		# extract the confidence (i.e., probability) associated with
		# the prediction
            confidence = detections[0, 0, i, 2]
            idx = int(detections[0, 0, i, 1])

		# filter out weak detections by ensuring the `confidence` is
		# greater than the minimum confidence
            if (confidence > mythreshold and (CLASSES[idx] == 'person')):
                # `detections`, then compute the (x, y)-coordinates of
    			# the bounding box for the object
                idx = int(detections[0, 0, i, 1])
                now = datetime.now()
                dt_string = now.strftime("%d.%m.%Y %H:%M:%S,%f")
                
                
                dt_obj = datetime.strptime(dt_string,
                           '%d.%m.%Y %H:%M:%S,%f')
                millisec = dt_obj.timestamp() * 1000
          
    			

                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")
                
    			# draw the prediction on the frame
                label = "{}: {:.2f}%".format(CLASSES[idx],
				confidence * 100)
                rects.append(box.astype("int"))
                objects = ct.update(rects)
                print("returned")
                '''
                cv2.rectangle(frame, (startX, startY), (endX, endY),COLORS[idx], 2)
                boxContainer = (label,(startX, startY), (endX, endY))
                
                y = startY - 15 if startY - 15 > 15 else startY + 15
                cv2.putText(frame, label, (startX, y),cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)
                deteccionInfo = {"label": CLASSES[idx]}
                '''
                for (objectID, centroid) in objects.items():
                    # draw both the ID of the object and the centroid of the
                    # object on the output frame
                    text = "ID {}".format(objectID)
                    y = startY - 15 if startY - 15 > 15 else startY + 15
                    cv2.putText(frame,text, (startX+ 150, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                    cv2.putText(frame, label, (startX, y),cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)


                    #cv2.putText(frame,text, (centroid[0] - 10, centroid[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                    cv2.circle(frame, (centroid[0], centroid[1]), 4, (0, 255, 0), -1)
                    cv2.rectangle(frame, (startX, startY), (endX, endY),COLORS[idx], 2)
                    
                    boxContainer = (label,(startX, startY), (endX, endY))
                    ret, jpeg = cv2.imencode('.jpg', frame)
                    deteccionInfo = {"label": CLASSES[idx],"id":objectID}
                a = False
                
            if deteccionInfo['label'] == None: 
                objectID = None
                deteccionInfo = {"label": "None","id":objectID}
                ret, jpeg = cv2.imencode('.jpg', frame)
            else:
                pass	
                #deteccionInfo ={"label": CLASSES[idx],"prediction": (confidence*100), "pos":((startX, startY), (endX, endY)), "date":dt_string, "timestamp":millisec  }
                #informacion.append(deteccionInfo)

				
				
        if a == True:
            ret, jpeg = cv2.imencode('.jpg', frame)
            if deteccionInfo['label'] == None:
                deteccionInfo = {"label": "None","id":None}
            else:
                pass	
            
        else: 
             pass
        ret, jpeg = cv2.imencode('.jpg', frame)
#return 
        
        return (jpeg.tobytes(), deteccionInfo)




