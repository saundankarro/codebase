from .metric_converstion import Metric as M

def temp(degree: int, scale: str,cvrt: str) -> int:
    
    if len(scale) > 1:
        scale = scale[0].upper()
    elif len(scale) < 0:
        raise ValueError("scale needs a value to convert the temperature")
    else:
        scale = scale.upper()
        
    if len(cvrt) > 1:
        cvrt = cvrt[0].upper()
    elif len(cvrt) < 0:
        raise ValueError("cvrt needs a value to convert the temperature")
    else:
        cvrt = cvrt.upper()
    
    if scale == 'F' and cvrt == 'C':
        res = (degree - 32)*5/9
    if scale == 'C' and cvrt == 'F':
        res = (degree*9/5) + 32
    if scale == 'C' and cvrt == 'K':
        res = degree + 273.15
    if scale == 'F' and cvrt == 'K':
        res = (degree - 32)*5/9 + 273.15
    
    return res

def conv_len(l:int, s:str, c:str):
    
    