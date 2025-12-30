"""  
Crear una aplicacion de calculadora con las opciones de:
- Sumar
- Restar
- Multiplicar
- Dividir

El programa debe mostrar un menu con cada opcion, y debe solicitar los valores
de operando1 y operando2 para realizar la operacion seleccionada."""

print("*** Aplicacion Calculadora ***")

salir = False
while not salir:
    print(f"""
          1. Sumar
          2. Restar
          3. Multiplicar
          4. Dividir
          5. Salir
          """)
    opcion = int(input("Seleccione una opcion: "))  
    
    if 1 <= opcion <= 4:
        operando1 = float(input("Ingrese el primer operando: "))
        operando2 = float(input("Ingrese el segundo operando: "))
        
        if opcion == 1: # Sumar
            resultado = operando1 + operando2
            print(f"El resultado de la suma es: {resultado}\n")
        elif opcion == 2: # Restar
            resultado = operando1 - operando2
            print(f"El resultado de la resta es: {resultado}\n")
        elif opcion == 3: # Multiplicar
            resultado = operando1 * operando2
            print(f"El resultado de la multiplicacion es: {resultado}\n")
        elif opcion == 4: # Dividir
            if operando2 != 0:
                resultado = operando1 / operando2
                print(f"El resultado de la division es: {resultado}\n")
            else:
                print("Error: No se puede dividir entre cero.\n")
                
    elif opcion == 5:
        print("Saliendo de la calculadora...\n")
        salir = True
    else:
        print("Opcion no valida, intente de nuevo.\n")