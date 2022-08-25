from AST.Abstract.Instruccion import Instruccion
from Entorno.RetornoType import TIPO_DATO, RetornoType


class Return_Instr(Instruccion):

    def __init__(self, tipo, expresion):
        self.tipo = tipo
        self.expresion = expresion

    def ejecutarInstruccion(self, entorno):

        if self.tipo == TIPO_DATO.FN:
            return RetornoType(0, TIPO_DATO.FN)
        else:
            valorRetorno = self.expresion.obtenerValor(entorno)
            return valorRetorno
