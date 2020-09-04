# -*- coding: utf-8 -*-

from ftplib import FTP
from django.conf import settings
import urllib.parse

FTP_SETTINGS = settings.FTP_SETTINGS

class XFTP(FTP):        

    
    def inicializarFTP(self,ruta_archivo):       
               
        self.connect(FTP_SETTINGS['ftp_url'], int(FTP_SETTINGS['ftp_port']))
        self.login(urllib.parse.quote(FTP_SETTINGS['ftp_user']), urllib.parse.quote(FTP_SETTINGS['ftp_pass']))
        #print(self.getwelcome())
        #print(self.pwd())  # Usually default is /      
        ftp_folder = FTP_SETTINGS['ftp_folder']
        self.cwd(ftp_folder)   
        array_dir = ruta_archivo.split("/")[:-1]        
        for dir in array_dir:          
            self.chdir(dir) 
        
        
    def getNombreArchivo(self,ruta_archivo):        
        
        pos = ruta_archivo.rindex("/") +1          
        return ruta_archivo[pos:len(ruta_archivo)]
    
    def existFile(self,filename):
        
        files = self.nlst()         
        return  filename in self.nlst()
    
    def enviarArchivo(self,ruta_archivo,nombre_archivo):        
       
        with open(ruta_archivo, 'rb') as image_file:            
            self.storbinary('STOR '+ nombre_archivo, image_file)                   
        self.close()
        
    def enviarFtp(self,ruta_archivo,path):        
        
        self.inicializarFTP(path)        
        nombre_archivo = self.getNombreArchivo(ruta_archivo)        
        if (self.existFile(nombre_archivo)):            
            self.delete(nombre_archivo)
       
        self.enviarArchivo(ruta_archivo,nombre_archivo)
            
            
    def upload(self, ruta_archivo,path, callback=None ):        
        self.enviarFtp(ruta_archivo,path)             

    def download(self, filename, callback=None):
        cmd = "RETR " + filename
        if callback is None:
            # Usar la callback por defecto
            with open(filename, "wb") as f:
                self.retrbinary(cmd, f.write)
        else:
            # Callback del usuario
            self.retrbinary(cmd, callback)
            
    
    # Change directories - create if it doesn't exist
    def chdir(self,dir):
        if self.directory_exists(dir) is False: # (or negate, whatever you prefer for readability)            
            self.mkd(dir)

        self.cwd(dir)
        
    
    # Check if directory exists (in current location)
    def directory_exists(self,dir):        
        filelist = []
        self.retrlines('LIST',filelist.append)
        for f in filelist:
            if f.split()[-1] == dir and f.upper().startswith('D'):
                return True
        return False    
