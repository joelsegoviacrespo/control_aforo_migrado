from djongo import models
from django.contrib import admin
from djongo import models
from instalacion.models import Instalacion,InstalacionEmbebido

       
       
class CamarasHistorico(models.Model):
    _id = models.ObjectIdField()
    nombre =  models.CharField(max_length=250, blank=False, default='')
    network_meraky_id = models.CharField(max_length=255, blank=False, default='')
    nif_cliente = models.CharField(max_length=255, blank=False, default='')
    nombre_camara = models.CharField(max_length=250, blank=False, default='')
    serial_camara = models.CharField(max_length=250, blank=False, default='')    
    fecha = models.DateField(auto_now_add=True,blank=True, null=True)
    nombre_zona_camara = models.CharField(max_length=250, blank=False, default='')
    nro_personas = models.IntegerField(default=0)
    suma_total_aforo =  models.BooleanField(blank=False, default=True)
   
    def __unicode__(self):
        return self.nombre_camara
    def __str__(self,):
        return str(self.nombre_camara)
    class Meta:
        db_table = "camaras_historico"
        
    objects = models.DjongoManager() 