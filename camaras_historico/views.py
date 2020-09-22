from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from djongo import models
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.utils.translation import activate
from camaras_historico.models import myCamaras
# Create your views here.



@login_required(login_url="/login/")
def insertar(request):
    pass
 
        #     print(error)
   # return render(request, 'aforoInfo/agregar.html', {'form': form})


@login_required(login_url="/login/")
def todos(request):
   
    pass
    

    #return render(request, "aforoInfo/todos.html", {'form': aforoInfos})

@login_required(login_url="/login/")
def editar(request, id):
    pass
    
   #return render(request, 'aforoInfo/editar.html', { 'form' : form })


@login_required(login_url="/login/")
def actualizar(request, id):
    pass
    
    #return render(request, 'aforoInfo/editar.html', { 'form' : form })


@login_required(login_url="/login/")
def eliminar(request, id):
    pass
 
    #return redirect("/aforoInfo/todos")
