# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
#from cliente.models import Cliente


# Register your models here.

# class ClienteInline(admin.StackedInline):
#     model = Cliente
#     can_delete = False
#     verbose_name_plural = 'cliente'
#
#
# # Define a new User admin
# class UserAdmin(BaseUserAdmin):
#     inlines = (ClienteInline,)
#
#
# # Re-register UserAdmin
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)


# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User
#
# from .models import Perfil
#
# class PerfilInline(admin.StackedInline):
#     model = Perfil
#     can_delete = False
#     verbose_name_plural = 'Perfil'
#     fk_name = 'user'
#
# class CustomUserAdmin(UserAdmin):
#     inlines = (PerfilInline, )
#
#     def get_inline_instances(self, request, obj=None):
#         if not obj:
#             return list()
#         return super(CustomUserAdmin, self).get_inline_instances(request, obj)
#
#
# admin.site.unregister(User)
# admin.site.register(User, CustomUserAdmin)