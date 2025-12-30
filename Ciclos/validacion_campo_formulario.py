print("*** Validacion de Campo de Formulario ***")

nombre_usuario = None

while not nombre_usuario:
    nombre_usuario = input("Ingrese su nombre de usuario: ").strip()
    
print(f"Nombre de usuario valido: {nombre_usuario}")