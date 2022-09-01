from AST.Abstract.Instruccion import Instruccion
from Entorno.EntornoTabla import EntornoTabla
from Entorno.RetornoType import TIPO_DATO, RetornoType
from Entorno.Simbolo import Simbolo



class For_Inst(Instruccion):

    def __init__(self, variable, expresion, instruccion):
        self.variable = variable
        self.expresion = expresion
        self.instruccion = instruccion

    def ejecutarInstruccion(self, entorno):
        
        condicionPrincipal = self.expresion.obtenerValor(entorno)
        
        num = 0

        newSimbolo = Simbolo()
        newSimbolo.iniciarSimboloPrimitivo(self.variable, condicionPrincipal.valor, tipo=TIPO_DATO.ENTERO)
        
        var = self.expresion.obtenerValor(entorno)
        tamano = var.valor
        if var is not None:
            while num < tamano:
                for instr in self.instruccion:
                    element = instr.ejecutarInstruccion(entorno)
                    if element is not None:
                        if element.tipo == TIPO_DATO.BREAK:
                            break
                        else:
                            return element

                    if len(self.variable) > num + 1:
                        var.valor = self.variable.valor[num]
                        entorno.iniciarSimboloPrimitivo(self.variable, self.expresion.valor[num + 1], tipo=TIPO_DATO.ENTERO)
                    num += 1




# entorno.agregarSimbolo(newSimbolo)

