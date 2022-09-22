from AST.Abstract.Instruccion import Instruccion
from AST.Expresion.Identificador import Identificador
from Entorno.Simbolo import Simbolo


class Asignacion(Instruccion):

    def __init__(self, identificador:Identificador, expresion):
        self.identificador = identificador
        self.expresion = expresion

   
    def ejecutar3D(self, entorno):
        pass