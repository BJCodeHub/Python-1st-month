length_conv =  (
'miles', 'kilometers', 'meters', 'inches', 'centimeters', 'millimeters', 'yards', 'parsecs', 'INM'
    )
req_conv = str(input('From {length_conv}; '))
req_converted = str(input('To {length_conv}: '))

def conversions(distance, conversion):
    return distance * conversion

if req_conv == 'kilometers' and req_converted == 'miles':
    miles = 1.6
    digits_req = float(int(input('distance: ')))
    conv = conversions (miles, digits_req)
    print (conv)

if req_conv == 'miles' and req_converted == 'kilometers':
    kilometers = 1/1.6
    digits_req = float(int(input('distance: ')))
    conv = conversions (kilometers, digits_req)
    print (conv)

# Instead you can use this simple code
length_conv =  (
'miles', 'kilometers', 'meters', 'inches', 'centimeters', 'millimeters', 'yards', 'parsecs', 'INM'
    )

req_conv = str(input(f'From {length_conv}: '))
req_converted = str(input(f'To {length_conv}: '))

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
    ('parsecs', 'meters'): 3.0857e+16,
    ('meters', 'parsecs'): 3.2408e-17,
    ('INM', 'meters'): 1852,
    ('meters', 'INM'): 0.000539957
}

def convert_distance(distance, unit_1, unit_2):
    conversion = conversions.get(unit_1, unit_2)
    
    if conversion is None:
        print("Invalid conversion units")
        return None
    return float(distance) * conversion

distance = float(input ('Distance: '))
conversion_distance = convert_distance(distance, req_conv, req_converted)
if conversion_distance is not None:
    print(f"{distance} {req_conv} is equals to {conversion_distance} {req_converted}")
