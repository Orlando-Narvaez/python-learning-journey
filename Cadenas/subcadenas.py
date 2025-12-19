# Programa: Ejemplo de subcadenas en python

frase = "Hola Mundo"
# Extraer una subcadena
# Python inicia los indices desde 0
# no incluye el indice final
#subcadena_hola = frase[0:4]
subcadena_hola = frase[:4]
print(f"Frase completa: {frase}")
print(f"Subcadena hola: {subcadena_hola}")

#subcadena_mundo = frase[5:10]
subcadena_mundo = frase[5:]
print(f"Subcadena mundo: {subcadena_mundo}")

correo = "juan@mail.com"
indice_arroba = correo.index("@")
print(f"Valor del indice del caracter arroba: {indice_arroba}")
usuario = correo[:indice_arroba]
print(f"Nombre de usuario: {usuario}")