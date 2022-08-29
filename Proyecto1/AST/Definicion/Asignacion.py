from AST.Abstract.Instruccion import Instruccion
from AST.Expresion.Identificador import Identificador
from Entorno.Simbolo import Simbolo


class Asignacion(Instruccion):

    def __init__(self, identificador:Identificador, expresion):
        self.identificador = identificador
        self.expresion = expresion

    def ejecutarInstruccion(self, entorno):
        existeSimbolo = entorno.obtenerSimbolo(self.identificador.nombre)

        if existeSimbolo:
            retornoExpresion = self.expresion.obtenerValor(entorno)
            existeSimbolo.iniciarSimboloPrimitivo(self.identificador.nombre,retornoExpresion.valor,retornoExpresion.tipo)


        else:
            variableAMostrar = self.identificador.nombre
            print(f"Error semantico asignacion de variable, no existe: {variableAMostrar} ")
