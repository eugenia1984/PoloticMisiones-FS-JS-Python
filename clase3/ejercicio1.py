#Escribe una clase de Python llamada Rectangulo que define por una longitud y un ancho y un método que calculará el área de un rectángulo.

class Rectangulo():
  #Atributo de clase
  def __init__(self, longitud, ancho):
    self.longitud = longitud
    self.ancho = ancho
    #Método de instancia
  def area_rectangulo(self):
    print(f"El area del rectángulo es {self.longitud * self.ancho}")

#Creo el objeto rectangulo1 basado en la clase Rectangulo que tiene longitud 10 y ancho 20
rectangulo1 = Rectangulo(10,20)
#Utilizo el método area_rectangulo para saber el área
rectangulo1.area_rectangulo()
