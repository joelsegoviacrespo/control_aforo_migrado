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

def hfs(request):
    context = {'foo': 'bar'}
    #return render(request, 'index.html', context) #si request es none entonces no rpesta atencion al context
    return render(request, 'hzfullscreen_bu.html', context)


@login_required(login_url="/login/")
def index(request):
    camarasAll =  Camaras.objects.all()
   
    return render(request, "index.html",  {'camaras':camarasAll})
 

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

