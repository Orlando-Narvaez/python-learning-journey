print("*** Menu Iterativo ***")

salir = False

while not salir:
    print(f"""
          1. Crear cuenta
          2. Eliminar cuenta
          3. salir
          """)
    opcion = int(input("Seleccione una opcion: "))  
    if opcion == 1:
        print("Creando cuenta...\n")
    elif opcion == 2:
        print("Eliminando cuenta...\n")
    elif opcion == 3:
        print("Saliendo...\n")
        salir = True
    else:
        print("Opcion no valida, intente de nuevo.\n")
else:
    print("Terminando el sistema de administracion de cuentas.")