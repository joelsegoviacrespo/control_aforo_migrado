# -*- encoding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from djongo import models
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.utils.translation import activate
from cliente.forms import ClienteForm, ClienteTodosForm
from cliente.models import Cliente
from app.models import Profile


#TODO: ELIMINAR: Está solo de referencia de los estilos, no incluir en la versión final
def mng(request):
    context = {'foo': 'bar'}
    return render(request, 'cliente/manage.html', context)


@login_required(login_url="/login/")
def cliente(request):
    activate('es')
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/cliente/todos')
            except Exception as e:
                print('%s (%s)' % (e, type(e)))
                pass
        else:
            print('no valido')
    else:
        form = ClienteForm()
    if form.errors:
        for field in form:
            for error in field.errors:
                #print(field.name % " | " % error)

                print(error)
        # for error in form.non_field_errors:
        #     print('NFE | ')
        #     print(error)
    return render(request, 'cliente/agregar.html', {'form': form})


@login_required(login_url="/login/")
def todos(request):
    activate('es')
    clientes =  Cliente.objects.all()
    for cliente in clientes:
        cliente.id = str(cliente._id)
    return render(request, "cliente/todos.html", {'form': clientes})


@login_required(login_url="/login/")
def editar(request, id):
    activate('es')
    cliente = get_object_or_404(Cliente, _id=id)
    form = ClienteForm(request.POST or None, instance=cliente)
    return render(request, 'cliente/editar.html', { 'form' : form })


@login_required(login_url="/login/")
def actualizar(request, id):
    activate('es')
    cliente = get_object_or_404(Cliente, _id=id)
    form = ClienteForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect("/cliente/todos")
    return render(request, 'cliente/editar.html', { 'form' : form })


@login_required(login_url="/login/")
def eliminar(request, id):
    activate('es')
    try:
        cliente = Cliente.objects.get(_id=id)
        cliente.delete()
    except Exception as e:
        print('%s (%s)' % (e, type(e)))
        pass
    #TODO: Enviar mensaje de eliminado
    return redirect("/cliente/todos")