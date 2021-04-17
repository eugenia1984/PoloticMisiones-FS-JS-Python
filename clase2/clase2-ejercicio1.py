# Escribe un programa Python que imprima "Hola mundo", si a es mayor que b.

# Opciçon 1 poniendo yo los valores de a y b:

a = 20
b = 10

if a > b:
  print("Hola Mundo")
else:
  print("a no es mayor que b")

# Opción 2, solicitando al usuario que ingrese los valores de A y B
A = int(input('Por favor ingresa un número, para guardarlo y luego compararlo: '))
B = int(input('Por favor ingresa un segundo número, para compararlo con el número ingresado anteriormente: '))
if A > B:
  print("Hola Mundo")
else:
  print("A (su primer núemro ingresado) no es mayor que B (su segundo número ingresado)")