# -*- encoding: utf-8 -*-
import simplejson as simplejson
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from djongo import models
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.utils.translation import activate
from usuarios.forms import UsuariosForm,UsuariosEditarForm
from usuarios.models import User

from django.template import RequestContext
from django.shortcuts import render_to_response
from usuarios.forms import LoginForm
from django.contrib.auth import authenticate, login

@login_required(login_url="/login/")
def register_user(request):
    activate('es')
    msg     = None
    success = False

    if request.method == "POST":

        form = SignUpForm(request.POST)
        if form.is_valid():

            user = form.save(commit=False)
            user.username = form.cleaned_data.get("username")
            user.raw_password = form.cleaned_data.get("password1")
            user.is_active = form.cleaned_data.get("is_active")
            user.email = form.cleaned_data.get("email")
            user.date_joined = datetime.datetime.now()
            user.first_name = form.cleaned_data.get("first_name")
            user.last_name = form.cleaned_data.get("last_name")
            # user = authenticate(username=username, password=raw_password)
            user.save()
            msg     = 'User created.'
            success = True
            #return redirect("/login/")
        else:
            msg = 'Form is not valid'    
    else:
        form = SignUpForm()

    return render(request, "usuarios/agregar.html", {"form": form, "msg" : msg, "success" : success })

def login_page(request):
    message = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST('username')
            password = request.POST('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    message = "Te has identificado de modo correcto"
                else:
                    message = "Tu usuario se encuentra inactivo"
            else:
                message = "Nombre de usuario y/o contraseña incorrecto"
        else:
            form = LoginForm()
        return render_to_response('login.html', {'message': message, 'form': form},
        context_instance=RequestContext(request))

@login_required(login_url="/login/")
def user(request):
    activate('es')
    if request.method == "POST":       
        form = UsuariosForm(request.POST)        
        if form.is_valid():
            
            user = form.save(commit=False)
            user.username = form.cleaned_data.get("username")
            user.raw_password = form.cleaned_data.get("password1")
            user.is_active = form.cleaned_data.get("is_active")
            user.email = form.cleaned_data.get("username")
            user.date_joined = datetime.datetime.now()
            user.first_name = form.cleaned_data.get("first_name")
            user.last_name = form.cleaned_data.get("last_name")
            user.save()
            return redirect('/usuarios/todos')
            
        else:
            form = UsuariosForm()
    else:
        form = UsuariosForm()
    if form.errors:
        for field in form:
            for error in field.errors:
                print(field.name)

                print(error)
        # for error in form.non_field_errors:
        #     print('NFE | ')
        #     print(error)
    return render(request, 'usuarios/agregar.html', {'form': form})



@login_required(login_url="/login/")
def todos(request):
    activate('es')
    usuariosTodos = {}
    #if request.user.is_staff:
    usuariosTodos = Usuarios.objects.all()
        
    #elif hasattr(request.user, 'cliente') and (request.user.cliente.get_id() is not None):
        
    #    instalaciones  = Instalacion.objects.filter(id_cliente=request.user.cliente.get_id())

    for usuarios in usuariosTodos:
        usuarios.id = str(usuarios._id)

    return render(request, "usuarios/todos.html", {'usuariosTodos': usuariosTodos})


@login_required(login_url="/login/")
def editar(request, id):
    activate('es')
    user = get_object_or_404(User, _id=id)
    if request.method == "POST":
        form = UsuariosEditarForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data.get("username")
            user.is_active = form.cleaned_data.get("is_active")
            user.email = form.cleaned_data.get("email")
            user.first_name = form.cleaned_data.get("first_name")
            user.last_name = form.cleaned_data.get("last_name")
            user.save()
            return redirect('/usuarios/todos')
            
        else:
            form = UsuariosEditarForm(instance=user)
 
    return render(request, 'usuarios/editar.html', { 'form' : form })


@login_required(login_url="/login/")
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
def eliminar(request, id):
    activate('es')
    try:
        usuarios = Usuarios.objects.get(_id=id)
        usuarios.delete()
    except Exception as e:
        print('%s (%s)' % (e, type(e)))
        pass
    return redirect("/usuarios/todos")


