# -*- encoding: utf-8 -*-
from django.urls import path
from django.conf.urls import url
from fondos import views

urlpatterns = [
    path('', views.fondos, name='fondos'),
    path('todos', views.todos),
    path('editar/<str:id>/', views.editar),
    path('actualizar/<str:id>/', views.actualizar),
    path('eliminar/<str:id>/', views.eliminar),
    path('listar_por_nif_cliente/<str:nif_cliente>/', views.listar_por_nif_cliente) 
]