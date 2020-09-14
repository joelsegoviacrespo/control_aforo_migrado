from djongo import models
from django.contrib import admin


# Create your models here.
class camaras_historico(models.Model):
    instalacion = models.EmbeddedField('Instalacion',null=True,blank=True)
    nombre_camara =  models.CharField(max_length=200)
    serial_camara = models.CharField(max_length=200)
    ts = models.CharField(max_length=200)
    zonas_camara = models.ArrayField (
    models.EmbeddedField('Info_zona_camara',null=True,blank=True)
    )

class instalacion(models.Model):
    nombre = models.CharField(max_length=200)

class info_zona_camara(models.Model):
    nombre_zona_camara = models.CharField(max_length=200)
    nro_persoas = models.IntegerField() 
    
