from .imperial import Imperial as I
from .metric import Metric as M


class imperial_conversions:
    
    @staticmethod
    def conv_to_f(v: int, o: str):
        
        orig = o.lower()
        
        if orig == 'c' or 'celsius' or 'centigrade':
            return (v*9/5)+32
        elif orig == 'k' or 'kelvin':
            return ((v-273.15)*9/5)+32
        else:
            return ValueError('Cannot convert from given scale. Please use proper temperature scales.')
    
    @staticmethod
    def len_conv(v: int,o: str,c: str):
        ### Takes v value in o original unit and converts it to v value in c converted units
        
        return res