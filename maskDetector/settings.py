from tensorflow.keras.models import load_model
import cv2 
import sys, os
from os.path import dirname, join
#sys.path.append(os.path.abspath(os.path.join('..', 'models')))


#text =" hello"
objectconfidence_threshold = 0.5
maskconfidence_threshold = 0.3
genderconfidence_threshold = 0.3




protoPath = join(dirname(__file__), "models/face_detector/deploy.prototxt")
modelPath = join(dirname(__file__), "models/face_detector/res10_300x300_ssd_iter_140000.caffemodel")
maskPath = join(dirname(__file__), "models/face_detector/mask_detector.model")


faceNet = cv2.dnn.readNetFromCaffe(protoPath,modelPath)

maskNet = load_model(maskPath)


#objectsNet = cv2.dnn.readNetFromCaffe(protoPath,modelPath)

#genderNet = load_model("models/genders/gender_detection.model")
