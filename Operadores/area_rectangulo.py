"""  
Se colicita calcular el area y perimetro de un rectangulo
"""

base = float(input("Ingrese la base del rectangulo: "))
altura = float(input("Ingrese la altura del rectangulo: "))

# Realizamos calculos
area = base * altura
perimetro = 2 * (base + altura)

# Mostramos resultados
print(f"El area del rectangulo es: {area}")
print(f"El perimetro del rectangulo es: {perimetro}")