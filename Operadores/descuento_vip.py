print("*** Sistema Descuentos VIP ***")

NO_PRODUCTO_DESCUENTO = 10
cantidad_productos = int(input("Ingrese la cantidad de productos comprados hoy: "))
tiene_membresia_vip = input("¿Tienes la membresia de la tienda? (si/no): ")

es_elegible_descuento = cantidad_productos >= NO_PRODUCTO_DESCUENTO and tiene_membresia_vip.strip().lower() == "si"
print(f"Es elegible para descuento VIP: {es_elegible_descuento}")