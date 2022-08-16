from AST.Abstract.Instruccion import Instruccion
from AST.Expresion.Identificador import Identificador
from Entorno.Simbolo import Simbolo


class Declaracion(Instruccion):

    def __init__(self, identificador:Identificador, expresion, tipo ):
        self.identificador = identificador
        self.expresion = expresion
        self.tipo = tipo

    def ejecutarInstruccion(self, entorno, txtSalida):
        existeSimbolo = entorno.existeSimbolo(self.identificador.nombre)

        if not existeSimbolo:
            retornoExpresion = self.expresion.obtenerValor(entorno)

            newSimbolo = Simbolo()
            newSimbolo.iniciarSimboloPrimitivo(self.identificador.nombre,retornoExpresion.valor, tipo = self.tipo )

            entorno.agregarSimobolo(newSimbolo)
        else:
            variableAMostrar = self.identificador.nombre
            print(f"Error semantico asignacion de variable, ya existe: {variableAMostrar} ")