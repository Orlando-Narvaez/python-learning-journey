"""  
Se solicita crear un sistema de reservacion de un hotel, se debe pedir la siguiente informacion al usuario:
1. Nombre del usuario
2. Dias de estadia en el hotel
3. Cuarto con vista al mar?

El hotel tiene las siguientes tarifas:
- Cuarto sin vista al mar: $150.50 por dia
- Cuarto con vista al mar: $190.50 por dia

El sistema debe calcular el costo total de la estadia dependiendo si escogio un cuarto con vista al mar o no.
Ademas de indicar si escogio un cuarto con vista al mar o no.
"""
print("*** Sistema de Reservación de Hotel ***")

# Variables del hotel
PRECIO_CUARTO_SIN_VISTA = 150.50
PRECIO_CUARTO_CON_VISTA = 190.50

# Pedir informacion al usuario
nombre = input("Ingrese su nombre: ")
dias_estadia = int(input("Ingrese los días de estadía: "))
tiene_vista_mar = input("¿Desea un cuarto con vista al mar? (s/n): ").strip().lower() == "s"
tiene_vista_mar_txt = "Sí" if tiene_vista_mar else "No"

# Calcular el precio total
if tiene_vista_mar:
    precio_total = dias_estadia * PRECIO_CUARTO_CON_VISTA
else:
    precio_total = dias_estadia * PRECIO_CUARTO_SIN_VISTA

# Mostrar los detalles de la reservacion
print(f"""
      ---------- Detalles de la Reservación ----------
      Nombre del huésped: {nombre}
      Días de estadía: {dias_estadia}
      Cuarto con vista al mar: {tiene_vista_mar_txt}
      Precio total de la estadía: ${precio_total:.2f}
      -------------------------------------------------""")