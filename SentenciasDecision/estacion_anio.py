"""  
Se solicita proporcionar el valor de un mes (valor numerico entre 1 y 12) e indicar a que estacion del año corresponde dicho mes segun 
la siguiente tabla:

meses 1,2 o 12 -> Invierno
meses 3,4 o 5 -> Primavera
meses 6,7 u 8 -> Verano
meses 9,10 o 11 -> Otoño
cualquier otro valor -> Mes incorrecto
"""
print("*** Determinación de la estación del año según el mes ***")  

mes = int(input("Ingrese el número del mes (1-12): "))

if mes == 1 or mes == 2 or mes == 12:
    estacion = "Invierno"
elif mes == 3 or mes == 4 or mes == 5:
    estacion = "Primavera"
elif mes == 6 or mes == 7 or mes == 8:
    estacion = "Verano"
elif mes == 9 or mes == 10 or mes == 11:
    estacion = "Otoño"
else:
    estacion = "Mes incorrecto"

print(f"La estación correspondiente al mes {mes} es: {estacion}")