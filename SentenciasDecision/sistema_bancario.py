print("*** Bienvenido al Sistema Bancario ***")

salir_sistema_txt = input("¿Desea salir del sistema? (s/n): ")
salir_sistema = salir_sistema_txt.strip().lower() == "s"

if not salir_sistema:
    print("Continuando en el sistema bancario...")
else:
    print("Saliendo del sistema bancario. ¡Hasta luego!")