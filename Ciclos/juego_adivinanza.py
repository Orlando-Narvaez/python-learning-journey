"""  
Crear un juego donde el jugador debe adivinar un numero secreto

Puedes usar un ciclo while hasta que el jugador adivine correctamente el numero

El numero secreto se puede crear usando la funcion rand int para generar un numero aleatorio entre 1 y 50

por cada intento fallido se debe incrementar una variable que lleve el conteo de intentos

El programa debe orientar al jugador si el numero ingresado es mayor o menor al numero secreto

Finalmente, cuando el jugador adivine el numero, se debe imprimir un mensaje de felicitacion junto con el numero de intentos realizados
"""
from random import randint

print("*** Juego de Adivinanza ***")

MAX_INTENTOS = 7
numero_adivinar = randint(1,50)
intentos = 0
numero = None

while numero != numero_adivinar and intentos < MAX_INTENTOS:
    numero = int(input("Ingrese un numero entre 1 y 50: "))
    
    if numero < numero_adivinar:
        print("El numero es mayor.")
    elif numero > numero_adivinar:
        print("El numero es menor.")
    elif numero < 1 or numero > 50:
        print("El numero debe estar entre 1 y 50.")
    
    intentos += 1

if numero == numero_adivinar:
    print(f"Felicidades! Adivinaste el numero {numero_adivinar} en {intentos} intentos.")   
else:
    print(f"Lo siento, has agotado tus intentos. El numero era {numero_adivinar}.")