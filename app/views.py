from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django import template
from camaras.models import Camaras
from camara_zona.models import CamaraZona
from django.forms.models import model_to_dict
from instalacion.models import Instalacion
from cliente.models import Cliente
from display.models import Display
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
from json import dumps
import re



today = date.today()
mydate = str(today.strftime("%Y-%m-%d"))
mydate1 = datetime.today()

mydate2 = datetime.today().strftime('%A')

serial_camara = "Q2GV-4YBM-YWWJ"



def TimeConverter(millis):
    #si ven este codigo, si se que se puede hacer mucho mas corto pero por razones que desconozco por los momentos no quiere funcionar de esa manera
    tsToString =str(millis)
    #print('tsToString')
    #print(tsToString)
    x=re.split('Timestamp|,',tsToString)
    #print('x')
    #print(x)
    y= x[1]
    #print('y')
    #print(y)
    z=y.split('(')
    #print('z')
    #print(z)
    final =z[1]
    #print('final')
    #print(final)
   #aqui ya obtengo el resultado de ts en milisegundos para convertir a horas convenciales

    lasMillis = int(final)
    #print(lasMillis)
    seconds=(lasMillis/1000)%60
    seconds = int(seconds)
    minutes=(lasMillis/(1000*60))%60
    minutes = int(minutes)
    hours=(lasMillis/(1000*60*60))%24
    result =("%d:%d:%d" % (hours, minutes, seconds))
    
    #print("ts: '",final,"' convertida a hora convencial es: '", result,"'")
    newResult = datetime.strptime(result, '%H:%M:%S')
    return newResult

#print(TimeConverter(13746338230108684000))
def grafica_semana():
    i =0
    
    datos_semana=[]
    dias_semana=[]
    for e in myCamaras.objects.all():
        comparativeDate = 0000
        if (e.serial_camara == serial_camara):
            if(e.fecha==mydate and mydate2== 'Sunday'):
                
                #print(e.serial_camara)
                datos_semana.append(e.zonas_camara[0].nro_personas)
                #print(datos_semana)
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
                    #print(myrefDate.strftime('%A'))
                    
                    if not i == 7 :
                        
                       
                        if str(datetime.strptime(e.fecha,'%Y-%m-%d').strftime('%A')) != str(myrefDate.strftime('%A')):
                           
                            
                            datos_semana.insert(0,e.zonas_camara[0].nro_personas)
                            
                            #print(datos_semana)
                            myrefDate = myrefDate-timedelta(i)
                            comparativeDate = myrefDate
                            #print('comparativeDate')
                            #print(comparativeDate)
                            #print('ingresando el valor:',e.zonas_camara[0].nro_personas, 'del dia:',myrefDate.strftime('%A') )
                            weekday=(myrefDate.strftime('%A'))
                            dias_semana.insert(0,weekday)
                            #print(dias_semana)
                            i=i+1
                            
                        else:
                            #print('se queria ingresar el valor :', e.zonas_camara[0].nro_personas,'del dia:',myrefDate.strftime('%A'))
                           
                            #print('esta fecha se dejo pasar porque ya existe en la grafica')
                            comparativeDate = myrefDate
                           
                       #print("no")
                        


                        if len(datos_semana) <9:
                            #print('no')
                            #print(datos_semana)
                            datos_semana.append(0)
                            #print('resultado final')
                            #print(datos_semana)
                            #print('resultado final')
                            #print(datos_semana)
                            break
                        
                    break

    return datos_semana
                    
                






                
