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
from camaras_historico.models import CamarasHistorico
from datetime import date
from datetime import datetime, timedelta
from json import dumps
import re
from operator import add
import Constantes
from calendar import monthrange
from Fecha import Fecha
import simplejson as simplejson
from usuarios_red.models import UsuariosRed
from jornada_laboral.models import JornadaLaboral

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
    return 0

def grafica_semana2(mydate, mydate1 ,mydate2,fecha_limite,fecha_limite_minima,seriales):
    #print('la fecha actual es',mydate2)
    mySerials=[]
    e= 0
    if (type(seriales )is list):
        for i in seriales:
            aux = seriales[e]
            mySerials.append(aux)
            
            #print(mySerials)
            e=e +1 
    else:
        
        mySerials.append(seriales)
        #print(seriales)
        
    
  
       




 
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
    for i in mySerials:
        #print("se está ejecutando este cilco for el primero")
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
            #print("se está ejecutando este cilco for el SEGUNDO")
            comparativeDate = 0000
            if (e.serial_camara == mySerials[contador]):
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
                                
                                #print('------------------ esto es la lista en total---', dias_semana, 'de este dia', e.fecha,'este valor',e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                                return dias_semana

                                

                            else:
                                pass
                        
                else:
                    #print("primera condicional")
                    if datetime.strptime(e.fecha, '%Y-%m-%d')  <= fecha_limite and datetime.strptime(e.fecha, '%Y-%m-%d') >=  myLocalSunday:
                       # print('fechas segun el rango')
                       # print(e.fecha)
                        #print("segunda condicional")

                        if datetime.strptime(e.fecha, '%Y-%m-%d').strftime('%A') == 'Monday' and e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas != varTemporal1 :
                            #print("esta guardando datos"+ str(e.zonas_camara[0].nro_personas) + "en lunes")
                            # print('se agrego al dia lunes el valor',e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                            dias_semana.pop(1)

                            dias_semana.insert(1,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                            varTemporal1 = e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas

                        if (datetime.strptime(e.fecha, '%Y-%m-%d').strftime('%A') == 'Tuesday' and e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas != varTemporal2) :
                            dias_semana.pop(2)
                            
                            #print("esta guardando datos"+ str(e.zonas_camara[0].nro_personas) + "en martes")
                            dias_semana.insert(2,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                            varTemporal1 = e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas

                        if (datetime.strptime(e.fecha, '%Y-%m-%d').strftime('%A') == 'Thursday' and e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas != varTemporal3)  :
                            dias_semana.pop(3)
                           
                            #print("esta guardando datos"+ str(e.zonas_camara[0].nro_personas) + "en miercoles")
                            dias_semana.insert(3,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                            varTemporal1 = e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas

                        if (datetime.strptime(e.fecha, '%Y-%m-%d').strftime('%A') == 'Wednesday' and e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas != varTemporal4) :
                            dias_semana.pop(4)
                            #print("esta guardando datos"+ str(e.zonas_camara[0].nro_personas) + "en jueves")
                            dias_semana.insert(4,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                            varTemporal1 = e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas


                        if (datetime.strptime(e.fecha, '%Y-%m-%d').strftime('%A') == 'Friday' and e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas != varTemporal5):
                            dias_semana.pop(5)
                            #print("esta guardando datos"+ str(e.zonas_camara[0].nro_personas) + "en viernes")
                            dias_semana.insert(5,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                            varTemporal1 = e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas

                        if (datetime.strptime(e.fecha, '%Y-%m-%d').strftime('%A') == 'Saturday' and e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas != varTemporal6) :
                            dias_semana.pop(6)
                            #print("esta guardando datos"+ str(e.zonas_camara[0].nro_personas) + "en sabado")
                            dias_semana.insert(6,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                            varTemporal1 = e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas

                        if (datetime.strptime(e.fecha, '%Y-%m-%d').strftime('%A') == 'Sunday' and e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas != varTemporal0):
                            #print("esta guardando datos"+ str(e.zonas_camara[0].nro_personas) + "en domingo")
                            dias_semana.pop(0)
                            #print('se agrego al dia domingo el valor',e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                            dias_semana.insert(0,e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas)
                            varTemporal1 = e.zonas_camara[0].nro_personas + e.zonas_camara[1].nro_personas
            else:
                pass
            #print(dias_semana)
            dias_semana_total= list( map(add, dias_semana, dias_semana_total) )
        #print("dias_semana_total000000000000000000000000000000000000")
        #print(dias_semana_total)
    return dias_semana_total


    
def grafica_semana_actual_acumulada(mydate, mydate1 ,mydate2,fecha_limite,fecha_limite_minima,seriales):
        return []
def grafica_semana_actual_acumulada2(mydate, mydate1 ,mydate2,fecha_limite,fecha_limite_minima,seriales):
    datos_semana_acumuladas= grafica_semana(mydate, mydate1 ,mydate2,fecha_limite,fecha_limite_minima,seriales)
    
    datosSemana=[]
    
    a=0

    today = date.today()
    myLocalDate = str(today.strftime("%Y-%m-%d"))
    nw=today.weekday()

    if (mydate != myLocalDate):
        #print('no es el dia de hoy')
        nw= 5
    else:
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

def esteMesActual(seriales, mydate, boolean):
    return []
def esteMesActual2(seriales, mydate, boolean):
    #inicio el array
    today = date.today()
    i = 0
    aux = 0
    myLocalDate = str(today.strftime("%m"))
    fechaAComparar = datetime.strptime(mydate, '%Y-%m-%d')
    ready = str(fechaAComparar.strftime("%m"))
    
    if (myLocalDate != ready and boolean == True ):
        
 
        if(i == aux):
            i=i+1
            date_time_obj = datetime.strptime(mydate, '%Y-%m-%d')
            #obtengo la cantidad de dias por mes
            weekDay,myMonthrange=monthrange(int(date_time_obj.strftime("%Y")),int(date_time_obj.strftime("%m")))
         
            dateToFunction(today-timedelta(month=i))
        else:
            myLocalDate = ready
            aux = i

    elif(myLocalDate != ready and boolean == False ):
        
        if(i == aux):
            i=i+1
            date_time_obj = datetime.strptime(mydate, '%Y-%m-%d')
            #obtengo la cantidad de dias por mes
            weekDay,myMonthrange=monthrange(int(date_time_obj.strftime("%Y")),int(date_time_obj.strftime("%m")))
            
            dateToFunction(today+timedelta(month=i))
        else:
            myLocalDate = ready
            aux = i     

    else:
         
        today = date.today()
        weekDay,myMonthrange=monthrange(int(today.strftime("%Y")), int(today.strftime("%m")))
        #obtengo e l dia de hoy
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

def esteMesAcumulado(seriales,mydate,state):
    return []
def esteMesAcumulado2(seriales,mydate,state):
    #inicio el array
    date_time_obj = datetime.strptime(mydate, '%Y-%m-%d')
    #obtengo la cantidad de dias por mes
    NWeekDay,NMonthRange=monthrange(int(date_time_obj.strftime("%Y")),int(date_time_obj.strftime("%m")))
    
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
    defecto = ""
    




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
    return [0,0,0,0,0,0,0,0,0,0]
def grafica_horas2(mydate):
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
    return []        
def grafica_horas_acumuladas2(mydate):
    today = date.today()
    myLocalDate = str(today.strftime("%Y-%m-%d"))
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
    if(mydate == myLocalDate ):
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
    else:
        
        nw=8
    
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
    #print(datosHoras)
    return datosHoras


#print(grafica_horas_acumuladas(mydate))
@login_required(login_url="/login/")
def index(request):
    
    #TODO: Orientarlo a un cliente en particular
    camarasAll =  Camaras.objects.all()    
    fecha_actual = Fecha.getFechaActual().strftime("%d-%m-%Y")
    
    info_grafica_semana = grafica_semana("", "" ,"","","","")
    info_grafica_semana_acumulada = grafica_semana_actual_acumulada("", "" ,"","","","")    
    esteMes = esteMesActual("","","")    
    MyesteMesAcumulado = esteMesAcumulado("","","")           
    info_grafica_horas = grafica_horas("")    
    info_grafica_horas_acumulado= grafica_horas_acumuladas("")    
    datosDevolver=  {'camaras':camarasAll,"fecha_actual":fecha_actual,'info_grafica_semana': info_grafica_semana,'info_grafica_horas':info_grafica_horas,'info_grafica_horas_acumulado':info_grafica_horas_acumulado,'info_grafica_semana_acumulada':info_grafica_semana_acumulada,'estemes':esteMes,'estemesacumulado':MyesteMesAcumulado}
    return render(request, "index.html",datosDevolver )

@login_required(login_url="/login/")
def index2(request):

 


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
        mySerial=['Q2GV-4YBM-YWWJ','Q2HV-B24V-ZKN5']
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
                                print('')
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
 
    #info_grafica_semana = grafica_semana(mydate, mydate1 ,mydate2,fecha_limite0,fecha_limite_minima0,mylist)
    
    #info_grafica_semana_pasada = grafica_semana_pasada(semana_a_restar, semana_a_restar_str,mydate3,fecha_limite,fecha_limite_minima1,mylist)
    
    #----------------Para las graficas de la tarjeta superior derecha (HOY)------------------
    info_grafica_horas = grafica_horas(mydate)
    info_grafica_horas_acumulado= grafica_horas_acumuladas(mydate)
    #----------------Para las graficas de la tarjeta superior derecha (ESTA SEMANA)------------------
    info_grafica_semana = grafica_semana(mydate, mydate1 ,mydate2,fecha_limite0,fecha_limite_minima0,mylist)
    info_grafica_semana_acumulada = grafica_semana_actual_acumulada(mydate, mydate1 ,mydate2,fecha_limite0,fecha_limite_minima0,mylist)
    #-------------Para las graficas de la tarjeta superior derecha (ESTE MES)------------------------
    
    esteMes = esteMesActual(mylist,mydate,1)
    MyesteMesAcumulado = esteMesAcumulado(mylist,mydate,1)  
    indice = 0
    
    datosDevolver=  {'camaras':camarasAll,'info_grafica_semana': info_grafica_semana,'info_grafica_horas':info_grafica_horas,'info_grafica_horas_acumulado':info_grafica_horas_acumulado,'info_grafica_semana_acumulada':info_grafica_semana_acumulada,'estemes':esteMes,'estemesacumulado':MyesteMesAcumulado}
    #de ejemplo
    mylist=['Q2GV-4YBM-YWWJ','Q2HV-B24V-ZKN5']
    if len(mylist) > 1:
        for i in mylist:
            info_camara1=grafica_semana(mydate, mydate1 ,mydate2,fecha_limite0,fecha_limite_minima0,mylist[indice])
            info_grafica_semana_acumulada1 = grafica_semana_actual_acumulada(mydate, mydate1 ,mydate2,fecha_limite0,fecha_limite_minima0,mylist[indice])
            #print('info camara a agragar al diccionario')
            #print(info_camara1)
            #nombre = "infocamara" + str(indice)
            #nombre1 ="infocamaraAcumulada"+ str(indice)
            #globals() [nombre] = info_camara1
            #globals() [nombre1]= info_grafica_semana_acumulada1

            #print("infocamara" + str(indice))
            datosDevolver["infocamara" + str(indice)] = grafica_semana(mydate, mydate1 ,mydate2,fecha_limite0,fecha_limite_minima0,mylist[indice])
            #print( grafica_semana(mydate, mydate1 ,mydate2,fecha_limite0,fecha_limite_minima0,mylist[indice]))
            #print(grafica_semana_actual_acumulada(mydate, mydate1 ,mydate2,fecha_limite0,fecha_limite_minima0,mylist[indice]))

            datosDevolver["infocamaraAcumulada"+str(indice)]=grafica_semana_actual_acumulada(mydate, mydate1 ,mydate2,fecha_limite0,fecha_limite_minima0,mylist[indice])
            indice = indice+1
    else:
         for i in mylist:
            info_camara1=grafica_semana(mydate, mydate1 ,mydate2,fecha_limite0,fecha_limite_minima0,mylist[indice])
            info_grafica_semana_acumulada1 = grafica_semana_actual_acumulada(mydate, mydate1 ,mydate2,fecha_limite0,fecha_limite_minima0,mylist[indice])
            #print('info camara a agragar al diccionario')
            #print(info_camara1)
            #nombre = "infocamara" + str(indice)
            #nombre1 ="infocamaraAcumulada"+ str(indice)
            #globals() [nombre] = info_camara1
            #globals() [nombre1]= info_grafica_semana_acumulada1

            #print("infocamara" + str(indice))
            datosDevolver["infocamara" + str(indice)] = grafica_semana(mydate, mydate1 ,mydate2,fecha_limite0,fecha_limite_minima0,mylist[indice])
            #print( grafica_semana(mydate, mydate1 ,mydate2,fecha_limite0,fecha_limite_minima0,mylist[indice]))
            #print(grafica_semana_actual_acumulada(mydate, mydate1 ,mydate2,fecha_limite0,fecha_limite_minima0,mylist[indice]))

            datosDevolver["infocamaraAcumulada"+str(indice)]=grafica_semana_actual_acumulada(mydate, mydate1 ,mydate2,fecha_limite0,fecha_limite_minima0,mylist[indice])
            indice = indice+1

            datosDevolver["infocamara1"]=[0,0,0,0,0,0,0,0,0,0]
            datosDevolver["infocamaraAcumulada1"]=[0,0,0,0,0,0,0,0,0,0]


    #grafica_semana(mydate, mydate1 ,mydate2,fecha_limite0,fecha_limite_minima0,mylist[indice])
   
    #print (datosDevolver)
    
 


    

    return render(request, "index.html",datosDevolver )
 

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




indiceTiempo=0 
@login_required(login_url="/login/")
def back(request):
    print("back@@@@@@@@@@@@@@@@@")
    global indiceTiempo
    print("indiceTiempo INICIAL: ",indiceTiempo)
    indiceTiempo = indiceTiempo -1
    indiceTiempoNP= abs(indiceTiempo)
    print("indiceTiempoNP: ",indiceTiempoNP)

    mySerial=['Q2GV-4YBM-YWWJ']
    mylist= mySerial


    hoy = date.today()
    hoy0= datetime.today()
    hoy1= datetime.today()
    today = date.today()
    mydate = str((today-timedelta(days=indiceTiempoNP)).strftime("%Y-%m-%d"))
    mydateToShow = str((today-timedelta(days=indiceTiempoNP)).strftime("%d-%m-%Y"))
    mydate1 = (datetime.today()-timedelta(days=indiceTiempoNP))
    mydate2 = (datetime.today()-timedelta(days=indiceTiempoNP)).strftime('%A')
    fecha_limite0 = hoy0-timedelta(days=indiceTiempoNP)
    fecha_limite_minima0 =(hoy0-timedelta(days=indiceTiempo))
    fecha_limite_minima1 =(hoy1-timedelta(days=indiceTiempo))
    
    fecha_limite =(hoy1-timedelta(days=indiceTiempo))


    info_grafica_horas = grafica_horas(mydate)
    info_grafica_horas_acumulado= grafica_horas_acumuladas(mydate)



    info_grafica_semana= grafica_semana(mydate, mydate1 ,mydate2,fecha_limite0,fecha_limite_minima0,mylist)
    info_grafica_semana_acumulada= grafica_semana_actual_acumulada(mydate, mydate1 ,mydate2,fecha_limite0,fecha_limite_minima0,mylist)


    esteMes= esteMesActual(mylist,mydate,False)
  
    MyesteMesAcumulado= esteMesAcumulado(mylist,mydate,False)
    #print(info_grafica_horas)
    #print(info_grafica_horas_acumulado)
    #print('HOLAAAAAAAAAAAAAAAAAAA')
    #print( info_grafica_horas)
    #print(info_grafica_horas_acumulado)
    

    fecha = mydateToShow
    
    return_sub_array = {'info_grafica_horas':info_grafica_horas,'info_grafica_horas_acumulado':info_grafica_horas_acumulado,' info_grafica_semana': info_grafica_semana,'info_grafica_semana_acumulada':info_grafica_semana_acumulada,'estemes':esteMes,'estemesacumulado':MyesteMesAcumulado,'fecha':fecha}
    #print('return_sub_array')
    #print(return_sub_array)
    return HttpResponse( json.dumps(return_sub_array))

@login_required(login_url="/login/")
def ahead(request):
    global indiceTiempo    
    print("indiceTiempo: ",indiceTiempo)
    indiceTiempo = indiceTiempo +1
    print("indiceTiempo2: ",indiceTiempo)
    indiceTiempoNP= abs(indiceTiempo)   
    mySerial=['Q2GV-4YBM-YWWJ']
    mylist= mySerial    
    hoy = date.today()
    hoy0= datetime.today()
    hoy1= datetime.today()
    today = date.today()
    mydate = str((today+timedelta(days=indiceTiempoNP)).strftime("%Y-%m-%d"))
    mydateToShow = str((today+timedelta(days=indiceTiempoNP)).strftime("%d-%m-%Y"))
    mydate1 = (datetime.today()+timedelta(days=indiceTiempoNP))
    mydate2 = (datetime.today()+timedelta(days=indiceTiempoNP)).strftime('%A')
    fecha_limite0 = hoy0-timedelta(days=indiceTiempoNP)
    fecha_limite_minima0 =(hoy0+timedelta(days=indiceTiempo))
    fecha_limite_minima1 =(hoy1+timedelta(days=indiceTiempo))

    fecha_limite =(hoy1-timedelta(days=indiceTiempo))   
    info_grafica_horas = grafica_horas(mydate)
    info_grafica_horas_acumulado= grafica_horas_acumuladas(mydate)  

    info_grafica_semana= grafica_semana(mydate, mydate1 ,mydate2,fecha_limite0,fecha_limite_minima0,mylist)
    info_grafica_semana_acumulada= grafica_semana_actual_acumulada(mydate, mydate1 ,mydate2,fecha_limite0,fecha_limite_minima0,mylist)  
    esteMes= esteMesActual(mylist,mydate,True)

    MyesteMesAcumulado= esteMesAcumulado(mylist,mydate,True)
    fecha = mydateToShow
    #print(info_grafica_horas)
    #print(info_grafica_horas_acumulado)
    #print('HOLAAAAAAAAAAAAAAAAAAA')
    #print( info_grafica_horas)
    #print(info_grafica_horas_acumulado)
    return_sub_array = {'info_grafica_horas':info_grafica_horas,'info_grafica_horas_acumulado':info_grafica_horas_acumulado,' info_grafica_semana': info_grafica_semana,'info_grafica_semana_acumulada':info_grafica_semana_acumulada,'estemes':esteMes,'estemesacumulado':MyesteMesAcumulado,'fecha':fecha}
    #print('return_sub_array')
    #print(return_sub_array)
            
    
    return HttpResponse( json.dumps(return_sub_array))


@login_required(login_url="/login/")
def hello(request):
    return HttpResponse('Hello World!')
#--------------------------------Informacion Para index_base.html



@login_required(login_url="/login/")
def pitarnfo(request):
    #print("AHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
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
    
    #graficas inferiores
    indice= 0
  


    datosDevolver={'info_grafica_horas':info_grafica_horas,'info_grafica_horas_acumulado':info_grafica_horas_acumulado,'info_grafica_semana_acumulada':info_grafica_semana_acumulada}

    #datosDevolver=  {'camaras':camarasAll,'info_grafica_semana': info_grafica_semana,'info_grafica_horas':info_grafica_horas,'info_grafica_horas_acumulado':info_grafica_horas_acumulado,'info_grafica_semana_acumulada':info_grafica_semana_acumulada,'estemes':esteMes,'estemesacumulado':MyesteMesAcumulado}
    #de ejemplo
    mylist=['Q2GV-4YBM-YWWJ','Q2HV-B24V-ZKN5']
    for i in mylist:
        
        info_camara1=grafica_semana(mydate, mydate1 ,mydate2,fecha_limite0,fecha_limite_minima0,mylist[indice])
        info_grafica_semana_acumulada1 = grafica_semana_actual_acumulada(mydate, mydate1 ,mydate2,fecha_limite0,fecha_limite_minima0,mylist[indice])
        #print('info camara a agragar al diccionario')
        #print(info_camara1)
        nombre = "infocamara" + str(indice)
        globals() [nombre] = info_camara1
        #print("infocamara" + str(indice))
        datosDevolver["infocamara" + str(indice)] =[1,2,3,4,5,6,7]
        indice = indice+1
        #grafica_semana(mydate, mydate1 ,mydate2,fecha_limite0,fecha_limite_minima0,mylist[indice])
    
    #print("AHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
    #print(datosDevolver)

    return render(request, "includes\index_base.html", datosDevolver )






def hfs(request):    
    #print("hfs")
    if hasattr(request.user.profile, 'cliente') and hasattr(request.user.profile.cliente, 'get_id') and (request.user.profile.cliente.get_id() is not None):    
        if hasattr(request.user.profile, 'instalacion') and hasattr(request.user.profile.instalacion, 'get_id') and (request.user.profile.instalacion.get_id() is not None):
            id_instalacion = request.user.profile.instalacion.get_id()
            display = Display.objects.filter(instalacion={'nif_cliente': request.user.profile.cliente.nif} and {'nombre': request.user.profile.instalacion.nombre_comercial}).first()            
            id_display = display.get_id()
#            id_display = "5f67fbcd37cb6511302af8ee"
        else:
          #print("else")
          display = Display.objects.filter(instalacion={'nif_cliente': request.user.profile.cliente.nif}).first()
          id_display = display.get_id()
#          id_display = "5f67fbcd37cb6511302af8ee"
    else:   
        #print("estoy en el else")     
        cliente = Cliente.objects.first()        
        instalacion = Instalacion.objects.filter(cliente={'nif': cliente.nif}).first()
        display = Display.objects.filter(instalacion={'nif_cliente': cliente.nif} and {'nombre': instalacion.nombre_comercial}).first()                
        id_display = display.get_id()
#        id_display = "5f67fbcd37cb6511302af8ee"
        #print("id_display:  ",id_display)

    data = { 
        'embebido':False, 
        'id_display': id_display       
    }     
    dataJSON = dumps(data)    
    
    return render(request, 'hzfullscreen_bu.html', {'data': dataJSON})

def hfsEmbebido(request):
    #print("hfsEmbebido")    
    if hasattr(request.user.profile, 'cliente') and hasattr(request.user.profile.cliente, 'get_id') and (request.user.profile.cliente.get_id() is not None):    
        if hasattr(request.user.profile, 'instalacion') and hasattr(request.user.profile.instalacion, 'get_id') and (request.user.profile.instalacion.get_id() is not None):
            id_instalacion = request.user.profile.instalacion.get_id()
            display = Display.objects.filter(instalacion={'nif_cliente': request.user.profile.cliente.nif} and {'nombre': request.user.profile.instalacion.nombre_comercial}).first()            
            id_display = display.get_id()
            #id_display = "5f67fbcd37cb6511302af8ee"
        else:
          #print("estoy en el else1")     
          display = Display.objects.filter(instalacion={'nif_cliente': request.user.profile.cliente.nif}).first()
          #id_display = "5f67fbcd37cb6511302af8ee"
          id_display = display.get_id()   
    else:
        #print("estoy en el else2")
        cliente = Cliente.objects.first()  
        #print("cliente",cliente.nif)      
        instalacion = Instalacion.objects.filter(cliente={'nif': cliente.nif}).first()
        #print("instalacion",instalacion.nombre_comercial)
        display = Display.objects.filter(instalacion={'nif_cliente': cliente.nif} and {'nombre': instalacion.nombre_comercial}).first()
        #print("display",display)                
        #id_display = "5f67fbcd37cb6511302af8ee"
        id_display = display.get_id()
        #print("id_display:  ",id_display)
    
       
    data = { 
        'embebido':True,
        'id_display': id_display        
    } 
    
    
    dataJSON = dumps(data)    
    return render(request, 'hzfullscreen_bu.html', {'data': dataJSON})


def generar_estadistica_generales(request,fecha_str,operacion):    

    fecha = ""
    derecha_disabled = False
    array_red_ethernet = []        
    array_red_wifi = [] 
    result = [] 
    if request.method == 'GET':
        try:              
              
            try:
                if request.method == 'GET':
                    #print("GET")
                    #print("fecha_str: ",fecha_str)                    
                    fecha_convert =  datetime.strptime(fecha_str, "%d-%m-%Y").date()
                    #print("fecha_convert: ",fecha_convert)
                    if (operacion == 'atras'):
                        fecha = (fecha_convert - timedelta(days=1)).strftime("%d-%m-%Y")
                        #print("fecha: ",fecha)
                    elif (operacion == 'delante'):
                        fecha = (fecha_convert + timedelta(days=1)).strftime("%d-%m-%Y")
                        #print("fecha: ",fecha)
                                            
                    derecha_disabled =  (fecha == Fecha.getFechaActual().strftime("%d-%m-%Y"))
                    fecha_consultar = datetime.strptime(fecha, "%d-%m-%Y").date()
                    result = generar_estadistica_conteo_red(array_red_ethernet,array_red_wifi,fecha_consultar)
                    array_red_ethernet = result[0]        
                    array_red_wifi = result[1]
                    hora_apertura = result[2]
                    hora_cierre = result[3]
                    
            except Exception as e:
                print('%s (%s)' % (e, type(e)))
                pass
            estadistica_js = {           
                "fecha" : str(fecha),      
                "derecha_disabled": derecha_disabled,
                "array_red_ethernet" : array_red_ethernet,
                "array_red_wifi" : array_red_wifi,
                "hora_apertura" : hora_apertura,
                "hora_cierre" : hora_cierre,                        
            }
            return HttpResponse(simplejson.dumps(estadistica_js), content_type='application/json')
        except Exception as e:
            print('%s (%s)' % (e, type(e)))
            return JsonResponse({'m': fecha_str, 'error:': 'parametros erroneos'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        pass
    return JsonResponse({'m': fecha_str, 'error:': 'parametros erroneos 2'},
                        status=status.HTTP_400_BAD_REQUEST)

def generar_estadistica_conteo_red(array_red_ethernet,array_red_wifi,fecha):
    
    #print("generar_estadistica_conteo_red")
  
    intervalo = get_intervaloPeriodo(fecha)
    start_date = intervalo[0]
    end_date = intervalo[1]  
    #print("start_date",start_date)
    #print("end_date",end_date)
    
    parametros = setParametros()    
    tiempo_medicion = parametros[0]    
    #print("tiempo_medicion",tiempo_medicion)
    tiempo_medicion_parametro = parametros[1]
    #print("tiempo_medicion_parametro",tiempo_medicion_parametro)    
    array_tiempo  = parametros[2]
    #print("array_tiempo",array_tiempo)    
    query = getQuery(start_date,end_date,tiempo_medicion,tiempo_medicion_parametro,array_tiempo)
    
    #print("QUERY")
    #print(query)

    usuariosRed = UsuariosRed.objects.mongo_aggregate(query)       
    lista = list(usuariosRed)  
    #print(list) 
    jornada = getHorarioLaboral()
    hora_apertura = jornada[0]
    hora_cierre = jornada[1]        
    #print("hora_apertura: ",hora_apertura)
    #print("hora_cierre: ",hora_cierre)    
    array_red_ethernet = [0] * len(array_tiempo)
    array_red_wifi = [0] * len(array_tiempo)
    """
    for i in range(len(array_red_ethernet)):
        print("i: ",i)
        print("array_red_ethernet[i]: ",array_red_ethernet[i])
    """   

    for dispositivoConectados in lista:
        #print("dispositivoConectados")
        #print(dispositivoConectados)
        result: OrderedDict[str, int] = dispositivoConectados
        #print("RESULTADOS!!!!!!!!!!!!!!!")        
        #print(result['_id'])
        #result_tiempo: OrderedDict[str, str] = result['_id']
        result_tiempo: OrderedDict[str, int] = dispositivoConectados
        nro_usuarios_ethernet = result['nro_usuarios_ethernet']
        nro_usuarios_wifi = result['nro_usuarios_wifi']
        result_hora: OrderedDict[str, str] = result['_id']
        
        #print("result_hora: ",result_tiempo)
        #print("tiempo_medicion: ",tiempo_medicion)
        hora = result_hora[tiempo_medicion]
        #print("hora: ",hora)
        #if hora in
        nro_usuarios_ethernet = int(result_tiempo['nro_usuarios_ethernet'])
        nro_usuarios_wifi = int(result_tiempo['nro_usuarios_wifi'])
        #print("nro_usuarios_ethernet: ",nro_usuarios_ethernet)        
        
       
        array_red_ethernet[hora] = nro_usuarios_ethernet
        array_red_wifi[hora] = nro_usuarios_wifi
        
                

        
    #print("ARREGLO DE PRESION ARTERIAL QUE VA PARA ESTADISTICA")
    #for i in range(len(array_presion_arterial_sys_hora)):
       #print("i: ",i)
       #print("array_presion_arterial_sys_hora[i]: ",array_presion_arterial_sys_hora[i])
       #print("array_presion_arterial_dia_hora[i]: ",array_presion_arterial_dia_hora[i])      

    return array_red_ethernet,array_red_wifi,hora_apertura,hora_cierre
    
def get_intervaloPeriodo(fecha_consulta):       
    
    #print("fecha_consulta:",fecha_consulta)
    start_date = Fecha.get_start_day(fecha_consulta)    
    end_date =  Fecha.get_end_day(fecha_consulta)     
    #print("start_date: ",start_date)
    #print("end_date: ",end_date)
    return start_date,end_date    
    
    
    


def getQuery(start_date,end_date,tiempo_medicion,tiempo_medicion_parametro,array_tiempo):
    query = [
      {
        "$match": {          
          "fecha": {
            "$gte": start_date,
            "$lte": end_date
          },
        }
      },
      {
        "$project": {
          "date": {
            "$dateToString": {
              "format": "%Y-%m-%d",
              "date": "$fecha"
            }
          },
        tiempo_medicion: { 
                tiempo_medicion_parametro: "$fecha"
        },
         "nro_usuarios_ethernet": "$nro_usuarios_ethernet",
         "nro_usuarios_wifi": "$nro_usuarios_wifi"
        }
      },
      {
     "$match":{
            tiempo_medicion:{"$in":array_tiempo}
          }
      },
      {
        "$group": {
          "_id": {
          tiempo_medicion: tiempo_medicion_parametro,
          "date": "$date"
          },                
          "nro_usuarios_ethernet": { 
            "$max": "$nro_usuarios_ethernet"
          },
          "nro_usuarios_wifi": { 
            "$max": "$nro_usuarios_wifi"
          },      
          
        }
      }  
    ]
    return query    

def get_array_tiempo(ultimo_dia):
    array_tiempo = []
    rango = ultimo_dia + 1
    for i in range(0,rango):
        array_tiempo.append(i)        
    return array_tiempo

def setParametrosAF(periodo_estadistica):
    
    if (periodo_estadistica == 1):
        tiempo_medicion = "hour"
        tiempo_medicion_parametro = "$hour"
        array_tiempo = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
    #Por semana
    if (periodo_estadistica == 2):
        tiempo_medicion = "dayOfWeek"
        tiempo_medicion_parametro = "$dayOfWeek"
        array_tiempo = [1,2,3,4,5,6,7]


    if (periodo_estadistica == 3):
        tiempo_medicion = "dayOfMonth"
        tiempo_medicion_parametro = "$dayOfMonth"            
        ultimo_dia = last_day_of_month(datetime.today())
        array_tiempo = get_array_tiempo(ultimo_dia)
        
    return tiempo_medicion,tiempo_medicion_parametro,array_tiempo

def setParametros():
    
    tiempo_medicion = "hour"
    tiempo_medicion_parametro = "$hour"
    array_tiempo = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]  

    
    return tiempo_medicion,tiempo_medicion_parametro,array_tiempo


def getHorarioLaboral():
    #print("getHorarioLaboral")
    jornada = JornadaLaboral.objects.all()[0]
    #print("jornada")
    #print(jornada)    
    hora_apertura = int(str(jornada.hora_apertura)[:2])
    hora_cierre = int(str(jornada.hora_cierre)[:2])
    #print("hora_apertura HL: ",hora_apertura)
    #print("hora_cierre: HL",hora_cierre)
    return hora_apertura,hora_cierre
    """
    if (request.user.profile.rol == Constantes.ADMINISTRADOR) and hasattr(request.user.profile, 'cliente') and (request.user.profile.cliente.get_id() is not None):
                jornadaTodos = JornadaLaboral.objects.all().filter(instalacion={'nif_cliente': request.user.profile.cliente.nif})
    
    elif (request.user.profile.rol > Constantes.ADMINISTRADOR) and hasattr(request.user.profile, 'cliente') and (request.user.profile.cliente.get_id() is not None):
          if hasattr(request.user.profile, 'instalacion') and hasattr(request.user.profile.instalacion, 'get_id') and (request.user.profile.instalacion.get_id() is not None):
              jornadaTodos = JornadaLaboral.objects.all().filter(instalacion={'nif_cliente': request.user.profile.cliente.nif} and {'nombre': request.user.profile.instalacion.nombre_comercial})
    """
def getQueryTotalAforo(verdadero,start_date,end_date,tiempo_medicion,tiempo_medicion_parametro,array_tiempo):
    query =[
        {
        "$match": {
         "suma_total_aforo": {
            "$eq": verdadero
          },
          "fecha": {
                "$gte": start_date,
                "$lte": end_date
          }
        }
      },
      {
        "$project": {
          "date": {
            "$dateToString": {
              "format": "%Y-%m-%d",
              "date": "$fecha"
            }
          },
          tiempo_medicion: { 
                    tiempo_medicion_parametro: "$fecha"
            },
         "nro_personas": "$nro_personas"
    
        }
      },
      {
         "$match":{
                tiempo_medicion:{"$in":array_tiempo}
              }
          },
      {
        "$group": {
          "_id": {
            tiempo_medicion: tiempo_medicion_parametro,
            "date": "$date",       
          },
          "total_nro_personas": { 
             "$sum": "$nro_personas"
          }
        }
      }
      
    ]
    return query
  
  
def generar_estadistica_total_aforo(periodo_estadistica):
    
    #print("generar_estadistica_total_aforo")
  
    intervalo = get_intervaloPeriodo_AF(periodo_estadistica)
    start_date = intervalo[0]
    end_date = intervalo[1]  
    #print("start_date",start_date)
    #print("end_date",end_date)
    
    parametros = setParametrosAF(periodo_estadistica)    
    tiempo_medicion = parametros[0]    
    #print("tiempo_medicion",tiempo_medicion)
    tiempo_medicion_parametro = parametros[1]
    #print("tiempo_medicion_parametro",tiempo_medicion_parametro)    
    array_tiempo  = parametros[2]
    #print("array_tiempo",array_tiempo)    
    query = getQueryTotalAforo(True,start_date,end_date,tiempo_medicion,tiempo_medicion_parametro,array_tiempo)
    
    #print("QUERY")
    #print(query)

    camarasHistorico = CamarasHistorico.objects.mongo_aggregate(query)       
    lista = list(camarasHistorico)  
    #print(list) 
    jornada = getHorarioLaboral()
    hora_apertura = jornada[0]
    hora_cierre = jornada[1]        
    #print("hora_apertura: ",hora_apertura)
    #print("hora_cierre: ",hora_cierre)    
    array_total_aforo = [0] * len(array_tiempo)
    array_total_persona = [0] * len(array_tiempo)
    """
    for i in range(len(array_red_ethernet)):
        print("i: ",i)
        print("array_red_ethernet[i]: ",array_red_ethernet[i])
    """   

    for nro_personas in lista:
        #print("dispositivoConectados")
        #print(dispositivoConectados)
        #result: OrderedDict[str, int] = nro_personas
        #print("RESULTADOS!!!!!!!!!!!!!!!")        
        #print(result['_id'])
        #result_tiempo: OrderedDict[str, str] = result['_id']
        result_tiempo: OrderedDict[str, int] = nro_personas
        #nro_personas = result['total_nro_personas']
        
        result_hora: OrderedDict[str, str] = result_tiempo['_id']
        
        #print("result_hora: ",result_tiempo)
        #print("tiempo_medicion: ",tiempo_medicion)
        hora = result_hora[tiempo_medicion]
        #print("hora: ",hora)
        #if hora in
        total_nro_personas = int(result_tiempo['total_nro_personas'])
        #nro_usuarios_wifi = int(result_tiempo['nro_usuarios_wifi'])
        #print("nro_usuarios_ethernet: ",nro_usuarios_ethernet)        
        
       
        array_total_aforo[hora] = total_nro_personas
        
        
                

        
    #print("ARREGLO DE TOTAL NÚMEROS DE PERSONAS QUE VA PARA ESTADISTICA")
    #for i in range(len(array_total_aforo)):
       #print("i: ",i)
       #print("array_total_aforo[i]: ",array_total_aforo[i])
             

    return array_total_aforo,array_total_persona,hora_apertura,hora_cierre
  
  
def totalAforo(request,periodo_estadistica):
    
     
    result = [] 
    if request.method == 'GET':
        try:        
            #print("periodo_estadistica: ",periodo_estadistica)
                
              
            try:                
                nro_aforo = 0
                result = generar_estadistica_total_aforo(periodo_estadistica)
                array_total_aforo = result[0]       
                array_total_persona = result[1]
                hora_apertura = result[2]
                hora_cierre = result[3]              
                    
                
            except Exception as e:
                print('%s (%s)' % (e, type(e)))
                pass
            red_js = {           
                "array_total_aforo" : array_total_aforo,
                "array_total_persona" : array_total_persona,                
                "hora_apertura" : hora_apertura,
                "hora_cierre" : hora_cierre,                              
            }
            return HttpResponse(simplejson.dumps(red_js), content_type='application/json')
        except Exception as e:
            print('%s (%s)' % (e, type(e)))
            return JsonResponse({'m': periodo_estadistica, 'error:': 'parametros erroneos'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        pass
    return JsonResponse({'m': periodo_estadistica, 'error:': 'parametros erroneos 2'},
                        status=status.HTTP_400_BAD_REQUEST)

  
def get_intervaloPeriodo_AF(periodo_estadistica):   
    
    
    if (periodo_estadistica == 1):
        start_date = Fecha.get_start_day(Fecha.getFechaActual())    
        end_date =  Fecha.get_end_day(Fecha.getFechaActual())
    
    elif (periodo_estadistica == 2):
        dia_semana = datetime.today().weekday()
        inicio_semana = datetime.today() - timedelta(days=dia_semana)        
        fin_semana =inicio_semana +  timedelta(days=6)         
        start_date = Fecha.get_start_day(inicio_semana)
        end_date =  Fecha.get_end_day(fin_semana)        
        
    elif (periodo_estadistica == 3):    
         inicio_mes = datetime.today() - timedelta(days=(datetime.today().day-1))                     
         fin_mes = last_date_of_month(datetime.today())               
         start_date = Fecha.get_start_day(inicio_mes)      
         end_date =  Fecha.get_end_day(fin_mes)         
        
    return start_date,end_date

def totalAforoDia(request,fecha_str,operacion):    

    fecha = ""
    derecha_disabled = False            
    array_total_aforo = [] 
    result = [] 
    if request.method == 'GET':
        try:              
              
            try:
                if request.method == 'GET':
                    #print("GET")
                    #print("fecha_str: ",fecha_str)                    
                    fecha_convert =  datetime.strptime(fecha_str, "%d-%m-%Y").date()
                    #print("fecha_convert: ",fecha_convert)
                    if (operacion == 'atras'):
                        fecha = (fecha_convert - timedelta(days=1)).strftime("%d-%m-%Y")
                        #print("fecha: ",fecha)
                    elif (operacion == 'delante'):
                        fecha = (fecha_convert + timedelta(days=1)).strftime("%d-%m-%Y")
                        #print("fecha: ",fecha)
                                            
                    derecha_disabled =  (fecha == Fecha.getFechaActual().strftime("%d-%m-%Y"))
                    fecha_consultar = datetime.strptime(fecha, "%d-%m-%Y").date()
                    result = generar_estadistica_aforo_dia(array_total_aforo,fecha_consultar)
                    array_total_aforo = result[0]        
                    #array_red_wifi = result[1]
                    hora_apertura = result[1]
                    hora_cierre = result[2]
                    
            except Exception as e:
                print('%s (%s)' % (e, type(e)))
                pass
            estadistica_js = {           
                "fecha" : str(fecha),      
                "derecha_disabled": derecha_disabled,
                "array_total_aforo" : array_total_aforo,    
                "hora_apertura" : hora_apertura,
                "hora_cierre" : hora_cierre,                        
            }
            return HttpResponse(simplejson.dumps(estadistica_js), content_type='application/json')
        except Exception as e:
            print('%s (%s)' % (e, type(e)))
            return JsonResponse({'m': fecha_str, 'error:': 'parametros erroneos'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        pass
    return JsonResponse({'m': fecha_str, 'error:': 'parametros erroneos 2'},
                        status=status.HTTP_400_BAD_REQUEST)

def generar_estadistica_aforo_dia(array_total_aforo,fecha):
    
    #print("generar_estadistica_aforo_dia")
  
    intervalo = get_intervaloPeriodo(fecha)
    start_date = intervalo[0]
    end_date = intervalo[1]  
    #print("start_date",start_date)
    #print("end_date",end_date)
    
    parametros = setParametros()    
    tiempo_medicion = parametros[0]    
    #print("tiempo_medicion",tiempo_medicion)
    tiempo_medicion_parametro = parametros[1]
    #print("tiempo_medicion_parametro",tiempo_medicion_parametro)    
    array_tiempo  = parametros[2]
    #print("array_tiempo",array_tiempo)    
    query = getQueryTotalAforo(True,start_date,end_date,tiempo_medicion,tiempo_medicion_parametro,array_tiempo)
    
    #print("QUERY")
    #print(query)

    usuariosRed = UsuariosRed.objects.mongo_aggregate(query)       
    lista = list(usuariosRed)  
    #print(list) 
    jornada = getHorarioLaboral()
    hora_apertura = jornada[0]
    hora_cierre = jornada[1]        
    #print("hora_apertura dia: ",hora_apertura)
    #print("hora_cierre dia: ",hora_cierre)    
    array_total_aforo = [0] * len(array_tiempo)
    #array_red_wifi = [0] * len(array_tiempo)
    """
    for i in range(len(array_red_ethernet)):
        print("i: ",i)
        print("array_red_ethernet[i]: ",array_red_ethernet[i])
    """   

    for nro_personas in lista:
        #print("dispositivoConectados")
        #print(dispositivoConectados)
        #result: OrderedDict[str, int] = nro_personas
        #print("RESULTADOS!!!!!!!!!!!!!!!")        
        #print(result['_id'])
        #result_tiempo: OrderedDict[str, str] = result['_id']
        result_tiempo: OrderedDict[str, int] = nro_personas
        #nro_personas = result['total_nro_personas']
        
        result_hora: OrderedDict[str, str] = result_tiempo['_id']
        
        #print("result_hora: ",result_tiempo)
        #print("tiempo_medicion: ",tiempo_medicion)
        hora = result_hora[tiempo_medicion]
        #print("hora: ",hora)
        #if hora in
        total_nro_personas = int(result_tiempo['total_nro_personas'])
        #nro_usuarios_wifi = int(result_tiempo['nro_usuarios_wifi'])
        #print("nro_usuarios_ethernet: ",nro_usuarios_ethernet)        
        
       
        array_total_aforo[hora] = total_nro_personas

        
                

        
    #print("ARREGLO DE PRESION ARTERIAL QUE VA PARA ESTADISTICA")
    #for i in range(len(array_presion_arterial_sys_hora)):
       #print("i: ",i)
       #print("array_presion_arterial_sys_hora[i]: ",array_presion_arterial_sys_hora[i])
       #print("array_presion_arterial_dia_hora[i]: ",array_presion_arterial_dia_hora[i])      

    return array_total_aforo,hora_apertura,hora_cierre


def aforoZona(request,periodo_estadistica):
    
     
    result = [] 
    if request.method == 'GET':
        try:        
            #print("periodo_estadistica: ",periodo_estadistica)
                
              
            try:                
                nro_aforo = 0
                result = generar_estadistica_aforo_zona(periodo_estadistica)
                dict_zonas_camara = result[0]                
                hora_apertura = result[1]
                hora_cierre = result[2]              
                    
                
            except Exception as e:
                print('%s (%s)' % (e, type(e)))
                pass
            red_js = {           
                "dict_zonas_camara" : dict_zonas_camara,                                
                "hora_apertura" : hora_apertura,
                "hora_cierre" : hora_cierre,                              
            }
            return HttpResponse(simplejson.dumps(red_js), content_type='application/json')
        except Exception as e:
            print('%s (%s)' % (e, type(e)))
            return JsonResponse({'m': periodo_estadistica, 'error:': 'parametros erroneos'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        pass
    return JsonResponse({'m': periodo_estadistica, 'error:': 'parametros erroneos 2'},
                        status=status.HTTP_400_BAD_REQUEST)

def generar_estadistica_total_aforo(periodo_estadistica):
    
    #print("generar_estadistica_total_aforo")
  
    intervalo = get_intervaloPeriodo_AF(periodo_estadistica)
    start_date = intervalo[0]
    end_date = intervalo[1]  
    #print("start_date",start_date)
    #print("end_date",end_date)
    
    parametros = setParametrosAF(periodo_estadistica)    
    tiempo_medicion = parametros[0]    
    #print("tiempo_medicion",tiempo_medicion)
    tiempo_medicion_parametro = parametros[1]
    #print("tiempo_medicion_parametro",tiempo_medicion_parametro)    
    array_tiempo  = parametros[2]
    #print("array_tiempo",array_tiempo)    
    query = getQueryTotalAforo(True,start_date,end_date,tiempo_medicion,tiempo_medicion_parametro,array_tiempo)
    
    #print("QUERY")
    #print(query)

    camarasHistorico = CamarasHistorico.objects.mongo_aggregate(query)       
    lista = list(camarasHistorico)  
    #print(list) 
    jornada = getHorarioLaboral()
    hora_apertura = jornada[0]
    hora_cierre = jornada[1]        
    #print("hora_apertura: ",hora_apertura)
    #print("hora_cierre: ",hora_cierre)    
    array_total_aforo = [0] * len(array_tiempo)
    array_total_persona = [0] * len(array_tiempo)
    """
    for i in range(len(array_red_ethernet)):
        print("i: ",i)
        print("array_red_ethernet[i]: ",array_red_ethernet[i])
    """   

    for nro_personas in lista:
        #print("dispositivoConectados")
        #print(dispositivoConectados)
        #result: OrderedDict[str, int] = nro_personas
        #print("RESULTADOS!!!!!!!!!!!!!!!")        
        #print(result['_id'])
        #result_tiempo: OrderedDict[str, str] = result['_id']
        result_tiempo: OrderedDict[str, int] = nro_personas
        #nro_personas = result['total_nro_personas']
        
        result_hora: OrderedDict[str, str] = result_tiempo['_id']
        
        #print("result_hora: ",result_tiempo)
        #print("tiempo_medicion: ",tiempo_medicion)
        hora = result_hora[tiempo_medicion]
        #print("hora: ",hora)
        #if hora in
        total_nro_personas = int(result_tiempo['total_nro_personas'])
        #nro_usuarios_wifi = int(result_tiempo['nro_usuarios_wifi'])
        #print("nro_usuarios_ethernet: ",nro_usuarios_ethernet)        
        
       
        array_total_aforo[hora] = total_nro_personas
        
        
                

        
    #print("ARREGLO DE TOTAL NÚMEROS DE PERSONAS QUE VA PARA ESTADISTICA")
    #for i in range(len(array_total_aforo)):
       #print("i: ",i)
       #print("array_total_aforo[i]: ",array_total_aforo[i])
             

    return array_total_aforo,array_total_persona,hora_apertura,hora_cierre



def generar_estadistica_aforo_zona(periodo_estadistica):
    
    #print("generar_estadistica_aforo_zona")
  
    intervalo = get_intervaloPeriodo_AF(periodo_estadistica)
    start_date = intervalo[0]
    end_date = intervalo[1]  
    #print("start_date",start_date)
    #print("end_date",end_date)
    
    parametros = setParametrosAF(periodo_estadistica)    
    tiempo_medicion = parametros[0]    
    #print("tiempo_medicion",tiempo_medicion)
    tiempo_medicion_parametro = parametros[1]
    #print("tiempo_medicion_parametro",tiempo_medicion_parametro)    
    array_tiempo  = parametros[2]
    #print("array_tiempo",array_tiempo)
    
    
    #zonas_camara = ["Aforo Interior planta 3","Aforo Office planta 3","Aforo Despacho planta 3","Aforo de Planta","Aforo Planta 7","Ocupación Mesa"]
    result_zona = getZonasXCamaras()
    zonas_camara = result_zona[0] 
    #print("zonas_camara: ",zonas_camara)
           
    query = getQueryAforoZona(start_date,end_date,tiempo_medicion,tiempo_medicion_parametro,array_tiempo,zonas_camara)
    
    #print("QUERY")
    #print(query)

    camarasHistorico = CamarasHistorico.objects.mongo_aggregate(query)       
    lista = list(camarasHistorico)  
    #print(list) 
    jornada = getHorarioLaboral()
    hora_apertura = jornada[0]
    hora_cierre = jornada[1]        
    #print("hora_apertura: ",hora_apertura)
    #print("hora_cierre: ",hora_cierre)
    
    #array_zonas_camara = ["Planta 3-Aforo Interior planta 3","Planta 3-Aforo Office planta 3","Planta 3-Aforo Despacho planta 3","Planta 3-Aforo de Planta","Planta 7-Aforo Planta 7","Planta 7-Ocupación Mesa"]
    camaras_zonas_camaras = result_zona[1]
    #print("!!!!camaras_zonas_camaras!!!!!: ",camaras_zonas_camaras)
    dict_zonas_camara = {}
    for zona_camara in camaras_zonas_camaras:
        #print("zona_camara: ",zona_camara)
        dict_zonas_camara[zona_camara] = [0] * len(array_tiempo)    
    
    #print("!!!!!!!!!!dict_zonas_camara!!!!!!!!!!!!")
    #print(dict_zonas_camara)
    """
    for i in range(len(array_red_ethernet)):
        print("i: ",i)
        print("array_red_ethernet[i]: ",array_red_ethernet[i])
    """   

    for nro_personas in lista:
        #print("nro_personas")
        #print(nro_personas)
        result: OrderedDict[str, int] = nro_personas
        #print("RESULTADOS!!!!!!!!!!!!!!!")        
        #print(result['_id'])
        #result_tiempo: OrderedDict[str, str] = result['_id']
        result_tiempo: OrderedDict[str, int] = nro_personas
        #print("result_tiempo!!!!")
        #print(result_tiempo)     
        
        result: OrderedDict[str, str] = result_tiempo['_id']
        
        #print("result_hora: ",result_tiempo)
        #print("tiempo_medicion: ",tiempo_medicion)
        hora = result[tiempo_medicion]
        #print("hora: ",hora)
        #if hora in
        total_nro_personas = int(result_tiempo['nro_personas'])
        #print("total_nro_personas: ",total_nro_personas)
        nombre_zona_camara = result['nombre_zona_camara']
        #print('nombre_zona_camara: ',nombre_zona_camara)        
        nombre_camara = result['nombre_camara']
        #print('nombre_camara: ',nombre_camara)
        
        zonaxcamara = nombre_camara+"-"+nombre_zona_camara
        #print("zonaxcamara: ",zonaxcamara)
        #array_total_aforo[hora] = total_nro_personas
        #dict_zonas_camara[nombre_zona_camara] = nombre_camara
        dict_zonas_camara[zonaxcamara][hora] = total_nro_personas
        
        #nro_usuarios_wifi = int(result_tiempo['nro_usuarios_wifi'])
        #print("nro_usuarios_ethernet: ",nro_usuarios_ethernet)        
        
       
        
        
        
                

        
    #print("ARREGLO DE TOTAL NÚMEROS DE PERSONAS QUE VA PARA ESTADISTICA")
    #print("??????? dict_zonas_camara ?????????")
    #print(dict_zonas_camara)
             

    return dict_zonas_camara,hora_apertura,hora_cierre

def getQueryAforoZona(start_date,end_date,tiempo_medicion,tiempo_medicion_parametro,array_tiempo,array_zona_camara):
    query =[
        {
        "$match": {
        "nombre_zona_camara": {
                "$in": array_zona_camara
          },
          "fecha": {
                "$gte": start_date,
                "$lte": end_date
          }
        }
      },
      {
        "$project": {
          "date": {
            "$dateToString": {
              "format": "%Y-%m-%d",
              "date": "$fecha"
            }
          },
          tiempo_medicion: { 
                    tiempo_medicion_parametro: "$fecha"
            },
         "nro_personas": "$nro_personas",
         "nombre_zona_camara": "$nombre_zona_camara",
         "nombre_camara": "$nombre_camara",         
    
        }
      },
      {
         "$match":{
                tiempo_medicion:{"$in":array_tiempo}
              }
          },
      {
        "$group": {
          "_id": {
            tiempo_medicion: tiempo_medicion_parametro,
            "date": "$date",
            "nombre_zona_camara" :"$nombre_zona_camara",
            "nombre_camara": "$nombre_camara",                    
          },
          "nro_personas": { 
             "$max": "$nro_personas"
          }
        }
      }
      
    ]
    return query


def getZonasXCamaras():
    
    zonas_camaras = []
    camaras_zonas_camaras = []
    camarasAll =  Camaras.objects.all()
    for camaras in camarasAll:                                       
        for zonas_camara in camaras.zonas_camara:                      
            zonas_camaras.append(zonas_camara.nombre_zona_camara)
            camaras_zonas_camaras.append(camaras.nombre_camara+"-"+zonas_camara.nombre_zona_camara)
    
    return zonas_camaras,camaras_zonas_camaras
            
def last_day_of_month(date_value):
    return monthrange(date_value.year, date_value.month)[1]

def last_date_of_month(date_value):
    return date_value.replace(day = last_day_of_month(date_value))
