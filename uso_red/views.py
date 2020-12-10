import simplejson as simplejson
from django.contrib.auth.decorators import login_required,permission_required
from django.http import HttpResponse
from djongo import models
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.utils.translation import activate
import Constantes
from rest_framework.decorators import api_view, authentication_classes, permission_classes
import time
from datetime import datetime
from datetime import datetime
from datetime import datetime, timedelta
from calendar import monthrange
import collections
from django.http import JsonResponse
from Fecha import Fecha


def generar_estadistica_conteo_red(array_red_ethernet,array_red_wifi,periodo_estadistica):
    
    print("generar_estadistica_conteo_red")
  
    intervalo = get_intervaloPeriodo(periodo_estadistica)
    start_date = intervalo[0]
    end_date = intervalo[1]  
    parametros = setParametros(periodo_estadistica)    
    tiempo_medicion = parametros[0]    
    tiempo_medicion_parametro = parametros[1]    
    array_tiempo  = parametros[2]
    
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
           "nro_usuarios_ethernet": "$nro_usuarios_ethernet",
           "nro_usuarios_wifi": "$nro_usuarios_wifi",
        }
      },
      {"$sort": {_id: 1}}  
    ]
    
    #print("QUERY")
    #print(query)

    usuariosRed = UsuariosRed.objects.mongo_aggregate(query)       
    lista = list(usuariosRed)    
    array_presion_arterial_sys_hora = [0] * len(array_tiempo)
    array_presion_arterial_dia_hora = [0] * len(array_tiempo)
    for i in range(len(array_presion_arterial_sys_hora)):
        print("i: ",i)
        print("array_presion_arterial_sys_hora[i]: ",array_presion_arterial_sys_hora[i])
        
    """     
    for medicionHistorico in lista:
        #print("medicionHistorico")
        #print(medicionHistorico)
        result: OrderedDict[str, int] = medicionHistorico
        #print("RESULTADOS!!!!!!!!!!!!!!!")        
        #print(result['_id'])
        maxima_presion_arterial_sys = result['maxima_presion_arterial_sys']
        maxima_presion_arterial_dia = result['maxima_presion_arterial_dia']
        #print('maxima_presion_arterial_sys', str(maxima_presion_arterial_sys))
        #print('maxima_presion_arterial_dia', str(maxima_presion_arterial_dia))        
        result_hora: OrderedDict[str, str] = result['_id']
        hora = result_hora[tiempo_medicion]        
        
        if (periodo_estadistica ==2):            
            if (hora-2 == -1):
                hora = len(array_tiempo)-1                
            else:
                hora = hora-2
                
        if (periodo_estadistica ==3):            
            if (hora-1 >= 0):        
                hora = hora-1
                
        #print("hora: ",hora) 
        if (periodo_estadistica !=1 and hora-1 >= 0):    
            array_presion_arterial_sys_hora[hora] = maxima_presion_arterial_sys
            array_presion_arterial_dia_hora[hora] = maxima_presion_arterial_dia
        elif (periodo_estadistica ==1):
            array_presion_arterial_sys_hora[hora] = maxima_presion_arterial_sys
            array_presion_arterial_dia_hora[hora] = maxima_presion_arterial_dia
        #print("hora: ",hora)
        """
        
    #print("ARREGLO DE PRESION ARTERIAL QUE VA PARA ESTADISTICA")
    #for i in range(len(array_presion_arterial_sys_hora)):
       #print("i: ",i)
       #print("array_presion_arterial_sys_hora[i]: ",array_presion_arterial_sys_hora[i])
       #print("array_presion_arterial_dia_hora[i]: ",array_presion_arterial_dia_hora[i])      

    return array_presion_arterial_sys_hora,array_presion_arterial_dia_hora


