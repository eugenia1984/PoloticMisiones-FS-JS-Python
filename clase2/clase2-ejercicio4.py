"""
Dada una lista (lista1=[12, 15, 32, 42, 55, 7, 122, 132, 150, 180, 200]), iterarla y mosrar los números divisibles por cinco, y si encuentra un número mayor que 150, detenga la iteraci´on del bucle.
"""

lista = [12, 15, 32, 42, 55, 7, 122, 132, 150, 180, 200]

for i in range(len(lista)):
  if lista[i] > 150:
    break
  elif lista[i] % 5 == 0:
    print(lista[i])