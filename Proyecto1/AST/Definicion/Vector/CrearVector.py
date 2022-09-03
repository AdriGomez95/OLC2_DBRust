from AST.Abstract.Instruccion import Instruccion
from Entorno.RetornoType import TIPO_DATO
from Entorno.Simbolo import Simbolo



class CrearVector(Instruccion):

    def __init__(self, idVector, tipo, listaValores, tamanio):
        self.idVector = idVector
        self.tipo = tipo
        self.listaValores = listaValores
        self.tamanio = tamanio

    def ejecutarInstruccion(self, entorno):
        if self.tamanio == 0:
            newSimbolo = Simbolo()
            newSimbolo.iniciarSimboloVector(self.idVector, self.tipo, self.listaValores, self.tamanio)

            entorno.agregarSimbolo(newSimbolo)
        else:
            newSimbolo = Simbolo()
            newSimbolo.iniciarSimboloVector(self.idVector, self.tipo, self.listaValores, self.tamanio.valor)

            entorno.agregarSimbolo(newSimbolo)
