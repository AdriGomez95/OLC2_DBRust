from AST.Abstract.Instruccion import Instruccion
from Entorno.EntornoTabla import EntornoTabla
from Entorno.Simbolos.Clase import Clase


class GuardarClase(Instruccion):

    def __init__(self, idClase, listaInstrucciones):
        self.idClase = idClase
        self.listaInstrucciones = listaInstrucciones

    def ejecutarInstruccion(self, entorno):
        existeClase = entorno.existeClase(self.idClase)

        if existeClase:
            print(f"Error semantico, la clase ya existe: {self.idClase}")
            return

        claseNueva = Clase(self.idClase,self.listaInstrucciones)
        entorno.agregarClase(claseNueva)

    def __str__(self):
        return f"GuardarClase ({self.idClase})"