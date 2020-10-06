# -*- encoding: utf-8 -*-
from django.urls import path
from django.conf.urls import url
from camara_zona import views

urlpatterns = [
    path('', views.camara_zona, name='camara_zona'),
    path('todos', views.todos),
    path('editar/<str:id>/', views.editar),
    path('actualizar/<str:id>/', views.actualizar),
    path('eliminar/<str:id>/', views.eliminar),
    path('listar_por_id_instalacion/<str:id_instalacion>/', views.listar_por_id_instalacion),
    
]