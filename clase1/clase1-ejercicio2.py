"""
2. Escribe un programa Python que acepte un número entero (n) y calcule el valor de n + n*n + n*n*n
"""
#Le pido al usuario que ingrese un número
n = float(input("Por favor ingrese un número, para poder hacer cálculos: "))

# Caclulo el cuadrado y el cubo del número ingresado
n_al_cuadrado = n*n
n_al_cubo = n*n*n

# Muestro los cálculos
print(f'El cuadrado del número ingresado es: {n_al_cuadrado} y el cubo del número ingresado es {n_al_cubo}')


