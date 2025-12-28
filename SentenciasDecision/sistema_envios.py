"""  
Crea un programa para determinar el costo de envio de un paquete segun el destino (Nacional o Internacional) y el peso del paquete.

costo tarifas:
- Nacional: 10 x kilo
- Internacional: 20 x kilo

el programa debe solicitar 2 valores:
destino (Nacional o Internacional)
peso (en kilos)

Al final debe imprimir el costo total del envio dle paquete.
"""
print("***Sistema de Envios***")

TARIFA_NACIONAL = 10
TARIFA_INTERNACIONAL = 20

destino = int(input("Ingrese el destino del paquete (1 para Nacional, 2 para Internacional): "))
peso = float(input("Ingrese el peso del paquete en kilos: "))

if destino == 1:
    costo = TARIFA_NACIONAL * peso
else:
    costo = TARIFA_INTERNACIONAL * peso
    
destino_txt = "Nacional" if destino == 1 else "Internacional"

print(f"El costo total del envio para un paquete {destino_txt} de {peso} kilos es: ${costo:.2f}")