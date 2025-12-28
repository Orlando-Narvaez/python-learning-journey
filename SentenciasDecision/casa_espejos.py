print("*** Bienvenido a la Casa de los Espejos ***")

edad = int(input("Por favor, ingrese su edad: "))
tienes_miedo_oscuridad = input("¿Tienes miedo a la oscuridad? (s/n): ")
tienes_miedo_oscuridad = tienes_miedo_oscuridad.strip().lower() == "s"

if not tienes_miedo_oscuridad and edad >= 10:
    print("Puedes entrar a la casa de los espejos. ¡Diviértete!")
else:
    print("Lo siento la casa de los espejos puede darte miedo. No puedes entrar.")