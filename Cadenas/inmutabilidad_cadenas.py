# Inmutabilidad en cadenas
cadena1 = 'Hola mundo'
# cadena[0] = 'h'  # Esto generará un error porque las cadenas son inmutables
cadena2 = cadena1 # Asignación de referencia
cadena1 = 'adios'  # Esto es válido, pero crea una nueva cadena
print(cadena1)
print(cadena2)