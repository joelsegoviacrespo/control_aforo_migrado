from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test,permission_required
from streaming.forms import StreamingForm
from django.utils.translation import activate
from django.http import HttpResponse
import json


from django.http.response import StreamingHttpResponse
from streaming.camera import LiveWebCam
from objectsDetector import views
do =views.detectordeObjetos()

global objectId
global threshold
global smooth
threshold = 0.5
smooth = 0
global state

#print("\n",state)




@login_required(login_url="/login/")
def streaming(request):
    activate('es')
    
    form = StreamingForm()
    
    return render(request, 'streaming/agregar.html', {'form': form})

@login_required(login_url="/login/")
def objD(request):
    if request.is_ajax():
        global state
        message = "Yes, AJAX!"
        response_json = request.POST['value']
        response_json = json.dumps(response_json)
        data = json.loads(response_json)
        if data =="true":
            clicked = True
            do.theDetection(clicked)
        else:
            clicked = False
            do.theDetection(clicked)
        print("\n AAAAAAAAAAAAAAAAAAAAAAAAAA \n",clicked)
     
            
            
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
        print(threshold)
         
    
        print ("\nVALORES QUE TENGO QUE ENVIAR A THEVALUES \n",threshold,smooth)
        do.thevalues(threshold,smooth)
        
    else:
        message = "Not Ajax"
    return HttpResponse(response_json)

@login_required(login_url="/login/")
def smoothValue(request):
    
    if request.is_ajax():
        
        message = "Yes, AJAX!"
        response_json = request.POST['value']
        response_json = json.dumps(response_json)
        data = json.loads(response_json)
        dataAux = int(data)
        dataAux = dataAux/10
        
        global threshold
        global smooth
        smooth = smooth + dataAux
        print(smooth)
        print ("\nVALORES QUE TENGO QUE ENVIAR A THEVALUES \n",threshold,smooth)
        do.thevalues(threshold,smooth)
        
    else:
        message = "Not Ajax"
    return HttpResponse(data)


def index(request):
	return render(request, 'streamapp/home.html')


def gen(camera):
	while True:
		frame = camera.get_frame()
        
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def livecam_feed(request):
    global threshold
    global smooth
    print ("\nVALORES QUE TENGO QUE ENVIAR A THEVALUES \n",threshold,smooth)
    do.thevalues(threshold,smooth)

    
    return StreamingHttpResponse(do.livecam_feed(),content_type='multipart/x-mixed-replace; boundary=frame')
                   