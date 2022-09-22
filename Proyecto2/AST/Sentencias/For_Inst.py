from AST.Abstract.Instruccion import Instruccion
from Entorno.EntornoTabla import EntornoTabla
from Entorno.RetornoType import TIPO_DATO, RetornoType
from Entorno.Simbolo import Simbolo



class For_Inst(Instruccion):

    def __init__(self, variable, expresion, instruccion):
        self.variable = variable
        self.expresion = expresion
        self.instruccion = instruccion

    
    def ejecutar3D(self, entorno):
        pass



