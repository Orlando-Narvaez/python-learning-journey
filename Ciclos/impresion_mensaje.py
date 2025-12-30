print("*** Repeticion de Mensaje ***")

mensaje = input("Ingrese el mensaje a imprimir: ")
veces = int(input("Ingrese el numero de veces a imprimir el mensaje: "))

for i in range(veces):
    print(f"{i+1}: {mensaje}")