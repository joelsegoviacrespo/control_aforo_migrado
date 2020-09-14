# -*- encoding: utf-8 -*-
import simplejson as simplejson
from django.contrib.auth.decorators import login_required,permission_required
from django.http import HttpResponse
from djongo import models
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.utils.translation import activate
from instalacion.forms import InstalacionForm,InstalacionEditarForm
from instalacion.models import Instalacion
import Constantes


@login_required(login_url="/login/")
@permission_required('instalacion.add_instalacion',login_url="/logout/")
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
@permission_required('instalacion.view_instalacion',login_url="/logout/")
def todos(request):
    activate('es')
    instalaciones = {}   
        
    
    if (request.user.profile.rol== Constantes.SUPERUSUARIO):    
        instalaciones = Instalacion.objects.all()
        
    elif (request.user.profile.rol == Constantes.ADMINISTRADOR) and hasattr(request.user.profile, 'cliente') and (request.user.profile.cliente.get_id() is not None):      
        instalaciones = Instalacion.objects.all().filter(cliente={'nif': request.user.profile.cliente.nif})
      
    elif (request.user.profile.rol > Constantes.ADMINISTRADOR) and hasattr(request.user.profile, 'cliente') and (request.user.profile.cliente.get_id() is not None): 

          if hasattr(request.user.profile, 'instalacion') and (request.user.profile.instalacion.get_id() is not None):
              instalaciones  = Instalacion.objects.all().filter(_id=request.user.profile.instalacion.get_id())

    for instalacion in instalaciones:
        instalacion.id = str(instalacion._id)

    return render(request, "instalacion/todos.html", {'instalaciones': instalaciones})


@login_required(login_url="/login/")
@permission_required('instalacion.change_instalacion',login_url="/logout/")
def editar(request, id):
    activate('es')
    instalacion = {}    
    instalacion = get_object_or_404(Instalacion, _id=id)
    #Aqui verifico si un cliente coloca una url en el navegador, 
    #si la url que contienela instalacion no pertenece al cliente 
    #logueado lo enviaa la url login
    if (request.user.profile.rol == Constantes.ADMINISTRADOR) and hasattr(request.user.profile, 'cliente') and (request.user.profile.cliente.get_id() is not None):        
        if (request.user.profile.cliente.nif != instalacion.cliente.nif):            
            return redirect('/accounts/logout/')
    
    
        
    form = InstalacionEditarForm(request.POST or None, instance=instalacion)
    return render(request, 'instalacion/editar.html', { 'form' : form })
    
    #else:
    #    return render('logout/')

@login_required(login_url="/login/")
@permission_required('instalacion.change_instalacion',login_url="/logout/")
def actualizar(request, id):
    activate('es')
    instalacion = get_object_or_404(Instalacion, _id=id)
    form = InstalacionEditarForm(request.POST or None, instance=instalacion)
    if form.is_valid():
        form.save()
        return redirect("/instalacion/todos")
    return render(request, 'instalacion/editar.html', { 'form' : form })

@login_required(login_url="/login/")
@permission_required('instalacion.delete_instalacion',login_url="/logout/")
def eliminar(request, id):
    activate('es')    
    try:
        instalacion = Instalacion.objects.get(_id=id)
        if (request.user.profile.rol == Constantes.ADMINISTRADOR) and hasattr(request.user.profile, 'cliente') and (request.user.profile.cliente.get_id() is not None):        
            if (request.user.profile.cliente.nif != instalacion.cliente.nif):                            
                return redirect('/accounts/logout/')
        instalacion.delete()
    except Exception as e:
        print('%s (%s)' % (e, type(e)))
        pass
    return redirect("/instalacion/todos")



def listar_por_nif_cliente(request, nif_cliente):
    print(nif_cliente)
    #instalaciones = Instalacion.objects.all().filter(id_cliente=id_cliente, instalacion_estado=True)
    #instalaciones = Instalacion.objects.values('cliente')
    instalaciones = Instalacion.objects.all().filter(cliente={'nif': nif_cliente}, instalacion_estado=True)        
    instalaciones_dict = {}
    for instalacion in instalaciones:
        instalaciones_dict[str(instalacion.nombre_comercial)] = instalacion.nombre_comercial
    
    return HttpResponse(simplejson.dumps(instalaciones_dict), content_type ="application/json")