# -*- encoding: utf-8 -*-
from djongo import models
from django import forms

from cliente.models import Cliente,ClienteEmbebido
from cliente.forms import ClienteEmbebidoForm

class Instalacion(models.Model):
    _id = models.ObjectIdField()
    #id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cliente = models.EmbeddedField(
       model_container=ClienteEmbebido,
       null=True,
       blank=True,
       model_form_class=ClienteEmbebidoForm
    )               
    nombre_comercial = models.CharField(max_length=255, blank=False, default='')
    direccion = models.CharField(max_length=255, blank=False, default='')
    telefono = models.CharField(max_length=20, blank=False, default='')
    movil = models.CharField(max_length=20, blank=False, default='')
    email = models.CharField(max_length=255, blank=False, default='')
    poblacion = models.CharField(max_length=255, blank=False, default='')
    provincia = models.CharField(max_length=255, blank=False, default='')
    codigo_postal = models.CharField(max_length=10, blank=False, default='')
    contacto_nombre = models.CharField(max_length=255, blank=False, default='')
    contacto_cargo = models.CharField(max_length=255, blank=False, default='')
    contacto_telefono = models.CharField(max_length=20, blank=False, default='')
    contacto_movil = models.CharField(max_length=20, blank=False, default='')
    contacto_email = models.CharField(max_length=255, blank=False, default='')
    tecnico_nombre = models.CharField(max_length=255, blank=False, default='')
    tecnico_cargo = models.CharField(max_length=255, blank=False, default='')
    tecnico_telefono = models.CharField(max_length=20, blank=False, default='')
    tecnico_movil = models.CharField(max_length=20, blank=False, default='')
    tecnico_email = models.CharField(max_length=255, blank=False, default='')
    instalacion_estado = models.BooleanField(blank=False, default=True)

    def __unicode__(self):
        return self.cliente

    def __str__(self,):
        return str(self.cliente)
    
    class Meta:
        db_table = "instalacion"
    
    objects = models.DjongoManager()
        
class InstalacionEmbebido(models.Model):
    _id = models.ObjectIdField()   
    nif_cliente = models.CharField(max_length=20, blank=False, default='')     
    nombre = models.CharField(max_length=255, blank=False, default='')
    
    class Meta:        
        abstract = True