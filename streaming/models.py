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
    
    
class SavedSettings(models.Model):
    _id = models.ObjectIdField()
    email = models.EmailField(max_length=255, blank=False, default='')
    objectsDetection =  models.BooleanField(default=False)
    maskDetection =  models.BooleanField(default=False)
    thresholdValue =  models.DecimalField(default=0.5, max_digits=2,decimal_places=2)
    smoothValue =  models.IntegerField(default=1)
    settings_date = models.DateField(auto_now = True)
    class Meta:
        db_table = "streaming_settings"
    
    
        
