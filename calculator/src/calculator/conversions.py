from .metric import Metric as M
from .imperial import Imperial as I
from .metric_conversions import metric_conversions as met
from .imperial_conversions import imperial_conversions as imp

def temp(degree: int, scale: str,cvrt: str) -> int:
    
    o = scale.lower()
    f = cvrt.lower()
    
    if f[0] == 'f':
        res = imp.conv_to_f(degree, o)
    elif f[0] == 'c':
        res = met.conv_to_c(degree, o)
    elif f[0] == 'k':
        res = met.conv_to_k(degree, o)
    else:
        raise ValueError('Cannot convert to final scale. Please use proper temperature scales')
        
    
    return res

def conv_len(l:int, s:str, c:str):
    
    return print(f"L: {l}\nS:{s}\nC:{c}")