from djongo import models
from django.contrib import admin
from djongo import models
from instalacion.models import Instalacion,InstalacionEmbebido
class ZonaCamara(models.Model):
    #_id = models.ObjectIdField()
    nombre_zona_camara = models.CharField(max_length=250, blank=False, default='')
    nro_personas = models.IntegerField(default=0)
    class Meta:
       abstract = True
class myCamaras(models.Model):
    _id = models.ObjectIdField()
    instalacion = models.EmbeddedField(
       model_container=InstalacionEmbebido,
       null=True,
       blank=True,
    )
    nombre_camara = models.CharField(max_length=250, blank=False, default='')
    serial_camara = models.CharField(max_length=250, blank=False, default='')
    ts = models.TimeField(blank=False)
    fecha = models.DateField(auto_now_add=True,blank=True, null=True)
    zonas_camara = models.ArrayField(
      model_container=ZonaCamara,
      null=True,
      blank=True,
    )
    def __unicode__(self):
        return self.nombre_camara
    def __str__(self,):
        return str(self.nombre_camara)
    class Meta:
        db_table = "camaras_historico"