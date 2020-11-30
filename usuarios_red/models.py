from djongo import models

class UsuariosRed(models.Model):    
    _id = models.ObjectIdField()
    nro_usuarios_ethernet = models.IntegerField(blank=True, default=0)
    nro_usuarios_wifi = models.IntegerField(blank=True, default=0)
    fecha = models.DateTimeField(null=True, blank=True)
           
   
    def __unicode__(self):
        return self.nro_usuarios_ethernet

    def __str__(self,):
        return str(self.nro_usuarios_ethernet)    
   
       
    class Meta:
        db_table = "usuarios_red" 
        
        