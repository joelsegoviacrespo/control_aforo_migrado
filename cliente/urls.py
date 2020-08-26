# -*- encoding: utf-8 -*-
from django.urls import path
from django.conf.urls import url
from cliente import views

urlpatterns = [
    path('', views.cliente, name='cliente'),
    path('mng', views.mng, name='mng'),          #muestra de la pagina base de estilos en form
    path('todos', views.todos),
    path('editar/<str:id>/', views.editar),
    path('actualizar/<str:id>/', views.actualizar),
    path('eliminar/<str:id>/', views.eliminar),
    path('configuracion/<str:id_cliente>/', views.configuracion),
]