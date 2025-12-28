"""  
Crear un sistema que ofrezca descuentos dependiendo del monto de la compra, o tambien si es miembro de la tienda.

se deben revisar las siguientes condiciones:
1. Si ha comprado mas de 1000 y es miembro -> descuento del 10%
2. Si solo es miembro de la tienda -> descuento del 5%
3. Si ha comprado mas de 1000 -> descuento del 0%
"""
print("*** Sistema de Descuentos de Tienda en Línea ***")

es_miembro = input("Es miembro de la tienda? (s/n): ").strip().lower() == "s"
total_pagar = int(input("Ingrese el monto total a pagar: "))

if es_miembro == True and total_pagar > 1000:
    descuento = total_pagar * 0.10
    valor_neto = total_pagar - descuento
    print(f"""
          Felicidades, has obtenido un descuento del 10%
          Monto de la compra: {total_pagar}
          Descuento: {descuento}
          Monto final a pagar: {valor_neto}
          """)
elif es_miembro == True:
    descuento = total_pagar * 0.05
    valor_neto = total_pagar - descuento
    print(f"""
          Felicidades, has obtenido un descuento del 5%
          Monto de la compra: {total_pagar}
          Descuento: {descuento}
          Monto final a pagar: {valor_neto}
          """)
else:
    print(f"""
          No has obtenido ningún descuento
          Monto final a pagar: {total_pagar}
          """)