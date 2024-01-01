from .metric import Metric

class metric_conversions:
    
    @staticmethod
    def conv_to_c(v: int, o: str):
        orig = o.lower()
        
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

    def len_conv(v: int,o: str,c: str):
        ### Takes v value in o original unit and converts it to v value in c converted units
        
        return res