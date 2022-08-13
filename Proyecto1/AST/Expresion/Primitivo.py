
from AST.Abstract.Expression import Expression
from Entorno.RetornoType import RetornoType
from enum import Enum


class Primitivo(Expression):


    def __init__(self, valor, tipoDato):
        self.valor = valor
        self.tipoDato = tipoDato

    def obtenerValor(self, entorno)-> RetornoType:
        return RetornoType(self.valor, self.tipoDato)