print("*** Uso del Operador NOT ***")

condicion1 = True
# El operador NOT invierte el valor de la condición
resultado = not condicion1
print(f"Condición 1: {condicion1}, Resultado NOT: {resultado}")

# Revisar si una variable es cadena vacía
texto = ""
es_cadena_vacia = not texto
print(f"Texto: '{texto}', ¿Es cadena vacía? {es_cadena_vacia}")

# Revisar si una variable no tiene ningun valor asigando
variable = None
es_valor_sin_valor = not variable
print(f"Variable: {variable}, ¿No tiene valor asignado? {es_valor_sin_valor}")