class Imperial:
    
    def length_unit(u):
        ### Determines unit of length used
        if len(u) == 2:
            if u[0] =='m':
                return 'miles'
            elif u[0] == 'i':
                return 'inches'
            elif u[0] == 'f':
                return 'feet'
            elif u[0] == 'y':
                return 'yards'
        else:
            raise ValueError('Not an Imperial Value')
        
        if len(u) > 2:
            if u == 'inch':
                return 'inches'
            elif u == 'mile':
                return 'miles'
            elif u == 'foot':
                return 'feet'
            elif u == 'yard':
                return 'yards'
            else:
                raise ValueError('Incorrect Values Entered. Please pass valid arguments.')
            
    def temp_units(u):
        if len(u) == 1 and u.lower() == 'f':
            return u
        elif len(u) > 1 and u.lower() == 'fahrenheit':
            return 'f'
        else:
            return ValueError('Not an Imperial temperature')