@api_view(['GET', 'POST'])
@authentication_classes([])
@permission_classes([])
def conteoUsoRed(request,periodo_estadistica):
    
    if request.method == 'GET':
        try:        
            print("periodo_estadistica: ",periodo_estadistica)    
              
            try:                
                nro_aforo = 0

            except Exception as e:
                print('%s (%s)' % (e, type(e)))
                pass
            red_js = {                             
                "nro_personas": nro_aforo,               
            }
            return HttpResponse(simplejson.dumps(red_js), content_type='application/json')
        except Exception as e:
            print('%s (%s)' % (e, type(e)))
            return JsonResponse({'m': id_display, 'error:': 'parametros erroneos'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        pass
    return JsonResponse({'m': id_display, 'error:': 'parametros erroneos 2'},
                        status=status.HTTP_400_BAD_REQUEST)




def get_intervaloPeriodo(periodo_estadistica):   
    
    
    if (periodo_estadistica == 1):
        start_date = Fecha.get_start_day(datetime.today())    
        end_date =  Fecha.get_end_day(datetime.today())
    
    elif (periodo_estadistica == 2):
        dia_semana = datetime.today().weekday()
        inicio_semana = datetime.today() - timedelta(days=dia_semana)        
        fin_semana =inicio_semana +  timedelta(days=6)         
        start_date = Fecha.get_start_day(inicio_semana)
        end_date =  Fecha.get_end_day(fin_semana)        
        
    elif (periodo_estadistica == 3):    
         #x = datetime(2019, 2, 17)
         inicio_mes = datetime.today() - timedelta(days=(datetime.today().day-1))
         start_date = Fecha.get_start_day(inicio_mes)         
         fin_mes = last_date_of_month(datetime.today())
         end_date =  Fecha.get_end_day(fin_mes)         
        
    return start_date,end_date

def last_day_of_month(date_value):
    return monthrange(date_value.year, date_value.month)[1]

def last_date_of_month(date_value):
    return date_value.replace(day = last_day_of_month(date_value))

def get_array_tiempo(ultimo_dia):
    array_tiempo = []
    rango = ultimo_dia + 1
    for i in range(0,rango):
        array_tiempo.append(i)        
    return array_tiempo


def setParametros(periodo_estadistica):
    
    #periodo_estadistica == hora y tipo es fecuencia cardiaca
    """if (tipo_estadistica==1):

        nombre_medicion = "frecuencia_cardiaca"
        valor_medicion = "$frecuencia_cardiaca"
        nombre_tiempo_medicion  = "hora_frecuencia_cardiaca"
        valor_tiempo_medicion = "$hora_frecuencia_cardiaca"  
        maxima_medicion = "maxima_frecuencia_cardiaca"    
     
         
         
    if (tipo_estadistica==2):

        nombre_medicion = "saturacion_oxigeno"
        valor_medicion = "$saturacion_oxigeno"
        nombre_tiempo_medicion  = "hora_saturacion_oxigeno"
        valor_tiempo_medicion = "$hora_saturacion_oxigeno"
        maxima_medicion = "maxima_saturacion_oxigeno"    
            

    if (tipo_estadistica==3):            
        nombre_medicion = "temperatura"
        valor_medicion = "$temperatura"
        nombre_tiempo_medicion  = "hora_temperatura"
        valor_tiempo_medicion = "$hora_temperatura"
        maxima_medicion = "maxima_temperatura"        
        


    if (tipo_estadistica==4):            
        nombre_medicion = ""
        valor_medicion = ""
        nombre_tiempo_medicion  = ""
        valor_tiempo_medicion = "$hora_presion_arterial"
        maxima_medicion = ""        
        
  
    """
    #tipos_estadistica = [1,2,3,4]
    #if (tipo_estadistica in tipos_estadistica):
        #Por Hora
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
    
    
   
    #return nombre_medicion,valor_medicion,tiempo_medicion,nombre_tiempo_medicion,tiempo_medicion_parametro,valor_tiempo_medicion,maxima_medicion,array_tiempo
    return tiempo_medicion,tiempo_medicion_parametro,array_tiempo
