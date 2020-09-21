# -*- encoding: utf-8 -*-
from django.contrib import admin
from djongo import models
from instalacion.models import InstalacionEmbebido
from instalacion.forms import InstalacionEmbebidoForm
from cliente.models import Cliente
from django.conf import settings

class Fondos(models.Model):
    _id = models.ObjectIdField()
    instalacion = models.EmbeddedField(
       model_container=InstalacionEmbebido,
       null=True,
       blank=True,
       model_form_class=InstalacionEmbebidoForm
    )            
    descripcion = models.CharField(max_length=255, blank=False, default='')
    orientacion = models.CharField(max_length=20, blank=False, default='')
    url_verde = models.CharField(max_length=255, blank=False, default='')
    nombre_archivo_verde = models.CharField(max_length=255, blank=False, default='')
    url_ambar = models.CharField(max_length=255, blank=False, default='')
    nombre_archivo_ambar = models.CharField(max_length=255, blank=False, default='')
    url_rojo = models.CharField(max_length=255, blank=False, default='')
    nombre_archivo_rojo = models.CharField(max_length=255, blank=False, default='')
    url_cerrado = models.CharField(max_length=255, blank=False, default='')
    nombre_archivo_cerrado = models.CharField(max_length=255, blank=False, default='')
    hora_apertura = models.TimeField(blank=False)
    hora_cierre = models.TimeField(blank=False)
    activo = models.BooleanField(blank=False, default=True)
    
    
    
    
    
    def __unicode__(self):
        return self.descripcion

    def __str__(self,):
        return str(self.descripcion)

    def get_id(self):
        return str(self._id)
    
    def save(self, *args, **kwargs):   

       if self._id is None:
           cliente = Cliente.objects.get(nif=self.instalacion.nif_cliente, cliente_estado=True)
           numero_cliente = cliente.numero_cliente
           instalacion_nombre = self.instalacion.nombre.replace(" ","_")       
           self.url_verde = self.url_verde+numero_cliente+"/"+instalacion_nombre+"/"+"imagen"+"/"+self.nombre_archivo_verde
           self.url_ambar = self.url_ambar+numero_cliente+"/"+instalacion_nombre+"/"+"imagen"+"/"+self.nombre_archivo_ambar
           self.url_rojo = self.url_rojo+numero_cliente+"/"+instalacion_nombre+"/"+"imagen"+"/"+self.nombre_archivo_rojo
           self.url_cerrado = self.url_cerrado+numero_cliente+"/"+instalacion_nombre+"/"+"imagen"+"/"+self.nombre_archivo_cerrado  
       
       else:
           cliente = Cliente.objects.get(nif=self.instalacion.nif_cliente, cliente_estado=True)
           numero_cliente = cliente.numero_cliente
           instalacion_nombre = self.instalacion.nombre.replace(" ","_")           
           
           self.url_verde = self.url_verde[0:self.url_verde.index(settings.MEDIA_URL)+len(settings.MEDIA_URL)]
           self.url_ambar = self.url_ambar[0:self.url_ambar.index(settings.MEDIA_URL)+len(settings.MEDIA_URL)]
           self.url_rojo = self.url_rojo[0:self.url_rojo.index(settings.MEDIA_URL)+len(settings.MEDIA_URL)]
           self.url_cerrado = self.url_cerrado[0:self.url_cerrado.index(settings.MEDIA_URL)+len(settings.MEDIA_URL)]
   
           self.url_verde = self.url_verde+numero_cliente+"/"+instalacion_nombre+"/"+"imagen"+"/"+self.nombre_archivo_verde           
           self.url_ambar = self.url_ambar+numero_cliente+"/"+instalacion_nombre+"/"+"imagen"+"/"+self.nombre_archivo_ambar
           self.url_rojo = self.url_rojo+numero_cliente+"/"+instalacion_nombre+"/"+"imagen"+"/"+self.nombre_archivo_rojo
           self.url_cerrado = self.url_cerrado+numero_cliente+"/"+instalacion_nombre+"/"+"imagen"+"/"+self.nombre_archivo_cerrado
           
           
       
       super(self.__class__, self).save(*args, **kwargs)        
       

    class Meta:
        db_table = "fondos"
    
    
class FondosEmbebido(models.Model):
           
    descripcion = models.CharField(max_length=255, blank=False, default='')
    orientacion = models.CharField(max_length=20, blank=False, default='')
    url_verde = models.CharField(max_length=255, blank=False, default='')    
    url_ambar = models.CharField(max_length=255, blank=False, default='')    
    url_rojo = models.CharField(max_length=255, blank=False, default='')    
    url_cerrado = models.CharField(max_length=255, blank=False, default='')    
    hora_apertura = models.TimeField(blank=False)
    hora_cierre = models.TimeField(blank=False)
    
    class Meta:        
        abstract = True        