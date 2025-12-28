print("*** Aplicación de Salud y Fitness ***")

# Constantes de IMC
META_PASOS_DIARIOS = 10000
CALORIAS_PASO = 0.04  # Valor aproximado, son kilocalorías por paso

# Pedimos los datos al usuario
nombre_usuario = input("Ingrese su nombre: ")
pasos_diarios = int(input("Ingrese la cantidad de pasos diarios que ha dado: "))

# Verificar si el usuario alcanzó la meta de pasos
meta_alcanzada = pasos_diarios >= META_PASOS_DIARIOS
meta_alcanzada_txt = "Sí" if meta_alcanzada else "No"

# Cacular calorías quemadas"
calorias_quemadas = pasos_diarios * CALORIAS_PASO

# Mostramos la información al usuario
print(f"\nUsuario: {nombre_usuario}")
print(f"Pasos dados hoy: {pasos_diarios}")
print(f"Calorías quemadas: {calorias_quemadas:.2f} kcal")
print(f"¿Meta de pasos alcanzada? {meta_alcanzada_txt}")
print(f"La meta diaria de pasos es: {META_PASOS_DIARIOS} pasos")