def grafica_horas():
    now = datetime.now()
    #hora de referencia
    myhora = now.strftime("%H:%M:%S")
    #hora que va a decrementar
    myHoraDeecremental = datetime.strptime('00:00:00',"%H:%M:%S")
    #hora indice que aunmenta el decremento
    horaIncremental ='00:00:00'
    #hora de referencia
    myrefHour=datetime.strptime('00:00:00',"%H:%M:%S")
    myrefHour=datetime.strptime('00:00:00',"%H:%M:%S")
    myrefHour1=datetime.strptime('03:00:00',"%H:%M:%S")
    myrefHour2=datetime.strptime('06:00:00',"%H:%M:%S")
    myrefHour3=datetime.strptime('09:00:00',"%H:%M:%S")
    myrefHour4=datetime.strptime('12:00:00',"%H:%M:%S")
    myrefHour5=datetime.strptime('15:00:00',"%H:%M:%S")
    myrefHour6=datetime.strptime('18:00:00',"%H:%M:%S")
    myrefHour7=datetime.strptime('21:00:00',"%H:%M:%S")
    myrefHour8=datetime.strptime('21:59:59',"%H:%M:%S")
    #print('si ves esto sobre una fecha...')
    #print(myrefHour)
    datos_horas=[0,0,0,0,0,0,0,0,0,0]
    #print(myhora)
    for e in myCamaras.objects.all():
        if (e.serial_camara == serial_camara):
            if(e.fecha==mydate ):
                tiempo =(TimeConverter(e.ts))
                if TimeConverter(e.ts) <=myrefHour:
                    
                    #varConverter = TimeConverter(var)
                    #TimeConverter(str(e.ts))
                    datos_horas.insert(0,e.zonas_camara[0].nro_personas)
                    datos_horas.append(0)
                    datos_horas.append(0)
                    datos_horas.append(0)
                    datos_horas.append(0)
                    datos_horas.append(0)
                    datos_horas.append(0)
                    datos_horas.append(0)
                    datos_horas.append(0)
                    datos_horas.append(0)
                    #print('hey----------------se cumplio la primera condicion, esta temprano')
                    
                    #print(varConverter)
                else: 
                    while myHoraDeecremental >= myrefHour:
                        
                        Time = TimeConverter(e.ts)
                        if myHoraDeecremental >= myrefHour and myHoraDeecremental <= myrefHour1:
                            #print('hey----------------se cumplio la segunda y la hora ronda la 1 y las 3')

                            #print(Time)
                            myHoraDeecremental = myHoraDeecremental-timedelta(minutes=10)
                            datos_horas.insert(0,e.zonas_camara[0].nro_personas)
                            #print(myHoraDeecremental)
                            #print('------myrefHour-----')
                            #print(myrefHour)
                            #print('se cumplio resto el valor')
                        #horaIncremental+timedelta('00:10:00')
                        #print(horaIncremental)
                        elif TimeConverter(e.ts) > myrefHour1 and myHoraDeecremental <= myrefHour2:
                            #print('lo que mando a imprimir')
                            #print(TimeConverter(e.ts))
                            #print('hey----------------se cumplio la segunda y la hora ronda la 3 y las 6')
                            datos_horas.insert(1,e.zonas_camara[0].nro_personas)
                            myHoraDeecremental = myHoraDeecremental-timedelta(minutes=10)
                        elif TimeConverter(e.ts) > myrefHour2 and myHoraDeecremental <= myrefHour3:
                            #print('lo que mando a imprimir')
                            #print(TimeConverter(e.ts))
                            #print('hey----------------se cumplio la segunda y la hora ronda la 6 y las 9')
                            datos_horas.insert(2,e.zonas_camara[0].nro_personas)
                            myHoraDeecremental = myHoraDeecremental-timedelta(minutes=10)
                        elif TimeConverter(e.ts) > myrefHour3 and myHoraDeecremental <= myrefHour4:
                            #print('lo que mando a imprimir')
                            #print(TimeConverter(e.ts))
                            #print('hey----------------se cumplio la segunda y la hora ronda la 9 y las 12')
                            myHoraDeecremental = myHoraDeecremental-timedelta(minutes=10)
                            datos_horas.insert(3,e.zonas_camara[0].nro_personas)
                        elif TimeConverter(e.ts) > myrefHour4 and myHoraDeecremental <= myrefHour5:
                            #print('lo que mando a imprimir')
                            #print(TimeConverter(e.ts))
                            
                            #print('hey----------------se cumplio la segunda y la hora ronda la 12 y las 15')
                            myHoraDeecremental = myHoraDeecremental-timedelta(minutes=10)
                            datos_horas.insert(4,e.zonas_camara[0].nro_personas)
                        elif TimeConverter(e.ts) > myrefHour5 and myHoraDeecremental <= myrefHour6:
                            #print('lo que mando a imprimir')
                            #print(TimeConverter(e.ts))
                            #print('hey----------------se cumplio la segunda y la hora ronda la 15 y las 18')
                            myHoraDeecremental = myHoraDeecremental-timedelta(minutes=10)
                            datos_horas.insert(5,e.zonas_camara[0].nro_personas)
                        elif TimeConverter(e.ts) > myrefHour6 and myHoraDeecremental <= myrefHour7:
                            #print('lo que mando a imprimir')
                            #print(TimeConverter(e.ts))
                            #print('hey----------------se cumplio la segunda y la hora ronda la 18 y las 21')
                            myHoraDeecremental = myHoraDeecremental-timedelta(minutes=10)
                            datos_horas.insert(6,e.zonas_camara[0].nro_personas)
                        elif TimeConverter(e.ts) > myrefHour4 and myHoraDeecremental <= myrefHour5:
                            #print('lo que mando a imprimir')
                            #print(TimeConverter(e.ts))
                            #print('hey----------------se cumplio la segunda y la hora ronda la 21 y las 11 y 59')
                            myHoraDeecremental = myHoraDeecremental-timedelta(minutes=10)
                            datos_horas.insert(7,e.zonas_camara[0].nro_personas)
                            
                        else:
                            myHoraDeecremental = myHoraDeecremental-timedelta(minutes=10)

    return datos_horas


