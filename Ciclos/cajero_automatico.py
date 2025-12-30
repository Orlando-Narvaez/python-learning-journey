"""  
Se les deja crear la aplicacion de cajero automatico.
Las funciones principales son: depositar, retirar y consultar saldo. 

El saldo puede tener un valor inicial por ej. 1000.0

Si haces un retiro se resta de tu saldo. Si haces un deposito se suma a tu saldo.
"""
print("*** Cajero Automatico ***")

saldo_actual = 1000.0
salir = False

while not salir:
    print(f"""
      Bienvenido a su cajero automatico
      1. Depositar
      2. Retirar
      3. Consultar saldo
      4. Salir
      """)
    
    opcion = int(input("Seleccione una opción: "))
    
    if opcion == 1:
        operacion = int(input("Ingrese el monto a depositar: "))
        saldo_actual = saldo_actual + operacion
        print(f"Su nuevo saldo es: {saldo_actual}")
    elif opcion == 2:
        operacion = int(input("Ingrese el monto a retirar: "))
        if operacion > saldo_actual:
            print("Fondos insuficientes para realizar el retiro.")  
        else:
            saldo_actual = saldo_actual - operacion
            print(f"Su nuevo saldo es: {saldo_actual}")
    elif opcion == 3:
        print(f"Su saldo actual es: {saldo_actual}")
    elif opcion == 4:
        salir = True
    else:
        print("Opcion no valida, intente de nuevo.\n")
else:
    print("Gracias por usar el cajero automatico. ¡Hasta luego!")