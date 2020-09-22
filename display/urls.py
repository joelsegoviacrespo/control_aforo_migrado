# -*- encoding: utf-8 -*-
from django.urls import path
from django.conf.urls import url
from display import views

urlpatterns = [
    path('', views.display, name='display'),
    path('configuracion/<str:id_display>/', views.configuracion)
        
]