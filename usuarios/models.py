# -*- encoding: utf-8 -*-
from django.contrib import admin
from djongo import models
from django.utils import timezone
from cliente.models import Cliente,ClienteEmbebido
from cliente.forms import ClienteEmbebidoForm


class UsuarioEmbebido(models.Model):
    _id = models.ObjectIdField()   
    nif_cliente = models.CharField(max_length=20, blank=False, default='')     
    nombre = models.CharField(max_length=255, blank=False, default='')
    
    class Meta:        
        abstract = True