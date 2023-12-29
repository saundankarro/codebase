class Metric:

        def length_unit(u):
            ### Determines unit of length used
            
            if len(u) == 1 and u == 'm':
                u = 'meter'
            else:
                raise ValueError('Incorrect value entered')
            
            if len(u) == 2 and u[1] == 'm':
                if u[0] =='m':
                    u = 'millimeter'
                elif u[0] == 'c':
                    u = 'centimeter'
                elif u[0] == 'k':
                    u = 'kilometer'
            else:
                raise ValueError('Not a Metric Value')
            
            if len(u) > 2 and u[:-5] == 'meter':
                if u[0:1] == 'me':
                    u = 'meter'
                elif u[0:3] == 'mill':
                    u = 'millimeter'
                elif u[0] == 'k':
                    u = 'kilometer'
                elif u[0] == 'c':
                    u = 'centimeter'
                else:
                    raise ValueError('Incorrect Values Entered. Please pass valid arguments.')
                