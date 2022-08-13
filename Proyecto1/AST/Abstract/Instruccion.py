from abc import ABC, abstractmethod

class Instruccion(ABC):

    @abstractmethod
    def ejecutarInstruccion(self, entorno, txtSalida):
        pass