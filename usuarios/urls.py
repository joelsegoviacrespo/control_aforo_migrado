# -*- encoding: utf-8 -*-
from django.urls import path
from django.conf.urls import url
from usuarios import views

urlpatterns = [
    path('', views.usuarios, name='usuarios'),
    path('todos', views.todos),
    path('editar/<str:id>/', views.editar),
    path('actualizar/<str:id>/', views.actualizar),
    path('eliminar/<str:id>/', views.eliminar)    
]