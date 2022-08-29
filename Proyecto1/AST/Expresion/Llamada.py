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
            print(f"Error semantico en la llamada, no existe la funcion: {self.identificador}")
            return RetornoType()

        ENTORNO_FUNCION = EntornoTabla(entorno.txtSalida,entorno)
        funcion = entorno.obtenerFuncion(self.identificador)

        ejecutoParametros = funcion.ejecutarParametros(ENTORNO_FUNCION, self.listaExpresiones, entorno)

        if not ejecutoParametros:
            print(f"Error semantico en los parametros de la funcion: {self.identificador}")
            return RetornoType()

        retorno = funcion.ejecutarInstruccion(ENTORNO_FUNCION)
        if retorno != None and isinstance(retorno,RetornoType):
            return retorno
        else:
            return RetornoType()

    def ejecutarInstruccion(self, entorno):
        self.obtenerValor(entorno)


'''
class Llamada(Instruccion, Expression):

    def __init__(self, identificador, listaExpresiones):
        self.identificador = identificador
        self.listaExpresiones = listaExpresiones

    def obtenerValor(self, entorno) -> RetornoType:
        existeFuncion = entorno.existeFuncion(self.identificador)

        if not existeFuncion:
            print(f"Error semantico en la llamada, no existe la funcion: **self.identificador**")
            return RetornoType()

        ENTORNO_FUNCION = EntornoTabla(entorno.txtSalida,entorno.padre)
        ENTORNO_FUNCION.tablaFunciones = entorno.tablaFunciones
        funcion = entorno.obtenerFuncion(self.identificador)

        ejecutoParametros = funcion.ejecutarParametros(ENTORNO_FUNCION, self.listaExpresiones, entorno)

        if not ejecutoParametros:
            print(f"Error semantico en los parametros de la funcion: **self.identificador**")
            return RetornoType()

        retorno = funcion.ejecutarInstruccion(ENTORNO_FUNCION)
        if retorno != None and isinstance(retorno,RetornoType):
            return retorno
        else:
            return RetornoType()

    def ejecutarInstruccion(self, entorno):
        self.obtenerValor(entorno)

'''
