# Programa: Función Bool en Python

# 1. Números (int, float)
print(bool(0))        # False (El vacio numerico es False)
print(bool(0.0))      # False
print(bool(42))       # True (Existe valor)


# 2. Texto(String)
# Cadena vacia = Nada = False
print(bool(""))       # False

# Cadena con espacio o texto = Algo = True
print(bool(" "))      # True
print(bool("Hola"))   # True

# 3. None (Ausencia de valor)
vacio = None
print(bool(vacio))    # False

print(bool(False))   # False
print(bool(True))    # True 