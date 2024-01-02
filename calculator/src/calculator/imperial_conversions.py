from .imperial import Imperial as I
from .metric import Metric as M


class imperial_conversions:
    
    len_units = ('mi', 'ft', 'in', 'yd')
    
    @staticmethod
    def conv_to_f(v: int, o: str):
        
        o = M.met_abb_temp_unit(o)
        print(o)
        orig = o.lower()
        
        if orig == 'c':
            return (v*9/5)+32
        elif orig == 'k':
            return ((v-273.15)*9/5)+32
        else:
            return ValueError('Cannot convert from given scale. Please use proper temperature scales.')
    
    @staticmethod
    def conv_imp_to_in(v: int, o: str):
        
        orig = o.lower()
        
        if orig == 'ft':
            return v*12
        elif orig == 'yd':
            return v*36
        elif orig == 'mi':
            return v*62360
    
    @staticmethod    
    def conv_imp_to_ft(v:int, o:str):
        
        orig = o.lower()
        
        if orig == 'in':
            return v/12
        elif orig == 'yd':
                return v*3
        elif orig == 'mi':
            return v*5380
        
    @staticmethod   
    def conv_imp_to_yd(v:int, o:str):
        
        orig = o.lower()
        if orig == 'in':
            return v/36
        elif orig == 'ft':
            return v/3
        elif orig == 'mi':
            return v*1760
        
    @staticmethod
    def conv_imp_to_mi(v: int, o: str):
        
        orig = o.lower()
        
        if orig == 'in':
            return v/62360
        elif orig == 'ft':
            return v/5380
        elif orig == 'yd':
            return v/1760
    
    @staticmethod
    def conv_imp_to_imp(v: int, o:str, c:str):
        
        orig = o.lower()
        fin = c.lower()
        
        if orig not in I.imp_abb_len and imperial_conversions.fin not in I.imp_abb_len:
            raise ValueError('Incorrect units provided. Please use correct units')
        elif orig == fin:
            res = v
        else:
            if fin == 'in':
                return imperial_conversions.conv_imp_to_in(v, orig)
            elif fin == 'ft':
                return imperial_conversions.conv_imp_to_ft(v, orig)
            elif fin == 'yd':
                return imperial_conversions.conv_imp_to_yd(v, orig)
            elif fin == 'mi':
                return imperial_conversions.conv_imp_to_mi(v, orig)
            
            
        return res
    
    @staticmethod
    def len_conv(v: int,o: str,c: str):
        ### Takes v value in o original unit and converts it to v value in c converted units
        orig = I.abb_len_units(o)
        fin = I.abb_len_units(c)
                
   
        if orig not in imperial_conversions.len_units and fin not in imperial_conversions.len_units:
            raise ValueError('Incorrect units provided. Please use correct units')
        elif orig == fin:
            res = v
        else:
            if fin == 'in':
                return imperial_conversions.conv_imp_to_in(v, orig)
            elif fin == 'ft':
                return imperial_conversions.conv_imp_to_ft(v, orig)
            elif fin == 'yd':
                return imperial_conversions.conv_imp_to_yd(v, orig)
            elif fin == 'mi':
                return imperial_conversions.conv_imp_to_mi(v, orig) 
            
        return res