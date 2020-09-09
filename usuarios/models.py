# -*- encoding: utf-8 -*-
from django.contrib import admin
from djongo import models
from cliente.models import Cliente,ClienteEmbebido
from cliente.forms import ClienteEmbebidoForm

# class Usuarios(models.Model):
#     _id = models.ObjectIdField()
#     cliente = models.EmbeddedField(
#        model_container=ClienteEmbebido,
#        null=True,
#        blank=True,
#        model_form_class=ClienteEmbebidoForm
#     ) 
#     id = models.CharField(max_length=20, blank=False, default='')
#     password = models.CharField(max_length=20, blank=False, default='')
#     last_login = models.DateTimeField(auto_now_add=True)
#     is_superuser = models.BooleanField(blank=False, default='')
#     username = models.CharField(max_length=30, blank=False, default='')
#     first_name = models.CharField(max_length=30, blank=False, default='')
#     last_name = models.CharField(max_length=30, blank=False, default='')
#     email = models.EmailField(max_length=50, blank=False, default='')
#     is_staff = models.BooleanField(blank='', default='')
#     is_active = models.BooleanField(blank=False, default='')
#     date_joined = models.DateTimeField(auto_now=True)
    
#     def __unicode__(self):
#         return self.cliente

#     def __str__(self,):
#         return str(self.cliente)

#     def get_id(self):
#         return str(self._id)
       
#     class Meta:
#         db_table = "auth.user"
#     objects = models.DjongoManager()

class UsuarioEmbebido(models.Model):
    _id = models.ObjectIdField()   
    nif_cliente = models.CharField(max_length=20, blank=False, default='')     
    nombre = models.CharField(max_length=255, blank=False, default='')
    
    class Meta:        
        abstract = True