from .metric import Metric as M
from .imperial import Imperial as I

class metric_conversions:
    
    len_units = ('mm', 'cm', 'm', 'km')
    
    @staticmethod
    def conv_to_c(v: int, o: str):
        
        if M.abb_met_temp_unit(o) in M.met_abb_temp_units:
            orig = M.abb_met_temp_unit(o)
        elif I.abb_temp_unit(o) == 'f':
            orig = I.abb_temp_unit(o)
        
        orig = orig.lower()
        
        if orig == 'f':
            return (v-32)*5/9
        elif orig == 'k':
            return v-273.15
        else:
            return ValueError('Cannot convert from given scale. Please use proper temperature scales.')
    
    @staticmethod
    def conv_to_k(v: int, o: str):
        orig = o.lower()
        
        if orig == 'f':
            return metric_conversions.conv_to_c(v, o) + 273.15
        elif orig == 'k':
            return v-273.15
        else:
            return ValueError('Cannot convert from given scale. Please use proper temperature scales.')
    
    @staticmethod
    def div_by_thous(l:int):
        return l/1000
    
    @staticmethod 
    def mult_by_thous(l:int):
        return l*1000
    
    @staticmethod
    def mult_by_hund(l:int):
        return l*100
    
    @staticmethod
    def div_by_hund(l:int):
        return l/100
    
    @staticmethod
    def len_conv(v: int,o: str,c: str):
        ### Takes v value in o original unit and converts it to v value in c converted units
        
        orig = o.strip().lower()
        fin = c.strip().lower()

        
        if orig not in metric_conversions.len_units and fin not in metric_conversions.len_units:
            raise ValueError('Incorrect units provided. Please use correct units')
        elif orig == fin:
            return v
        elif (orig == 'mm' and fin == 'm') or (orig == 'm' and fin == 'km'):
            return metric_conversions.div_by_thous(v)
        elif (orig == 'km' and fin =='m') or (orig == 'm' and fin == 'mm'):
            return metric_conversions.mult_by_thous(v)
        elif orig == 'cm' and fin == 'm':
            return metric_conversions.div_by_hund(v)
        elif orig == 'm' and fin == 'cm':
            return metric_conversions.mult_by_hund(v)
