# Regla y convenciones en nombre de variables en Python

# Ejemplos de reglas estrictas
nombre_usuario = 'orlando'  # Uso de guion bajo para separar palabras
# 1nombre-usuario = 'orlando'  # No se permite empezar con un número ni usar guion medio

# No podemos usar palabras reservadas
# def = 'definicion'  # 'def' es una palabra reservada en Python

# sensible a mayusculas y minusculas
nombre = 'Orlando'
Nombre = 'Juan'
print(nombre)  # Imprime 'Orlando'
print(Nombre)  # Imprime 'Juan'

# snake case
nombre_completo = 'Orlando Narvaez Baracaldo'

# Prefijo y sufijo
es_casado = True  # Prefijo 'es_' para booleanos
nombre_txt = 'orlando.txt'  # Sufijo '_txt' para indicar tipo de dato