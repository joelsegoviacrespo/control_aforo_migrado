# -*- encoding: utf-8 -*-
from django.contrib import admin
from djongo import models
from instalacion.models import InstalacionEmbebido, Instalacion
from instalacion.forms import InstalacionEmbebidoForm


class Valores(models.Model):
    _id = models.ObjectIdField()
    instalacion = models.EmbeddedField(
       model_container=InstalacionEmbebido,
       null=True,
       blank=True,
       model_form_class=InstalacionEmbebidoForm
    )            
    descripcion = models.CharField(max_length=255, blank=False, default='')
    maximo_aforo = models.IntegerField(blank=True, default=0)
    mostrar_valor = models.CharField(max_length=255, blank=False, default='')
    mostrar_capacidad = models.BooleanField(blank=False, default=True)
    mostrar_ambar = models.BooleanField(blank=False, default=True)
    activo = models.BooleanField(blank=False, default=True)
    
    
    
    
    def __unicode__(self):
        return self.descripcion

    def __str__(self,):
        return str(self.descripcion)

    def get_id(self):
        return str(self._id)
    
    def save(self, *args, **kwargs):
        
        #print("instalacion.nif_cliente: ",self.instalacion.nif_cliente)
        #print("instalacion.nombre: ",self.instalacion.nombre)      
        #network_meraky_id = self.__class__.objects.filter(cliente={'nif': self.instalacion.nif_cliente}, instalacion_estado=True)
        instalacion = Instalacion.objects.filter(cliente={'nif': self.instalacion.nif_cliente},nombre_comercial=self.instalacion.nombre)[0]
        #instalaciones = Instalacion.objects.all().filter(cliente={'nif': nif_cliente}, instalacion_estado=True)
        #print("instalacion_o _v3: ",instalacion)
        self.instalacion.network_meraky_id = instalacion.network_meraky_id
        #print("network_meraky_id: ",network_meraky_id)        
        #self.instalacion.network_meraky_id = network_meraky_id       
                       
        super(self.__class__, self).save(*args, **kwargs)
    
        
       
    class Meta:
        db_table = "valores"
    
class ValoresEmbebido(models.Model):       
    descripcion = models.CharField(max_length=255, blank=False, default='')
    maximo_aforo = models.IntegerField(blank=True, default=0)
    mostrar_valor = models.CharField(max_length=255, blank=False, default='')
    mostrar_capacidad = models.BooleanField(blank=False, default=True)
    mostrar_ambar = models.BooleanField(blank=False, default=True)
    
    class Meta:        
        abstract = True
        
    
    
        
