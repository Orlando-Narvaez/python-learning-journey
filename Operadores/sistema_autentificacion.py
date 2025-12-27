"""
Crea un programa para validar el usuario y password proporcionados por el usuario.

crea 2 constantes con los valores correctos y posteriormente compara que el usuario y password
proporcionados coincidan con los valores correctos.

Debe soilicotar el usuario  y el password al usuario y si son iguales que los valores correctos
almacenados en las constantes debe imprimir Trues, de lo contrario debe imprimir False.
"""
print("***Sistema de Autenticación***")
usuario = "admin"
password = "123"

dato1 = input("Cual es su Usuario?: ")
dato2 = input("Cual es su Password: ")

es_correcto = dato1.strip() == usuario and password == dato2.strip()    

print(f"Datos correctos: {es_correcto}")