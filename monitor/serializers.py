# -*- encoding: utf-8 -*-
from rest_framework import serializers


class MonitorSerializer(serializers.Serializer):
    mwf = serializers.CharField(max_length=20)
    mbt = serializers.CharField(max_length=20)

class MonitorLinkSerializer(serializers.Serializer):
    url = serializers.CharField(max_length=255)
    token = serializers.CharField(max_length=700)

class MonitorFSSerializer(serializers.Serializer):
    camara = serializers.CharField(max_length=20)
    zona = serializers.CharField(max_length=100)


class MonitorShowSerializer(serializers.Serializer):
    id_camara_zona = serializers.CharField(max_length=255)
    mac_wifi = serializers.CharField(max_length=30)
    nro_personas = serializers.CharField(max_length=10)
    color_barra_cabecera = serializers.CharField(max_length=3)
    logotipo_archivo_nombre = serializers.CharField(max_length=300)
    logotipo_posicion = serializers.CharField(max_length=3)
    fondo_imagen_archivo_nombre = serializers.CharField(max_length=300)
    aforo_formato = serializers.CharField(max_length=3)
    aforo_mostrar_maximo = serializers.BooleanField()
    aforo_mostrar_casi_lleno = serializers.BooleanField()
    aforo_frase_verde = serializers.CharField(max_length=150)
    aforo_frase_ambar = serializers.CharField(max_length=150)
    aforo_frase_rojo = serializers.CharField(max_length=150)