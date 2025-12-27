print("*** Sistema Préstamo de Libros ***")

DISTANCIA_PERMITIDA = 5
tiene_credencial = input("¿Tiene credencial de estudiante? (s/n): ")
distancia_biblioteca = int(input("Ingrese la distancia a la biblioteca en km: "))

es_elegible_prestamo = (tiene_credencial.strip().lower() == 's') or (distancia_biblioteca <= DISTANCIA_PERMITIDA)
print(f"¿Es elegible para préstamo de libros? {es_elegible_prestamo}")