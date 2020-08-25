# -*- encoding: utf-8 -*-
from django.urls import path
from django.conf.urls import url
from monitor import views

urlpatterns = [
    path('', views.monitor, name='monitor'),
    path('obtenerURL', views.obtenerURL, name='obtener_url'),  # get display URL
    path('show', views.showOnDisplay, name='show'),  # muestra los cambios en el monitor
    path('todos', views.todos),
    path('editar/<str:id>/', views.editar),
    path('actualizar/<str:id>/', views.actualizar),
    path('eliminar/<str:id>/', views.eliminar),
    path('configuracion/<str:id_monitor>/', views.configuracion),
    #path('configuracion_camaras/<str:id_monitor>/', views.configuracion_camaras),
]