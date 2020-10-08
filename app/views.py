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
import Constantes
from calendar import monthrange


serial_camara = "Q2GV-4YBM-YWWJ"

def TimeConverter(millis):
    #si ven este codigo, si se que se puede hacer mucho mas corto pero por razones que desconozco por los momentos no quiere funcionar de esa manera
    tsToString =str(millis)
    x=re.split('Timestamp|,',tsToString)
    y= x[1]
    z=y.split('(')
    final =z[1]
    lasMillis = int(final)
    #print(lasMillis)
    seconds=(lasMillis/1000)%60
    seconds = int(seconds)
    minutes=(lasMillis/(1000*60))%60
    minutes = int(minutes)
    hours=(lasMillis/(1000*60*60))%24
    result =("%d:%d:%d" % (hours, minutes, seconds))
    newResult = datetime.strptime(result, '%H:%M:%S')
    return newResult

def grafica_semana(mydate, mydate1 ,mydate2,fecha_limite,fecha_limite_minima,seriales):
    #print('la fecha actual es',mydate2)
    
    #print('indiceeeeeeeeeeeeeeeeeee')
    #print(seriales)
    #print('estoy recibiendo de argumento:',mydate, mydate1 ,mydate2,)
    #mydate = str(today.strftime("%Y-%m-%d"))
    #mydate1 = datetime.today()
    #mydate2 = datetime.today().strftime('%A')
   # print('estoy recibiendo la siguente informacion: mi fecha dereferencia es:',mydate, 'mydate1:' ,mydate1, 'mydate2:', mydate2,'fecha limite:',fecha_limite,'fecha limite minima:',fecha_limite_minima)
    #no me queria funcionar el indice i
    contador= 0
    int(contador)
    #filtro del limite de la semana
    if fecha_limite_minima.strftime('%A') == 'Saturday' and datetime.strptime(mydate, '%Y-%m-%d').strftime('%A') == 'Saturday':
        while fecha_limite_minima <= datetime.strptime(mydate, '%Y-%m-%d'):
            fecha_limite_minima =fecha_limite_minima+timedelta(days=1)
            #print(fecha_limite_minima)

    else:
        while fecha_limite_minima.strftime('%A') != 'Sunday':
            fecha_limite_minima =fecha_limite_minima+timedelta(days=1)
            #print('fecha_limite_minima')
            #print(fecha_limite_minima)
    




    dias_semana_total=[0,0,0,0,0,0,0,0,0,0]
    for i in seriales:
        dias_semana=[0,0,0,0,0,0,0]
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
                if(mydate2== 'Sunday'):
                    #print('la fecha del documento es:',e.fecha , 'y la de referencia es:',mydate)
                    if(str(e.fecha)==str(mydate) ):
                       
                        
                        if datetime.strptime(e.fecha, '%Y-%m-%d')  <= fecha_limite and datetime.strptime(e.fecha, '%Y-%m-%d') >= fecha_limite_minima:
                            
                            if datetime.strptime(e.fecha, '%Y-%m-%d').strftime('%A') == 'Sunday' and e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas != varTemporal1 :
                                


                                dias_semana.append(e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)

                                #print('esto viene de ese documento',e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas, 'de la fecha',e.fecha, 'con el id', e._id)
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
                                print(dias_semana)
                                #print('------------------ esto es la lista en total---', dias_semana, 'de este dia', e.fecha,'este valor',e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                                return dias_semana

                                

                            else:
                                pass
                        
                else:
                   
                    if datetime.strptime(e.fecha, '%Y-%m-%d')  <= fecha_limite and datetime.strptime(e.fecha, '%Y-%m-%d') >= fecha_limite_minima:
                       # print('fechas segun el rango')
                       # print(e.fecha)


                        if datetime.strptime(e.fecha, '%Y-%m-%d').strftime('%A') == 'Monday' and e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas != varTemporal1 :
                           # print('se agrego al dia lunes el valor',e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                            dias_semana.pop(1)

                            dias_semana.insert(1,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                            varTemporal1 = e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas

                        if (datetime.strptime(e.fecha, '%Y-%m-%d').strftime('%A') == 'Tuesday' and e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas != varTemporal2) and (datetime.strptime(e.fecha, '%Y-%m-%d') >= myLocalSunday):
                            dias_semana.pop(2)

                            dias_semana.insert(2,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                            varTemporal1 = e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas

                        if (datetime.strptime(e.fecha, '%Y-%m-%d').strftime('%A') == 'Thursday' and e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas != varTemporal3) and (datetime.strptime(e.fecha, '%Y-%m-%d') >= myLocalSunday) :
                            dias_semana.pop(3)

                            dias_semana.insert(3,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                            varTemporal1 = e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas

                        if (datetime.strptime(e.fecha, '%Y-%m-%d').strftime('%A') == 'Wednesday' and e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas != varTemporal4) and (datetime.strptime(e.fecha, '%Y-%m-%d') >= myLocalSunday):
                            dias_semana.pop(4)

                            dias_semana.insert(4,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                            varTemporal1 = e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas


                        if (datetime.strptime(e.fecha, '%Y-%m-%d').strftime('%A') == 'Friday' and e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas != varTemporal5)and (datetime.strptime(e.fecha, '%Y-%m-%d') >= myLocalSunday) :
                            dias_semana.pop(5)

                            dias_semana.insert(5,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                            varTemporal1 = e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas

                        if (datetime.strptime(e.fecha, '%Y-%m-%d').strftime('%A') == 'Saturday' and e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas != varTemporal6)and (datetime.strptime(e.fecha, '%Y-%m-%d') >= myLocalSunday) :
                            dias_semana.pop(6)

                            dias_semana.insert(6,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                            varTemporal1 = e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas

                        if (datetime.strptime(e.fecha, '%Y-%m-%d').strftime('%A') == 'Sunday' and e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas != varTemporal0)and (datetime.strptime(e.fecha, '%Y-%m-%d') >= myLocalSunday) :
                            dias_semana.pop(0)
                            #print('se agrego al dia domingo el valor',e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                            datos_semana.insert(0,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                            varTemporal1 = e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas
            else:
                pass
            #print(dias_semana)
            dias_semana_total= list( map(add, dias_semana, dias_semana_total) )
                         
    return dias_semana_total

def grafica_semana_actual_acumulada(mydate, mydate1 ,mydate2,fecha_limite,fecha_limite_minima,seriales):
    datos_semana_acumuladas= grafica_semana(mydate, mydate1 ,mydate2,fecha_limite,fecha_limite_minima,seriales)
    datosSemana=[]
    a=0
    today = date.today()
    nw=today.weekday()
    if nw == 6:
        nw= -1
    #print(nw)
    diaDeHoy = (int(today.strftime("%d")))
    for i in datos_semana_acumuladas:
        
        if(a == 0):
            #print('primera condicional')

           
            datosSemana.append(datos_semana_acumuladas[a])
           
            a=a+1
        elif (a>nw+1):
        
            
            pass
        else:
           
            datosSemana.append(datos_semana_acumuladas[a]+datosSemana[a-1])
           
            a=a+1

    #print(datosSemana)      
                   
                    
    return datosSemana


def esteMesActual(seriales):
    #inicio el array
    
    #obtengo la cantidad de dias por mes
    
    today = date.today()
    weekDay,myMonthrange=monthrange(int(today.strftime("%Y")), int(today.strftime("%m")))
    #obtengo el dia de hoy
    diaDeHoy = (int(today.strftime("%d")))

    #print(int(today.strftime("%Y")))
    #print(int(today.strftime("%m")))
    
    #print(myMonthrange)
    #print("el dia de hoy tiene esta cantidad de dias en su mes", myMonthrange)
    #una vez obtenida la cantidad de dias de este me se hacen las condicionales respectivas

    switch_casos = {
	31: dias31(today,seriales),
	30: dias30(today,seriales),
	29: dias29(today,seriales),
	28: dias28(today,seriales),
    }
    esteMes = switch_casos.get(myMonthrange,default())
    #print ('total')
    #print (esteMes)
    #alamcenar lo que retorne en una variable y retornarla
    datosMes=[]
    a=0
    
    for i in esteMes:
        if(a == 0):
            #print('primera condicional')
            datosMes.append(esteMes[a])
            a=a+1
        elif (a>diaDeHoy-1):
            pass
        else:   
            datosMes.append(esteMes[a])  
            a=a+1
    #print(datosMes)
    return datosMes

def esteMesAcumulado(seriales):
    #inicio el array
    
    #obtengo la cantidad de dias por mes
    
    today = date.today()
    weekDay,myMonthrange=monthrange(int(today.strftime("%Y")), int(today.strftime("%m")))
    #obtengo el dia de hoy
    diaDeHoy = (int(today.strftime("%d")))

    #print(int(today.strftime("%Y")))
    #print(int(today.strftime("%m")))
    
    #print(myMonthrange)
    #print("el dia de hoy tiene esta cantidad de dias en su mes", myMonthrange)
    #una vez obtenida la cantidad de dias de este me se hacen las condicionales respectivas

    switch_casos = {
	31: dias31(today,seriales),
	30: dias30(today,seriales),
	29: dias29(today,seriales),
	28: dias28(today,seriales),
    }
    esteMes = switch_casos.get(myMonthrange,default())
    #print ('total')
    #print (esteMes)
    #alamcenar lo que retorne en una variable y retornarla
    datosSemanaAcum=[]
    a=0
    
    for i in esteMes:
        if(a == 0):
           # print('primera condicional')
            datosSemanaAcum.append(esteMes[a])
            a=a+1
        elif (a>diaDeHoy-1):
            pass
        else:
            datosSemanaAcum.append(esteMes[a]+datosSemanaAcum[a-1])
            a=a+1
    #print(datosSemanaAcum)
    return datosSemanaAcum



def dias31(today,seriales):
    contador= 0
    int(contador)
    
    datos_semana_total=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in seriales:
        datos_semana=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for e in myCamaras.objects.all():
            #print('fecha e')
            #separar la fecha para usar el mes
            if e.fecha is not None :
                fechaASeparar = str(e.fecha)
                separado=    fechaASeparar.split('-')
                #print('fecha a separar')
                #print(separado)
                date = separado[1]
                
            else:
                pass

              
            comparative = str(today.strftime("%m"))
           # print('fecha',date, 'a comparar', comparative)
            if (e.serial_camara == seriales[contador] and date !=0):
                #print(seriales[contador])
                if date == comparative:
                    #obtener el dia de esa fecha 
                    diaASeparar =str(e.fecha)
                    diaSeparado = diaASeparar.split('-')
                    dia = diaSeparado[2]
                    #aqui se filtra por dias
                    if(int(dia)==1):
                        datos_semana.insert(0,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                    elif(int(dia)==2):
                       # print('esto pasa')
                        datos_semana.insert(1,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==3):
                        datos_semana.insert(2,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==4):
                        datos_semana.insert(3,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==5):
                        datos_semana.insert(4,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==6):
                        datos_semana.insert(5,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==7):
                        datos_semana.insert(6,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==8):
                        datos_semana.insert(7,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==9):
                        datos_semana.insert(8,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                       # print(datos_semana)
                    elif(int(dia)==10):
                        datos_semana.insert(9,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==11):
                        datos_semana.insert(10,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==12):
                        datos_semana.insert(11,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==13):
                        datos_semana.insert(12,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==14):
                        datos_semana.insert(13,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==15):
                        datos_semana.insert(14,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==16):
                        datos_semana.insert(15,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==17):
                        datos_semana.insert(16,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==18):
                        datos_semana.insert(17,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==19):
                        datos_semana.insert(18,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==20):
                        datos_semana.insert(19,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==21):
                        datos_semana.insert(20,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==22):
                        datos_semana.insert(21,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==23):
                        datos_semana.insert(22,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==24):
                        datos_semana.insert(23,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==25):
                        datos_semana.insert(24,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==26):
                        datos_semana.insert(25,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==27):
                        datos_semana.insert(26,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==28):
                        datos_semana.insert(27,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==29):
                        datos_semana.insert(28,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==30):
                        datos_semana.insert(29,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==31):
                        datos_semana.insert(30,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                else:
                    #print(datos_semana)
                    pass
            total= list( map(add, datos_semana, datos_semana_total) )
            
        contador=contador+1
            
    #print('total')
    #print(total)   
    return total   
   
def dias30(today,seriales):
    contador= 0
    int(contador)
    
    datos_semana_total=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in seriales:
        datos_semana=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for e in myCamaras.objects.all():
            #print('fecha e')
            #separar la fecha para usar el mes
            if e.fecha is not None :
                fechaASeparar = str(e.fecha)
                separado=    fechaASeparar.split('-')
                #print('fecha a separar')
                #print(separado)
                date = separado[1]
                
            else:
                pass

              
            comparative = str(today.strftime("%m"))
            #print('fecha',date, 'a comparar', comparative)
            if (e.serial_camara == seriales[contador] and date !=0):
                #print(seriales[contador])
                if date == comparative:
                    #obtener el dia de esa fecha 
                    diaASeparar =str(e.fecha)
                    diaSeparado = diaASeparar.split('-')
                    dia = diaSeparado[2]
                    #aqui se filtra por dias
                    if(int(dia)==1):
                        datos_semana.insert(0,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                    elif(int(dia)==2):
                        #print('esto pasa')
                        datos_semana.insert(1,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==3):
                        datos_semana.insert(2,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==4):
                        datos_semana.insert(3,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==5):
                        datos_semana.insert(4,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==6):
                        datos_semana.insert(5,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==7):
                        datos_semana.insert(6,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==8):
                        datos_semana.insert(7,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==9):
                        datos_semana.insert(8,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==10):
                        datos_semana.insert(9,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==11):
                        datos_semana.insert(10,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==12):
                        datos_semana.insert(11,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==13):
                        datos_semana.insert(12,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==14):
                        datos_semana.insert(13,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==15):
                        datos_semana.insert(14,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==16):
                        datos_semana.insert(15,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==17):
                        datos_semana.insert(16,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==18):
                        datos_semana.insert(17,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==19):
                        datos_semana.insert(18,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                       # print(datos_semana)
                    elif(int(dia)==20):
                        datos_semana.insert(19,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==21):
                        datos_semana.insert(20,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==22):
                        datos_semana.insert(21,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==23):
                        datos_semana.insert(22,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==24):
                        datos_semana.insert(23,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==25):
                        datos_semana.insert(24,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==26):
                        datos_semana.insert(25,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==27):
                        datos_semana.insert(26,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==28):
                        datos_semana.insert(27,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==29):
                        datos_semana.insert(28,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==30):
                        datos_semana.insert(29,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    
                else:
                   # print(datos_semana)
                    pass
            total= list( map(add, datos_semana, datos_semana_total) )
            
        contador=contador+1
            
    #print('total')
    #print(total)   
    return total   

def dias29(today,seriales):
    contador= 0
    int(contador)
    
    datos_semana_total=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in seriales:
        datos_semana=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for e in myCamaras.objects.all():
            #print('fecha e')
            #separar la fecha para usar el mes
            if e.fecha is not None :
                fechaASeparar = str(e.fecha)
                separado=    fechaASeparar.split('-')
                #print('fecha a separar')
                #print(separado)
                date = separado[1]
                
            else:
                pass

              
            comparative = str(today.strftime("%m"))
            #print('fecha',date, 'a comparar', comparative)
            if (e.serial_camara == seriales[contador] and date !=0):
                #print(seriales[contador])
                if date == comparative:
                    #obtener el dia de esa fecha 
                    diaASeparar =str(e.fecha)
                    diaSeparado = diaASeparar.split('-')
                    dia = diaSeparado[2]
                    #aqui se filtra por dias
                    if(int(dia)==1):
                        datos_semana.insert(0,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                    elif(int(dia)==2):
                        #print('esto pasa')
                        datos_semana.insert(1,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==3):
                        datos_semana.insert(2,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==4):
                        datos_semana.insert(3,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==5):
                        datos_semana.insert(4,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==6):
                        datos_semana.insert(5,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==7):
                        datos_semana.insert(6,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==8):
                        datos_semana.insert(7,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==9):
                        datos_semana.insert(8,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==10):
                        datos_semana.insert(9,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==11):
                        datos_semana.insert(10,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==12):
                        datos_semana.insert(11,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==13):
                        datos_semana.insert(12,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                       #print(datos_semana)
                    elif(int(dia)==14):
                        datos_semana.insert(13,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==15):
                        datos_semana.insert(14,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==16):
                        datos_semana.insert(15,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==17):
                        datos_semana.insert(16,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==18):
                        datos_semana.insert(17,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==19):
                        datos_semana.insert(18,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==20):
                        datos_semana.insert(19,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==21):
                        datos_semana.insert(20,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==22):
                        datos_semana.insert(21,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==23):
                        datos_semana.insert(22,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==24):
                        datos_semana.insert(23,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==25):
                        datos_semana.insert(24,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==26):
                        datos_semana.insert(25,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==27):
                        datos_semana.insert(26,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==28):
                        datos_semana.insert(27,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==29):
                        datos_semana.insert(28,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    
                else:
                    #print(datos_semana)
                    pass
            total= list( map(add, datos_semana, datos_semana_total) )
            
        contador=contador+1
            
    #print('total')
    #print(total)   
    return total   

def dias28(today,seriales):
    contador= 0
    int(contador)
    
    datos_semana_total=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in seriales:
        datos_semana=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for e in myCamaras.objects.all():
            #print('fecha e')
            #separar la fecha para usar el mes
            if e.fecha is not None :
                fechaASeparar = str(e.fecha)
                separado=    fechaASeparar.split('-')
                #print('fecha a separar')
                #print(separado)
                date = separado[1]
                
            else:
                pass

              
            comparative = str(today.strftime("%m"))
            #print('fecha',date, 'a comparar', comparative)
            if (e.serial_camara == seriales[contador] and date !=0):
                #print(seriales[contador])
                if date == comparative:
                    #obtener el dia de esa fecha 
                    diaASeparar =str(e.fecha)
                    diaSeparado = diaASeparar.split('-')
                    dia = diaSeparado[2]
                    #aqui se filtra por dias
                    if(int(dia)==1):
                        datos_semana.insert(0,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                    elif(int(dia)==2):
                        #print('esto pasa')
                        datos_semana.insert(1,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==3):
                        datos_semana.insert(2,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==4):
                        datos_semana.insert(3,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==5):
                        datos_semana.insert(4,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==6):
                        datos_semana.insert(5,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==7):
                        datos_semana.insert(6,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==8):
                        datos_semana.insert(7,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                       # print(datos_semana)
                    elif(int(dia)==9):
                        datos_semana.insert(8,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==10):
                        datos_semana.insert(9,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==11):
                        datos_semana.insert(10,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==12):
                        datos_semana.insert(11,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==13):
                        datos_semana.insert(12,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==14):
                        datos_semana.insert(13,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==15):
                        datos_semana.insert(14,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==16):
                        datos_semana.insert(15,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==17):
                        datos_semana.insert(16,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==18):
                        datos_semana.insert(17,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==19):
                        datos_semana.insert(18,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==20):
                        datos_semana.insert(19,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==21):
                        datos_semana.insert(20,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==22):
                        datos_semana.insert(21,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==23):
                        datos_semana.insert(22,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==24):
                        datos_semana.insert(23,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==25):
                        datos_semana.insert(24,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==26):
                        datos_semana.insert(25,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==27):
                        datos_semana.insert(26,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    elif(int(dia)==28):
                        datos_semana.insert(27,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                        #print(datos_semana)
                    
                else:
                    #print(datos_semana)
                    pass
            total= list( map(add, datos_semana, datos_semana_total) )
            
        contador=contador+1
            
    #print('total')
    #print(total)   
    return total   
def default():
    print('')
    




myHoraDeecremental = datetime.strptime('00:00:00',"%H:%M:%S")
#print(myHoraDeecremental)
myHoraDeecremental = myHoraDeecremental-timedelta(minutes=10)
#print('Hora decremental de prueba')
#print(myHoraDeecremental)
if myHoraDeecremental ==  datetime.strptime('23:50:00',"%H:%M:%S"):
    pass
    #print('se cumple la condicional')
else:
    pass
    #print('no se cumplio')
    
    
# HORAS---------------------------------------------------------------------------------------------------------------------
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
        
#HORAS ACUMULADAS--------------------------------------------------------------------------------------------------------------------------------
        
def grafica_horas_acumuladas(mydate):
    datosHoras=[]
    datos_horas_acumuladas = grafica_horas(mydate)
    now = datetime.now()
    #hora de referencia
    myhora = now.strftime("%H:%M:%S")
    myHoraDeecremental = datetime.strptime(myhora,"%H:%M:%S").time()
    #print(myHoraDeecremental)
    #horas de referencia para comparar
    myrefHour=datetime.strptime('00:00:00',"%H:%M:%S").time()
    myrefHour1=datetime.strptime('03:00:00',"%H:%M:%S").time()
    myrefHour2=datetime.strptime('06:00:00',"%H:%M:%S").time()
    myrefHour3=datetime.strptime('09:00:00',"%H:%M:%S").time()
    myrefHour4=datetime.strptime('12:00:00',"%H:%M:%S").time()
    myrefHour5=datetime.strptime('15:00:00',"%H:%M:%S").time()
    myrefHour6=datetime.strptime('18:00:00',"%H:%M:%S").time()
    myrefHour7=datetime.strptime('21:00:00',"%H:%M:%S").time()
    myrefHour8=datetime.strptime('21:59:59',"%H:%M:%S").time()
    nw=3
    #print(myHoraDeecremental, '      ',myrefHour)
    if (myHoraDeecremental >= myrefHour and myHoraDeecremental < myrefHour1):
        nw = 1
    elif (myHoraDeecremental >= myrefHour1 and myHoraDeecremental < myrefHour2):
        nw =2
    elif (myHoraDeecremental >= myrefHour2 and myHoraDeecremental < myrefHour3):
        nw = 3
        #print('se estan comparando')
    elif (myHoraDeecremental >= myrefHour3 and myHoraDeecremental < myrefHour4):
        nw = 4
    elif (myHoraDeecremental >= myrefHour4 and myHoraDeecremental < myrefHour5):
        nw = 5
        #print('se estan comparando')
    elif (myHoraDeecremental >= myrefHour5 and myHoraDeecremental < myrefHour6):
        nw = 6
        #print('se estan comparando')
    elif (myHoraDeecremental >= myrefHour6 and myHoraDeecremental < myrefHour7):
        nw = 7
        #print('se estan comparando')
    elif (myHoraDeecremental >= myrefHour7 and myHoraDeecremental < myrefHour8):
        nw = 8
    
    a=0
    for i in datos_horas_acumuladas:
        
        if(a == 0):
            #print('primera condicional')

           
            datosHoras.append(datos_horas_acumuladas[a])
           
            a=a+1
        elif (a>nw+1):
        
            
            pass
        else:
           
            datosHoras.append(datos_horas_acumuladas[a]+datosHoras[a-1])
           
            a=a+1
    #print('datosHoras')
   # print(datosHoras)
    return datosHoras


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
    if (request.user.profile.rol== Constantes.SUPERUSUARIO):
        mySerial=['Q2GV-4YBM-YWWJ']
        mylist= mySerial

       
    else:
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
                                print('***************************no se parece')
                                pass
                            
                            if (Camaras.objects.filter(instalacion__startswith={'nombre': MyInstalacion}) is not None):
                                #print('intalacion.nombre',o.instalacion.nombre,'mi instalacion var',MyInstalacion )
                                if str(o.instalacion.nombre) == MyInstalacion:
                                    #print('------tenemos una camara con esas caracteristicas')
                                    mySerial.append(o.serial_camara)
                        else:
                            print('no encontro nada--------------------')
        #print('el serial es:')
        mylist=list(dict.fromkeys(mySerial))
        #print(mylist)
    
    
    
    fecha_limite0 = hoy0
    fecha_limite =(hoy1-timedelta(weeks=1))

    camarasAll =  Camaras.objects.all()
 
    #info_grafica_semana = grafica_semana(mydate, mydate1 ,mydate2,fecha_limite0,fecha_limite_minima0,mylist)
    
    #info_grafica_semana_pasada = grafica_semana_pasada(semana_a_restar, semana_a_restar_str,mydate3,fecha_limite,fecha_limite_minima1,mylist)
    
    #----------------Para las graficas de la tarjeta superior derecha (HOY)------------------
    info_grafica_horas = grafica_horas(mydate)
    info_grafica_horas_acumulado= grafica_horas_acumuladas(mydate)
    #----------------Para las graficas de la tarjeta superior derecha (ESTA SEMANA)------------------
    info_grafica_semana = grafica_semana(mydate, mydate1 ,mydate2,fecha_limite0,fecha_limite_minima0,mylist)
    info_grafica_semana_acumulada = grafica_semana_actual_acumulada(mydate, mydate1 ,mydate2,fecha_limite0,fecha_limite_minima0,mylist)
    #-------------Para las graficas de la tarjeta superior derecha (ESTE MES)------------------------
    MyesteMesAcumulado = esteMesAcumulado(mylist)
    esteMes = esteMesActual(mylist)
    
    

    return render(request, "index.html",  {'camaras':camarasAll,'info_grafica_semana': info_grafica_semana,'info_grafica_horas':info_grafica_horas,'info_grafica_horas_acumulado':info_grafica_horas_acumulado,'info_grafica_semana_acumulada':info_grafica_semana_acumulada,'estemes':esteMes,'estemesacumulado':MyesteMesAcumulado})
 

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
def home(request):
    #print('HEEEEEEEEEEEEEEY')
    hoy = date.today()
    today = date.today()
    mydate = str((today-timedelta(weeks=1)).strftime("%Y-%m-%d"))

    info_grafica_horas = [1,2,3,4,5,6,7,8]
    info_grafica_horas_acumulado= grafica_horas_acumuladas(mydate)

    info_grafica_semana=[1,2,3,4,5,6,7]
    info_grafica_semana_acumulada=[1,2,3,4,5,6,7]
    esteMes=[1,2,3,4,5,6,7,8,9,10,11,12,13,15,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    MyesteMesAcumulado=[1,2,3,4,5,6,7,8,9,10,11,12,13,15,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    return_sub_array = {'info_grafica_horas':info_grafica_horas,'info_grafica_horas_acumulado':info_grafica_horas_acumulado,' info_grafica_semana': info_grafica_semana,'info_grafica_semana_acumulada':info_grafica_semana_acumulada,'estemes':esteMes,'estemesacumulado':MyesteMesAcumulado}
            
    
    return HttpResponse( json.dumps(return_sub_array))


@login_required(login_url="/login/")
def hello(request):
    return HttpResponse('Hello World!')
#--------------------------------Informacion Para index_base.html



@login_required(login_url="/login/")
def pitarnfo(request):
    if (request.user.profile.rol== Constantes.SUPERUSUARIO):
        mySerial=['Q2GV-4YBM-YWWJ']
        mylist= mySerial

       
    else:
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
                                   # print('------tenemos una camara con esas caracteristicas')
                                    mySerial.append(o.serial_camara)
                        else:
                            #print('no encontro nada--------------------')
                            pass
        #print('el serial es:')
        mylist=list(dict.fromkeys(mySerial))
        #print(mylist)

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
    fecha_limite0 =(hoy0)


    today = date.today()
    mydate = str(today.strftime("%Y-%m-%d"))
    mydate1 = datetime.today()
    mydate2 = datetime.today().strftime('%A')

    #graficas horas y horas acumuladas para las tarjeta Inferiores-----------------------------------------------------------------
    info_grafica_horas = grafica_horas(mydate)
    info_grafica_horas_acumulado= grafica_horas_acumuladas(mydate)
    #------------------------------------------------------------------------------------------------------------------------------
   
    #------------------------------------------------------------------------------------------------------------------------------
    info_grafica_semana_acumulada = grafica_semana_actual_acumulada(mydate, mydate1 ,mydate2,fecha_limite0,fecha_limite_minima0,mylist)
    #print('info grafica de la semana acumulada-----------------------------------------------------------------------------------------')
    #print(info_grafica_semana_acumulada)
    
  
    return render(request, "index_base.html",  {'info_grafica_horas':info_grafica_horas,'info_grafica_horas_acumulado':info_grafica_horas_acumulado,'info_grafica_semana_acumulada':info_grafica_semana_acumulada})






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