# ERROR COMÚN DE PRINCIPIANTE
respuesta_usuario = "False"  # Esto es texto

# La funcion bool evalua si el string esta vacio o no
es_verdad = bool(respuesta_usuario)

print(f"Valor de es_verdad: {es_verdad}")  # Siempre sera True porque el string no esta vacio

# Forma correcta de validar vacio:
texto_vacio = ""
es_vacio = bool(texto_vacio)    # Esto sera False porque el string esta vacio
print(f"Valor de es_vacio: {es_vacio}") # Imprime: False