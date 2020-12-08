from datetime import datetime
from pytz import timezone


class Fecha:
    
    
    def getHoraMinutoActual():
        fmt = "%H:%M"        
        zone = 'Europe/Madrid'
        now_time = datetime.now(timezone(zone))
        return now_time.strftime(fmt)


    def getFechaActual():
        #fmt = "%Y-%m-%d %H:%M:%S"        
        zone = 'Europe/Madrid'
        now_time = datetime.now(timezone(zone))
        return now_time
        
