#### DEFINCION DE LAS CLASES ####

class Vehiculo():
    def __init__(self, tipo):
        self.tipo = tipo

    def __str__(self):
        return f"{self.tipo}"

class Minibus(Vehiculo):

    def __init__(self, capacidad = 6):
        Vehiculo.__init__(self, "Minibus")
        self.capacidad = capacidad
        #lista de pasajeros del vehiculo
        self.pasajeros = []
    
    def asientos_disponibles(self):
        return self.capacidad - len(self.pasajeros)
    
    def cargar_pasajeros(self, Pasajero):
        if not self.asientos_disponibles():
            return False
        self.pasajeros.append(Pasajero)
        return True

    def __str__(self):
        return f"Vehiculo Minibus de Capacidad {self.capacidad}"

class Pasajero():

    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre

    def __str__(self):
        return f"Persona: DNI {self.dni} - {self.nombre}"

#### FUNCIONES ADICIONALES #####
def buscar_persona(personas, dni):
    for una_persona in personas:
        if una_persona.dni == dni:
            return True
    return False

def cargar_personas(personas):

    while len(personas) < 50:
        try:
            dni = int(input("Ingrese el DNI de la Persona (0 para terminar): "))
            if dni == 0 : break
            if buscar_persona(personas, dni):
                print("La persona ya esta cargada. Intente nuevamente con otro DNI. ")
            else:
                nombre = input("Ingrese el Nombre de la Persona: ")
                if nombre:
                    pasajero_instancia = Pasajero(dni, nombre)
                    personas.append(pasajero_instancia)
                else:
                    print("No ha ingresado un nombre. Intente nuevamente.")
        except ValueError:
            print("¡Ha ingresado un valor erroneo. Intente nuevamente.!")

#### APLICACION #####

print("INICIANDO APLICACION")
minibus1 = Minibus(2)

#lista de personas general del sistema
lista_personas = []

cargar_personas(lista_personas)

for persona in lista_personas:
    if minibus1.cargar_pasajeros(persona):
        print(f"Se cargo el pasajero {persona} al {minibus1}")
    else:
        print(f"Ya se ha superado la capacidad del {minibus1} y no se pueden cargar a {persona}.")

print("FIN DE MI APLICACION")
