from djongo import models

class UsuariosRed(models.Model):    
    _id = models.ObjectIdField()
    nro_usuarios_ethernet = models.IntegerField(blank=True, default=0)
    nro_usuarios_wifi = models.IntegerField(blank=True, default=0)
    fecha = models.DateTimeField(null=True, blank=True)
    network_meraky_id = models.CharField(max_length=255, blank=False, default='')
           
   
    def __unicode__(self):
        return self.network_meraky_id

    def __str__(self,):
        return str(self.network_meraky_id)    
   
       
    class Meta:
        db_table = "usuarios_red" 
        
    objects = models.DjongoManager() 