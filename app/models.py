# -*- encoding: utf-8 -*-
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
#from cliente.models import Cliente
from django.utils import timezone


class Profile(models.Model):
    ADMINISTRADOR = 1
    CLIENTE = 2
    USUARIO = 3
    ROLE_CHOICES = (
        (USUARIO, 'Usuario'),
        (CLIENTE, 'Cliente'),
        (ADMINISTRADOR, 'Administrador'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #id_cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, blank=True, null=True, default=None)
    rol = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=False, blank=False, default=0)

    def __str__(self):
        return self.user.username


class ProfileInline(admin.StackedInline):
    model = Profile
    # max_num = 1
    can_delete = False
    verbose_name_plural = 'perfil'


# Define un nuevo usuario admin
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)


# Deshacer el registro del usuario admin
admin.site.unregister(User)
# Registra el nuevo usuario
admin.site.register(User, UserAdmin)

# @receiver(post_save, sender=User)
# def create_or_update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()

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

##class Image(models.Model):
    ##smapshot = models.CharField( on_delete=models.CASCADE,max=255)
    ##timestamp = models.DateTimeField(default=timezone.now)