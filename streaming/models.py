# -*- encoding: utf-8 -*-
from djongo import models



class Streaming(models.Model):
    _id = models.ObjectIdField()
    label = models.CharField(blank=False, default=True, max_length= 255)
    mask = models.BooleanField(default=True)
    personid = models.CharField( default=True,blank=False,max_length= 255)
    
    
    def get_id(self):
        return str(self._id)
    _id = models.ObjectIdField() 
       
    class Meta:
        db_table = "streaming"
    
    
    
    
        
