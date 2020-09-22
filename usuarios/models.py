# -*- encoding: utf-8 -*-
from django.contrib import admin
from djongo import models
from django import forms
from cliente.models import Cliente,ClienteEmbebido
from cliente.forms import ClienteEmbebidoForm
from instalacion.models import Instalacion,InstalacionEmbebido
from instalacion.forms import InstalacionEmbebidoForm

# class Asignacion(models.Model):
#     _id = models.ObjectIdField()
#     cliente = models.EmbeddedField(
#         model_container=ClienteEmbebido,
#         null=True,
#         blank=True,
#         model_form_class=ClienteEmbebidoForm
#     )

    # class Meta:
    #     model = "app_profile"
    # objects = models.DjongoManager()
    
class UsuarioEmbebido(models.Model):
    _id = models.ObjectIdField()   
    nif_cliente = models.CharField(max_length=20, blank=False, default='')     
    nombre = models.CharField(max_length=255, blank=False, default='')
    
    class Meta:        
        abstract = True