#STRING: CADENA. Son una secuencia de caracteres. Se indican entre comillas simples o dobles. Podemos acceder a elementos dentro de la cadena.

nombre1 = "Harry"
print(nombre1[0])  # imprime H porque siempre comienza desde 0

# Las podemos concatenar.
first_name = 'Albert'
second_name = 'Einstein'
full_name = first_name + ' ' + last_name

# Otro modo es con Template Literal:
print(f"El nombre completo es: {first_name} {last_name}")