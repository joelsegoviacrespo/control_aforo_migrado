# -*- encoding: utf-8 -*-
from django.urls import path
from django.conf.urls import url
from uso_red import views

urlpatterns = [
    
    path('conteoUsoRed/', views.conteoUsoRed)
        
]