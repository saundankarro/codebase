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
        return I.abb_len_units(o)
    elif o in M.met_abb_len_units or o in M.met_len_units:
        return M.abb_met_len_unit(o)

def temp(degree: int, scale: str, cvrt: str) -> int:
    
    o = abb_tmp_unit(scale)
    
    f = abb_tmp_unit(cvrt)
    
   
    if f in I.imp_abb_temp:
        res = imp.conv_to_f(degree, o)
    elif f in M.met_abb_temp_units:
        res = met.conv_to_c(degree, o)
    elif f[0] == 'k':
        res = met.conv_to_k(degree, o)
    else:
        raise ValueError('Cannot convert to final unit. Please use proper temperature units')
        
    
    return res

@staticmethod
def conv_btwn_in_cm(l:int, s:str, c:str):

    
    orig = abb_len_unit(s)
    fin = abb_len_unit(c)
    
    if orig == 'in' and fin == 'cm':
        return l*2.54
    elif orig == 'cm' and fin == 'in':
        return l/2.54

@staticmethod
def check_imp_unit(u):
    if u in I.imp_abb_len or u in I.imp_len:
        return True
    else:
        return False

@staticmethod
def check_met_unit(u):
    if u in M.met_abb_len_units or u in M.met_len_units:
        return True
    else:
        return False

@staticmethod
def check_unit_system(a: str, b: str):
    s = a.strip()
    c = b.strip()

    sic = check_imp_unit(s)
    cic = check_imp_unit(c)
    smc = check_met_unit(s)
    cmc = check_met_unit(c)
    
    
    imp_bool_1 = check_imp_unit(s)
    imp_bool_2 = check_imp_unit(c)
    met_bool_1 = check_met_unit(s)
    met_bool_2 = check_met_unit(c)

    
    if imp_bool_1 == True and met_bool_2 == True:
        return 'im'
    elif met_bool_2 == True and imp_bool_2 == True:
        return 'mi'
    elif imp_bool_1 == True and imp_bool_2 == True:
        return 'ii'
    elif met_bool_1 == True and met_bool_2 == True:
        return 'mm'
    else:
        raise ValueError("One or more of the units provided are not from the Metric system or the Imperial system.")

@staticmethod
def det_met_or_imp(s):
    i = check_imp_unit(s)
    m = check_met_unit(s)

    if i == True:
        return I.abb_len_units(s)
    elif m == True:
        return M.abb_met_len_unit(s)
    else:
        raise ValueError("Incorrect units provided. Please use units from the Metric system or the Imperial system.")

@staticmethod
def conv_len(l:int, s:str, c:str):
    
    u1 = det_met_or_imp(s)
    u2 = det_met_or_imp(c)
    
    len_sys_check = check_unit_system(u1,u2)
    
    if len_sys_check == 'ii':
        return imp.len_conv(l, u1, u2)
    elif len_sys_check == 'mm':
        return met.len_conv(l,u1,u2)
    elif len_sys_check == 'mi':
        l_cm = met.len_conv(l, u1, 'cm')
        l_in = conv_btwn_in_cm(l_cm, 'cm', 'in')
        return imp.len_conv(l_in, 'in', u2)
    elif len_sys_check == 'im':
        l_cm = imp.len_conv(l, u1, 'in')
        l_in = conv_btwn_in_cm(l_cm, 'in', 'cm')
        return met.len_conv(l_in, 'cm', u2)
    else:
        raise ValueError('Incorrect units provided. Please provide correct values to convert')
   
    return res