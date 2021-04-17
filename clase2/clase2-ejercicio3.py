"""
Escribe un programa en Python que reciba 5 números enteros del usuario y los guarde en una lista.
Luego recorre la lista y mostrar los números por pantalla.
"""
numeros_enteros_ingresados = []

contador = 0

while contador < 5:
    numero = int(input("Escribe un número: "))
    numeros_enteros_ingresados.append(numero)
    contador += 1

print(f"Sus números ingresados son : {numeros_enteros_ingresados}")