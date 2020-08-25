# -*- encoding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from djongo import models
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.utils.translation import activate
from aforoInfo.forms import AforoInfoForm
from aforoInfo.models import AforoInfo





@login_required(login_url="/login/")
def aforoInfo(request):
    activate('es')    
    if request.method == "POST":
        form = AforoInfoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/aforoInfo/todos')
            except Exception as e:
                print('%s (%s)' % (e, type(e)))
                pass
        else:
            print('no valido')
    else:
        form = AforoInfoForm()
    if form.errors:
        for field in form:
            for error in field.errors:
                print("field.name")
                print(field.name)

                print(error)
        # for error in form.non_field_errors:
        #     print('NFE | ')
        #     print(error)
    return render(request, 'aforoInfo/agregar.html', {'form': form})


@login_required(login_url="/login/")
def todos(request):
    activate('es')
    aforoInfos =  AforoInfo.objects.all()
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    for aforoInfo in aforoInfos:
        aforoInfo.id = str(aforoInfo._id)
        print("aforoInfo.nro_aforo")
        print(aforoInfo.nro_aforo)
        print("aforoInfo.cola")
        print(aforoInfo.cola)
    return render(request, "aforoInfo/todos.html", {'form': aforoInfos})


@login_required(login_url="/login/")
def editar(request, id):
    activate('es')
    aforoInfo = get_object_or_404(AforoInfo, _id=id)
    form = AforoInfoForm(request.POST or None, instance=aforoInfo)
    return render(request, 'aforoInfo/editar.html', { 'form' : form })


@login_required(login_url="/login/")
def actualizar(request, id):
    activate('es')
    aforoInfo = get_object_or_404(AforoInfo, _id=id)
    form = AforoInfoForm(request.POST or None, instance=aforoInfo)
    if form.is_valid():
        form.save()
        return redirect("/aforoInfo/todos")
    return render(request, 'aforoInfo/editar.html', { 'form' : form })


@login_required(login_url="/login/")
def eliminar(request, id):
    activate('es')
    try:
        aforoInfo = AforoInfo.objects.get(_id=id)
        aforoInfo.delete()
    except Exception as e:
        print('%s (%s)' % (e, type(e)))
        pass
    #TODO: Enviar mensaje de eliminado
    return redirect("/aforoInfo/todos")