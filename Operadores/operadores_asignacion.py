print("*** Operadores de Asignacion ***")
numero = 10
print(f"Valor inicial: {numero}")
numero = 5
print(f"Asignacion (=): {numero}")
cadena = "Saludos desde python"
print(f"Asignacion (=): {cadena}")

# Asignacion multiples
x, y, z = 1, "hola", -9.5
print(f"Asignacion multiple: x={x}, y={y}, z={z}")

# Asiganacion encadenada
a = b = c = 20
print(f"Asignacion encadenada: a={a}, b={b}, c={c}")

# Intercambio de valores de una variable, sin utilizar una variable temporal
x, y = 5, 10
# Aplicando el concepto de asignacion multiple, intercambiamos los valores
x, y = y, x
print(f"Intercambio de valores: x={x}, y={y}")

# Recibir multiples valores de la entrada del usuario
nombre, apellido = input("Ingrese su nombre y apellido separados por una coma (,): ").split(",")
print(f"Nombre: {nombre.strip()}, Apellido: {apellido.strip()}")