# Metodos cadena

cadena1 = 'hola mundo' 
print(f'cadena original: {cadena1}')
mayusculas = cadena1.upper() # convierte a mayusculas
print(f'cadena en mayusculas: {mayusculas}')
minusculas = mayusculas.lower() # convierte a minusculas
print(f'cadena en minusculas: {minusculas}')

cadena2 = '   hola mundo   '
print(f'cadena original con espacios: {cadena2}')
print(f'cadena sin espacios a la izquierda: "{cadena2.strip()}"') # elimina espacios