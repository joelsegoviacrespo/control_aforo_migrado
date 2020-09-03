# -*- encoding: utf-8 -*-
from django.contrib import admin
from djongo import models
from instalacion.models import InstalacionEmbebido
from instalacion.forms import InstalacionEmbebidoForm

class Usuarios(models.Model):
    _id = models.ObjectIdField()
    id = models.CharField(max_length=20, blank=False, default='')
    password = models.CharField(max_length=50, blank=False, default='')
    last_login = models.DateTimeField(blank=False, default='')
    is_superuser = models.BooleanField(blank=False, default='')
    username = models.CharField(max_length=255, blank=False, default='')
    first_name = models.CharField(max_length=255, blank=False, default='')
    last_name = models.CharField(max_length=255, blank=False, default='')
    email = models.EmailField(max_length=255, blank=False, default='')
    is_staff = models.BooleanField(blank=False, default='')
    is_active = models.BooleanField(blank=False, default='')
    date_joined = models.DateTimeField(blank=False, default='')
    
    def __unicode__(self):
        return self.username

    def __str__(self,):
        return str(self.username)

    def get_id(self):
        return str(self._id)
       
    class Meta:
        db_table = "auth.user"
    
    
        
