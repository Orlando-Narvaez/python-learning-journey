"""  
Crear un programa para indicar cual es el numero mayor entre dos numeros ingresados por el usuario.
"""

print("*** Programa para encontrar el número mayor entre dos números ***")

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

if numero1 == numero2:
    print(f"El numero {numero1} es igual al número {numero2}.")
elif numero1 > numero2:
    print(f"El numero {numero1} es mayor que el número {numero2}.")
else: 
    print(f"El numero {numero2} es mayor que el número {numero1}.")