
class BasesDatos:
    def __init__(self, nombreDB, tipo, fila):
        self.nombreDB = nombreDB
        self.tipo = tipo
        self.fila = fila

    def toString(self):
        return self.nombreDB + " - " + self.tipo + " [" + str(self.fila) + "]"