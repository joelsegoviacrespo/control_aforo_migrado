# -*- encoding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from djongo import models


class Cliente(models.Model):
    _id = models.ObjectIdField()
    user = models.OneToOneField(User, on_delete=models.SET_NULL, blank=True, null=True)
    nif = models.CharField(max_length=20, blank=False, default='')
    razon_social = models.CharField(max_length=255, blank=False, default='')
    direccion = models.CharField(max_length=255, blank=False, default='')
    poblacion = models.CharField(max_length=255, blank=False, default='')
    provincia = models.CharField(max_length=255, blank=False, default='')
    codigo_postal = models.CharField(max_length=10, blank=False, default='')
    telefono = models.CharField(max_length=20, blank=False, default='')
    movil = models.CharField(max_length=20, blank=False, default='')
    email = models.EmailField(max_length=255, blank=False, default='')
    administracion_nombre = models.CharField(max_length=255, blank=False, default='')
    administracion_cargo = models.CharField(max_length=255, blank=False, default='')
    administracion_telefono = models.CharField(max_length=20, blank=False, default='')
    administracion_movil = models.CharField(max_length=20, blank=False, default='')
    administracion_email = models.EmailField(max_length=255, blank=False, default='')
    tecnico_nombre = models.CharField(max_length=255, blank=False, default='')
    tecnico_cargo = models.CharField(max_length=255, blank=False, default='')
    tecnico_telefono = models.CharField(max_length=20, blank=False, default='')
    tecnico_movil = models.CharField(max_length=20, blank=False, default='')
    tecnico_email = models.EmailField(max_length=255, blank=False, default='')
    cliente_estado= models.BooleanField(blank=False, default=True)

    def __unicode__(self):
        return self.razon_social

    def __str__(self,):
        return str(self.razon_social)

    def get_id(self):
        return str(self._id)

#hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
# class ClinteInline(admin.StackedInline):
#     model = Cliente
#     can_delete = False
#     verbose_name_plural = 'clientes'
#
# # Define a new User admin
# class UserAdmin(BaseUserAdmin):
#     inlines = (ClinteInline,)
#hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh

#===============================================
    # class Meta:
    #     proxy = True
    #     ordering = ('first_name',)

    # def __unicode__(self):
    #     return self.razon_social
    #
    # def __str__(self,):
    #     return str(self.razon_social)

    # def save(self, *args, **kwargs):
    #     userObj = self.user
    #
    #     userObj.is_staff = False
    #     userObj.save()
    #
    #     ClienteGroup = Cliente.objects.get(name='cliente')
    #     ClienteGroup.user_set.add(userObj)
    #
    #     super(Cliente, self).save(*args, **kwargs)
#===============================================