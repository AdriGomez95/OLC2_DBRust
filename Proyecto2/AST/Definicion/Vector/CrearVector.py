from AST.Abstract.Instruccion import Instruccion
from Entorno.RetornoType import TIPO_DATO
from Entorno.Simbolo import Simbolo



class CrearVector(Instruccion):

    def __init__(self, idVector, tipo, listaValores, tamanio):
        self.idVector = idVector
        self.tipo = tipo
        self.listaValores = listaValores
        self.tamanio = tamanio

   
    def ejecutar3D(self, entorno):
        pass
