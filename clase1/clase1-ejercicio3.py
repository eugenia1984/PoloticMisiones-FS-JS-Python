"""
3. Escribe un programa en Python que acepte una cadena de caracteres y cuente el tamaño de la cadena y cuantas veces aparece la letra A (mayuscula y minúscula)
"""
#Le pido al usuario que ingrese un número
my_string = str(input("Por favor ingrese un texto corto: "))

#cuento el tamaño de la cadena
tamanio_cadena = len(my_string)
print (f'Ingreso {tamanio_cadena} cantidad de caracteres.')

#cuento la cantidad de a ingresadas
cantidad = my_string.lower().count('a')
print (f'Ingreso {cantidad} veces el caracter a.')