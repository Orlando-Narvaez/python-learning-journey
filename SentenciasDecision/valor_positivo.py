print("*** Revisión de valor positivo ***")

numero = int(input("Ingresa un número: "))

if numero > 0:
    print(f"El número {numero} es positivo.")
elif numero == 0:
    print("El número es cero.")
else:
    print(f"El número {numero} es negativo.")