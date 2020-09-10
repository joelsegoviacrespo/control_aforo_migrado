# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django import template
from camaras.models import Camaras


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
#from urllib.request import urlopen
#from urllib.request.urlopen import urlopen

def hfs(request):
    context = {'foo': 'bar'}
    #return render(request, 'index.html', context) #si request es none entonces no rpesta atencion al context
    return render(request, 'hzfullscreen_bu.html', context)


@login_required(login_url="/login/")
def index(request):
    camarasAll =  Camaras.objects.all()
    zonas_camaras = []
    url = "https://api.meraki.com/api/v1/devices/Q2HV-B24V-ZKN5/camera/generateSnapshot"
    #url2= "https://api.meraki.com/api/v1/devices/Q2GV-4YBM-YWWJ/camera/generateSnapshot"
    a=1
    b=2
    formeee = {}
    for camaras in camarasAll:
                    #print("1")
                    #print(camaras._id)
                    #print("2")
                    #print(camaras.nombre_camara)
                    #print("3")
                    #print(camaras.serial_camara)
                    #print("4")
                   # print(camaras.instalacion.nombre)
                    #camaras.instalacion = model_to_dict(camaras.instalacion)
                    zonas_camaras = []
                    

                    
                    
                    #print ("serial camaras")
                    #print (camaras.serial_camara)
                    
                    for zonas_camara in camaras.serial_camara:
                        #print(camaras.serial_camara)
                        url = "https://api.meraki.com/api/v1/devices/Q2HV-B24V-ZKN5/camera/generateSnapshot"
                        url2 = "https://api.meraki.com/api/v1/devices/Q2GV-4YBM-YWWJ/camera/generateSnapshot"  
                        #print(url)
                        #consulta a meraki

                        payload = {}
                        headers = {
                        'X-Cisco-Meraki-API-Key': '920a310b87feb3832739a79d573845404c6825d0',
                        'Content-Type': 'application/json'
                        }
                        response = {}
                        response2 = {}
                        
                        
                        #print(zonas_camara.nombre_zona_camara)
                        #print(zonas_camara.nro_personas)
                        #zonas_camara = model_to_dict(zonas_camara)
                        zonas_camaras.append(zonas_camara)
                        #print("zonas_camara")
                        #rint(zonas_camaras)
                    
                        camaras.zonas_camara = zonas_camaras
                        response = requests.request("POST", url, headers=headers, data = payload)
                        #print(response.response, flush=True)
                        response2= requests.request("POST",url2 ,headers=headers, data = payload)
                        #print ("response2")
                        #print(response)
                        #print (response2)
                        if(not response and not response2):
                            extract = "/static/assets/img/people.jpg"
                        
                        else:
                            urlResponse = json.loads(response.text)
                            urlResponse2 = json.loads(response2.text)
                            extract = urlResponse.get('url')
                            extract2= urlResponse2.get('url')
                            #print(extract)
                            #print(extract2)
                            #consulta a meraki
                            urls= {"meraki":extract,"meraki2":extract2}
                            zonas_camaras.append = (urls)
                            camarasAll =  Camaras.objects.all()
                            #camarasAll.append({"urls":{"meraki":extract,"meraki2":extract2}})
                            serial = camaras.serial_camara
                            
                            #                   extract = urlResponse.get('url')
                            #result = urllib.request.urlopen(extract)
                            #htmlSource = base64.b64encode(result.read())      
                            #print(result)
    if request.user.is_staff:
                            
                                #instalaciones = Instalacion.objects.filter('cliente':)
                                
        formeee = {'foo': 'staff', 'meraki' : extract, 'serial':serial, 'meraki2':extract2}
        print ("el forme del staff:"+formeee)
                                #form2 ={'foo':'staff','meraki': response2}
    else:
        id_cliente = 0
        id_instalacion = 0
        monitores = {}
        estadisticas = {}
        if hasattr(request.user, 'cliente'):            
            id_cliente = request.user.cliente.get_id()        
            id_instalacion = Instalacion.objects.values('_id').filter(id_cliente_id=id_cliente, instalacion_estado=True)[0]       
            monitores = Monitor.objects.filter(id_instalacion_id=id_instalacion, monitor_estado=True) 
            formeee = {'id_cliente': id_cliente, 'monitores' : monitores, 'estadisticas' : estadisticas, 'meraki' : extract, 'serial':serial, 'meraki2':extract2}
            print("Este es del else:"+formeee)

                                    #form2 = {'id_cliente' : id_cliente, 'monitores' : monitores, 'estadisticas' : estadisticas, 'meraki' : response2} 


                                #ninguno de los prints se imprimen
                                #print(post, flush=True)
                                #print(result.text.encode('utf8'),flush = True)


                                #variable con la url extraida y convertida a base64 
                                #result = base64.b64encode(urlopen(urlResponse.get('url')).read())

                                #print(result, flush=True)  
                                #print(response2.text.encode('utf8', {'flush': form2})) 
    formeee={'meraki':extract,'meraki2':extract2}
    print ("Objeto completo de camaras:",camarasAll)
    return render(request, "index.html",  {'formee': formeee,'camaras':camarasAll})
                                

                                





    
  
   
            #agregado para hacer debug no funciona logging
            #fmt = getattr(settings, 'LOG_FORMAT', None)
            #lvl = getattr(settings, 'LOG_LEVEL', logging.DEBUG)
            #logging.basicConfig(format=fmt, level=lvl)
            #logging.debug("Logging started on %s for %s" % (logging.root.name, logging.getLevelName(lvl)))
            #logging.debug("Oh hai!----------------------------")
   
  

    
    #return render(request, "index.html", {'form2':form2})

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

