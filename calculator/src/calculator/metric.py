class Metric:
    met_len_units = ('meter', 'meters', 'centimeter', 'centimeteres', 'millimeters', 'millimeter', 'kilometer', 'kilometers')
    met_abb_len_units = ('m', 'cm', 'mm', 'km')
    met_temp_units = ('celsius',  'centigrade', 'kelvin')
    met_abb_temp_units = ('c', 'k')
        
    @staticmethod
    def abb_len_unit(v):
        u = v.strip().lower()
        print(f"abb u:- {u}")
        if len(u) <= 2:
            Metric.check_if_len_abb(u)
        elif u in Metric.met_len_units:
            if 'centimeter' in u:
                return 'cm'
            elif 'millimeter' in u:
                return 'mm'
            elif 'kilometer'in u:
                return 'km'
            elif 'meter' in u:
                return 'm'
        else:
                return ValueError('Units provided are not Metric units. Please use correct units.')
    
    @staticmethod
    def check_if_len_abb(u):
        ### Check if abbreviated units are correct abbreviations of Metric units
        if u in Metric.met_abb_len_units:
            return u
        else:
            return ValueError('Units provided are not Metric units. Please use correct units.')
    
    @staticmethod
    def abb_met_len_unit(u):
        
        print(f"Metric abbreviation function u before abbreviation:- {u}")
        
        ### Abbreviates units if they are correct Metric units
        if len(u)<= 2:
            print(f"Metric abbreviation function check for length of 2: {u}")
            Metric.check_if_len_abb(u)
        elif len(u) > 2 and u in Metric.met_len_units:
            u = Metric.abb_len_unit(u)
            print(f"Metric abbreviation function u after abbreviation:- {u}")
            Metric.check_if_len_abb(u)
        else:
            raise ValueError('Incorrect Values Entered. Please pass valid arguments.')
    
    @staticmethod
    def abb_met_temp_unit(u):
        print(f"metric abb_temp_unit u - {u}")
        if len(u) == 1 and u.lower() in Metric.met_abb_temp_units:
            return u.lower()
        elif len(u) > 1 and u.lower() in Metric.met_temp_units:
            if u[0].lower == 'c':
                return 'c'
            elif u[0] == 'k':
                return 'k'
        else:
            return ValueError('Not an Metric temperature')