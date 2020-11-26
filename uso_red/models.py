from djongo import models

class UsoRed(models.Model):    
    _id = models.ObjectIdField()
    fecha = models.DateTimeField(null=True, blank=True)
    enviadosGB = models.FloatField(blank=True,default=0.00)   
    recibidosGB = models.FloatField(blank=True,default=0.00)   
    tipo_red = models.CharField(max_length=255, blank=False, default='')
           

    def __unicode__(self):
        return self.tipo_red

    def __str__(self,):
        return str(self.tipo_red)    
   
       
    class Meta:
        db_table = "uso_red"   
