# Programa: Receta de cocina
"""
Crear un programa para solicitar algunos valores importantes para una receta de cocina.

Los valores que debe inrtroducir el usuario son:
- Nombre de la receta (string)
- Ingredientes
- Tiempo de preparación en minutos
- Dificultad (fácil, medio, difícil)

Mandar a imprimir receta
"""
print("*** Receta de Cocina ***")   

nombre_receta = input("Ingrese el nombre de la receta: ")
ingredientes = input("Ingrese todos los ingredientes necesarios: ")
tiempo_preparacion = int(input("Ingrese el tiempo de preparacion en minutos: "))
dificultad = input("Ingrese la dificulta (fácil, medio, difícil): ")

print("\n--- Receta Ingresada ---")
print(f"Nombre de la receta: {nombre_receta}")  
print(f"Ingredientes: {ingredientes}")
print(f"Tiempo de preparación: {tiempo_preparacion} minutos")
print(f"Dificultad: {dificultad}")