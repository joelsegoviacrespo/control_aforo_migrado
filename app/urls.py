# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""
from django.conf.urls import url, include
from django.urls import path, re_path
from app import views
urlpatterns = [
    re_path(r'^.*\.html', views.pages, name='pages'),
    path('hfs', views.hfs, name='hfs'),
    path('hfsEmbebido', views.hfsEmbebido, name='hfs'),
    path('', views.index, name='home'),
    path('monitor/', include('monitor.urls')),
    path('camara_zona/', include('camara_zona.urls')),
    path('cliente/', include('cliente.urls')),
    path('instalacion/', include('instalacion.urls')),
    path('camaras/', include('camaras.urls')),
    path('aforoInfo/', include('aforoInfo.urls')),
    path('valores/', include('valores.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('fondos/', include('fondos.urls')),
    path('camaras_historico/', include('camaras_historico.urls')),
    path('display/', include('display.urls')),
    path('uso_red/', include('uso_red.urls')),
    path('jornada_laboral/', include('jornada_laboral.urls')),
    path('usuarios_red/', include('usuarios_red.urls')),    
    url('back/', views.back),
    url('ahead/', views.ahead),
    path('generar_estadistica_generales/<str:fecha_str>/<str:operacion>', views.generar_estadistica_generales),
    path('totalAforo/<int:periodo_estadistica>', views.totalAforo),
    path('totalAforo/<str:fecha_str>/<str:operacion>', views.totalAforoDia),
    path('aforoZona/<int:periodo_estadistica>', views.aforoZona), 
    path('streaming/', include('streaming.urls')),
]