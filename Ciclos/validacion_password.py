"""  
Crear un  programa para solicitar la validacion al momento de crear un valor de un password

La contraseña debe tener al menos 6 caracteres

En caso de no cumplir con esta condicion el programa debe volver a solicitar un nuevo valor hasta que cumpla con la condicion

Si el valor proporcionado es valido, se debe imprimir: Password valido y finalizar el programa.
"""

print("*** Validacion de Password ***")

password = input("Ingrese su password (minimo 6 caracteres): ")

while len(password) < 6:
    password = input("Ingrese su password (minimo 6 caracteres): ")    
else:
    print("Password valido.")