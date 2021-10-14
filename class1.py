class Vuelo:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.pasajeros = []
    def getdisponible(self):
        return self.capacidad-len(self.pasajeros)
    def addPasajero(self,nombre):
        if self.getdisponible():
            self.pasajeros.append(nombre)
            return True
        else:
            return False
        if not self.getdisponible():
            return False
            self.addPasajero(nombre)
            return True

vuelo = Vuelo(3)

print(vuelo.getdisponible())
vuelo.addPasajero('max')

print(vuelo.getdisponible())
vuelo.addPasajero('max1')
vuelo.addPasajero('max2')
vuelo.addPasajero('max3')

print( vuelo.getdisponible())
