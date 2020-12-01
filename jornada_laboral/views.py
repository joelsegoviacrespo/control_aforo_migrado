# -*- encoding: utf-8 -*-
import simplejson as simplejson
from django.contrib.auth.decorators import login_required,permission_required
from django.http import HttpResponse
from djongo import models
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.utils.translation import activate
from jornada_laboral.forms import JornadaLaboralForm,JornadaLaboralEditarForm
from jornada_laboral.models import JornadaLaboral
import Constantes


@login_required(login_url="/login/")
@permission_required('valores.add_valores',login_url="/logout/")
def jornada_laboral(request):
    activate('es')
    if request.method == "POST":       
        form = JornadaLaboralForm(request.POST)        
        if form.is_valid():
            try:
                form.save()
                return redirect('/jornada_laboral/todos')
            except:
                pass
    else:
        form = JornadaLaboralForm()
    if form.errors:
        for field in form:
            for error in field.errors:
                print(field.name)

                print(error)
        # for error in form.non_field_errors:
        #     print('NFE | ')
        #     print(error)
    return render(request, 'jornada_laboral/agregar.html', {'form': form})



@login_required(login_url="/login/")
@permission_required('valores.view_valores',login_url="/logout/")
def todos(request):
    activate('es')
    jornadaTodos = {}
    
    if (request.user.profile.rol== Constantes.SUPERUSUARIO):
        jornadaTodos = JornadaLaboral.objects.all()
        
    elif (request.user.profile.rol == Constantes.ADMINISTRADOR) and hasattr(request.user.profile, 'cliente') and (request.user.profile.cliente.get_id() is not None):
            jornadaTodos = JornadaLaboral.objects.all().filter(instalacion={'nif_cliente': request.user.profile.cliente.nif})

    elif (request.user.profile.rol > Constantes.ADMINISTRADOR) and hasattr(request.user.profile, 'cliente') and (request.user.profile.cliente.get_id() is not None):
          if hasattr(request.user.profile, 'instalacion') and hasattr(request.user.profile.instalacion, 'get_id') and (request.user.profile.instalacion.get_id() is not None):
              jornadaTodos = JornadaLaboral.objects.all().filter(instalacion={'nif_cliente': request.user.profile.cliente.nif} and {'nombre': request.user.profile.instalacion.nombre_comercial})

            
   

    for jornada in jornadaTodos:
        jornada.id = str(jornada._id)

    return render(request, "jornada_laboral/todos.html", {'jornadaTodos': jornadaTodos})

@login_required(login_url="/login/")
@permission_required('valores.change_valores',login_url="/logout/")
def editar(request, id):
    activate('es')
    jornada = get_object_or_404(JornadaLaboral, _id=id)
    #Aqui verifico si un cliente coloca una url en el navegador, 
    #si la url que contienela instalacion no pertenece al cliente 
    #logueado lo enviaa la url login
    if (request.user.profile.rol == Constantes.ADMINISTRADOR) and hasattr(request.user.profile, 'cliente') and (request.user.profile.cliente.get_id() is not None):                
        if (request.user.profile.cliente.nif != jornada.instalacion.nif_cliente):            
            return redirect('/accounts/logout/')
    
    form = JornadaLaboralEditarForm(request.POST or None, instance=jornada)
 
    return render(request, 'jornada_laboral/editar.html', { 'form' : form })


@login_required(login_url="/login/")
@permission_required('valores.change_valores',login_url="/logout/")
def actualizar(request, id):
    activate('es')
    jornada = get_object_or_404(JornadaLaboral, _id=id)
    form = JornadaLaboralEditarForm(request.POST or None, instance=jornada)
    if form.is_valid():
        form.save()
        return redirect("/jornada_laboral/todos")
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
        jornada = jornada_laboral.objects.get(_id=id)
        if (request.user.profile.rol == Constantes.ADMINISTRADOR) and hasattr(request.user.profile, 'cliente') and (request.user.profile.cliente.get_id() is not None):                
            if (request.user.profile.cliente.nif != jornada.instalacion.nif_cliente):            
                return redirect('/accounts/logout/')
        jornada.delete()
    except Exception as e:
        print('%s (%s)' % (e, type(e)))
        pass
    return redirect("/jornada_laboral/todos")


