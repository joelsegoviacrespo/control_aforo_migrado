from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test,permission_required
from streaming.forms import StreamingForm
from django.utils.translation import activate
from django.http import HttpResponse
import json

import cv2
from django.http.response import StreamingHttpResponse
from streaming.camera import LiveWebCam
from objectsDetector import views
from objectsDetector.models import Objects
#do =views.detectordeObjetos()
from maskDetector import views
#ma =views.detectordeMascaras()


from objectsDetector.camera import objectsDetector
from maskDetector.camera import maskDetector


global objectId
global threshold
global smooth
threshold = 0.5
smooth = 0
global state
global clicked
clicked = False

global clicked1
clicked1 =False


#print("\n",state)




@login_required(login_url="/login/")
def streaming(request):
    activate('es')
    
    form = StreamingForm()
    
    return render(request, 'streaming/agregar.html', {'form': form})

@login_required(login_url="/login/")
def objD(request):
    if request.is_ajax():
        global clicked
        global clicked1
        message = "Yes, AJAX!"
        response_json = request.POST['value']
        response_json = json.dumps(response_json)
        data = json.loads(response_json)
        if data =="true":
            clicked = True
            #do.theDetection(clicked,clicked1)
        else:
            clicked = False
            #do.theDetection(clicked,clicked1)
        #print("\n AAAAAAAAAAAAAAAAAAAAAAAAAA \n",clicked)
     
            
            
        #print("\n",state)



    else:
        message = "Not Ajax"
    return HttpResponse(message)


@login_required(login_url="/login/")
def maskD(request):
    if request.is_ajax():
        global clicked
        global clicked1
        message = "Yes, AJAX!"
        response_json = request.POST['value']
        response_json = json.dumps(response_json)
        data = json.loads(response_json)
        if data =="true":
            clicked1 = True
            #do.theDetection(clicked,clicked1)
        else:
            clicked1 = False
            #do.theDetection(clicked,clicked1)
        #print("\n AAAAAAAAAAAAAAAAAAAAAAAAAA \n",clicked)
     
            
            
        #print("\n",state)



    else:
        message = "Not Ajax"
    return HttpResponse(message)

@login_required(login_url="/login/")
def smoothValue(request):
    if request.is_ajax():
        global clicked
        global clicked1
        message = "Yes, AJAX!"
        response_json = request.POST['value']
        response_json = json.dumps(response_json)
        data = json.loads(response_json)
        if data =="true":
            clicked1 = True
           # do.theDetection(clicked,clicked1)
        else:
            clicked1 = False
            #do.theDetection(clicked,clicked1)
        #print("\n AAAAAAAAAAAAAAAAAAAAAAAAAA \n",clicked)
     
            
            
        #print("\n",state)



    else:
        message = "Not Ajax"
    return HttpResponse(message)


#detections values

@login_required(login_url="/login/")

def thresholdValue(request):
    
    if request.is_ajax():
        
        message = "Yes, AJAX!"
        response_json = request.POST['value']
        response_json = json.dumps(response_json)
        data = json.loads(response_json)
        dataAux = int(data)
        dataAux = dataAux/10
       
        
        global threshold
        global smooth
        threshold = threshold + dataAux
        #print(threshold)
         
    
       #print ("\nVALORES QUE TENGO QUE ENVIAR A THEVALUES \n",threshold,smooth)
        #do.thevalues(threshold,smooth)
        
    else:
        message = "Not Ajax"
    return HttpResponse(response_json)



def index(request):
	return render(request, 'streamapp/home.html')

def add_info(info):
	instance = Objects()
	instance.label=  info['label']
	#print("\n","LABEl", instance.get_label())
	instance.save()
    

def gen(camera):
	while True:
		global threshold
		global smooth
		global clicked
		global clicked1
		
		
		if clicked == True:
			frame = camera.get_frame()
			(frames,info) = objectsDetector.objectsdetector(frame,threshold,smooth)
		#print(info)
			add_info(info)
		elif (clicked1 == True and clicked == False):
			frame = camera.get_frame()
			(frames,info) = maskDetector.maskdetector(frame,threshold,smooth)
	
		else:
			frame = camera.get_frame()
			ret, frames = cv2.imencode('.jpg', frame)
			frames = frames.tobytes()
			
			
		
		
		yield (b'--frame\r\n'
					b'Content-Type: image/jpeg\r\n\r\n' + frames + b'\r\n\r\n')

def livecam_feed(request):
    global threshold
    global smooth
    #print ("\nVALORES QUE TENGO QUE ENVIAR A THEVALUES \n",threshold,smooth)
    #do.thevalues(threshold,smooth)
    #ma.thevalues(threshold,smooth)

    
    return StreamingHttpResponse(gen(LiveWebCam()),content_type='multipart/x-mixed-replace; boundary=frame')
                   




