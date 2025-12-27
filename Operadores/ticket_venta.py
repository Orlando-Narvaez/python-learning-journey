print("*** Generación de Ticket de Venta ***")

precio_leche = float(input("Ingrese el precio de la leche: "))
precio_pan = float(input("Ingrese el precio del pan: "))
precio_lechuga = float(input("Ingrese el precio de la lechuga: "))
precio_platano = float(input("Ingrese el precio del plátano: "))    
descuento_porcentaje = int(input("Ingrese el porcentaje de descuento (0-100): "))

# Calculo del subtotal (sin impuestos)
subtotal = precio_leche + precio_pan + precio_lechuga + precio_platano

# Calculo del descuento
descuento = subtotal * (descuento_porcentaje / 100)

# subtotal despues del descuento
subtotal_descuento = subtotal - descuento

# Calculo con impuestos (16%)
impuestos = subtotal_descuento * 0.16

# Calculo total de la compra (con impuestos)
total_compra = subtotal_descuento + impuestos 
print(f"""
      ----- Ticket de Venta -----
      subtotal: ${subtotal:.2f}
      Descuento ${descuento} ({descuento_porcentaje}%)
      subtotal con descuento: ${subtotal_descuento:.2f}
      impuestos (16%): ${impuestos:.2f}
      costo total: ${total_compra:.2f}
      ---------------------------""")