# -*- encoding: utf-8 -*-
import simplejson as simplejson
from django.contrib.auth.decorators import login_required,permission_required
from django.http import HttpResponse
from djongo import models
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.utils.translation import activate
from usuarios.forms import UsuariosForm,UsuariosEditarForm
from django.contrib.auth.hashers import PBKDF2PasswordHasher
from django.contrib.auth.models import User
from django.template import RequestContext
from django.shortcuts import render_to_response
from usuarios.forms import LoginForm
from django.contrib.auth import authenticate, login
import datetime
import Constantes
from django.contrib.auth.hashers import make_password, check_password

@login_required(login_url="/login/")
def usuarios(request):
    activate('es')
    if request.method == "POST":       
        form = UsuariosForm(request.POST)   
        print(form.is_valid())      
        if form.errors:
            for field in form:
                for error in field.errors:
                    print(field.name)

                    print(error)     
        if form.is_valid():
            
            user = form.save(commit=False)
            user.username = form.cleaned_data.get("username")
            user.raw_password = form.cleaned_data.get("password1")
            user.is_active = form.cleaned_data.get("is_active")
            user.email = form.cleaned_data.get("email")
            user.date_joined = datetime.datetime.now()
            user.first_name = form.cleaned_data.get("first_name")
            user.last_name = form.cleaned_data.get("last_name")
            user.password = make_password(user.password)
            user.save()
            return redirect('/usuarios/todos')
            
        else:
            form = UsuariosForm()
    else:
        form = UsuariosForm()
        # for error in form.non_field_errors:
        #     print('NFE | ')
        #     print(error)
    return render(request, 'usuarios/agregar.html', {'form': form})



@login_required(login_url="/login/")
@permission_required('usuarios.view_user',login_url="/logout/")
def todos(request):
    activate('es')
    usuariosTodos = {}

    # if request.user.is_staff:
    if (request.user.profile.rol== Constantes.SUPERUSUARIO):
        usuariosTodos = User.objects.all()

    # elif hasattr(request.user, 'cliente') and (request.user.cliente.get_id() is not None):
    elif (request.user.profile.rol == Constantes.ADMINISTRADOR) and hasattr(request.user.profile, 'cliente') and (request.user.profile.cliente.get_id() is not None):
        usuariosTodos  = User.objects.all().filter(id_=request.user.profile.cliente.get_id())

    # for usuarios in usuariosTodos:
    #     usuarios.id = str(usuarios._id)

    return render(request, "usuarios/todos.html", {'usuariosTodos': usuariosTodos})


@login_required(login_url="/login/")
@permission_required('usuarios.change_user',login_url="/logout/")
def editar(request, id):
    activate('es')
    user = get_object_or_404(User, _id=id)
    if (request.user.profile.rol == Constantes.ADMINISTRADOR) and hasattr(request.user.profile, 'cliente') and (request.user.profile.cliente.get_id() is not None):                
        if (request.user.profile.cliente.nif != valores.instalacion.nif_cliente):            
            return redirect('/accounts/logout/')

    form = UsuariosEditarForm(request.POST or None, instance=user)
 
    return render(request, 'usuarios/editar.html', { 'form' : form })


@login_required(login_url="/login/")
@permission_required('usuarios.change_user',login_url="/logout/")
def actualizar(request, id):
    activate('es')
    usuarios = get_object_or_404(Usuarios, _id=id)
    form = UsuariosEditarForm(request.POST or None, instance=usuarios)
    if form.is_valid():
        form.save()
        return redirect("/usuarios/todos")
    if form.errors:
      for field in form:
          for error in field.errors:
              print(field.name)
    
              print(error)
      # for error in form.non_field_errors:
      #     print('NFE | ')
      #     print(error)
    return render(request, 'usuarios/editar.html', { 'form' : form })


@login_required(login_url="/login/")
@permission_required('usuaeios.delete_user',login_url="/logout/")
def eliminar(request, id):
    activate('es')
    try:
        usuarios = User.objects.get(_id=id)
        if (request.user.profile.rol == Constantes.ADMINISTRADOR) and hasattr(request.user.profile, 'cliente') and (request.user.profile.cliente.get_id() is not None):                
            if (request.user.profile.cliente.nif != valores.instalacion.nif_cliente):            
                return redirect('/accounts/logout/')
        usuarios.delete()
    except Exception as e:
        print('%s (%s)' % (e, type(e)))
        pass
    return redirect("/usuarios/todos")


