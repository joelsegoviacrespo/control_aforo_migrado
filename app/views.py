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
from operator import add
cliente = Cliente.objects.all()

#for e in Cliente.objects.all():
    #print(e.nif)
    

#for e in Instalacion.objects.all():
    #print(e.nombre_comercial)
#for e in Camaras.objects.all():
    
    #print('serial de camaras')
    #print(e.serial_camara)

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
def grafica_semana(mydate, mydate1 ,mydate2,fecha_limite,fecha_limite_minima,seriales):
    #print('indiceeeeeeeeeeeeeeeeeee')
    #print(seriales)
    #print('estoy recibiendo de argumento:',mydate, mydate1 ,mydate2,)
    #mydate = str(today.strftime("%Y-%m-%d"))
    #mydate1 = datetime.today()
    #mydate2 = datetime.today().strftime('%A')
    #print('estoy recibiendo la siguente informacion: mi fecha dereferencia es:',mydate, 'mydate1:' ,mydate1, 'mydate2:', mydate2,'fecha limite:',fecha_limite,'fecha limite minima:',fecha_limite_minima)
    #no me queria funcionar el indice i
    contador= 0
    int(contador)
    dias_semana_total=[0,0,0,0,0,0,0,0,0,0]
    for i in seriales:
        datos_semana=[0,0,0,0,0,0,0,0,0,0]
        varTemporal0= 0000
        varTemporal1= 0000
        varTemporal2= 0000
        varTemporal3= 0000
        varTemporal4= 0000
        varTemporal5= 0000
        varTemporal6= 0000
        myLocalSunday=datetime.strptime(str(mydate), '%Y-%m-%d')
        #print('mylocalsunday')
        #print(myLocalSunday)
        while myLocalSunday.strftime('%A') != 'Sunday':
            myLocalSunday =(myLocalSunday-timedelta(days=1))
            #print(myLocalSunday)
        #print(myLocalSunday)
        for e in myCamaras.objects.all():
            comparativeDate = 0000
            if (e.serial_camara == seriales[contador]):
                if(e.fecha==mydate and mydate2== 'Sunday'):
                    if datetime.strptime(e.fecha, '%Y-%m-%d')  <= fecha_limite and datetime.strptime(e.fecha, '%Y-%m-%d') >= fecha_limite_minima:
                        if datetime.strptime(e.fecha, '%Y-%m-%d').strftime('%A') == 'Sunday' and e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas != varTemporal1 :


                            dias_semana.append(e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                            varTemporal0 = e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas
                            dias_semana.append(0)
                            dias_semana.append(0)
                            dias_semana.append(0)
                            dias_semana.append(0)
                            dias_semana.append(0)
                            dias_semana.append(0)
                            dias_semana.append(0)
                            dias_semana.append(0)
                            dias_semana.append(0)
                            dias_semana.append(0)
                            #print('------------------ esto es la lista en total---', dias_semana, 'de este dia', e.fecha,'este valor',e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                            return dias_semana
                            break

                        else:
                            pass
                        
                        
                        
                else:
                    if datetime.strptime(e.fecha, '%Y-%m-%d')  <= fecha_limite and datetime.strptime(e.fecha, '%Y-%m-%d') >= fecha_limite_minima:
                       # print('fechas segun el rango')
                       # print(e.fecha)


                        if datetime.strptime(e.fecha, '%Y-%m-%d').strftime('%A') == 'Monday' and e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas != varTemporal1 :
                           # print('se agrego al dia lunes el valor',e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                            datos_semana.pop(1)

                            datos_semana.insert(1,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                            varTemporal1 = e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas

                        if (datetime.strptime(e.fecha, '%Y-%m-%d').strftime('%A') == 'Tuesday' and e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas != varTemporal2) and (datetime.strptime(e.fecha, '%Y-%m-%d') >= myLocalSunday):
                            datos_semana.pop(2)

                            datos_semana.insert(2,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                            varTemporal1 = e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas

                        if (datetime.strptime(e.fecha, '%Y-%m-%d').strftime('%A') == 'Thursday' and e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas != varTemporal3) and (datetime.strptime(e.fecha, '%Y-%m-%d') >= myLocalSunday) :
                            datos_semana.pop(3)

                            datos_semana.insert(3,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                            varTemporal1 = e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas

                        if (datetime.strptime(e.fecha, '%Y-%m-%d').strftime('%A') == 'Wednesday' and e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas != varTemporal4) and (datetime.strptime(e.fecha, '%Y-%m-%d') >= myLocalSunday):
                            datos_semana.pop(4)

                            datos_semana.insert(4,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                            varTemporal1 = e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas


                        if (datetime.strptime(e.fecha, '%Y-%m-%d').strftime('%A') == 'Friday' and e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas != varTemporal5)and (datetime.strptime(e.fecha, '%Y-%m-%d') >= myLocalSunday) :
                            datos_semana.pop(5)

                            datos_semana.insert(5,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                            varTemporal1 = e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas

                        if (datetime.strptime(e.fecha, '%Y-%m-%d').strftime('%A') == 'Saturday' and e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas != varTemporal6)and (datetime.strptime(e.fecha, '%Y-%m-%d') >= myLocalSunday) :
                            datos_semana.pop(6)

                            datos_semana.insert(6,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                            varTemporal1 = e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas

                        if (datetime.strptime(e.fecha, '%Y-%m-%d').strftime('%A') == 'Sunday' and e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas != varTemporal0)and (datetime.strptime(e.fecha, '%Y-%m-%d') >= myLocalSunday) :
                            datos_semana.pop(0)
                            #print('se agrego al dia domingo el valor',e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                            datos_semana.insert(0,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                            varTemporal1 = e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas
            dias_semana_total= list( map(add, datos_semana, dias_semana_total) )
            
                
                   
                    
    return dias_semana_total

def grafica_semana_pasada(mydate, mydate1 ,mydate2,fecha_limite,fecha_limite_minima,seriales ):
    #print('estoy recibiendo de argumento:',mydate, mydate1 ,mydate2,)
    #mydate = str(today.strftime("%Y-%m-%d"))
    #mydate1 = datetime.today()
    #mydate2 = datetime.today().strftime('%A')
    #print('semana pasada----------------------------------------')
    #print('estoy recibiendo la siguente informacion: mi fecha dereferencia es:',mydate, 'mydate1:' ,mydate1, 'mydate2:', mydate2,'fecha limite:',fecha_limite,'fecha limite minima:',fecha_limite_minima)
    i =0
   
    dias_semana_total=[0,0,0,0,0,0,0,0,0,0,0]
    contador= 0
    int(contador)
    for i in seriales:
        
        datos_semana=[0,0,0,0,0,0,0,0,0,0]
        varTemporal0= 0000
        varTemporal1= 0000
        varTemporal2= 0000
        varTemporal3= 0000
        varTemporal4= 0000
        varTemporal5= 0000
        varTemporal6= 0000
        while fecha_limite.strftime('%A') != 'Saturday':
            fecha_limite =fecha_limite+timedelta(days=1)
        #print('fecha_limite')

        #print(fecha_limite)

        while fecha_limite_minima.strftime('%A') != 'Sunday':
           fecha_limite_minima =fecha_limite_minima-timedelta(days=1)
        #print('fecha_limite_minima')
        #print(fecha_limite_minima)
        for e in myCamaras.objects.all():
            comparativeDate = 0000
            if (e.serial_camara == seriales[contador]):

                if datetime.strptime(e.fecha, '%Y-%m-%d')  <= fecha_limite :
                   # print('fechas segun el rango')
                   # print(e.fecha)


                    if datetime.strptime(e.fecha, '%Y-%m-%d').strftime('%A') == 'Monday' and e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas != varTemporal1 :
                       # print('se agrego al dia lunes el valor',e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        datos_semana.pop(1)

                        datos_semana.insert(1,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        varTemporal1 = e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas

                    if (datetime.strptime(e.fecha, '%Y-%m-%d').strftime('%A') == 'Tuesday' and e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas != varTemporal2):
                        datos_semana.pop(2)

                        datos_semana.insert(2,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        varTemporal1 = e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas

                    if (datetime.strptime(e.fecha, '%Y-%m-%d').strftime('%A') == 'Thursday' and e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas != varTemporal3):
                        datos_semana.pop(3)

                        datos_semana.insert(3,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        varTemporal1 = e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas

                    if (datetime.strptime(e.fecha, '%Y-%m-%d').strftime('%A') == 'Wednesday' and e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas != varTemporal4):
                        datos_semana.pop(4)

                        datos_semana.insert(4,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        varTemporal1 = e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas

                    if (datetime.strptime(e.fecha, '%Y-%m-%d').strftime('%A') == 'Friday' and e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas != varTemporal5):
                        datos_semana.pop(5)

                        datos_semana.insert(5,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        varTemporal1 = e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas

                    if (datetime.strptime(e.fecha, '%Y-%m-%d').strftime('%A') == 'Saturday' and e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas != varTemporal6):
                        datos_semana.pop(6)

                        datos_semana.insert(6,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        varTemporal1 = e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas

                    if (datetime.strptime(e.fecha, '%Y-%m-%d').strftime('%A') == 'Sunday' and e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas != varTemporal0):
                        datos_semana.pop(0)
                        #print('se agrego al dia domingo el valor',e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        datos_semana.insert(0,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        varTemporal1 = e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas

            dias_semana_total= list( map(add, datos_semana, dias_semana_total) )
        contador=contador+1                
                   
                    
    return dias_semana_total

 
    
def grafica_semana_acumulada(mydate, mydate1 ,mydate2,fecha_limite,fecha_limite_minima,seriales ):
    #print('estoy recibiendo de argumento:',mydate, mydate1 ,mydate2,)
    #mydate = str(today.strftime("%Y-%m-%d"))
    #mydate1 = datetime.today()
    #mydate2 = datetime.today().strftime('%A')
    #print('semana pasada----------------------------------------')
    #print('estoy recibiendo la siguente informacion: mi fecha dereferencia es:',mydate, 'mydate1:' ,mydate1, 'mydate2:', mydate2,'fecha limite:',fecha_limite,'fecha limite minima:',fecha_limite_minima)
    i =0
   
    contador= 0
    int(contador)           
    dias_semana_total=[0,0,0,0,0,0,0,0,0,0]
    for i in seriales:
        datos_semana=[0,0,0,0,0,0,0,0,0,0]
        varTemporal0= 0000
        varTemporal1= 0000
        varTemporal2= 0000
        varTemporal3= 0000
        varTemporal4= 0000
        varTemporal5= 0000
        varTemporal6= 0000
        while fecha_limite.strftime('%A') != 'Saturday':
            fecha_limite =fecha_limite+timedelta(days=1)
        #print('fecha_limite')

        #print(fecha_limite)

        while fecha_limite_minima.strftime('%A') != 'Sunday':
           fecha_limite_minima =fecha_limite_minima-timedelta(days=1)
        #print('fecha_limite_minima')
        #print(fecha_limite_minima)
        for e in myCamaras.objects.all():
            comparativeDate = 0000
            if (e.serial_camara == serial_camara):

                if datetime.strptime(e.fecha, '%Y-%m-%d')  <= fecha_limite :
                   # print('fechas segun el rango')
                   # print(e.fecha)


                    if datetime.strptime(e.fecha, '%Y-%m-%d').strftime('%A') == 'Monday' and e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas != varTemporal1 :
                       # print('se agrego al dia lunes el valor',e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        datos_semana.pop(1)

                        datos_semana.insert(1,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        varTemporal1 = e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas

                    if (datetime.strptime(e.fecha, '%Y-%m-%d').strftime('%A') == 'Tuesday' and e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas != varTemporal2):
                        datos_semana.pop(2)

                        datos_semana.insert(2,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        varTemporal1 = e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas

                    if (datetime.strptime(e.fecha, '%Y-%m-%d').strftime('%A') == 'Thursday' and e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas != varTemporal3):
                        datos_semana.pop(3)

                        datos_semana.insert(3,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        varTemporal1 = e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas

                    if (datetime.strptime(e.fecha, '%Y-%m-%d').strftime('%A') == 'Wednesday' and e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas != varTemporal4):
                        datos_semana.pop(4)

                        datos_semana.insert(4,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        varTemporal1 = e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas

                    if (datetime.strptime(e.fecha, '%Y-%m-%d').strftime('%A') == 'Friday' and e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas != varTemporal5):
                        datos_semana.pop(5)

                        datos_semana.insert(5,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        varTemporal1 = e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas

                    if (datetime.strptime(e.fecha, '%Y-%m-%d').strftime('%A') == 'Saturday' and e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas != varTemporal6):
                        datos_semana.pop(6)

                        datos_semana.insert(6,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        varTemporal1 = e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas

                    if (datetime.strptime(e.fecha, '%Y-%m-%d').strftime('%A') == 'Sunday' and e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas != varTemporal0):
                        datos_semana.pop(0)
                        #print('se agrego al dia domingo el valor',e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        datos_semana.insert(0,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        varTemporal1 = e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas
            dias_semana_total= list( map(add, datos_semana, dias_semana_total) )
            contador=contador+1           
    a=0
    total=0
    for i in datos_semana:
        #print('hola esto se ejecuta')
        if(a == 0):
            #print('primera condicional')
            total =total+ datos_semana[a]
            #print(total)
            a=a+1
            
            total =total+ datos_semana[a]
            #print(total)
            a=a+1
        elif (a>=7):
            #print('segunda condicional')
            #print(a)
           
            
            pass
        else:
            total =total+ datos_semana[a]
            #print(total)
            a=a+1
    #print('semana')
    #print(datos_semana)      
    #print(total)
    return total     
                

def este_mes(mylist):
     #para el primer parametro
    hoy = date.today()
    hoy0= datetime.today()
    hoy1= datetime.today()
    today = date.today()
    newtoday = datetime.today()
    mydate = str(today.strftime("%Y-%m-%d"))
    #mydateA = str(newtoday-timedelta(weeks=2).strtime("%Y-%m-%d"))
    #para esta semana

    mydate1 = datetime.today()
    mydate2 = datetime.today().strftime('%A')
    fecha_limite0 = hoy0
    fecha_limite_minima =(hoy1-timedelta(weeks=2))
    fecha_limite_minima0 =(hoy0-timedelta(weeks=2))
    fecha_limite_minima1 =(hoy0-timedelta(weeks=3))
    fecha_limite_minima2 =(hoy0-timedelta(weeks=5))
    
    
    #para la semana anterior

    hoy0= datetime.today()
    today = date.today()
    newtoday = datetime.today()
    mydate = str(today.strftime("%Y-%m-%d"))
    #mydateA = str(newtoday-timedelta(weeks=2).strftime("%Y-%m-%d"))
    fecha_limite =(hoy1-timedelta(weeks=1))
    fecha_limite1 =(hoy1-timedelta(weeks=2))
    fecha_limite2 =(hoy1-timedelta(weeks=3))
    
    

    
    
    semana_a_restarA = (hoy-timedelta(weeks=1))
    semana_a_restarB = (hoy-timedelta(weeks=2))
    semana_a_restarC = (hoy-timedelta(weeks=3))
    
    

    semana_a_restar_strA = datetime.strptime(str(hoy-timedelta(weeks=1)),"%Y-%m-%d")
    semana_a_restar_strB = datetime.strptime(str(hoy-timedelta(weeks=2)),"%Y-%m-%d")
    semana_a_restar_strC = datetime.strptime(str(hoy-timedelta(weeks=3)),"%Y-%m-%d")
    
    mydate2 = datetime.today().strftime('%A')

    mydate3 = (datetime.today()-timedelta(weeks=1))
    mydate31 =mydate3.strftime('%A')
    mydate4 = (datetime.today()-timedelta(weeks=2))
    mydate41 =mydate4.strftime('%A')
    mydate5 = (datetime.today()-timedelta(weeks=3))
    mydate51 = mydate5.strftime('%A')
    
    



    esteMes=[]  

    esteMes.append(grafica_semana_acumulada(mydate, mydate1 ,mydate2,fecha_limite0,fecha_limite_minima0,mylist))
   
    #print('result1')
    #print(grafica_semana_acumulada(mydate, mydate1 ,mydate2,fecha_limite0,fecha_limite_minima0))
    esteMes.append(grafica_semana_acumulada(semana_a_restarA, semana_a_restar_strA,mydate31,fecha_limite,fecha_limite_minima,mylist))
    
    #print('result2')
    #print( grafica_semana_acumulada(semana_a_restarA, semana_a_restar_strA,mydate31,fecha_limite,fecha_limite_minima))
    esteMes.append(grafica_semana_acumulada(semana_a_restarB, semana_a_restar_strB,mydate41,fecha_limite1,fecha_limite_minima1,mylist))
    #print('result3')
    #print(    grafica_semana_acumulada(semana_a_restarB, semana_a_restar_strB,mydate41,fecha_limite1,fecha_limite_minima1)
#)
    esteMes.append(grafica_semana_acumulada(semana_a_restarC, semana_a_restar_strC,mydate51,fecha_limite2,fecha_limite_minima2,mylist))
    
    #print('result4')
    #print(grafica_semana_acumulada(semana_a_restarC, semana_a_restar_strC,mydate51,fecha_limite2,fecha_limite_minima2))
    #print('este mes-----')
    #print(esteMes)
    return esteMes

def mes_pasado(mylist):
     #para el primer parametro
    hoy = date.today()
    
    hoy1= datetime.today()
    today = date.today()
    newtoday = datetime.today()
    mydate = str(today.strftime("%Y-%m-%d"))
    #mydateA = str(newtoday-timedelta(weeks=2).strtime("%Y-%m-%d"))
    #para esta semana

    mydate1 = datetime.today()
    mydate2 = datetime.today().strftime('%A')
    
    fecha_limite_minima =(hoy1-timedelta(weeks=6))
    fecha_limite_minima1 =(hoy1-timedelta(weeks=7))
    fecha_limite_minima2 =(hoy1-timedelta(weeks=8))
    fecha_limite_minima3 =(hoy1-timedelta(weeks=9))
    
    #para la semana anterior

    hoy0= datetime.today()
    today = date.today()
    newtoday = datetime.today()
    
    #mydateA = str(newtoday-timedelta(weeks=2).strftime("%Y-%m-%d"))
    fecha_limite =(hoy1-timedelta(weeks=5))
    fecha_limite1 =(hoy1-timedelta(weeks=6))
    fecha_limite2 =(hoy1-timedelta(weeks=7))
    fecha_limite3 =(hoy1-timedelta(weeks=8))
    
    

    
    semana_a_restar = (hoy-timedelta(weeks=5))
    semana_a_restarA = (hoy-timedelta(weeks=6))
    semana_a_restarB = (hoy-timedelta(weeks=7))
    semana_a_restarC = (hoy-timedelta(weeks=8))
    
    
    semana_a_restar_str = datetime.strptime(str(hoy-timedelta(weeks=5)),"%Y-%m-%d")
    semana_a_restar_strA = datetime.strptime(str(hoy-timedelta(weeks=6)),"%Y-%m-%d")
    semana_a_restar_strB = datetime.strptime(str(hoy-timedelta(weeks=7)),"%Y-%m-%d")
    semana_a_restar_strC = datetime.strptime(str(hoy-timedelta(weeks=8)),"%Y-%m-%d")

    mydate = str(today.strftime("%Y-%m-%d"))
    mydate2 = (datetime.today()-timedelta(weeks=5))
    mydate21 = mydate2.strftime('%A')
    mydate3 = (datetime.today()-timedelta(weeks=6))
    mydate31 =mydate3.strftime('%A')
    mydate4 = (datetime.today()-timedelta(weeks=7))
    mydate41 =mydate4.strftime('%A')
    mydate5 = (datetime.today()-timedelta(weeks=8))
    mydate51 = mydate5.strftime('%A')
    
    



    mesPasado=[]  

    mesPasado.append(grafica_semana_acumulada(semana_a_restar, semana_a_restar_str,mydate21,fecha_limite,fecha_limite_minima,mylist))
    mesPasado.append(grafica_semana_acumulada(semana_a_restarA, semana_a_restar_strA,mydate31,fecha_limite1,fecha_limite_minima1,mylist))
    mesPasado.append(grafica_semana_acumulada(semana_a_restarB, semana_a_restar_strB,mydate41,fecha_limite2,fecha_limite_minima2,mylist))
    #print('result de hace 7 semanas')
    var = grafica_semana_acumulada(semana_a_restarB, semana_a_restar_strB,mydate41,fecha_limite2,fecha_limite_minima2,mylist)
    #print('se va a ejecutar la iteracion que me da problemas')
    #print(grafica_semana_acumulada(semana_a_restarB, semana_a_restar_strB,mydate41,fecha_limite2,fecha_limite_minima2))
    #print(var)
    mesPasado.append(grafica_semana_acumulada(semana_a_restarC, semana_a_restar_strC,mydate51,fecha_limite3,fecha_limite_minima3,mylist))
    
    #print('----------resultado del mes pasado del la septima semana-----')
    #print(var)

    return mesPasado



myHoraDeecremental = datetime.strptime('00:00:00',"%H:%M:%S")
#print(myHoraDeecremental)
myHoraDeecremental = myHoraDeecremental-timedelta(minutes=10)
#print('Hora decremental de prueba')
#print(myHoraDeecremental)
#if myHoraDeecremental ==  datetime.strptime('23:50:00',"%H:%M:%S"):
    #print('se cumple la condicional')
#else:
    #print('no se cumplio')
    
def grafica_horas(mydate):
    varTemporal1 = 0
    varTemporal2 = 0
    varTemporal3 = 0
    varTemporal4 = 0
    varTemporal5 = 0
    varTemporal6 = 0
    varTemporal7 = 0
    varTemporal8 = 0
    #print('se esta ejecutandoooooooooooooooooooooo')
    now = datetime.now()
    #hora de referencia
    myhora = now.strftime("%H:%M:%S")
    #hora que va a decrementar
    myHoraDeecremental = datetime.strptime('23:00:00',"%H:%M:%S")
    #hora indice que aunmenta el decremento
    horaIncremental ='00:00:00'
    #hora de referencia
    #myrefHour=datetime.strptime('23:59:59',"%H:%M:%S")
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
    datos_horas_acumuladas=[1,2,3,4,5,6,7]
    #print(myhora)
    for e in myCamaras.objects.all():
        
        if (e.serial_camara == serial_camara):
            
            if(e.fecha==mydate ):
                #print('se esta ejecutandoooooooooooooooooooooo')
                #print(e.zonas_camara[0].nro_personas)
                tiempo =(TimeConverter(e.ts))
                
                if TimeConverter(e.ts) <=myrefHour1 and  TimeConverter(e.ts)> myrefHour8:
                    #print('se esta ejecutando la primera condicional')
                    
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
                   
                    #while myHoraDeecremental >= myrefHour:
                    #for i in datos_horas_acumuladas:
                    
                    #print(e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                    if TimeConverter(e.ts) >= myrefHour and TimeConverter(e.ts) <= myrefHour1:
                        #print('hey----------------se cumplio la segunda y la hora ronda la 1 y las 3')
                        #print(Time)
                        if varTemporal1 != (e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas):
                            datos_horas.pop(0)
                            myHoraDeecremental = myHoraDeecremental-timedelta(minutes=10)
                            datos_horas.insert(0,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                            varTemporal1 = e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas
                        else:
                            pass
                        
                    #horaIncremental+timedelta('00:10:00')
                    #print(horaIncremental)
                    if TimeConverter(e.ts) > myrefHour1 and TimeConverter(e.ts) <= myrefHour2:
                        
                        #print('hey----------------se cumplio la segunda y la hora ronda la 3 y las 6')
                        if varTemporal2 != (e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas):
                            datos_horas.pop(1)
                            datos_horas.insert(1,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                            myHoraDeecremental = myHoraDeecremental-timedelta(minutes=10)
                            varTemporal2 = e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas
                            
                        else:
                            pass
                        
                        

                    if TimeConverter(e.ts) > myrefHour2 and TimeConverter(e.ts) <= myrefHour3:
                        
                        #print('hey----------------se cumplio la segunda y la hora ronda la 6 y las 9')
                        if varTemporal3 != (e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas):
                            datos_horas.pop(2)
                            datos_horas.insert(2,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                            myHoraDeecremental = myHoraDeecremental-timedelta(minutes=10)
                            varTemporal3 = e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas
                            
                        else:
                            pass
                    if TimeConverter(e.ts) > myrefHour3 and TimeConverter(e.ts) <= myrefHour4:
                        
                        #print('hey----------------se cumplio la segunda y la hora ronda la 9 y las 12')
                        if varTemporal4 != (e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas):
                            myHoraDeecremental = myHoraDeecremental-timedelta(minutes=10)
                            
                            
                            datos_horas.pop(3)
                            datos_horas.insert(3,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                            varTemporal4 = e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas
                        else:
                            pass
                    if TimeConverter(e.ts) > myrefHour4 and TimeConverter(e.ts) <= myrefHour5:
                        
                        
                        #print('hey----------------se cumplio la segunda y la hora ronda la 12 y las 15')
                        if varTemporal5 != (e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas):
                            myHoraDeecremental = myHoraDeecremental-timedelta(minutes=10)
                            datos_horas.pop(4)
                            datos_horas.insert(4,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                            
                            varTemporal5 = e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas
                        else:
                            pass
                    if TimeConverter(e.ts) > myrefHour5 and TimeConverter(e.ts) <= myrefHour6:
                        
                        #print('hey----------------se cumplio la segunda y la hora ronda la 15 y las 18')
                        if varTemporal6 != (e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas):
                            myHoraDeecremental = myHoraDeecremental-timedelta(minutes=10)
                            datos_horas.pop(5)
                            datos_horas.insert(5,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                            
                            varTemporal6 = e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas
                        else:
                            pass
                    if TimeConverter(e.ts) > myrefHour6 and TimeConverter(e.ts) <= myrefHour7:
                       
                        #print('hey----------------se cumplio la segunda y la hora ronda la 18 y las 21')
                        if varTemporal7 != (e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas):
                            myHoraDeecremental = myHoraDeecremental-timedelta(minutes=10)
                            datos_horas.pop(6)
                            datos_horas.insert(6,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                            
                            varTemporal7 = e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas
                        else:
                            pass
                    if TimeConverter(e.ts) > myrefHour7 and TimeConverter(e.ts) <= myrefHour8:
                        
                        #print('hey----------------se cumplio la segunda y la hora ronda la 21 y las 11 y 59')
                        if varTemporal8 != (e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas):
                            myHoraDeecremental = myHoraDeecremental-timedelta(minutes=10)
                            datos_horas.pop(7)
                            datos_horas.insert(7,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                            
                            varTemporal8 = e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas
                        else:
                            pass
                        
                    else:
                        #print('no se cumplieron ningunas de las anteriores')
                        myHoraDeecremental = myHoraDeecremental-timedelta(minutes=10)
            
    return datos_horas
        

        
def grafica_horas_acumuladas(mydate):
    
    varTemporal1 = 0
    varTemporal2 = 0
    varTemporal3 = 0
    varTemporal4 = 0
    varTemporal5 = 0
    varTemporal6 = 0
    varTemporal7 = 0
    varTemporal8 = 0
    #print('se esta ejecutandoooooooooooooooooooooo')
    now = datetime.now()
    #hora de referencia
    myhora = now.strftime("%H:%M:%S")
    #hora que va a decrementar
    myHoraDeecremental = datetime.strptime('23:00:00',"%H:%M:%S")
    #hora indice que aunmenta el decremento
    horaIncremental ='00:00:00'
    #hora de referencia
    #myrefHour=datetime.strptime('23:59:59',"%H:%M:%S")
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
    
    
    i=0
    #print(myhora)
    for e in myCamaras.objects.all():
        
        if (e.serial_camara == serial_camara):
            
            if(e.fecha==mydate ):
                #print('se esta ejecutandoooooooooooooooooooooo')
                #print(e.zonas_camara[0].nro_personas)
                tiempo =(TimeConverter(e.ts))
                
                if TimeConverter(e.ts) <=myrefHour1 and  TimeConverter(e.ts)> myrefHour8:
                    #print('se esta ejecutando la primera condicional')
                    
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
                   
                    #while myHoraDeecremental >= myrefHour:
                    #for i in datos_horas_acumuladas:
                    
                    #print(e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                    if TimeConverter(e.ts) >= myrefHour and TimeConverter(e.ts) <= myrefHour1:
                        #print('hey----------------se cumplio la segunda y la hora ronda la 1 y las 3')
                        #print(Time)
                        if varTemporal1 != (e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas):
                            datos_horas.pop(0)
                            myHoraDeecremental = myHoraDeecremental-timedelta(minutes=10)
                            datos_horas.insert(0,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                            varTemporal1 = e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas
                        else:
                            pass
                        
                    #horaIncremental+timedelta('00:10:00')
                    #print(horaIncremental)
                    if TimeConverter(e.ts) > myrefHour1 and TimeConverter(e.ts) <= myrefHour2:
                        
                        #print('hey----------------se cumplio la segunda y la hora ronda la 3 y las 6')
                        if varTemporal2 != (e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas):
                            datos_horas.pop(1)
                            datos_horas.insert(1,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                            myHoraDeecremental = myHoraDeecremental-timedelta(minutes=10)
                            varTemporal2 = e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas
                            
                        else:
                            pass
                        
                        

                    if TimeConverter(e.ts) > myrefHour2 and TimeConverter(e.ts) <= myrefHour3:
                        
                        #print('hey----------------se cumplio la segunda y la hora ronda la 6 y las 9')
                        if varTemporal3 != (e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas):
                            datos_horas.pop(2)
                            datos_horas.insert(2,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                            myHoraDeecremental = myHoraDeecremental-timedelta(minutes=10)
                            varTemporal3 = e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas
                            
                        else:
                            pass
                    if TimeConverter(e.ts) > myrefHour3 and TimeConverter(e.ts) <= myrefHour4:
                        
                        #print('hey----------------se cumplio la segunda y la hora ronda la 9 y las 12')
                        if varTemporal4 != (e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas):
                            myHoraDeecremental = myHoraDeecremental-timedelta(minutes=10)
                            
                            
                            datos_horas.pop(3)
                            datos_horas.insert(3,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                            varTemporal4 = e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas
                        else:
                            pass
                    if TimeConverter(e.ts) > myrefHour4 and TimeConverter(e.ts) <= myrefHour5:
                        
                        
                        #print('hey----------------se cumplio la segunda y la hora ronda la 12 y las 15')
                        if varTemporal5 != (e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas):
                            myHoraDeecremental = myHoraDeecremental-timedelta(minutes=10)
                            datos_horas.pop(4)
                            datos_horas.insert(4,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                            
                            varTemporal5 = e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas
                        else:
                            pass
                    if TimeConverter(e.ts) > myrefHour5 and TimeConverter(e.ts) <= myrefHour6:
                        
                        #print('hey----------------se cumplio la segunda y la hora ronda la 15 y las 18')
                        if varTemporal6 != (e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas):
                            myHoraDeecremental = myHoraDeecremental-timedelta(minutes=10)
                            datos_horas.pop(5)
                            datos_horas.insert(5,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                            
                            varTemporal6 = e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas
                        else:
                            pass
                    if TimeConverter(e.ts) > myrefHour6 and TimeConverter(e.ts) <= myrefHour7:
                       
                        #print('hey----------------se cumplio la segunda y la hora ronda la 18 y las 21')
                        if varTemporal7 != (e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas):
                            myHoraDeecremental = myHoraDeecremental-timedelta(minutes=10)
                            datos_horas.pop(6)
                            datos_horas.insert(6,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                            
                            varTemporal7 = e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas
                        else:
                            pass
                    if TimeConverter(e.ts) > myrefHour7 and TimeConverter(e.ts) <= myrefHour8:
                        
                        #print('hey----------------se cumplio la segunda y la hora ronda la 21 y las 11 y 59')
                        if varTemporal8 != (e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas):
                            myHoraDeecremental = myHoraDeecremental-timedelta(minutes=10)
                            datos_horas.pop(7)
                            datos_horas.insert(7,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                            
                            varTemporal8 = e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas
                        else:
                            pass
                        
                    else:
                        #print('no se cumplieron ningunas de las anteriores')
                        myHoraDeecremental = myHoraDeecremental-timedelta(minutes=10)
    datos_horas_acumuladas=[]
    a=0
    #print('datos horas')
    #print(datos_horas)
    for i in datos_horas:
        #print('hola esto se ejecuta')
        if(a == 0):
            #print('primera condicional')

            #print(a)
            datos_horas_acumuladas.append(datos_horas[a])
            #print(datos_horas_acumuladas)
            a=a+1
        elif (a>7):
           # print('segunda condicional')
           # #print(a)
            #print(datos_horas_acumuladas)
            
            pass
        else:
           # print('tercera condicional')
            #print(a)
            datos_horas_acumuladas.append(datos_horas[a]+datos_horas_acumuladas[a-1])
           # print(datos_horas_acumuladas)
            a=a+1
        #print(datos_horas_acumuladas)    

    return datos_horas_acumuladas


#print(grafica_horas_acumuladas(mydate))
@login_required(login_url="/login/")
def index(request):

    


    #argumentos ordenados
    #para el primer parametro
    hoy = date.today()
    today = date.today()
    mydate = str(today.strftime("%Y-%m-%d"))

    semana_a_restar = (hoy-timedelta(weeks=1))
    #para el segundo parametro
    mydate1 = datetime.today()

    semana_a_restar_str = datetime.strptime(str(hoy-timedelta(weeks=1)),"%Y-%m-%d")
    #para el tercer parametro
    mydate2 = datetime.today().strftime('%A')

    mydate3 = (datetime.today()-timedelta(weeks=1)).strftime('%A')
    #para el cuarto parametro
    hoy0= datetime.today()
    hoy1= datetime.today()
    #para el quinto parametro
    fecha_limite_minima0 =(hoy0-timedelta(weeks=1))
    fecha_limite_minima1 =(hoy1-timedelta(weeks=1))
     
    '''for e in Cliente.objects.all():
        if(Cliente.objects.filter(nif=request.user.profile.cliente.nif).first() is not None ):

            display = Cliente.objects.filter(nif=request.user.profile.cliente.nif).first()            
            id_display = e.nif
            print('que imprime esto')
            print(request.user.profile.cliente.nif)'''
    
    mySerial=[]
    for e in Cliente.objects.all():
        if(Cliente.objects.filter(nif=request.user.profile.cliente.nif).first() is not None ):
            id_display = e.nif
           
           
            for i in Instalacion.objects.all():
                for o in Camaras. objects.all():
                    #print('pasa algo')
                    if (Instalacion.objects.filter(cliente__startswith={'nif': request.user.profile.cliente.nif}) is not None):
                        if(i.cliente.nif ==request.user.profile.cliente.nif):
                        #display = Instalacion.objects.filter(nif=id_display).first()            
            
                            #print('----------que imprime esto--------------------')
                            #print(request.user.profile.cliente.nif)
                            MyInstalacion= i.nombre_comercial
                            #print(MyInstalacion)
                        else:
                            #print('***************************no se parece')
                            pass

                    
                        if (Camaras.objects.filter(instalacion__startswith={'nombre': MyInstalacion}) is not None):
                            #print('intalacion.nombre',o.instalacion.nombre,'mi instalacion var',MyInstalacion )
                           
                            if str(o.instalacion.nombre) == MyInstalacion:
                                #print('------tenemos una camara con esas caracteristicas')
                                mySerial.append(o.serial_camara)
                    #else:
                        #print('no encontro nada--------------------')
    #print('el serial es:')
    mylist=list(dict.fromkeys(mySerial))
    #print(mylist)
    
    
    
    fecha_limite0 = hoy0
    fecha_limite =(hoy1-timedelta(weeks=1))

    camarasAll =  Camaras.objects.all()
    #print(mydate2)
    info_grafica_semana = grafica_semana(mydate, mydate1 ,mydate2,fecha_limite0,fecha_limite_minima0,mylist)
    
    info_grafica_semana_pasada = grafica_semana_pasada(semana_a_restar, semana_a_restar_str,mydate3,fecha_limite,fecha_limite_minima1,mylist)
    
    #print('info_grafica_semana')
    #print(info_grafica_semana)
    formato_hora = ["H","H","H","H","H","H","H","H","H"]
    formato_semana= ["D", "L", "M", "M", "J", "V", "S"]
    info_grafica_horas = grafica_horas(mydate)
    #print('INFO DE GRAFICAS DE ESTA SEMANA Y LASIGUIENTE')
   # print(info_grafica_semana)
   # print('---------------------grafica semana pasada--------------------------------')
   # print( grafica_semana(semana_a_restar, semana_a_restar_str,mydate3,fecha_limite,fecha_limite_minima1))
    #print('-----------fin grafica pasada----------------------------')
    info_grafica_horas_acumulado= grafica_horas_acumuladas(mydate)
    #print('info_grafica_horas')
    #print(info_grafica_horas)
    #print('info a imprimir mosca raull')
   # print('---------------------grafica semanal--------------------------------')
    #print(grafica_semana(mydate, mydate1 ,mydate2,fecha_limite0,fecha_limite_minima0))
    #print('---------------------grafica semanal acumulada--------------------------------')
    #print(grafica_semana_acumulada(mydate, mydate1 ,mydate2,fecha_limite0,fecha_limite_minima0))
    esteMes = este_mes(mylist)
    #print('-----------------este mes---------------------')
    #print(este_mes())
    #print('-------------------mes pasado----------------')
    #print(mes_pasado())
    mesPasado = mes_pasado(mylist)
    return render(request, "index.html",  {'camaras':camarasAll,'info_grafica_semana': info_grafica_semana,'info_grafica_horas':info_grafica_horas,'info_grafica_horas_acumulado':info_grafica_horas_acumulado,'info_grafica_semana_pasada':info_grafica_semana_pasada,'estemes':esteMes,'mespasado':mesPasado})
 

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

@login_required(login_url="/login/")
def pitarnfo(request):
    
    today = date.today()
    mydate = str(today.strftime("%Y-%m-%d"))
    mydate1 = datetime.today()

    mydate2 = datetime.today().strftime('%A')
    
    info_grafica_horas = grafica_horas()
    info_grafica_horas_acumulado= grafica_horas_acumuladas(mydate)
    info_grafica_semana = grafica_semana(mydate, mydate1 ,mydate2)
    
    return render(request, "index_base.html",  {'info_grafica_semana': info_grafica_semana,'info_grafica_horas':info_grafica_horas,'info_grafica_horas_acumulado':info_grafica_horas_acumulado})

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