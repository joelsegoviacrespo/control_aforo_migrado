from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django import template
from camaras.models import Camaras
from camara_zona.models import CamaraZona
from django.forms.models import model_to_dict
from instalacion.models import Instalacion
from monitor.models import Monitor
import sys
import http.client
import mimetypes
from pip._vendor import requests
import logging
import base64
from django.conf import settings
import json
import urllib.request
import calendar
import datetime
import pytz
from datetime import date


from aforoInfo.models import AforoInfo
from django.core import serializers
from rest_framework.renderers import JSONRenderer


from camaras_historico.models import myCamaras
from datetime import date
from datetime import datetime, timedelta


today = date.today()
mydate = str(today.strftime("%Y-%m-%d"))
mydate1 = datetime.today()

mydate2 = datetime.today().strftime('%A')

serial_camara = "Q2GV-4YBM-YWWJ"



def TimeConverter(millis):
    millis = int(millis)
    seconds=(millis/1000)%60
    seconds = int(seconds)
    minutes=(millis/(1000*60))%60
    minutes = int(minutes)
    hours=(millis/(1000*60*60))%24
    result =("%d:%d:%d" % (hours, minutes, seconds))
    return result

print(TimeConverter(13746338230108684000))
def grafica_semana():
    i =0
    
    datos_semana=[]
    for e in myCamaras.objects.all():
        comparativeDate = 0000
        if (e.serial_camara == serial_camara):
            if(e.fecha==mydate and mydate2== 'Sunday'):
                print(e.serial_camara)
                datos_semana.append(e.zonas_camara[0].nro_personas)
                print(datos_semana)
                datos_semana.append(0)
                datos_semana.append(0)
                datos_semana.append(0)
                datos_semana.append(0)
                datos_semana.append(0)
                datos_semana.append(0)
                datos_semana.append(0)
                datos_semana.append(0)
                datos_semana.append(0)
                return datos_semana
                break
            else:
                myrefDate=mydate1
                while myrefDate.strftime('%A') != 'Sunday':
                    print(myrefDate.strftime('%A'))
                    
                    if not i == 7 :
                        # print(e.zonas_camara[0].nro_personas)
                       
                        if comparativeDate != myrefDate:
                            datos_semana.insert(0,e.zonas_camara[0].nro_personas)
                            
                            print(datos_semana)
                            myrefDate = myrefDate-timedelta(i)
                            comparativeDate = myrefDate
                            print('comparativeDate')
                            print(comparativeDate)
                            print('ingresando el valor:',e.zonas_camara[0].nro_personas, 'del dia:',myrefDate.strftime('%A') )
                            i=i+1
                            
                        else:
                            print('esta fecha se dejo pasar porque ya existe en la grafica')
                            comparativeDate = myrefDate
                           
                       #print("no")
                        


                        if len(datos_semana) <9:
                            print('no')
                            print(datos_semana)
                            datos_semana.append(0)
                            print('resultado final')
                            print(datos_semana)
                            print('resultado final')
                            print(datos_semana)
                            break
                        
                    break

    return datos_semana
                    
                
def grafica_horas():
    now = datetime.now()
    myhora = now.strftime("%H:%M:%S")
    datos_horas=[]
    print(myhora)
    for e in myCamaras.objects.all():
        if (e.serial_camara == serial_camara):
            if(e.fecha==mydate ):
                
                print(e.serial_camara)
                datos_horas.append(e.zonas_camara[0].nro_personas)
                print(datos_horas)
                datos_horas.append(0)
                datos_horas.append(0)
                datos_horas.append(0)
                datos_horas.append(0)
                datos_horas.append(0)
                datos_horas.append(0)
                datos_horas.append(0)
                datos_horas.append(0)
                datos_horas.append(0)
                return datos_horas
                break
            else:
                myrefDate=mydate1
                while myrefDate.strftime('%A') != 'Sunday':
                    print(myrefDate.strftime('%A'))
                    i =0
                    if not i == 6 :
                        # print(e.zonas_camara[0].nro_personas)

                        datos_horas.insert(0,e.zonas_camara[0].nro_personas)

                        print(datos_horas)
                        myrefDate = myrefDate-timedelta(i)


                       #print("no")
                        i=i+1


                        if len(datos_horas) <9:
                            print('no')
                            print(datos_horas)
                            datos_horas.append(0)
                            print('resultado final')
                            print(datos_horas)
                            print('resultado final')
                            print(datos_horas)
                            break
                        
                    break

    return datos_horas

                
            
    

        







def hfs(request):
    context = {'foo': 'bar'}
    return render(request, 'hzfullscreen_bu.html', context)

@login_required(login_url="/login/")
def index(request):
    camarasAll =  Camaras.objects.all()
    
    info_grafica_semana = grafica_semana()
    
    print('info_grafica_semana')
    print(info_grafica_semana)
    formato_hora = ["H","H","H","H","H","H","H","H","H"]
    formato_semana= ["D", "L", "M", "M", "J", "V", "S"]
    info_grafica_horas = grafica_horas()


    url = "https://api.meraki.com/api/v1/devices/Q2HV-B24V-ZKN5/camera/generateSnapshot"
    url2 = "https://api.meraki.com/api/v1/devices/Q2GV-4YBM-YWWJ/camera/generateSnapshot"  

    payload = {}
    headers = {
    'X-Cisco-Meraki-API-Key': '920a310b87feb3832739a79d573845404c6825d0',
    'Content-Type': 'application/json'
    }

    response = {}
    response2 = {}
   
    response = requests.request("POST", url, headers=headers, data = payload)
    response2= requests.request("POST",url2 ,headers=headers, data = payload)

    if(not response and not response2):
            
        extract = "/static/assets/img/people.jpg"
        extract2 = "/static/assets/img/people.jpg"
      
    else:
        urlResponse = json.loads(response.text)
        urlResponse2 = json.loads(response2.text)
        extract = urlResponse.get('url')
        extract2= urlResponse2.get('url')

    return render(request, "index.html",  {'camaras':camarasAll,'url1':extract,'url2':extract2,'info_grafica_semana': info_grafica_semana,'info_grafica_horas':info_grafica_horas})
 

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        load_template = request.path.split('/')[-1]
        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template('error-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'error-500.html' )
        return HttpResponse(html_template.render(context, request))

