print("*** Dibujar Triangulo de Asteriscos simtrico ***")

numero_filas = int(input("Ingrese el numero de filas para el triangulo: "))

# Iterer sobre cada fila
for fila in range(1, numero_filas+1):
    espacios_blanco = " " * (numero_filas - fila)
    asteriscos = "*" * (2 * fila - 1 )
    print(f"{espacios_blanco}{asteriscos}")