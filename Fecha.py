from datetime import datetime
from pytz import timezone


class Fecha:
    
    
    def getfechaActual():
        fmt = "%H:%M"        
        zone = 'Europe/Madrid'
        now_time = datetime.now(timezone(zone))
        return now_time.strftime(fmt)
        