from AST.Abstract.Instruccion import Instruccion
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
                element = self.instruccion.ejecutarInstruccion(entorno)
                if element is not None:
                    if element.tipo == TIPO_DATO.BREAK_ST:
                        break
                    elif element.tipo == TIPO_DATO.CONTINUE_ST:
                        continue
                    else:
                        return element
                condicionPrincipal = self.condicion.ejecutarInstruccion(entorno)
                if condicionPrincipal.tipo != TIPO_DATO.BOOL:
                    print("error en la condicion, no es un valor booleano")
                    return
