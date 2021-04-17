nombres = ["Harry", "Ron", "Hermione"] 
# ejemplo de listax, va entre [] y se separa con , sus elementos

print(nombres) 
# modo de imprimir una lista. se imprime: ['Harry', 'Ron', 'Hermione']

print(nombres[0]) 
# Imprime el primer elemento, la listas empiezan desde cero, en este caso es: Harry. El ùltimo número de la lista es [-1]

nombres.append("Draco") 
# modo de agregar un elemento a la lista al final. 
# Queda: ['Harry', 'Ron', 'Hermione', 'Draco']

nombres.pop() 
# elimina el último elemento, pero si pongo nombres.pop(nro) me va a eliminar el elemento que esté en el lugar que indica el nro.

nombres.sort() 
# Lo ordena por orden afabético en este caso que son string, lo que no puede hacer es ordenar INT con STR

for i in nombres:
  if i == "Ron":
    print(i)
# Para recorrer una lista, en general se utiliza: i, e, x. En este caso hago que se busque si RON está en la lista

squares = []
for x in range(1, 11):
  squares.append(x*2)
# Si compruebo con print(squares) me imprime: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# Para hacer listas de números, en este caso me queda la tabla del dos

squares = [x**2 for x in range(1, 11)]
# Si hago print(squares), me imprime: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

finishers = ["Sam", "Bob", "Ada", "Bea"]
first_two = finishers[:2]
# Si hago print(first_two), imprime ['Sam', 'Bob'] los dos primeros
# Si quiero imprimir desde un elemento N en adelante, sería finishers[N:], me va a imprimir desde el elemento N incluido hasta el final.
# Si queiro hacer que me vaya iomprimiendo de a pasos, es decir imprima alguno elementosy otros saltee, pongo finishers[::N], y me va a ir imprimiendo cada N elementos, por ejemplo para finishers[::2] me imprime ['Sam', 'Ada'], va de 2 en 2

copy_of_nombres = nombres[:]
# para hacer una copia de la lista

# Todos los métodos de las listas son:

# .append()   
# Para agregar un item a la lista

# .count()   
# Cuenta cuantas veces está en la lista ese elemento que indico dentro de los ()

# .extend(list2)    
""" Itinera dentro de su argumento y va agregando elemento por elemento a la lista, va a quedar con todos los elementos de la primer lista y a continuación todos los elementos de la lista indicada entre (); todo junto formara una nueva lista en la original. 
Por ejemplo:
my_list = ['geeks', 'for']
another_list = [6, 0, 4, 1]
my_list.extend(another_list)
print my_list
Output:
['geeks', 'for', 6, 0, 4, 1]

Pero si tenemos una string cmo lita nos la va a separar, por ejeplo:
my_list = ['geeks', 'for', 6, 0, 4, 1]
my_list.extend('geeks')
print my_list
Output:
['geeks', 'for', 6, 0, 4, 1, 'g', 'e', 'e', 'k', 's']
"""
# index()
# Te devuelve la posición en que está el elemento indicado entre () en la cadena

# insert(position, item)
# Para insertar un nuevo item en la posición que se indica

# pop(position)
# Elimina el último elemento

# remove()
# Borra el item que indico entre ()

# reverse()
# Te cambia el orden del último al primero

# sort()   p
# Lo ordena por orden afabético en este caso que son string, lo que no puede hacer es ordenar INT con STR



