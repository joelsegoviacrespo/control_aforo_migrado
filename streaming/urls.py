# -*- encoding: utf-8 -*-
from django.urls import path
from django.conf.urls import url
from streaming import views

urlpatterns = [
    path('', views.streaming, name='streaming'),        
]