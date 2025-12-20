"""
Sistema generador de Emails

Se solicita crear una nueva version del sistema generador de emails

Para generar un email debe solicitar al usuario los siguientes datos:
- Nombre
- Apellido
- Nombre de la empresa
- Extension del dominio (com, net, org)

Con los datos recibidos el sistema debera realizar lo siguiente:
- Los espacios del nombre y apellido deben ser remplazados por puntos
- El email debe generarse en minusculas
- los espacios del nombre de la empresa deben ser eliminados
"""
print("*** Sistema generador de Emails ***")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
empresa = input("Ingrese el nombre de la empresa: ")
extension = input("Ingrese la extension del dominio (com, net, org): ")

# Normalizando
nombre_email = nombre.strip().lower().replace(" ",".")
apellido_email = apellido.strip().lower().replace(" ", ".")
empresa_email = empresa.strip().lower().replace(" ", "")
extension_email = extension.strip().lower().replace(" ", "")

print(f"{nombre_email}.{apellido_email}@{empresa_email}{extension_email}")