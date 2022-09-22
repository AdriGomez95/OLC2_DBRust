from AST.Abstract.Instruccion import Instruccion
from Entorno.EntornoTabla import EntornoTabla
from Entorno.RetornoType import TIPO_DATO, RetornoType


class While_inst(Instruccion):

    def __init__(self, condicion, instruccion):
        self.condicion = condicion
        self.instruccion = instruccion

    
    def ejecutar3D(self, entorno):
        pass

                
