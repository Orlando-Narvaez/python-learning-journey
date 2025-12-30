print("*** Uso de break y continue ***")

# Ejemplo con break
for numero in range(1, 11):
    if numero % 2 == 0:
        print(f"Número par encontrado: {numero}. Saliendo del ciclo.")
        break
    
# Ejmplo con continue
for numero in range(1, 11):
    if numero % 2 == 1:
        print(f"Número impar encontrado: {numero}. Saltando a la siguiente iteración.")
        continue
    print(f"Numero par procesado: {numero}")