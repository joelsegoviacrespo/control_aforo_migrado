from datetime import datetime
from pytz import timezone


class Fecha:
    
    
    def getFechaActualByFormato(fmt):        
        zone = 'Europe/Madrid'
        now_time = datetime.now(timezone(zone))
        return now_time.strftime(fmt)
    
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
    
    def get_start_day(today):        
        return datetime(today.year, today.month, today.day)

    def get_end_day(today):        
        return datetime(today.year, today.month, today.day,23,59,59)
    
    def get_start_minute_day(today):    
        return datetime(today.year, today.month, today.day,today.hour,today.minute,0)

    def get_end_minute_day(today):
        return datetime(today.year, today.month, today.day,today.hour,today.minute,59)
    
    def get_start_hora(today):
            
        print("hora del dia")
        print(str(datetime(today.year, today.month, today.day,today.hour,0,0)))
        return datetime(today.year, today.month, today.day,today.hour,0,0)

    def get_end_hora(today):
        print("final de la hora del dia")
        print(str(datetime(today.year, today.month, today.day,today.hour,59,59)))
        return datetime(today.year, today.month, today.day,today.hour,59,59)
        
    