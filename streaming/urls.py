# -*- encoding: utf-8 -*-
from django.urls import path
from django.conf.urls import url
from streaming import views

urlpatterns = [
    path('', views.streaming, name='streaming'),
    path('objD/',views.objD, name='objD'),
    path('thresholdValue/',views.thresholdValue, name='thresholdValue'),
    path('smooth/',views.smoothValue, name='smooth'),
]