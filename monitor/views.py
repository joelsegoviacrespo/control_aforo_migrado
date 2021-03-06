# -*- encoding: utf-8 -*-
#import pymongo
from djongo import models
import simplejson
from django.http import HttpResponse
import random
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.utils.translation import activate
#from pymongo import MongoClient
from rest_framework import views, status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.conf import settings

from camara_zona.models import CamaraZona
from monitor.forms import MonitorForm, MonitorEditarForm, MonitorShowForm
from monitor.models import Monitor
from camaras.models import Camaras
from aforoInfo.models import AforoInfo
from django.forms.models import model_to_dict
from django.core import serializers


import calendar
import datetime
import pytz
from datetime import date
today = date.today()

from .serializers import MonitorSerializer, MonitorLinkSerializer, MonitorFSSerializer, MonitorShowSerializer


@api_view(['GET', 'POST'])
@authentication_classes([])
@permission_classes([])
def obtenerURL(request):  # Atiende las solicitude de obtener Link por parte del STB
    if request.method == 'POST':
        monitor_data = JSONParser().parse(request)
        monitor_serializer = MonitorSerializer(data=monitor_data)

        if monitor_serializer.is_valid():
            # TODO: Verificación del STB contra la BD de Meraki
            # TODO: Agregarle la orientación bien que se reciba de la consulta anterior o que se obtenga de la bd de Aforo
            # TODO: Refinar la busqueda solo devolver el _id

            monitor = Monitor.objects.get(mac_wifi=monitor_data['mwf'])
            url = "monitor/show?m=%s;o=%s" % (str(monitor._id), "H")
            link_info = {"url": url, "token": "OWJDWU3ROWJDQOWDKPOQE92IJKDSHFFW8FKFSFIW803923234U2342J3HJ24HJ4B23J4"}
            monitor_link_serializer = MonitorLinkSerializer(data=link_info)

            if monitor_link_serializer.is_valid():
                return JsonResponse(monitor_link_serializer.data, status=status.HTTP_201_CREATED)

    return JsonResponse({'monitor_link_serializer': 'errors'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@authentication_classes([])
@permission_classes([])
def showOnDisplay(request):
    if request.method == 'GET':
        id_monitor = request.GET.get('m', None)
        orientacion = request.GET.get('o', 'H')

        #TODO: Ajustar esto, no debe ir a dos tablas a buscar lo mismo
        monitor = Monitor.objects.filter(_id=id_monitor, monitor_estado=True)[0]
        camara_zona = CamaraZona.objects.values('id_camara_zona').filter(_id=monitor.id_camara_zona, camara_zona_estado=True)[0]
        id_camara_zona = camara_zona['id_camara_zona']
        camara = id_camara_zona.split('_')[0]
        zona = id_camara_zona.split('_')[1]
        context = {'camara': camara, 'zona': zona, 'monitor' : str(monitor._id)}

        if camara is not None and zona is not None:
            return render(request, 'hzfullscreen.html', {'form': context})

        return JsonResponse({'m': id_monitor, 'o': orientacion, 'error:': 'parametros erroneos 1'},
                            status=status.HTTP_400_BAD_REQUEST)

    return JsonResponse({'error:': 'request method not allowed'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
@authentication_classes([])
@permission_classes([])
def configuracion_old(request, id_monitor):
    if request.method == 'GET':
        try:
            # TODO: Ajustar esto, no debe ir a dos tablas a buscar lo mismo
            monitor = Monitor.objects.values().filter(_id=id_monitor, monitor_estado=True)[0]
            camara_zona = CamaraZona.objects.values('id_camara_zona').filter(_id=monitor["id_camara_zona"], camara_zona_estado=True)[0]
            id_camara_zona = camara_zona['id_camara_zona']
            camara_serial = id_camara_zona.split('_')[0]
            zona_numero = id_camara_zona.split('_')[1]
            nro_personas = 0
            #random.randint(0, 50)
            #Obtiene el número de personas en el sitio
            try:
                """conn = MongoClient(settings.DB_IP + ":" + settings.DB_PORT)
                db = conn[settings.DB_NAME]
                collection = db[settings.DB_COLLECTION]
                collection2 = db[settings.DB_COLLECTION2]
                data = collection.find_one({'camara_serial':camara_serial,'zona':zona_numero}, sort=[('_id', pymongo.DESCENDING)])
                data2 = collection2.find_one({})
                if data2 is not None:
                    nro_aforo = data2['nro_aforo']
                else:
                    nro_aforo = 0"""
            except Exception as e:
                print('%s (%s)' % (e, type(e)))
                pass
            monitor_js = {
                "id_camara_zona": monitor["id_camara_zona"],
                "mac_wifi": monitor["mac_wifi"],
                "nro_personas": nro_aforo,
                "aforo_maximo": monitor["aforo_maximo"],
                "texto_barra_cabecera" : monitor ["texto_barra_cabecera"],
                "color_barra_cabecera": monitor["color_barra_cabecera"],
                "logotipo_archivo_nombre": monitor["logotipo_archivo_nombre"],
                "logotipo_posicion": monitor["logotipo_posicion"],
                "fondo_imagen_archivo_nombre": monitor["fondo_imagen_archivo_nombre"],
                "aforo_formato": monitor["aforo_formato"],
                "aforo_mostrar_maximo": monitor["aforo_mostrar_maximo"],
                "aforo_mostrar_casi_lleno": monitor["aforo_mostrar_casi_lleno"],
                "aforo_frase_verde": monitor["aforo_frase_verde"],
                "aforo_frase_ambar": monitor["aforo_frase_ambar"],
                "aforo_frase_rojo": monitor["aforo_frase_rojo"]
            }
            return HttpResponse(simplejson.dumps(monitor_js), content_type='application/json')
        except Exception as e:
            print('%s (%s)' % (e, type(e)))
            return JsonResponse({'m': id_monitor, 'error:': 'parametros erroneos'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        pass
    return JsonResponse({'m': id_monitor, 'error:': 'parametros erroneos 2'},
                        status=status.HTTP_400_BAD_REQUEST)


# def listar_por_id_instalacion(request, id_instalacion):
#     camara_zonas = CamaraZona.objects.all().filter(id_instalacion=id_instalacion, camara_zona_estado=True)
#     camara_zonas_dict = {}
#     for camara_zona in camara_zonas:
#         camara_zonas_dict[str(camara_zona._id)] = camara_zona.id_camara_zona
#     return HttpResponse(simplejson.dumps(camara_zonas_dict), content_type="application/json")

# Las demás
@login_required(login_url="/login/")
def monitor(request):
    activate('es')
    if request.method == "POST":
        form = MonitorForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('/monitor/todos')
            except Exception as e:
                print('%s (%s)' % (e, type(e)))
                pass
    else:
        # return HttpResponseForbidden('allowed only via POST')
        form = MonitorForm()
    return render(request, 'monitor/agregar.html', {'form': form})


@login_required(login_url="/login/")
def todos(request):
    activate('es')
    monitores = Monitor.objects.all()

    for monitor in monitores:
        monitor.id = str(monitor._id)
        #TODO: crear los campos en el modelo de monitor
        camara_zona = CamaraZona.objects.values('id_camara_zona').filter(_id=monitor.id_camara_zona)[:1].get()
        id_camara_zona = camara_zona['id_camara_zona']
        arr_camara_zona = id_camara_zona.split("_", 2)
        if len(arr_camara_zona) > 1:
            monitor.camara_serial = arr_camara_zona[0]
            monitor.zona_numero = arr_camara_zona[1]
        else:
            monitor.camara_serial .camara_serial = ''
            monitor.zona_numero = ''
    return render(request, "monitor/todos.html", {'form': monitores})


@login_required(login_url="/login/")
def editar(request, id):
    activate('es')
    monitor = get_object_or_404(Monitor, _id=id)
    form = MonitorEditarForm(request.POST or None, instance=monitor)
    return render(request, 'monitor/editar.html', {'form': form})


@login_required(login_url="/login/")
def actualizar(request, id):
    activate('es')
    monitor = get_object_or_404(Monitor, _id=id)
    form = MonitorForm(request.POST or None, instance=monitor)
    # form.id_camara_zona = "AAAA-BBBB-CCCC-DDDD_0"

    if form.is_valid():
        form.save()
        return redirect("/monitor/todos")
    return render(request, 'monitor/editar.html', {'form': form})


@login_required(login_url="/login/")
def eliminar(request, id):
    activate('es')
    try:
        monitor = Monitor.objects.get(_id=id)
        monitor.delete()
    except Exception as e:
        print('%s (%s)' % (e, type(e)))
        pass
    # TODO: Enviar mensaje de eliminado
    return redirect("/monitor/todos")


@api_view(['GET', 'POST'])
@authentication_classes([])
@permission_classes([])
def configuracion(request, id_monitor):
    if request.method == 'GET':
        try:
            # TODO: Ajustar esto, no debe ir a dos tablas a buscar lo mismo
            #monitor = Monitor.objects.values().filter(_id=id_monitor, monitor_estado=True)[0]
            monitor = Monitor.objects.values().filter(monitor_estado=True)[0]
            camara_zona = CamaraZona.objects.values('id_camara_zona').filter(_id=monitor["id_camara_zona"], camara_zona_estado=True)[0]
            id_camara_zona = camara_zona['id_camara_zona']
            camara_serial = id_camara_zona.split('_')[0]
            zona_numero = id_camara_zona.split('_')[1]
            nro_personas = 0
            #random.randint(0, 50)
            #Obtiene el número de personas en el sitio
            try:
                
                aforoInfo =  AforoInfo.objects.all()
                 
                print("aforoInfo")
                print(aforoInfo)
                print("aforoInfo.nro_aforo")
                print(aforoInfo.nro_aforo)
                print("aforoInfo.cola")
                print(aforoInfo.cola)
                
                
                #conn = MongoClient(settings.DB_IP + ":" + settings.DB_PORT)
                #conn = MongoClient(settings.DB_FULL)
                """db = conn[settings.DB_NAME]
                collection = db[settings.DB_COLLECTION]
                collection2 = db[settings.DB_COLLECTION2]
                #data = collection.find_one({'camara_serial':camara_serial,'zona':zona_numero}, sort=[('_id', pymongo.DESCENDING)])
                data2 = collection2.find_one({})
                print("data2: ",data2)"""
                if data2 is not None:
                    nro_aforo = data2['nro_aforo']
                else:
                    nro_aforo = 0
            except Exception as e:
                print('%s (%s)' % (e, type(e)))
                pass
            
            monitor_js = {
                "id_camara_zona": monitor["id_camara_zona"],
                "mac_wifi": monitor["mac_wifi"],
                "nro_personas": nro_aforo,
                "aforo_maximo": monitor["aforo_maximo"],
                "texto_barra_cabecera" : monitor ["texto_barra_cabecera"],
                "color_barra_cabecera": monitor["color_barra_cabecera"],
                "logotipo_archivo_nombre": monitor["logotipo_archivo_nombre"],
                "logotipo_posicion": monitor["logotipo_posicion"],
                "fondo_imagen_archivo_nombre": monitor["fondo_imagen_archivo_nombre"],
                "aforo_formato": monitor["aforo_formato"],
                "aforo_mostrar_maximo": monitor["aforo_mostrar_maximo"],
                "aforo_mostrar_casi_lleno": monitor["aforo_mostrar_casi_lleno"],
                "aforo_frase_verde": monitor["aforo_frase_verde"],
                "aforo_frase_ambar": monitor["aforo_frase_ambar"],
                "aforo_frase_rojo": monitor["aforo_frase_rojo"]
            }
            return HttpResponse(simplejson.dumps(monitor_js), content_type='application/json')
        except Exception as e:
            print('%s (%s)' % (e, type(e)))
            return JsonResponse({'m': id_monitor, 'error:': 'parametros erroneos'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        pass
    return JsonResponse({'m': id_monitor, 'error:': 'parametros erroneos 2'},
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@authentication_classes([])
@permission_classes([])
def configuracion_camaras(request, id_monitor):
    if request.method == 'GET':
        try:
            print("configuracion_camaras")
            # TODO: Ajustar esto, no debe ir a dos tablas a buscar lo mismo
             
            #monitor = Monitor.objects.values().filter(_id=id_monitor, monitor_estado=True)[0]
            print("configuracion_camaras2")
            monitor = Monitor.objects.values().filter(monitor_estado=True)[0]
            print("configuracion_camaras3")
            #camara_zona = CamaraZona.objects.values('id_camara_zona').filter(_id=monitor["id_camara_zona"], camara_zona_estado=True)[0]
            
            #id_camara_zona = camara_zona['id_camara_zona']
            id_camara_zona = 0
            print("configuracion_camaras4")
            #camara_serial = id_camara_zona.split('_')[0]
            camara_serial = ""
            print("configuracion_camaras5")
            #zona_numero = id_camara_zona.split('_')[1]
            zona_numero = 0
            print("configuracion_camaras6")
            nro_personas = 0
            camarasAll =  Camaras.objects.all()
            print("antes1")
            #random.randint(0, 50)
            #Obtiene el número de personas en el sitio
         
            



            try:
                """print(settings.DB_IP)
                print(settings.DB_PORT)
                print(settings.DB_NAME)
                conn = MongoClient(settings.DB_FULL)
                db = conn[settings.DB_NAME]
                collection = db[settings.DB_COLLECTION]
                collection2 = db[settings.DB_COLLECTION2]
                #data = collection.find_one({'camara_serial':camara_serial,'zona':zona_numero}, sort=[('_id', pymongo.DESCENDING)])
                data2 = collection2.find_one({})
                print("data2")
                print(data2)"""
                if data2 is not None:
                    nro_aforo = data2['nro_aforo']
                    print("nro_aforo")
                    print(nro_aforo)

                   


                else:
                    nro_aforo = 0
                
                print("antes del for")
                print("len camaras")
                print(len(camarasAll))
                for camaras in camarasAll:
                    print("1")
                    print(camaras._id)
                    print("2")
                    print(camaras.nombre_camara)
                    print(camaras.nro_personas)
                    print("3")
                    print(camaras.serial_camara)
                    print("4")
                    #print(camaras.instalacion.nombre)
                    #camaras.instalacion = model_to_dict(camaras.instalacion)
                    zonas_camaras = []
                    for zonas_camara in camaras.zonas_camara:
                        print(zonas_camara.nombre_zona_camara)
                        print(zonas_camara.nro_personas)
                        zonas_camara = model_to_dict(zonas_camara)
                        zonas_camaras.append(zonas_camara)
                        print("zonas_camara")
                        print(zonas_camara)
                        
                    camaras.zonas_camara = zonas_camaras
                   #camaras =  model_to_dict(camaras)
                   
                camaras_serialize = serializers.serialize('json', camarasAll)
                #zonas_camaras = []#camaras.zonas_camara
                print("camaras_serialize")
                print(camaras_serialize)
                #print("zonas_camaras")
                #print(zonas_camaras)
            except Exception as e:
                print('%s (%s)' % (e, type(e)))
                pass
            monitor_js = {
                "id_camara_zona": monitor["id_camara_zona"],
                "mac_wifi": monitor["mac_wifi"],
                "nro_personas": nro_aforo,
                "aforo_maximo": monitor["aforo_maximo"],
                "texto_barra_cabecera" : monitor ["texto_barra_cabecera"],
                "color_barra_cabecera": monitor["color_barra_cabecera"],
                "logotipo_archivo_nombre": monitor["logotipo_archivo_nombre"],
                "logotipo_posicion": monitor["logotipo_posicion"],
                "fondo_imagen_archivo_nombre": monitor["fondo_imagen_archivo_nombre"],
                "aforo_formato": monitor["aforo_formato"],
                "aforo_mostrar_maximo": monitor["aforo_mostrar_maximo"],
                "aforo_mostrar_casi_lleno": monitor["aforo_mostrar_casi_lleno"],
                "aforo_frase_verde": monitor["aforo_frase_verde"],
                "aforo_frase_ambar": monitor["aforo_frase_ambar"],
                "aforo_frase_rojo": monitor["aforo_frase_rojo"],
                #"zonas_camaras":zonas_camaras,
                "camaras": camaras_serialize
            }
            return HttpResponse(simplejson.dumps(monitor_js), content_type='application/json')
        except Exception as e:
            print('%s (%s)' % (e, type(e)))
            return JsonResponse({'m': id_monitor, 'error:': 'parametros erroneos'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        pass
    return JsonResponse({'m': id_monitor, 'error:': 'parametros erroneos 2'},
                        status=status.HTTP_400_BAD_REQUEST)
