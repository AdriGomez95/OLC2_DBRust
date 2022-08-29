from AST.Abstract.Expression import Expression
from AST.Definicion.Declaracion import Declaracion
from Entorno.EntornoTabla import EntornoTabla
from Entorno.RetornoType import RetornoType, TIPO_DATO
from Entorno.Simbolos.Clase import Clase
from Entorno.Simbolos.Funcion import Funcion
from Entorno.Simbolos.Instancia import Instancia


class InstanciaObjeto(Expression):

    def __init__(self, idClase, listaExpresiones):
        self.idClase =idClase
        self.listaExpresiones = listaExpresiones

    def obtenerValor(self, entorno) -> RetornoType:
        existeClase = entorno.existeClase(self.idClase)

        if existeClase is not True:
            print(f"Error semantico en {self.idClase} no existe")
            return

        clasePlantilla:Clase  = entorno.obtenerClase(self.idClase)
        ENTORNO_CLASE = EntornoTabla(entorno.consola, None)

        if len(clasePlantilla.instrucciones) != len(self.listaExpresiones):
            print(f"Error semantico, las expresiones enviadas no coincide con las propiedades de la clase")
            return

        index = 0
        for instruccion in clasePlantilla.instrucciones:

            if isinstance(instruccion, Declaracion):
                instruccion.retornoCompilado = self.listaExpresiones[index].obtenerValor(entorno)
                instruccion.ejecutarInstruccion(ENTORNO_CLASE)
                index += 1

            elif instruccion(instruccion, Funcion):
                pass

        instancia = Instancia(self.idClase, "", ENTORNO_CLASE)
        return RetornoType(valor=instancia, tipo=TIPO_DATO.OBJETO)