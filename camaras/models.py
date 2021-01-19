# -*- encoding: utf-8 -*-
from djongo import models
from instalacion.models import Instalacion,InstalacionEmbebido


class ZonaCamara(models.Model):
    id_zona = models.IntegerField(blank=True, default=0)    
    nombre_zona_camara = models.CharField(max_length=250, blank=False, default='')
    nombre_zona_camara_mostrar = models.CharField(max_length=250, blank=False, default='')
    nro_personas = models.IntegerField(default=0)
    x0 = models.FloatField(blank=True,default=0.00)
    x1 = models.FloatField(blank=True,default=0.00)
    y0 = models.FloatField(blank=True,default=0.00)
    y1 = models.FloatField(blank=True,default=0.00)    
    es_puerta =  models.BooleanField(blank=False, default=True)
    suma_total_aforo =  models.CharField(max_length=5, blank=False, default='')
    class Meta:        
       abstract = True

class Camaras(models.Model):
    _id = models.ObjectIdField()
    instalacion = models.EmbeddedField(
       model_container=InstalacionEmbebido,
       null=True,
       blank=True,
       #model_form_class=ClienteEmbebidoForm
    )            
    nombre_camara = models.CharField(max_length=250, blank=False, default='')
    snapshot = models.CharField(max_length=250, blank=False, default='')
    serial_camara = models.CharField(max_length=250, blank=False, default='')
    imagen_defecto = models.CharField(max_length=250, blank=False, default='')    
    zonas_camara = models.ArrayField(
      model_container=ZonaCamara,
      null=True,
      blank=True,
      #model_form_class=AplicacionesSistemaEmbebidoForm
    
    )  

    activo = models.BooleanField(blank=False, default=True)
    
    
    def __unicode__(self):
        return self.nombre_camara

    def __str__(self,):
        return str(self.nombre_camara)
    
    class Meta:
        db_table = "camaras"
    
    

