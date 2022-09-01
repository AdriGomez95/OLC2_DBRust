from AST.Abstract.Instruccion import Instruccion
from Entorno.EntornoTabla import EntornoTabla
from Entorno.RetornoType import TIPO_DATO, RetornoType


class While_inst(Instruccion):

    def __init__(self, condicion, instruccion):
        self.condicion = condicion
        self.instruccion = instruccion

    def ejecutarInstruccion(self, entorno):
        condicionPrincipal = self.condicion.obtenerValor(entorno)
        
        if condicionPrincipal.tipo != TIPO_DATO.BOOLEAN:
            print(f"Error semantico en el while, tipo de dato a comparar no valido")
            return RetornoType()
        else:
        
            while condicionPrincipal.valor:
                for instr in self.instruccion:
                    valorRetorno = instr.ejecutarInstruccion(entorno)
                    if valorRetorno is not None:
                        if valorRetorno.tipo == TIPO_DATO.BREAK:
                            break
                        else:
                            return valorRetorno
                    condicionPrincipal = self.condicion.obtenerValor(entorno)
                    if condicionPrincipal.tipo != TIPO_DATO.BOOLEAN:
                        print("error en la condicion, no es un valor booleano")
                        return

                
