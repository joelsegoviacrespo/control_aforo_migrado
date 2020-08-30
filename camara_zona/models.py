# -*- encoding: utf-8 -*-
from djongo import models
#from instalacion.models import Instalacion


class CamaraZona(models.Model):
    _id = models.ObjectIdField()
    #id_instalacion = models.ForeignKey(Instalacion, on_delete=models.CASCADE, blank=False)
    id_camara_zona = models.CharField(max_length=255, blank=False, default='')
    descripcion = models.CharField(max_length=250, blank=False, default='')
    camara_zona_estado = models.BooleanField(blank=False, default=True)

    def __unicode__(self):
        #return self.id_camara_zona
        return "s% - s%" % str(self.id_camara_zona.id_cliente, self.id_camara_zona)

    def __str__(self):
        return str(self.id_camara_zona)