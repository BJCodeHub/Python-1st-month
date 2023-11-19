while True:
        length_conv = (
                    'miles', 'nautical miles', 'feet','light-years', 'kilometers', 'meters', 'inches', 'centimeters', 'millimeters', 'yards'
        )
        conversions = {
                ('kilometers', 'miles'): 0.621371,
                ('miles', 'kilometers'): 1.60934,
                ('meters', 'inches'): 39.3701,
                ('inches', 'meters'): 0.0254,
                ('centimeters', 'inches'): 0.393701,
                ('inches', 'centimeters'): 2.54,
                ('millimeters', 'inches'): 0.0393701,
                ('inches', 'millimeters'): 25.4,
                ('yards', 'meters'): 0.9144,
                ('meters', 'yards'): 1.09361,
                ('miles', 'yards'): 1760,
                ('yards', 'miles'): 0.000568182,
                ('meters', 'kilometers'): 0.001,
                ('kilometers', 'meters'): 1000,
                ('centimeters', 'meters'): 0.01,
                ('meters', 'centimeters'): 100,
                ('millimeters', 'centimeters'): 0.1,
                ('centimeters', 'millimeters'): 10,
                ('nautical miles', 'kilometers'): 1.852,
                ('kilometers', 'nautical miles'): 0.539957,
                ('feet', 'meters'): 0.3048,
                ('meters', 'feet'): 3.28084,
                ('light-years', 'kilometers'): 9.461e+12,
                ('kilometers', 'light-years'): 1.057e-13,
            }

        measuring_unit = {
                'kilometers': 'km',
                'miles': 'mi',
                'meter': 'm',
                'inches': 'in',
                'centimeters': 'cm',
                'millimeters': 'mm',
                'yards': 'yd',
                'nautical miles': 'nmi',
                'feet': 'ft',
                'light-years': 'ly',
            }

        convert_from = input(f'Select from {length_conv}: ')
        convert_to = input(f'Select convertion to from {length_conv}: ')

        def convert_distance(distance, unit_1, unit_2):
            convertion_factor = conversions.get((unit_1, unit_2))

            if convertion_factor is None:
                print('Invalid convertion')
                return None
            return distance *convertion_factor


        distance = float(input('Distance: ')) 
                   
        if distance > 0 :
            converted_distance = convert_distance(distance, convert_from, convert_to)
            if converted_distance is not None:
                units_from = measuring_unit[convert_from]
                units_to = measuring_unit[convert_to]

                print (f'{distance} {units_from} = {converted_distance} {units_to}')

        else:
            print("Invalid distance!")
            continue