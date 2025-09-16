import math

print('*** Constantes en Python ***')

PI = 3.14159
print('Valor de PI:', PI)

NOMBRE_BASE_DATOS = "clientes_db"
print('Nombre de la base de datos:', NOMBRE_BASE_DATOS)

# Esto NO se debe hacer, no se debe modificar el valor de una constante
NOMBRE_BASE_DATOS = "nueva_db" # No recomendado
print('No cambiar el valor de una constante, pero se hizo:', NOMBRE_BASE_DATOS)

# Usar una constante del lenguaje Python, aunque en este caso no esta en mayusculas
print('valor de math.pi:', math.pi)