# -*- encoding: utf-8 -*-
import simplejson as simplejson
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from djongo import models
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.utils.translation import activate
from fondos.forms import FondosForm,FondosEditarForm
from fondos.models import Fondos
from uploadfile import UpLoadFile
import os
from django.conf import settings
from instalacion.models import Instalacion
from cliente.models import Cliente

@login_required(login_url="/login/")
def fondos(request):
    activate('es')
    url_media = request.build_absolute_uri('/mosayk/')
    if request.method == "POST" and request.FILES['uploadVerde'] and request.FILES['uploadAmbar'] and request.FILES['uploadRojo'] and request.FILES['uploadCierre']:       
        form = FondosForm(request.POST)        
        if form.is_valid():
            try:
                #dir="F1000/panaderia1/imagen/" 
                print("if")
                print("@@@@@@@@@@@@@@@request.POST")
                print(request.POST)
                numero_cliente = form.cleaned_data['numero_cliente']                
                print("numero_cliente: ",numero_cliente)
                nombre_instalacion = request.POST['instalacion-nombre']
                print("nombre_instalacion: ",nombre_instalacion)
                nombre_directorio = nombreDirCliente(numero_cliente, nombre_instalacion)               
                createDirCliente(nombre_directorio)                        
                UpLoadFile().send(request.FILES['uploadVerde'],nombre_directorio)
                UpLoadFile().send(request.FILES['uploadAmbar'],nombre_directorio)
                UpLoadFile().send(request.FILES['uploadRojo'],nombre_directorio)
                UpLoadFile().send(request.FILES['uploadCierre'],nombre_directorio)
                form.save()
                return redirect('/fondos/todos')
            except:
                pass
    else:
        form = FondosForm()
    if form.errors:
        for field in form:
            for error in field.errors:
                print(field.name)

                print(error)
        # for error in form.non_field_errors:
        #     print('NFE | ')
        #     print(error)
    return render(request, 'fondos/agregar.html', {'form': form,'url_media':url_media})



@login_required(login_url="/login/")
def todos(request):
    activate('es')
    fondosTodos = {}
    #if request.user.is_staff:
    fondosTodos = Fondos.objects.all()
        
    #elif hasattr(request.user, 'cliente') and (request.user.cliente.get_id() is not None):
        
    #    instalaciones  = Instalacion.objects.filter(id_cliente=request.user.cliente.get_id())

    for fondos in fondosTodos:
        fondos.id = str(fondos._id)

    return render(request, "fondos/todos.html", {'fondosTodos': fondosTodos})


@login_required(login_url="/login/")
def editar(request, id):
    activate('es')
    url_media = request.build_absolute_uri('/mosayk/')
    fondos = get_object_or_404(Fondos, _id=id)
    print(fondos)
    form = FondosEditarForm(request.POST or None, instance=fondos)
 
    return render(request, 'fondos/editar.html', { 'form' : form, 'url_media':url_media  })


@login_required(login_url="/login/")
def actualizar(request, id):
    activate('es')
    fondos = get_object_or_404(Fondos, _id=id)
    form = FondosEditarForm(request.POST or None, instance=fondos)
    if form.is_valid():
        
        numero_cliente = form.cleaned_data['numero_cliente']                
        print("numero_cliente: ",numero_cliente)
        nombre_instalacion = request.POST['instalacion-nombre']
        print("nombre_instalacion: ",nombre_instalacion)
        nombre_directorio = nombreDirCliente(numero_cliente, nombre_instalacion)               
        createDirCliente(nombre_directorio)
                     
        if 'uploadVerde' in request.FILES:
             UpLoadFile().send(request.FILES['uploadVerde'],nombre_directorio)
             
        if 'uploadAmbar' in request.FILES:
            UpLoadFile().send(request.FILES['uploadAmbar'],nombre_directorio)
            
        if 'uploadRojo' in request.FILES:
            UpLoadFile().send(request.FILES['uploadRojo'],nombre_directorio)
        
        if 'uploadCierre' in request.FILES:
            UpLoadFile().send(request.FILES['uploadCierre'],nombre_directorio)        
                    
        form.save()
        return redirect("/fondos/todos")
    if form.errors:
      for field in form:
          for error in field.errors:
              print(field.name)
    
              print(error)
      # for error in form.non_field_errors:
      #     print('NFE | ')
      #     print(error)
    return render(request, 'fondos/editar.html', { 'form' : form })


@login_required(login_url="/login/")
def eliminar(request, id):
    activate('es')
    try:
        fondos = Fondos.objects.get(_id=id)
        fondos.delete()
    except Exception as e:
        print('%s (%s)' % (e, type(e)))
        pass
    return redirect("/fondos/todos")

def createDirCliente(directorio):        
    if not os.path.exists(os.path.join(settings.MEDIA_ROOT, directorio)):        
        os.makedirs(os.path.join(settings.MEDIA_ROOT, directorio))

def nombreDirCliente(numero_cliente,nombre_instalacion):
    
    dir = numero_cliente+"/"+nombre_instalacion+"/"+"imagen/"
    dir = dir.replace(" ","_")
    print("dir: ",dir)        
    return dir
    
def listar_por_nif_cliente(request, nif_cliente): 
    
    cliente = Cliente.objects.values('numero_cliente').get(nif=nif_cliente, cliente_estado=True)    
    instalaciones = Instalacion.objects.all().filter(cliente={'nif': nif_cliente}, instalacion_estado=True)        
    instalaciones_dict = {}
    for instalacion in instalaciones:
        instalaciones_dict[str(instalacion.nombre_comercial)] = instalacion.nombre_comercial
    
    instalacion_js = {
        "instalaciones": instalaciones_dict,
        "cliente": cliente
    }
    return HttpResponse(simplejson.dumps(instalacion_js), content_type ="application/json")



