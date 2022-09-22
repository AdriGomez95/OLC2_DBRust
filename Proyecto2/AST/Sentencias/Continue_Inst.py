from AST.Abstract.Instruccion import Instruccion
from Entorno.RetornoType import TIPO_DATO, RetornoType


class Continue_Inst(Instruccion):

    def __init__(self, tipo):
        self.tipo = tipo

    
    def ejecutar3D(self, entorno):
        pass

