"""
2. Escribe un programa Python que acepte un número entero (n) y calcule el valor de n + n*n + n*n*n
"""
#Le pido al usuario que ingrese un número
n = float(input("Por favor ingrese un número, para poder hacer cálculos: "))

# Caclulo el cuadrado y el cubo del número ingresado
n_al_cuadrado = n*n
n_al_cubo = n*n*n
resultado = n + n_al_cuadrado + n_al_cubo

# Muestro los cálculos
print(f'El resultado del número ingresado, sumado el número al cuadrado y el número al cubo es:  {resultado}')


