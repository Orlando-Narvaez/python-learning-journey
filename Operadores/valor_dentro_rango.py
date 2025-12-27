"""
Solicitar al usuario un valor entre 0 y 5 e indicarle si el valor proporcionafo esta dentro del rango

se deben definir 2 constantes, VALOR_MINIMO y VALOR_MAXIMO

Y debemos comprobar si el valor proporcionado se encuentra en el rango 0 y 5

Finalmente se debe imprimir valor dentro del rango: True/False 
"""
print("***Rango de Valores***")

VALOR_MINIMO = 0
VALOR_MAXIMO = 5

valor_ingresado = int(input("Ingrese un numero entero: "))

resultado = valor_ingresado >= VALOR_MINIMO and valor_ingresado <= VALOR_MAXIMO
print(f"El numero {valor_ingresado} esta dentro del rango: {resultado}")