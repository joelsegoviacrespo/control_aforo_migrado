# -*- encoding: utf-8 -*-
import simplejson
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from djongo import models
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.utils.translation import activate
from camara_zona.forms import CamaraZonaForm, CamaraZonaEditarForm
from camara_zona.models import CamaraZona
#from cliente.models import Cliente


@login_required(login_url="/login/")
def camara_zona(request):
    activate('es')
    if request.method == "POST":
        try:
            form = CamaraZonaForm(request.POST)
            if form.is_valid():
                form.instance.id_camara_zona = form['camara_serial'].value() + "_" + form['zona_numero'].value()
                form.save()
                return redirect('/camara_zona/todos')
        except Exception as e:
            print('%s (%s)' % (e, type(e)))
            pass
    else:
        form = CamaraZonaForm()
    return render(request, 'camara_zona/agregar.html', {'form': form})


@login_required(login_url="/login/")
def todos(request):
    activate('es')
    camara_zonas =  CamaraZona.objects.all()
    for camara_zona in camara_zonas:
        camara_zona.id = str(camara_zona._id)
        arr_camara_zona = camara_zona.id_camara_zona.split("_",2)
        if len(arr_camara_zona) > 1:
            camara_zona.camara_serial = arr_camara_zona[0]
            camara_zona.zona_numero = arr_camara_zona[1]
        else:
            camara_zona.camara_serial = ''
            camara_zona.zona_numero = ''
    return render(request, "camara_zona/todos.html", {'form': camara_zonas})


@login_required(login_url="/login/")
def editar(request, id):
    activate('es')
    camara_zona = get_object_or_404(CamaraZona, _id=id)
    form = CamaraZonaEditarForm(request.POST or None, instance=camara_zona)
    return render(request, 'camara_zona/editar.html', { 'form' : form})


@login_required(login_url="/login/")
def actualizar(request, id):
    activate('es')
    camara_zona = get_object_or_404(CamaraZona, _id=id)
    form = CamaraZonaForm(request.POST or None, instance=camara_zona)
    if form.is_valid():
        form.instance.id_camara_zona = str(form['camara_serial'].value()).upper() + "_" + form['zona_numero'].value()
        form.save()
        return redirect("/camara_zona/todos")

    form = CamaraZonaEditarForm(request.POST or None, instance=camara_zona)

    return render(request, 'camara_zona/editar.html', { 'form' : form })


@login_required(login_url="/login/")
def eliminar(request, id):
    activate('es')
    try:
        camara_zona = CamaraZona.objects.get(_id=id)
        camara_zona.delete()
    except Exception as e:
        print('%s (%s)' % (e, type(e)))
        pass
    return redirect("/camara_zona/todos")


def listar_por_id_instalacion(request, id_instalacion):
    camara_zonas = CamaraZona.objects.all().filter(id_instalacion=id_instalacion, camara_zona_estado=True)
    camara_zonas_dict = {}
    for camara_zona in camara_zonas:
        camara_zonas_dict[str(camara_zona._id)] = camara_zona.id_camara_zona
    return HttpResponse(simplejson.dumps(camara_zonas_dict), content_type="application/json")



    # if request.method == 'POST':https://www.instagram.com/p/2QJuRMA1Wh/?hl=es
    #     print request.POST.get('my_field')
    #
    #     form = MyForm(request.POST)
    #
    #     print form['my_field'].value()
    #     print form.data['my_field']
    #
    #     if form.is_valid():
    #
    #         print form.cleaned_data['my_field']
    #         print form.instance.my_field
    #
    #         form.save()
    #         print form.instance.id  # now this one can access id/pk