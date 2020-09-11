from django.db import models
from django.contrib import admin


# Create your models here.
class Historico(models.Model):
    instalacion = models.EmbeddedField(
        model_container = Instalacion
         )
    nombre_camara =  models.CharField()
    serial_camara = models.CharField()
    ts = models.CharField()
    zonas_camaras = models.ArrayField (
        
        info_zona_camara = models.EmbeddedField(
            model_container = Info_zona_camara
            )
    )

class Instalacion(models.Model):
    nombre = models.CharField()

class Info_zona_camara(models.Model):
    nombre_zona_camara = models.CharField()
    nro_persoas = models.IntegerField() 
    
