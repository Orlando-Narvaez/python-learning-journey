# Revisar si una variable se encuentra dentro de un rango entre 1 y 10
dato = int(input("Ingrese un número entre 1 y 10: "))

# Revisamos si esta dentro del rango
#dentro_rango = 1 <= dato <= 10
#print(f"¿El número {dato} está dentro del rango de 1 a 10? {dentro_rango}")

# Revisamos la logica inversa, si el dato esta fuera de rango
esta_fuera_rango = not (1 <= dato <= 10)
print(f"¿El número {dato} está fuera del rango de 1 a 10? {esta_fuera_rango}")
