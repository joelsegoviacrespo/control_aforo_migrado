# -*- encoding: utf-8 -*-
import simplejson as simplejson
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from djongo import models
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.utils.translation import activate
from instalacion.forms import InstalacionForm,InstalacionEditarForm
from instalacion.models import Instalacion


@login_required(login_url="/login/")
def instalacion(request):
    activate('es')
    if request.method == "POST":
        form = InstalacionForm(request.POST)        
        if form.is_valid():
            try:
                form.save()
                return redirect('/instalacion/todos')
            except:
                pass
    else:
        form = InstalacionForm()
    if form.errors:
        for field in form:
            for error in field.errors:
                print(field.name)

                print(error)
        # for error in form.non_field_errors:
        #     print('NFE | ')
        #     print(error)
    return render(request, 'instalacion/agregar.html', {'form': form})



@login_required(login_url="/login/")
def todos(request):
    activate('es')
    instalaciones = {}
    #if request.user.is_staff:
    instalaciones = Instalacion.objects.all()
        
    #elif hasattr(request.user, 'cliente') and (request.user.cliente.get_id() is not None):
        
    #    instalaciones  = Instalacion.objects.filter(id_cliente=request.user.cliente.get_id())

    for instalacion in instalaciones:
        instalacion.id = str(instalacion._id)

    return render(request, "instalacion/todos.html", {'instalaciones': instalaciones})


@login_required(login_url="/login/")
def editar(request, id):
    activate('es')
    instalacion = get_object_or_404(Instalacion, _id=id)
    #myObj = Instalacion.objects.values('cliente')
    #print("instalacion.cliente.nif")
    
    #print(instalacion.cliente.nif)
    
    #print("myObj")
    #print(myObj)
    
    form = InstalacionEditarForm(request.POST or None, instance=instalacion)
 
    return render(request, 'instalacion/editar.html', { 'form' : form })


@login_required(login_url="/login/")
def actualizar(request, id):
    activate('es')
    instalacion = get_object_or_404(Instalacion, _id=id)
    form = InstalacionEditarForm(request.POST or None, instance=instalacion)
    if form.is_valid():
        form.save()
        return redirect("/instalacion/todos")
    return render(request, 'instalacion/editar.html', { 'form' : form })


@login_required(login_url="/login/")
def eliminar(request, id):
    activate('es')
    try:
        instalacion = Instalacion.objects.get(_id=id)
        instalacion.delete()
    except Exception as e:
        print('%s (%s)' % (e, type(e)))
        pass
    return redirect("/instalacion/todos")


def listar_por_id_cliente(request, id_cliente):
    instalaciones = Instalacion.objects.all().filter(id_cliente=id_cliente, instalacion_estado=True)
    instalaciones_dict = {}
    for instalacion in instalaciones:
        instalaciones_dict[str(instalacion._id)] = instalacion.nombre_comercial
    return HttpResponse(simplejson.dumps(instalaciones_dict), content_type ="application/json")