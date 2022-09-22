from http.client import CONTINUE
from typing import List
from AST.Abstract.Instruccion import Instruccion
from Entorno.RetornoType import RetornoType, TIPO_DATO
from Entorno.Simbolo import Simbolo


class Funcion(Simbolo, Instruccion):


    def __init__(self, identificador, listaParametros, listaInstrucciones, tipo):
        super().__init__()
        super().iniciarSimboloFuncion(identificador,listaParametros,listaInstrucciones,tipo)


    #1.ENTERO   2.DECIMAL   3.CADENA   4.BOOLEAN   5.VOID   6.NULL   7.&STR(CADENA2)  8.CHAR   9.FN
    comparacionTipo = [
        [TIPO_DATO.ENTERO, TIPO_DATO.DECIMAL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL],
        [TIPO_DATO.DECIMAL, TIPO_DATO.DECIMAL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL],
        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.CADENA, TIPO_DATO.NULL, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL],
        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.BOOLEAN, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL],
        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL],
        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL],
        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.CADENA2, TIPO_DATO.NULL, TIPO_DATO.NULL],
        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.CHAR, TIPO_DATO.NULL],
        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.FN],
    ]

    def ejecutarParametros(self, entornoFuncion, expresiones: [], entornoQueLlamo) -> bool:
        declaraciones  = self.parametros

        if len(declaraciones) != len(expresiones):
            print(f"Error semantico en la funcion, la lista de parametros no coincide")
            return False

        index = 0
        for declaracion in declaraciones:

            if declaracion.esReferencia is True:
                declaracion.entornoReferencia = entornoQueLlamo
                declaracion.valorReferencia =  expresiones[index]

            declaracion.retornoCompilado = expresiones[index].obtenerValor(entornoQueLlamo)
            declaracion.ejecutarInstruccion(entornoFuncion)
            index += 1

        return True


    def ejecutar3D(self, entorno):
        pass


    def __str__(self):
        return f"Funcion {self.identificador}"
