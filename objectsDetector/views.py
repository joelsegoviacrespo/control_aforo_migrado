from django.shortcuts import render
import cv2
# Create your views here.
from django.http.response import StreamingHttpResponse
from objectsDetector.camera import objectsDetector
from maskDetector.camera import maskDetector
from streaming.camera import LiveWebCam
from objectsDetector.forms import ObjectsForm
from objectsDetector.models import Objects
import numpy as np 
import json

# Create your views here.
global mythreshold
global mysmooth

global isClicked
global isClicked1
isClicked = False
isClicked1 = False

'''
def add_info(info):
	instance = Objects()
	instance.label=  info['label']
	#print("\n","LABEl", instance.get_label())
	instance.save()
    

def gen(camera):
	while True:
		global mythreshold
		global mysmooth
		global isClicked
		global isClicked1
		
		
		if isClicked == True:
			frame = camera.get_frame()
			(frames,info) = objectsDetector.objectsdetector(frame,mythreshold,mysmooth)
		#print(info)
			add_info(info)
		elif (isClicked1 == True and isClicked == False):
			frame = camera.get_frame()
			(frames,info) = maskDetector.maskdetector(frame,mythreshold,mysmooth)
	
		else:
			frame = camera.get_frame()
			ret, frames = cv2.imencode('.jpg', frame)
			frames = frames.tobytes()
			
			
		
		
		yield (b'--frame\r\n'
					b'Content-Type: image/jpeg\r\n\r\n' + frames + b'\r\n\r\n')






def livecam_feed(request):


	return gen(LiveWebCam(),
				content_type='multipart/x-mixed-replace; boundary=frame')


class detectordeObjetos():

	def object_feed(request):
		
		return StreamingHttpResponse(gen(LiveWebCam()),
						content_type='multipart/x-mixed-replace; boundary=frame')
						
	def livecam_feed(request):
		
		return gen(LiveWebCam())
						
	
	def gen(camera):
		while True:
			frame = camera.get_frame()
			yield (b'--frame\r\n'
					b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

	def index(request):
		return render(request, 'streamapp/home.html')


	


	def video_feed(request):
		return StreamingHttpResponse(gen(VideoCamera()),
						content_type='multipart/x-mixed-replace; boundary=frame')


	def webcam_feed(request):
		return StreamingHttpResponse(gen(IPWebCam()),
					content_type='multipart/x-mixed-replace; boundary=frame')
'''

'''
	def theDetection(request,clicked,clicked1):
		global isClicked
		global isClicked1
		isClicked = clicked
		isClicked1 = clicked1

	def thevalues(request,th,sm):
		global mythreshold
		global mysmooth
		mythreshold = th
		mysmooth = sm
		print("\n INFO PARA VERIFICAR",th,sm)
'''
	

# Create your views here.

