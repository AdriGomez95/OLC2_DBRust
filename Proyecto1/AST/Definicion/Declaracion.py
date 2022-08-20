from AST.Abstract.Instruccion import Instruccion
from AST.Expresion.Identificador import Identificador
from Entorno.RetornoType import RetornoType
from Entorno.Simbolo import Simbolo


class Declaracion(Instruccion):

    def __init__(self, identificador:Identificador, expresion, tipo, mutable ):
        self.identificador = identificador
        self.valorInicializacion  = expresion
        self.tipo = tipo
        self.mutable = mutable
        self.retornoCompilado = None



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
                # manejo de errores
                return

            existeSimbolo = entorno.existeSimbolo(self.identificador.nombre)
            if existeSimbolo:
                # manejo de errores
                return

            newSimbolo = Simbolo()
            newSimbolo.iniciarSimboloPrimitivo(self.identificador.nombre, retornoExpresion.valor, tipo=self.tipo)

            entorno.agregarSimobolo(newSimbolo)


        else:
            pass


'''
    def ejecutarInstruccion(self, entorno, txtSalida):
        existeSimbolo = entorno.existeSimbolo(self.identificador.nombre)

        if not existeSimbolo:
            retornoExpresion = self.expresion.obtenerValor(entorno)

            newSimbolo = Simbolo()
            newSimbolo.iniciarSimboloPrimitivo(self.identificador.nombre,retornoExpresion.valor, tipo = self.tipo )

            entorno.agregarSimobolo(newSimbolo)
            #print(f"aqui ***************  {self.tipo} ")
        else:
            variableAMostrar = self.identificador.nombre
            print(f"Error semantico declaracion de variable, ya existe: {variableAMostrar} ")
'''
