# zip --> To loop over multiple lists at a time, use zip function

contries = ['Andorra', 	'Armenia', 'Austria', 'Azerbaijan']	
capitals = ['Andorra la Vella', 'Yerevan','Vienna', 'Baku']

for contry, capital in zip(contries, capitals):
    print(f'Capital of {contry} is {capital}')
