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

from instalacion.models import Instalacion
from monitor.models import Monitor


def hfs(request):
    context = {'foo': 'bar'}
    #return render(request, 'index.html', context) si request es none entonces no rpesta atencion al context
    return render(request, 'hzfullscreen_bu.html', context)


@login_required(login_url="/login/")
def index(request):

    if request.user.is_staff:

        #instalaciones = Instalacion.objects.filter('cliente':)
        form = {'foo': 'staff'}
    else:
        id_cliente = 0
        id_instalacion = 0
        monitores = {}
        estadisticas = {}
        if hasattr(request.user, 'cliente'):            
           id_cliente = request.user.cliente.get_id()        
           id_instalacion = Instalacion.objects.values('_id').filter(id_cliente_id=id_cliente, instalacion_estado=True)[0]       
           monitores = Monitor.objects.filter(id_instalacion_id=id_instalacion, monitor_estado=True)  
      
        form = {'id_cliente': id_cliente, 'monitores' : monitores, 'estadisticas' : estadisticas}

    return render(request, "index.html",  {'form': form})

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
