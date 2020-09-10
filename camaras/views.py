# -*- encoding: utf-8 -*-
from djongo import models
import simplejson
from django.http import HttpResponse
import random
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils.translation import activate

from rest_framework import views, status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.conf import settings

from django.contrib.auth.decorators import login_required
from djongo import models
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.utils.translation import activate
from camaras.forms import CamarasForm
from camaras.models import Camaras
from aforoInfo.models import AforoInfo
from monitor.models import Monitor
from django.forms.models import model_to_dict
from django.core import serializers

import calendar
import datetime
import pytz
from datetime import date
today = date.today()

@login_required(login_url="/login/")
def camaras(request):
    activate('es')
    if request.method == "POST":
        form = CamarasForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/camaras/todos')
            except Exception as e:
                print('%s (%s)' % (e, type(e)))
                pass
        else:
            print('no valido')
    else:
        form = CamarasForm()
    if form.errors:
        for field in form:
            for error in field.errors:
                print("field.name")
                print(field.name)
                #print(field.name % " | " % error)

                print(error)
        # for error in form.non_field_errors:
        #     print('NFE | ')
        #     print(error)
    return render(request, 'camaras/agregar.html', {'form': form})


@login_required(login_url="/login/")
def todos(request):
    activate('es')
    if request.user.is_staff:
        camarasAll =  Camaras.objects.all()
    elif hasattr(request.user, 'cliente') and (request.user.cliente.get_id() is not None):
        camaras  = Camara.objects.filter(id_cliente=request.user.cliente.get_id())
        for camaras in camarasAll:
            camaras.id = str(camaras._id)
        return render(request, "camaras/todos.html", {'form': camarasAll})
    

@login_required(login_url="/login/")
def editar(request, id):
    activate('es')
    camaras = get_object_or_404(Camaras, _id=id)
    form = CamarasForm(request.POST or None, instance=camaras)
    return render(request, 'camaras/editar.html', { 'form' : form })


@login_required(login_url="/login/")
def actualizar(request, id):
    activate('es')
    camaras = get_object_or_404(Camaras, _id=id)
    form = CamarasForm(request.POST or None, instance=camaras)
    if form.is_valid():
        form.save()
        return redirect("/camaras/todos")
    return render(request, 'camaras/editar.html', { 'form' : form })


@login_required(login_url="/login/")
def eliminar(request, id):
    activate('es')
    try:
        camaras = Camaras.objects.get(_id=id)
        camaras.delete()
    except Exception as e:
        print('%s (%s)' % (e, type(e)))
        pass
    #TODO: Enviar mensaje de eliminado
    return redirect("/camaras/todos")


@api_view(['GET', 'POST'])
@authentication_classes([])
@permission_classes([])
def configuracion_camaras(request, id_monitor):
    #print("configuracion_camaras")
    if request.method == 'GET':
        try:           
            
          



            id_camara_zona = 0         
            camara_serial = ""         
            zona_numero = 0            
            nro_personas = 0       
            nro_aforo = 0
            #random.randint(0, 50)
            #Obtiene el número de personas en el sitio
            try:
                camarasAll =  Camaras.objects.all()
                monitor = Monitor.objects.values().filter(monitor_estado=True)[0]
                aforoInfo =  AforoInfo.objects.first()
                  
                if aforoInfo is not None:
                    nro_aforo = aforoInfo.nro_aforo
                
                for camaras in camarasAll:
                    #print(camaras._id)                
                    #print(camaras.nombre_camara)                
                    #print(camaras.serial_camara)

                    zonas_camaras = []
                    for zonas_camara in camaras.zonas_camara:
                        zonas_camara = model_to_dict(zonas_camara)
                        zonas_camaras.append(zonas_camara)
                        
                    camaras.zonas_camara = zonas_camaras
                   
                   
                camaras_serialize = serializers.serialize('json', camarasAll)
                
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




@api_view(['GET', 'POST'])
@authentication_classes([])
@permission_classes([])
def configuracion(request, id_monitor):
    #print("configuracion")
    if request.method == 'GET':
        try:
            
            monitor = Monitor.objects.values().filter(monitor_estado=True)[0]
            id_camara_zona = 0            
            camara_serial = ""            
            zona_numero = 0
            nro_personas = 0
            camarasAll =  Camaras.objects.all()


            mond_info =0
            tues_info = 0
            wedn_info = 0
            thur_info = 0
            frid_info =0
            satu_info = 0
            sund_infor = 0
            total_day_info =0
            grafica_info = [1,2,3,4,5,6,7,8,9]
            

            nro_aforo = 0

            try:
                aforoInfo =  AforoInfo.objects.first()  
                if aforoInfo is not None:                   
                    nro_aforo = aforoInfo.nro_aforo


                    total_day_info = aforoInfo.nro_aforo
                    date =today.strftime("%d, %m, %Y")
                    #print(date)
                    Date = datetime.datetime.strptime(date, '%d, %m, %Y').weekday()
                    


                    print(Date)
                    if Date==0:
                        total_day_info = aforoInfo.nro_aforo
                        mond_info =total_day_info
                        grafica_info.append(mond_info)
                        
                        print("l")
                    elif Date==1:
                        total_day_info = aforoInfo.nro_aforo
                        tues_info =total_day_info 
                        print("m")
                        
                        grafica_info.append(mond_info)
                        print(grafica_info)
                    elif Date==2:
                        total_day_info = aforoInfo.nro_aforo
                        wedn_info =total_day_info
                        print("m")
                        grafica_info.append(tues_info)
                        print(grafica_info)
                    elif Date==3:
                        total_day_info = aforoInfo.nro_aforo
                        thur_info =total_day_info
                        print("j")
                        grafica_info.append(thur_info)
                        print(grafica_info)
                    elif Date==4:
                        total_day_info = aforoInfo.nro_aforo
                        frid_info =total_day_info
                        print("v")
                        grafica_info.append(frid_info)
                        print(grafica_info)
                    elif Date==5:
                        total_day_info = aforoInfo.nro_aforo
                        satu_info =total_day_info
                        print("s")
                        grafica_info.append(satu_info)
                        print(grafica_info)
                    elif Date==6:
                        total_day_info = aforoInfo.nro_aforo
                        sund_info =total_day_info
                        print("d") 
                        grafica_info.append(sund_info)
                        print(grafica_info)


                
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
            }
            return HttpResponse(simplejson.dumps(monitor_js), content_type='application/json')
        except Exception as e:
            print('%s (%s)' % (e, type(e)))
            return JsonResponse({'m': id_monitor, 'error:': 'parametros erroneos'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        pass
    return JsonResponse({'m': id_monitor, 'error:': 'parametros erroneos 2'},
                        status=status.HTTP_400_BAD_REQUEST)
