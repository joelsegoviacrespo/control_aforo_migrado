# -*- encoding: utf-8 -*-
from djongo import models
from django import forms
from instalacion.models import InstalacionEmbebido
from instalacion.forms import InstalacionEmbebidoForm
from valores.models import ValoresEmbebido
from valores.forms import ValoresEmbebidoForm
from fondos.models import FondosEmbebido
from fondos.forms import FondosEmbebidoForm
from posicion.models import PosicionEmbebido
from posicion.forms import PosicionEmbebidoForm
from espacios.models import EspaciosEmbebido
from espacios.forms import EspaciosEmbebidoForm


class Display(models.Model):
    _id = models.ObjectIdField()    
    instalacion = models.EmbeddedField(
       model_container=InstalacionEmbebido,
       null=True,
       blank=True,
       model_form_class=InstalacionEmbebidoForm
    )
    descripcion = models.CharField(max_length=255, blank=False, default='')
    valores = models.EmbeddedField(
       model_container=ValoresEmbebido,
       null=True,
       blank=True,
       model_form_class=ValoresEmbebidoForm
    )            
    fondos = models.EmbeddedField(
       model_container=FondosEmbebido,
       null=True,
       blank=True,
       model_form_class=FondosEmbebidoForm
    )    
    posicion = models.EmbeddedField(
       model_container=PosicionEmbebido,
       null=True,
       blank=True,
       model_form_class=PosicionEmbebidoForm
    )
    espacios = models.EmbeddedField(
       model_container=EspaciosEmbebido,
       null=True,
       blank=True,
       model_form_class=EspaciosEmbebidoForm
    )                                             
    activo = models.BooleanField(blank=False, default=True)
    
    def __unicode__(self):
        return self.descripcion

    def __str__(self,):
        return str(self.descripcion)

    def get_id(self):
        return str(self._id)
    
    class Meta:
        db_table = "display"