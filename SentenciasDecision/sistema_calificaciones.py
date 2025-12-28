"""  
Crear un programa para convertir una calificacion numerica (entre 0 y 10) a una calificacion letra (de la F a la A)

Si es mayor o igual a 9 y menor o igual a 10 -> A
Si es mayor o igual a 8 y menor a 9 -> B
Si es mayor o igual a 7 y menor a 8 -> C
Si es mayor o igual a 6 y menor a 7 -> D    
Si es mayor o igual a 0 y menor a 6 -> F
cualquier otro valor -> Calificación inválida
"""
print("*** Sistema de Calificaciones ***")

calificacion_numerica = int(input("Ingrese la calificación numérica (0-10): "))

if calificacion_numerica >= 9 and calificacion_numerica <= 10:
    calificacion_letra = "A"
elif calificacion_numerica >= 8 and calificacion_numerica  < 9:
    calificacion_letra = "B"
elif calificacion_numerica >= 7 and calificacion_numerica < 8:
    calificacion_letra = "C"
elif calificacion_numerica >= 6 and calificacion_numerica < 7:
    calificacion_letra = "D"
elif calificacion_numerica >= 0 and calificacion_numerica < 6:
    calificacion_letra = "F"
else:
    calificacion_letra = "Calificación inválida"
    
print(f"La calificación correspondiente a {calificacion_numerica} es: {calificacion_letra}")