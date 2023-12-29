class Imperial:
    
    def length_unit(u):
        ### Determines unit of length used
        if len(u) == 2:
            if u[0] =='m':
                u = 'miles'
            elif u[0] == 'i':
                u = 'inches'
            elif u[0] == 'f':
                u = 'feet'
            elif u[0] == 'y':
                u = 'yard'
        else:
            raise ValueError('Not an Imperial Value')
        
        if len(u) > 2:
            if u == 'inch':
                u = 'inches'
            elif u == 'mile':
                u = 'miles'
            elif u == 'foot':
                u = 'feet'
            elif u == 'yard':
                u = 'yards'
            else:
                raise ValueError('Incorrect Values Entered. Please pass valid arguments.')
            