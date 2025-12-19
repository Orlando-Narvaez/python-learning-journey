# Concatenacion de cadenas
cadena1 = "Hola"
cadena2 = "mundo"
concatenacion = cadena1 + " " + cadena2
print(concatenacion)

# Utilizando el metodo join
concatenacion2 = " ".join([cadena1, cadena2])
print(concatenacion2)

# Metodo moderno: f-strings (Python 3.6+)
nombre = "Juan"
edad = 30
print(f"Me llamo {nombre} y tengo {edad + 4} años.")