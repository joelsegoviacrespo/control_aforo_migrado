# -*- encoding: utf-8 -*-
from django.contrib import admin
from djongo import models
from instalacion.models import InstalacionEmbebido
from instalacion.forms import InstalacionEmbebidoForm
from cliente.models import Cliente
from django.conf import settings

class Posicion(models.Model):
    _id = models.ObjectIdField()
    instalacion = models.EmbeddedField(
       model_container=InstalacionEmbebido,
       null=True,
       blank=True,
       model_form_class=InstalacionEmbebidoForm
    )            
    posicion_reloj = models.IntegerField(blank=True, default=0)
    color = models.CharField(max_length=20, blank=False, default='')
    activo = models.BooleanField(blank=False, default=True)
  
    
    def __unicode__(self):
        return self.posicion_reloj

    def __str__(self,):
        return str(self.posicion_reloj)

    def get_id(self):
        return str(self._id)
    
       

    class Meta:
        db_table = "posicion"
    
    
class PosicionEmbebido(models.Model):
           
   posicion_reloj = models.IntegerField(blank=True, default=0)
   color = models.CharField(max_length=20, blank=False, default='')
    
   class Meta:        
        abstract = True        