"""
Escribe un programa Python que acepte 5 números decimales del usuario.
"""

# Opción 1:

numeros_ingresados = []

contador = 0

while contador < 5:
    numero = float(input("Escribe un número: "))
    numeros_ingresados.append(numero)
    contador += 1

print(f"Sus números ingresados son : {numeros_ingresados}")

"""
# opción 2:
while True:
  numeros = input(" Por favor escriba cinco números decimales separados por espacios: ")
  numeros = numeros.split()
  largo_de_numeros = len(numeros)
  if largo_de_numeros == 5:
    break

for i in range(largo_de_numeros):
  numeros[i] = float(numeros[i])
  print(numeros[i])
"""




