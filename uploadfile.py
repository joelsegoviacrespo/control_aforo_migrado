from xftp import XFTP
from ftplib import error_perm
from ftplib import FTP
from OverwriteStorage import OverwriteStorage
from django.conf import settings
import os


class UpLoadFile():     
        
    def sendXFTP(self,ruta_archivo,path):               
        try:            
            ftp = XFTP()            
            ftp.upload(ruta_archivo,path)            
        except error_perm:
            print("No tienes los permisos suficientes. ")
            print(error_perm)
            ftp.quit()
    
    def upload(self,fs,ruta_archivo,archivo):                           
        fs.save(ruta_archivo, archivo)
         
         
    def send(self,archivo,path):               
        try:                        
            fs = OverwriteStorage()                                  
            ruta_archivo = self.getRutaArchivo(fs,archivo.name,path)   
            print("ruta_archivo: "+ruta_archivo)                     
            self.upload(fs,ruta_archivo,archivo)                            
            self.sendXFTP(ruta_archivo,path)         
               
        except error_perm:
            print ("No tienes los permisos suficientes.")
            ftp.quit()
            
    def getRutaArchivo(self,fs,name,path):
        nombre_archivo = self.getNombreArchivo(fs,name)
        part_dir = os.path.join(path, nombre_archivo)
        return os.path.join(settings.MEDIA_ROOT, part_dir)
        
    def getNombreArchivo(self,fs,name):
         return fs.get_available_name(name)  
        
        
        