# -*- encoding: utf-8 -*-
from django.urls import path
from django.conf.urls import url
from streaming import views



urlpatterns = [
    path('', views.streaming, name='streaming'),
    path('objD/',views.objD, name='objD'),
    path('maskD/',views.maskD, name='maskD'),
    path('thresholdValue/',views.thresholdValue, name='thresholdValue'),
    path('smooth/',views.smoothValue, name='smooth'),
    path('livecam_feed', views.livecam_feed, name='livecam_feed'),
    path('show_info/',views.loadConfig, name = 'show_info'),
    path('save_config/',views.saveConfig, name = 'save_config'),
]