@login_required(login_url="/login/")
def index(request):
    camarasAll =  Camaras.objects.all()
    
    info_grafica_semana = grafica_semana()
    
    #print('info_grafica_semana')
    #print(info_grafica_semana)
    formato_hora = ["H","H","H","H","H","H","H","H","H"]
    formato_semana= ["D", "L", "M", "M", "J", "V", "S"]
    info_grafica_horas = grafica_horas()
    #print('info_grafica_horas')
    #print(info_grafica_horas)



    return render(request, "index.html",  {'camaras':camarasAll,'info_grafica_semana': info_grafica_semana,'info_grafica_horas':info_grafica_horas})
 

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



def hfs(request):    
    if hasattr(request.user.profile, 'cliente') and hasattr(request.user.profile.cliente, 'get_id') and (request.user.profile.cliente.get_id() is not None):    
        if hasattr(request.user.profile, 'instalacion') and hasattr(request.user.profile.instalacion, 'get_id') and (request.user.profile.instalacion.get_id() is not None):
            id_instalacion = request.user.profile.instalacion.get_id()
            display = Display.objects.filter(instalacion={'nif_cliente': request.user.profile.cliente.nif} and {'nombre': request.user.profile.instalacion.nombre_comercial}).first()            
            id_display = display.get_id()
        else:
          display = Display.objects.filter(instalacion={'nif_cliente': request.user.profile.cliente.nif}).first()
          id_display = display.get_id()
    else:        
        cliente = Cliente.objects.first()        
        instalacion = Instalacion.objects.filter(cliente={'nif': cliente.nif}).first()
        display = Display.objects.filter(instalacion={'nif_cliente': cliente.nif} and {'nombre': instalacion.nombre_comercial}).first()                
        id_display = display.get_id()


    data = { 
        'embebido':False, 
        'id_display': id_display       
    }     
    dataJSON = dumps(data)    
    return render(request, 'hzfullscreen_bu.html', {'data': dataJSON})

def hfsEmbebido(request):    
    if hasattr(request.user.profile, 'cliente') and hasattr(request.user.profile.cliente, 'get_id') and (request.user.profile.cliente.get_id() is not None):    
        if hasattr(request.user.profile, 'instalacion') and hasattr(request.user.profile.instalacion, 'get_id') and (request.user.profile.instalacion.get_id() is not None):
            id_instalacion = request.user.profile.instalacion.get_id()
            display = Display.objects.filter(instalacion={'nif_cliente': request.user.profile.cliente.nif} and {'nombre': request.user.profile.instalacion.nombre_comercial}).first()            
            id_display = display.get_id()
        else:
          display = Display.objects.filter(instalacion={'nif_cliente': request.user.profile.cliente.nif}).first()
          id_display = display.get_id()   
    else:
        cliente = Cliente.objects.first()        
        instalacion = Instalacion.objects.filter(cliente={'nif': cliente.nif}).first()
        display = Display.objects.filter(instalacion={'nif_cliente': cliente.nif} and {'nombre': instalacion.nombre_comercial}).first()                
        id_display = display.get_id()
     
    
       
    data = { 
        'embebido':True,
        'id_display': id_display        
    } 
    
    
    dataJSON = dumps(data)    
    return render(request, 'hzfullscreen_bu.html', {'data': dataJSON})