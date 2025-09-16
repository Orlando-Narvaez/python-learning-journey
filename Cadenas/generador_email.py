'''
 Crear un programa para generar un email a partir de los siguientes datos:
    - Nombre: Juan Pérez
    - Empresa: OpenAI
    - Dominio: com.co

el email debe tener el siguiente formato: todo en minusculas y separado por .
'''

# Generador de email
nombre = 'Orlando Narvaez Baracaldo '
empresa = 'OpenAI '
dominio = ' com.co'

email = f"{nombre.strip().lower().replace(' ', '.')}@{empresa.strip().lower().replace(' ', '.')}.{dominio.strip().lower()}"
print(email)