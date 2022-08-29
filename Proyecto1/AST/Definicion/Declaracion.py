from AST.Abstract.Instruccion import Instruccion
from AST.Expresion.Identificador import Identificador
from Entorno.RetornoType import RetornoType
from Entorno.Simbolo import Simbolo


class Declaracion(Instruccion):

    def __init__(self, identificador:Identificador, expresion, tipo, mutable, esReferencia = False ):
        self.identificador = identificador
        self.valorInicializacion  = expresion
        self.tipo = tipo
        self.mutable = mutable
        self.retornoCompilado = None

        self.esReferencia = esReferencia
        self.entornoReferencia = None
        self.valorReferencia = None




    def ejecutarInstruccion(self, entorno):
        if self.valorInicializacion is not None or self.retornoCompilado is not None:

            retornoExpresion = RetornoType()
            if self.valorInicializacion is not None:
                retornoExpresion = self.valorInicializacion.obtenerValor(entorno)
            else:
                retornoExpresion = self.retornoCompilado
                self.tipo = retornoExpresion.tipo

            tipoDeclaracion = self.tipo
            tipoExpresion = retornoExpresion.tipo

            if tipoDeclaracion != tipoExpresion:
                print(f"Error semantico en declaracion, el tipo de expresion no coincide con el tipo de variable ")
                return

            existeSimbolo = entorno.existeSimboloEnActual(self.identificador.nombre)
            if existeSimbolo:
                print(f"Error semantico en declaracion, ya existe la variable: {self.identificador.nombre} ")
                return




            newSimbolo = Simbolo()
            newSimbolo.iniciarSimboloPrimitivo(self.identificador.nombre, retornoExpresion.valor, tipo=self.tipo)

            if self.esReferencia is True:
                newSimbolo.entornoReferencia = self.entornoReferencia
                newSimbolo.valorReferencia = self.valorReferencia
                newSimbolo.iniciarSimboloPrimitivo(self.identificador.nombre, None, tipo=self.tipo)

            else:
                newSimbolo.iniciarSimboloPrimitivo(self.identificador.nombre, retornoExpresion.valor, tipo=self.tipo)

            entorno.agregarSimbolo(newSimbolo)


        else:
            pass



