# -*- encoding: utf-8 -*-
from djongo import models
import os
from instalacion.models import Instalacion

def path_and_rename(path, prefix):
    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        # project = "pid_%s" % (instance.project.id,)
        if instance:
            if instance._id:
                print('instance name')
                instance_id = "%s" % str(instance._id, )
                # filename = '{}.{}.{}.{}'.format(prefix, project, complaint_id, ext)
                filename = '{}_{}.{}'.format(prefix, instance_id, ext)
            else:
                print('random name')
                # TODO: Revisar que se hace en este caso
                #random_id = "rid_%s" % (uuid4().hex,)
                random_id = "123456789"
                # filename = '{}.{}.{}.{}'.format(prefix, project, random_id, ext)
                filename = '{}_{}.{}'.format(prefix, random_id, ext)
            #Retorna la ruta completa al archivo
        return os.path.join(path, filename)

    return wrapper

class Monitor(models.Model):
    WHITE = 'WTH'
    GREY30 = 'G30'
    GREY60 = 'G60'
    BLACK = 'BLK'
    HEADER_COLOR = (
        (WHITE, 'Blanco'),
        (GREY30, 'Gris 30'),
        (GREY60, 'Gris 60'),
        (BLACK, 'Negro'),
    )

    CENTER = 'CTR'
    RIGHT = 'RGT'
    LEFT = 'LFT'
    LOGO_ALIGN = (
        (CENTER, 'Centro'),
        (RIGHT, 'Derecha'),
        (LEFT, 'Izquierda'),
    )

    PERCENT = 'PCT'
    NUMBER = 'NMB'

    FORMAT = (
        (PERCENT, 'Porcentaje'),
        (NUMBER, 'Número'),
    )

    _id = models.ObjectIdField()
    id_instalacion = models.ForeignKey(Instalacion, on_delete=models.CASCADE, blank=False)
    id_camara_zona = models.CharField(max_length=255, blank=False, default='')
    mac_wifi = models.CharField(max_length=30, blank=False, default='')
    descripcion = models.CharField(max_length=300, blank=False, default='')
    color_barra_cabecera = models.CharField(max_length=3, choices=HEADER_COLOR, default=BLACK)
    texto_barra_cabecera = models.CharField(max_length=100, blank=False, default='')
    logotipo = models.ImageField(upload_to='images/', blank=True)
    logotipo_archivo_nombre = models.CharField(max_length=300, blank=True, default='')
    logotipo_posicion = models.CharField(max_length=3, choices=LOGO_ALIGN, default=RIGHT)
    fondo_imagen = models.ImageField(upload_to='images/',blank=True)
    fondo_imagen_archivo_nombre = models.CharField(max_length=300, blank=True, default='')
    aforo_maximo = models.IntegerField(blank=False, default='0')
    aforo_formato = models.CharField(max_length=3, choices=FORMAT, default=NUMBER)
    aforo_mostrar_maximo = models.BooleanField(blank=False, default=False)
    aforo_mostrar_casi_lleno = models.BooleanField(blank=False, default=False)
    aforo_frase_verde = models.CharField(max_length=150, blank=True, default='')
    aforo_frase_ambar = models.CharField(max_length=150, blank=True, default='')
    aforo_frase_rojo = models.CharField(max_length=150, blank=True, default='')
    monitor_estado = models.BooleanField(blank=False, default=True)

    def __unicode__(self):
        return self.descripcion

    def __str__(self,):
        return str(self.descripcion)

    def __init__(self, *args, **kwargs):
        super(Monitor, self).__init__(*args, **kwargs)

# def logotipo_nombre(instance, filename):
#     ext = filename.split('.')[-1]
#     filename = "%s_%s.%s" % ("LG", str(instance.id), ext)
#     return os.path.join('uploads', filename)
#
# def fondo_nombre(instance, filename):
#     ext = filename.split('.')[-1]
#     filename = "%s_%s.%s" % ("LG", str(instance.id), ext)
#     return os.path.join('uploads', filename)
#
#
# def ruta_nombre_logo(instance, filename):
#     ext = filename.split('.')[-1]
#     if instance:
#         print('instancia cargada')
#         if instance.logotipo==None:
#             random_id = "LG_%s" % (uuid4().hex,)
#             filename = '{}.{}'.format(random_id, ext)
#             logotipo_archivo
#         else:
#             filename = instance.logotipo
#     return os.path.join('images/', "LG", filename)



    # def wrapper(instance, filename):
    #     ext = filename.split('.')[-1]
    #     # project = "pid_%s" % (instance.project.id,)
    #     if instance:
    #         if instance._id:
    #             print('instance name')
    #             instance_id = "%s" % str(instance._id, )
    #             # filename = '{}.{}.{}.{}'.format(prefix, project, complaint_id, ext)
    #             filename = '{}_{}.{}'.format(prefix, instance_id, ext)
    #         else:
    #             print('random name')
    #             # TODO: Revisar que se hace en este caso
    #             #random_id = "rid_%s" % (uuid4().hex,)
    #             random_id = "123456789"
    #             # filename = '{}.{}.{}.{}'.format(prefix, project, random_id, ext)
    #             filename = '{}_{}.{}'.format(prefix, random_id, ext)
    #         #Retorna la ruta completa al archivo
    #     return os.path.join(path, filename)
    #
    # def path_and_rename(path, prefix):
    #     return wrapper

