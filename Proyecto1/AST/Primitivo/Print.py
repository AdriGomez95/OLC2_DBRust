import tkinter

from AST.Abstract.Instruccion import Instruccion



class Print(Instruccion):

    def __init__(self, expression):
        self.expression = expression

    def ejecutarInstruccion(self, entorno, txtSalida):
        retorno = self.expression.obtenerValor(entorno)
        #print(f"{retorno}")
        txtSalida.insert(tkinter.END, f"{retorno.valor}\n")