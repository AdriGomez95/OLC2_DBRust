from AST.Abstract.Instruccion import Instruccion
from Entorno.RetornoType import RetornoType, TIPO_DATO


class CrearInstanciaObjeto(Instruccion):

    def __init__(self,idClase, idInstancia, expresion):
        self.idClase = idClase
        self.idInstancia = idInstancia
        self.expresion = expresion
        self.valorCompilador = None

    def ejecutarInstruccion(self, entorno):
        existeClase = entorno.existeClase(self.idClase)

        if existeClase is not True:
            print(f"Error semantico, no existe la instancia: {self.idClase}")
            return

        existeInstancia = entorno.existeSimbolo(self.idInstancia)
        if existeInstancia:
            print(f"Error semantico, la instancia ya esta creada: {self.idInstancia}")
            return

        expresionInstancia: RetornoType = self.expresion.obtenerValor(entorno)

        if expresionInstancia.tipo != TIPO_DATO.OBJETO:
            print(f"Error semantico, la expresion no es una instancia")
            return

        if expresionInstancia.valor.idClase != self.idClase:
            print(f"Error semantico, las clases no coiciden")
            return

        instanciaSimbolo = expresionInstancia.valor
        instanciaSimbolo.identificador = self.idInstancia

        entorno.agregarSimbolo(instanciaSimbolo)