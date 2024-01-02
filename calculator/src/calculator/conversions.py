from .metric import Metric as M
from .imperial import Imperial as I
from .metric_conversions import metric_conversions as met
from .imperial_conversions import imperial_conversions as imp


@staticmethod
def abb_tmp_unit(o: str):
    
    if o in I.imp_abb_temp or o in I.imp_temp:
        return I.abb_temp_unit(o)
    elif o in M.met_abb_temp_units or o in M.met_temp_units:
        return M.abb_met_temp_unit(o)

@staticmethod
def abb_len_unit(o: str):
    
    if o in I.imp_abb_len or o in I.imp_len:
        return I.abb_len_unit(o)
    elif o in M.met_abb_temp_units or o in M.met_temp_units:
        return M.abb_met_temp_unit(o)

def temp(degree: int, scale: str, cvrt: str) -> int:
    
    print(f"scale - {scale}")
    o = abb_tmp_unit(scale)
    
    print(f"Abbreviated unit to convert from")
        
    print(f"o = {o}")
    print(f"************************************")
    print(f"cvrt = {cvrt}")
    
    f = abb_tmp_unit(cvrt)

    print(f"f = {f}")
    
    if f in I.imp_abb_temp:
        res = imp.conv_to_f(degree, o)
    elif f in M.met_abb_temp_units:
        res = met.conv_to_c(degree, o)
    elif f[0] == 'k':
        res = met.conv_to_k(degree, o)
    else:
        raise ValueError('Cannot convert to final unit. Please use proper temperature units')
        
    
    return res

def conv_btwn_in_cm(l:int, s:str, c:str):
    orig = abb_len_unit(s)
    fin = abb_len_unit(c)
    
    if orig == 'in' and fin == 'cm':
        return l*2.54
    elif orig == 'cm' and fin == 'in':
        return l/2.54

def conv_len(l:int, s:str, c:str):
    
    if I.abb_len_units(s) in imp.len_units and I.abb_len_units(c) in imp.len_units:
        return imp.len_conv(l, s, c)
    elif M.met_abb_len_unit(s) in met.len_units and I.abb_len_units(c) in imp.len_units:
        l_cm = met.len_conv(l, s, 'cm')
        l_in = conv_btwn_in_cm(l_cm, 'cm', 'in')
        res = imp.len_conv(l_in, 'in', c)
   
    return res