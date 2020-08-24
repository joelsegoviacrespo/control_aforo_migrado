# -*- encoding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from djongo import models
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.utils.translation import activate
from camaras.forms import CamarasForm
from camaras.models import Camaras





@login_required(login_url="/login/")
def camaras(request):
    activate('es')
    if request.method == "POST":
        form = CamarasForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/camaras/todos')
            except Exception as e:
                print('%s (%s)' % (e, type(e)))
                pass
        else:
            print('no valido')
    else:
        form = CamarasForm()
    if form.errors:
        for field in form:
            for error in field.errors:
                print("field.name")
                print(field.name)

                print(error)
        # for error in form.non_field_errors:
        #     print('NFE | ')
        #     print(error)
    return render(request, 'camaras/agregar.html', {'form': form})


@login_required(login_url="/login/")
def todos(request):
    activate('es')
    camarasAll =  Camaras.objects.all()
    for camaras in camarasAll:
        camaras.id = str(camaras._id)
    return render(request, "camaras/todos.html", {'form': camarasAll})


@login_required(login_url="/login/")
def editar(request, id):
    activate('es')
    camaras = get_object_or_404(Camaras, _id=id)
    form = CamarasForm(request.POST or None, instance=camaras)
    return render(request, 'camaras/editar.html', { 'form' : form })


@login_required(login_url="/login/")
def actualizar(request, id):
    activate('es')
    camaras = get_object_or_404(Camaras, _id=id)
    form = CamarasForm(request.POST or None, instance=camaras)
    if form.is_valid():
        form.save()
        return redirect("/camaras/todos")
    return render(request, 'camaras/editar.html', { 'form' : form })


@login_required(login_url="/login/")
def eliminar(request, id):
    activate('es')
    try:
        camaras = Camaras.objects.get(_id=id)
        camaras.delete()
    except Exception as e:
        print('%s (%s)' % (e, type(e)))
        pass
    #TODO: Enviar mensaje de eliminado
    return redirect("/camaras/todos")