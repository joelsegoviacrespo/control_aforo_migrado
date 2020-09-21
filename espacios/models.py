# -*- encoding: utf-8 -*-
from djongo import models
from instalacion.models import Instalacion,InstalacionEmbebido


class ZonaCamara(models.Model):
    #_id = models.ObjectIdField()
    nombre_zona_camara = models.CharField(max_length=250, blank=False, default='')
    nro_personas = models.IntegerField(default=0)
    
    
    class Meta:        
       abstract = True

class Espacios(models.Model):
    _id = models.ObjectIdField()
    instalacion = models.EmbeddedField(
       model_container=InstalacionEmbebido,
       null=True,
       blank=True,
       #model_form_class=ClienteEmbebidoForm
    )            
    descripcion = models.CharField(max_length=250, blank=False, default='')    
    zonas_camara = models.ArrayField(
      model_container=ZonaCamara,
      null=True,
      blank=True,
      #model_form_class=AplicacionesSistemaEmbebidoForm
    
    )  

    activo = models.BooleanField(blank=False, default=True)
    
    
    def __unicode__(self):
        return self.descripcion

    def __str__(self,):
        return str(self.descripcion)
    
    class Meta:
        db_table = "espacios"
    
    
class EspaciosEmbebido(models.Model):
           
   descripcion = models.CharField(max_length=250, blank=False, default='')    
   zonas_camara = models.ArrayField(
      model_container=ZonaCamara,
      null=True,
      blank=True,
      #model_form_class=AplicacionesSistemaEmbebidoForm    
    )
   
   class Meta:        
        abstract = True       
    
            
        
