# -*- encoding: utf-8 -*-
import simplejson as simplejson
from django.contrib.auth.decorators import login_required,permission_required
from django.http import HttpResponse
from djongo import models
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.utils.translation import activate
from valores.forms import ValoresForm,ValoresEditarForm
from valores.models import Valores
import Constantes


@login_required(login_url="/login/")
@permission_required('valores.add_valores',login_url="/logout/")
def valores(request):
    activate('es')
    if request.method == "POST":       
        form = ValoresForm(request.POST)        
        if form.is_valid():
            try:
                form.save()
                return redirect('/valores/todos')
            except:
                pass
    else:
        form = ValoresForm()
    if form.errors:
        for field in form:
            for error in field.errors:
                print(field.name)

                print(error)
        # for error in form.non_field_errors:
        #     print('NFE | ')
        #     print(error)
    return render(request, 'valores/agregar.html', {'form': form})



@login_required(login_url="/login/")
@permission_required('valores.view_valores',login_url="/logout/")
def todos(request):
    activate('es')
    valoresTodos = {}
    
    if (request.user.profile.rol== Constantes.SUPERUSUARIO):
        valoresTodos = Valores.objects.all()
        
    elif (request.user.profile.rol == Constantes.ADMINISTRADOR) and hasattr(request.user.profile, 'cliente') and (request.user.profile.cliente.get_id() is not None):
            valoresTodos = Valores.objects.all().filter(instalacion={'nif_cliente': request.user.profile.cliente.nif})

    elif (request.user.profile.rol > Constantes.ADMINISTRADOR) and hasattr(request.user.profile, 'cliente') and (request.user.profile.cliente.get_id() is not None):
          if hasattr(request.user.profile, 'instalacion') and hasattr(request.user.profile.instalacion, 'get_id') and (request.user.profile.instalacion.get_id() is not None):
              valoresTodos = Valores.objects.all().filter(instalacion={'nif_cliente': request.user.profile.cliente.nif} and {'nombre': request.user.profile.instalacion.nombre_comercial})

            
   

    for valores in valoresTodos:
        valores.id = str(valores._id)

    return render(request, "valores/todos.html", {'valoresTodos': valoresTodos})

@login_required(login_url="/login/")
@permission_required('valores.change_valores',login_url="/logout/")
def editar(request, id):
    activate('es')
    valores = get_object_or_404(Valores, _id=id)
    #Aqui verifico si un cliente coloca una url en el navegador, 
    #si la url que contienela instalacion no pertenece al cliente 
    #logueado lo enviaa la url login
    if (request.user.profile.rol == Constantes.ADMINISTRADOR) and hasattr(request.user.profile, 'cliente') and (request.user.profile.cliente.get_id() is not None):                
        if (request.user.profile.cliente.nif != valores.instalacion.nif_cliente):            
            return redirect('/accounts/logout/')
    
    form = ValoresEditarForm(request.POST or None, instance=valores)
 
    return render(request, 'valores/editar.html', { 'form' : form })


@login_required(login_url="/login/")
@permission_required('valores.change_valores',login_url="/logout/")
def actualizar(request, id):
    activate('es')
    valores = get_object_or_404(Valores, _id=id)
    form = ValoresEditarForm(request.POST or None, instance=valores)
    if form.is_valid():
        form.save()
        return redirect("/valores/todos")
    if form.errors:
      for field in form:
          for error in field.errors:
              print(field.name)
    
              print(error)
      # for error in form.non_field_errors:
      #     print('NFE | ')
      #     print(error)
    return render(request, 'valores/editar.html', { 'form' : form })


@login_required(login_url="/login/")
@permission_required('valores.delete_valores',login_url="/logout/")
def eliminar(request, id):
    activate('es')
    try:
        valores = Valores.objects.get(_id=id)
        if (request.user.profile.rol == Constantes.ADMINISTRADOR) and hasattr(request.user.profile, 'cliente') and (request.user.profile.cliente.get_id() is not None):                
            if (request.user.profile.cliente.nif != valores.instalacion.nif_cliente):            
                return redirect('/accounts/logout/')
        valores.delete()
    except Exception as e:
        print('%s (%s)' % (e, type(e)))
        pass
    return redirect("/valores/todos")


