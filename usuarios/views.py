# -*- encoding: utf-8 -*-
import simplejson as simplejson
from django.contrib.auth.decorators import login_required,permission_required
from django.http import HttpResponse
from djongo import models
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.utils.translation import activate
from usuarios.forms import UsuariosForm,UsuariosEditarForm,UsuariosAsignarForm
from django.contrib.auth.hashers import PBKDF2PasswordHasher
from django.contrib.auth.models import User, Permission, Group
from django.contrib.contenttypes.models import ContentType
from django.template import RequestContext
from django.shortcuts import render_to_response
from app.models import Profile
from cliente.models import Cliente
from instalacion.models import Instalacion
from usuarios.forms import LoginForm
from django.contrib.auth import authenticate, login
import datetime
import Constantes
from django.contrib.auth.hashers import make_password, check_password

@login_required(login_url="/login/")
@permission_required('usuarios.add_usuarios',login_url="/logout/")
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

            print(user)
            print(user.pk)

            client = request.POST.get('cliente')
            client_in = Cliente.objects.get(_id = client)
            instalation = request.POST.get('instalacion')
            instalation_in = Instalacion.objects.get(_id = instalation)
            perfil = Profile(
                user = user,
                cliente = client_in,
                instalacion = instalation_in,
                rol = 3
            )
            perfil.save()

            print(client)
            groups = request.POST.get('group')
            user.groups.add(groups)

            # def read_groups(request,id):
            #     grupos = group.objects.all()
            #     stringval=""
            #     for grupo in grupos:
            #         stringval += "Usuarios: " + grupo.auth_group
                
            #     return HttpResponse(stringval)
            #     print (grupo, stringval)

            # group = Group.objects.get(name='Usuarios')
            # user.groups.add(group)

            # client = request.POST.get('cliente')
            # user.profile.add(client)

            # def read_cliente(request,id):
            #     cliente = cliente.objects.get(id=id)
            #     stringval="numero_cliente: "+cliente.numero_cliente
            #     return HttpResponse(stringval)

            
            return redirect('/usuarios/todos')
            
            # client = request.POST.get('cliente-nif')
            # user.profile.cliente.add(client)
            
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
    client = getattr(request.user.profile, "cliente", None)

    if (request.user.profile.rol== Constantes.SUPERUSUARIO):
        usuariosTodos = User.objects.all()

    elif (request.user.profile.rol == Constantes.ADMINISTRADOR) and client:
        usuariosTodos = User.objects.filter(profile__cliente=client)
        print(client)

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
            if (request.user.profile.cliente.nif != user.cliente.nif_cliente):            
                return redirect('/accounts/logout/')
        usuarios.delete()
    except Exception as e:
        print('%s (%s)' % (e, type(e)))
        pass
    return redirect("/usuarios/todos")


