print("*** Suma Acumulativa ***")

# SUmar los primeros 5 numeros
MAXIMO = 5
numero = 1
acumulador_suma = 0 

while numero <= MAXIMO:
    print(f"Sumando: {acumulador_suma} + {numero}")
    acumulador_suma += numero
    numero += 1
    print(f"Acumulado: {acumulador_suma}\n")

print("La suma acumulada es:", acumulador_suma)