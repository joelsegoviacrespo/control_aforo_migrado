# -*- encoding: utf-8 -*-
from django.contrib import admin
from djongo import models
from instalacion.models import InstalacionEmbebido, Instalacion
from instalacion.forms import InstalacionEmbebidoForm


class JornadaLaboral(models.Model):
    _id = models.ObjectIdField()
    instalacion = models.EmbeddedField(
       model_container=InstalacionEmbebido,
       null=True,
       blank=True,
       model_form_class=InstalacionEmbebidoForm
    )
    hora_apertura = models.TimeField(blank=False)
    hora_cierre = models.TimeField(blank=False)
    activo = models.BooleanField(blank=False, default=True)
    
    
    
    
    def __unicode__(self):
        return self.hora_apertura

    def __str__(self,):
        return str(self.hora_apertura)

    def get_id(self):
        return str(self._id)
    
    def save(self, *args, **kwargs):        

        instalacion = Instalacion.objects.filter(cliente={'nif': self.instalacion.nif_cliente},nombre_comercial=self.instalacion.nombre)[0]
        self.instalacion.network_meraky_id = instalacion.network_meraky_id                      
        super(self.__class__, self).save(*args, **kwargs)
    
        
       
    class Meta:
        db_table = "jornada_laboral"
    
    
    
    
        
