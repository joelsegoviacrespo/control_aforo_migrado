# -*- encoding: utf-8 -*-
from djongo import models

class AforoInfo(models.Model):
    _id = models.ObjectIdField()      
    nro_aforo = models.IntegerField(blank=True, default=0) 
    cola = models.IntegerField(blank=True, default=0)   
    
    class Meta:
        db_table = "aforo_info"
