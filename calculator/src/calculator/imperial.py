class Imperial:
    
    imp_len = ('mile', 'miles', 'inch', 'inches', 'feet', 'foot', 'yard', 'yards')
    imp_abb_len = ('mi', 'in', 'ft', 'yd')
    imp_temp = ('fahrenheit')
    imp_abb_temp = ('f')
    
    @staticmethod
    def imp_abb_len_unit(v):
        u = v.lower()
        if u in Imperial.imp_len:
            if 'mile' in u:
                return 'mi'
            elif 'inch' in u:
                return 'in'
            elif 'foot' in u or 'feet' in u:
                return 'ft'
            elif 'yard' in u:
                return 'yd'
            else:
                return ValueError('Units provided are not Imperial units. Please use correct units.')
        elif u in Imperial.abb_len_units:
            return u.strip()
    
    @staticmethod
    def check_if_len_abb(u: str):
        ### Check if abbreviated units are correct abbreviations of Imperial units
        
        if len(u) == 2 and u in Imperial.imp_abb_len:
            
            return u
        else:
            return ValueError('Units provided are not Imperial units. Please use correct units.')
    
    @staticmethod
    def abb_len_units(u):
        ### Abbreviates units if not already abbreviated
        if len(u) > 2 and u.strip().lower() in Imperial.imp_len:
            u = Imperial.imp_abb_len_unit(u)
            return Imperial.check_if_len_abb(u)
        elif len(u) == 2:
            return Imperial.check_if_len_abb(u)
        else:
            raise ValueError('Incorrect Values Entered. Please pass valid arguments.')
    
    @staticmethod
    def abb_temp_unit(u):

        if len(u) == 1 and u.strip().lower() in Imperial.imp_abb_temp:
            return u.lower()
        elif len(u) > 1 and u.strip().lower() in Imperial.imp_temp:
            return 'f'
        else:
            return ValueError('Not an Imperial temperature')