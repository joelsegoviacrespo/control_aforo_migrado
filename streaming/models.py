# -*- encoding: utf-8 -*-
from djongo import models



class Streaming(models.Model):
    _id = models.ObjectIdField()  
    
    
    def get_id(self):
        return str(self._id)
        
       
    class Meta:
        db_table = "streaming"
    
    
    
    
        
