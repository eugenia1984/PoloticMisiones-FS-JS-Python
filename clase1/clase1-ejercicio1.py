"""
1. Escribe un programa Python que acepte el radio de un círculo del usuario y calcule el área.
"""
#Pido al usaurio ingresar el radio y lo guardo en la variable radio
radio = float (input("Por favor ingrese el radio de un círculo, para poder calcular el área: "))

#Calculo el área
area = (3.14*radio)**2

#Con print muestro el área
print(f'El área del círculo es de: {area}')

