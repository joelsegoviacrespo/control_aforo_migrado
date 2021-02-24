from django.shortcuts import render
import cv2
# Create your views here.
from django.http.response import StreamingHttpResponse
from objectsDetector.camera import objectsDetector
from streaming.camera import LiveWebCam
from objectsDetector.forms import ObjectsForm
from objectsDetector.models import Objects
import numpy as np 
import json
'''
info = json.dumps(info)
	info = json.loads(info)
	print("\n AAAAAAAA,\n" ,info['label'])
	form = ObjectsForm(info)
	if form.is_valid():
		instance = Objects.objects.create(info)
		 
		try:
			#form = (id =form.get("id"))
			instance.save()
			print("saved")
			return redirect('/aforoInfo/todos')
		except Exception as e:
			print('%s (%s)' % (e, type(e)))
			pass
	else:
		print('no valido')
	if form.errors:
		for field in form:
			for error in field.errors:
				print("field.name")
				print(field.name)

				print(error)
	
	try:
		info.save()
	except Exception as e:
		print('%s (%s)' % (e, type(e)))
		pass
	 
'''
'''

	try:
		print("\n*******",info['label'])
		valor = ObjectsForm(info['label'])
		valor.save()
		return redirect('/aforoInfo/todos')
	except Exception as e:
		print('%s (%s)' % (e, type(e)))
		pass
        
'''
# Create your views here.
global mythreshold
global mysmooth

global isClicked
isClicked = False


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
		
		
		if isClicked == True:
			frame = camera.get_frame()
			(frames,info) = objectsDetector.objectsdetector(frame,mythreshold,mysmooth)
		#print(info)
			add_info(info)
		else:
			frame = camera.get_frame()
			ret, frames = cv2.imencode('.jpg', frame)
			frames = frames.tobytes()
			pass
			
		
		
		yield (b'--frame\r\n'
					b'Content-Type: image/jpeg\r\n\r\n' + frames + b'\r\n\r\n')






def livecam_feed(request):


	return gen(LiveWebCam(),
				content_type='multipart/x-mixed-replace; boundary=frame')

class detectordeObjetos():

	def theDetection(request,clicked):
		global isClicked
		isClicked = clicked

	def thevalues(request,th,sm):
		global mythreshold
		global mysmooth
		mythreshold = th
		mysmooth = sm
		print("\n INFO PARA VERIFICAR",th,sm)

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


# Create your views here.


