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
from streaming.models import Streaming
from streaming.models import SavedSettings
from cliente.models import Cliente



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
    print("\n PRIMER METODO \n")
    loadConfig(request)

    
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
        global smooth
        
        message = "Yes, AJAX!"
        response_json = request.POST['value']
        response_json = json.dumps(response_json)
        data = json.loads(response_json)
        dataAux = int(data)
        if data =="true":
            clicked1 = True
            smooth = smooth - dataAux
           # do.theDetection(clicked,clicked1)
        else:
            clicked1 = False
            smooth = smooth + dataAux
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

def add_info(info,info1):
    
    instance = Streaming()
    print(type(info))
    print(info.values())

    instance = Streaming()
    instance.label=info['label']
    instance.personid=info['id']
    instance.mask=info1['mask']
    
    instance.save()

    instance.save();print ("\n guardado!! \n")

def show_info():
    
    data ={
        'detection':'info',
        'mask':'info'
    }
    datas = str(data)
    print("\nLLAMADO \n")
    yield (datas)
    yield (datas)
    yield (datas)
    yield (datas)
    yield (datas)
    yield (datas)
    yield (datas)
    yield (datas)
    yield (datas)
    yield (datas)

	#print("\n","LABEl", instance.get_label())



def gen(camera):
    
    while True:
        show_info()
        
        
        global threshold
        global smooth
        global clicked
        global clicked1
        if (clicked == True and clicked1 == False):
            frame = camera.get_frame()
            (frames,info) = objectsDetector.objectsdetector(frame,threshold,smooth)
		#print(info)
            info1={"mask":False} 
            add_info(info,info1)


        elif (clicked1 == True and clicked == False):
            frame = camera.get_frame()
            (frames,info1) = maskDetector.maskdetector(frame,threshold,smooth)
            #print("\n",type(info1['mask']),"\n")
            info = {"label":"None", "id":"None"} 
            add_info(info,info1)
        elif (clicked1 == True and clicked == True):
            frame = camera.get_frame()


            (frames,info1) = maskDetector.maskdetector(frame,threshold,smooth)
            (frames2,info) = objectsDetector.objectsdetector(frame,threshold,smooth)
            
            
            add_info(info,info1)
	
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
                   

@login_required(login_url="/login/")
def saveConfig(request):
    print("\n HEY EXISTO\n ")
    global threshold
    global smooth

    global clicked
    global clicked1

    instance = SavedSettings()

    print("\n var 1",clicked,"\n var2",clicked1)
    print("\n var 1",threshold,"\n var2",smooth)

    
    instance.objectsDetection = clicked
    instance.maskDetection = clicked1

    instance.thresholdValue= threshold
    instance.smoothValue = smooth

    current_user = request.user
    instance.email=current_user.email
    
    instance.save()
    return HttpResponse("yeah")
@login_required(login_url="/login/")
def loadConfig(request):
    print("\n HEY EXISTO2\n ")
    global threshold
    global smooth
    global clicked
    global clicked1

    #instance = SavedSettings()
    current_user = request.user
    try:
        (a) = SavedSettings.objects.filter(email=current_user.email).values('objectsDetection').latest('settings_date')
        (b) = SavedSettings.objects.filter(email=current_user.email).values('maskDetection').latest('settings_date')
        (c) = SavedSettings.objects.filter(email=current_user.email).values('thresholdValue',).latest('settings_date')
        (d) = SavedSettings.objects.filter(email=current_user.email).values('smoothValue').latest('settings_date')
        threshold =c['thresholdValue']
        smooth =d['smoothValue']
        clicked =a['objectsDetection']
        clicked1 =b['maskDetection']
    except:
        threshold =0.5
        smooth =1
        clicked =False
        clicked1 =False


    #print(a)
    
    
    return HttpResponse("yeah")



