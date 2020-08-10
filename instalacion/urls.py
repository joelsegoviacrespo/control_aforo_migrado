# -*- encoding: utf-8 -*-
from django.urls import path
from django.conf.urls import url
from instalacion import views

urlpatterns = [
    path('', views.instalacion, name='instalacion'),
    path('todos', views.todos),
    path('editar/<str:id>/', views.editar),
    path('actualizar/<str:id>/', views.actualizar),
    path('eliminar/<str:id>/', views.eliminar),
    path('listar_por_id_cliente/<str:id_cliente>/', views.listar_por_id_cliente)
]