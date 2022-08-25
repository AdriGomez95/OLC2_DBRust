from AST.Abstract.Expression import Expression
from AST.Abstract.Instruccion import Instruccion
from Entorno.EntornoTabla import EntornoTabla
from Entorno.RetornoType import RetornoType


class Llamada(Instruccion, Expression):

    def __init__(self, identificador, listaExpresiones):
        self.identificador = identificador
        self.listaExpresiones = listaExpresiones

    def obtenerValor(self, entorno) -> RetornoType:
        existeFuncion = entorno.existeFuncion(self.identificador)

        if not existeFuncion:
            return RetornoType()

        ENTORNO_FUNCION = EntornoTabla(entorno.txtSalida,entorno.padre)
        ENTORNO_FUNCION.tablaFunciones = entorno.tablaFunciones
        funcion = entorno.obtenerFuncion(self.identificador)

        ejecutoParametros = funcion.ejecutarParametros(ENTORNO_FUNCION, self.listaExpresiones, entorno)

        if not ejecutoParametros:
            
            return RetornoType()

        retorno = funcion.ejecutarInstruccion(ENTORNO_FUNCION)
        if retorno != None and isinstance(retorno,RetornoType):
            return retorno
        else:
            return RetornoType()

    def ejecutarInstruccion(self, entorno):
        self.obtenerValor(entorno)

