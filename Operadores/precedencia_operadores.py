# 1. Parentesis (): Los parentesis tienen la mayor precedencia
# 2. Exponentes **: Este operador calcula la potencia de un numero
# 3. Unario +, -: Estos operadores realizan operaciones unarias de positivo y negativo
# 4. Multiplicacion *, Division /, Modulo % y Division Entera //
# 5. Suma + y Resta -: Estos operadores realizan operaciones de aritmeticas basicas
# 6. Comparaciones (==, !=, >, <, >=, <=)
# 7. Operadores logicos (and, or, not)
# 8. Asignacion (=, +=, -=, *=, /=, etc.)

# Ejemplo de precedencia de operadores
resultado = 12 / 3 + 2 * 3 - 1
print(f"El resultado de la expresion es: {resultado}")
# En este caso, la operacion se evalua de la siguiente manera:
# 1. Multiplicacion: 2 * 3 = 6  
# 2. Division: 12 / 3 = 4
# 3. Suma: 4 + 6 = 10
# 4. Resta: 10 - 1 = 9
# Por lo tanto, el resultado final es 9