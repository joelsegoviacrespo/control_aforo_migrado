# -*- encoding: utf-8 -*-
from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
#from django.contrib.auth.models import User
from djongo import models


class Cliente(models.Model):
    _id = models.ObjectIdField()
    #user = models.OneToOneField(User, on_delete=models.SET_NULL, blank=True, null=True)
    numero_cliente = models.CharField(max_length=20, blank=False, default='') 
    nif = models.CharField(max_length=20, blank=False, default='')
    razon_social = models.CharField(max_length=255, blank=False, default='')
    direccion = models.CharField(max_length=255, blank=False, default='')
    poblacion = models.CharField(max_length=255, blank=False, default='')
    provincia = models.CharField(max_length=255, blank=False, default='')
    codigo_postal = models.CharField(max_length=10, blank=False, default='')
    contacto = models.CharField(max_length=255, blank=False, default='')
    cargo = models.CharField(max_length=255, blank=False, default='')
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
    
    def save(self, *args, **kwargs):       
       if self.__class__.objects.all().count() == 0:          
           self.numero_cliente = 'F1000';
       else:         
           if self._id is None:
           # Obtengo el ultimo numero de cliente 
                ultimo_numero_cliente = self.__class__.objects.all().order_by("-numero_cliente")[0].numero_cliente        
                numero_cliente_str = ultimo_numero_cliente[ultimo_numero_cliente.index('F')+1:len(ultimo_numero_cliente)]    
                numero_cliente = int(numero_cliente_str) + 1                     
                self.numero_cliente = 'F'+str(numero_cliente)
            
           
                       
       super(self.__class__, self).save(*args, **kwargs)    
       
    class Meta:
        db_table = "cliente"
    
    
        
class ClienteEmbebido(models.Model):
    nif = models.CharField(max_length=20, blank=False, default='')
    #razon_social = models.CharField(max_length=255, blank=False, default='')
    
    def __unicode__(self):
        return self.nif

    def __str__(self,):
        return str(self.nif)

    
    class Meta:        
        abstract = True
        
        
        
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