# -*- encoding: utf-8 -*-
from django.urls import path
from django.conf.urls import url
from usuarios_red import views

urlpatterns = [
    
    path('dispositivosConectados/<int:periodo_estadistica>', views.dispositivosConectados)
        
]