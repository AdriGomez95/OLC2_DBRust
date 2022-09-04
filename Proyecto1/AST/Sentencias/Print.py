import tkinter

from AST.Abstract.Instruccion import Instruccion
from main import Adriana


class Print(Instruccion):

    def __init__(self, expression):
        self.expression = expression

    def ejecutarInstruccion(self, entorno):        
        retorno = self.expression.obtenerValor(entorno)
        #print(f"{retorno}")
        entorno.txtSalida.insert(tkinter.END, f"{retorno.valor}\n")