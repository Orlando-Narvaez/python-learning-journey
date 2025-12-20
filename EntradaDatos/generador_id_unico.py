"""
Sistema generador ID unico

Con los datos recibidos el sistema debera realizar lo siguiente:

1. Del valor recibido de nombre, usar solo las 2 primeras letras y convertirlas en mayusculas
2. Del  valor de apellido, usar las 3 primeras letras y convertirlas a mayusculas
3. del valor de año, tomar los 2 ultimos digitos

Ademas el sistema debera generar un valor aleatorio de 4 digitos, con ayuda de la funcion 
randint del modulo random

Finalmente, con los datos obtenidos generar un ID unico uniendo los valores obtenidos.
"""
from random import randint

nombre = input("Ingrese el nombre: ")
apellido = input("Ingrese su apellido: ")
anio_nacimiento = input("Ingrese su año de nacimiento: ")

# Normalizar los valores
nombre_2 = nombre.strip().upper()[:2]
apellido_3 = apellido.strip().lower()[:3]
anio_nacimiento_2 = anio_nacimiento.strip()[-2:]

# Generar numero aleatorio
numero_aleatorio = f"{randint(0, 9999):04d}"

id_unico = f"{nombre_2}{apellido_3}{anio_nacimiento_2}{numero_aleatorio}"

print(f"su ID unico es: {id_unico}")

