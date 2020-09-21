# -*- encoding: utf-8 -*-
import simplejson as simplejson
from django.contrib.auth.decorators import login_required,permission_required
from django.http import HttpResponse
from djongo import models
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.utils.translation import activate
from display.forms import DisplayForm
from display.models import Display
import Constantes
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from camaras.models import Camaras
import time

@login_required(login_url="/login/")
#@permission_required('valores.add_valores',login_url="/logout/")
def display(request):
    activate('es')
    if request.method == "POST":       
        form = DisplayForm(request.POST)        
        if form.is_valid():
            try:
                form.save()
                return redirect('/valores/todos')
            except:
                pass
    else:
        form = DisplayForm()
    if form.errors:
        for field in form:
            for error in field.errors:
                print(field.name)

                print(error)
        # for error in form.non_field_errors:
        #     print('NFE | ')
        #     print(error)
    return render(request, 'display/agregar.html', {'form': form})




@api_view(['GET', 'POST'])
@authentication_classes([])
@permission_classes([])
def configuracion(request, id_display):
    
    if request.method == 'GET':
        try:            
            display = Display.objects.filter(_id = id_display,activo=True).first()
            horario_laboral = False            
            #Convierto la hora de apertura y cierre
            hora_apertura = display.fondos.hora_apertura.strftime("%H:%M:%S")
            hora_cierre = display.fondos.hora_cierre.strftime("%H:%M:%S")
            #Calculo la Hora Actual
            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)
            #print(current_time)
            #print(hora_apertura)
            #print(hora_cierre)
            
            if (current_time>= hora_apertura) and (current_time<= hora_cierre):
                horario_laboral = True
              
            try:                
                nro_aforo = 0
                camarasAll =  Camaras.objects.all()
                i=0
                for camaras in camarasAll:
                    j=0                   
                    for zonas_camara in camaras.zonas_camara:
                        if (i==0 and j==0):                                                 
                            nro_aforo = zonas_camara.nro_personas                            
                        j = j+1
                    i= i+1  


                
            except Exception as e:
                print('%s (%s)' % (e, type(e)))
                pass
            display_js = {                
                "url_verde": display.fondos.url_verde,     
                "url_ambar": display.fondos.url_ambar,    
                "url_rojo": display.fondos.url_rojo,    
                "url_cerrado": display.fondos.url_cerrado,     
                "hora_apertura": str(display.fondos.hora_apertura), 
                "hora_cierre": str(display.fondos.hora_cierre),    
                "maximo_aforo": display.valores.maximo_aforo,
                "mostrar_valor": display.valores.mostrar_valor,
                "mostrar_capacidad": display.valores.mostrar_capacidad,
                "mostrar_ambar": display.valores.mostrar_ambar,   
                "posicion_reloj": display.posicion.posicion_reloj,
                "color": display.posicion.color,                 
                "nro_personas": nro_aforo,
                "horario_laboral": horario_laboral
                
            }
            return HttpResponse(simplejson.dumps(display_js), content_type='application/json')
        except Exception as e:
            print('%s (%s)' % (e, type(e)))
            return JsonResponse({'m': id_display, 'error:': 'parametros erroneos'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        pass
    return JsonResponse({'m': id_display, 'error:': 'parametros erroneos 2'},
                        status=status.HTTP_400_BAD_REQUEST)

