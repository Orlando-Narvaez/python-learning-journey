"""  
Crear un sistema para validar los valores de usuario y password proporcionados.

se deben definir dos constantes con los valores validos:
- usuario = "admin"
- password = "1234"

y el sistema debe comparar los valores validos contra los valores ingresados por el usuario.

Se deben considerar los siguientes casos:
1. Usuario y password correctos -> "Bienvenido al sistema"
2. Usuario invalido
3. Password invalido
4. Usuario y password invalidos
"""

USUARIO_SISTEMA = "admin"
PASSWORD_SISTEMA = "123"

usuario_ingresado = input("Ingrese usuario: ")
password_ingresado = input("Ingrese password: ")

if usuario_ingresado == USUARIO_SISTEMA and password_ingresado == PASSWORD_SISTEMA:
    print(f"Bienvenido al sistema")
elif password_ingresado == PASSWORD_SISTEMA:
    print(f"Usuario invalido")
elif usuario_ingresado == USUARIO_SISTEMA:
    print(f"Password invalido")
else:
    print(f"Usuario y password invalidos")