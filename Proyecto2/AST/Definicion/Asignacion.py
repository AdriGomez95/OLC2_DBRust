from AST.Abstract.Instruccion import Instruccion
from AST.Expresion.Identificador import Identificador
from Entorno.Simbolo import Simbolo


class Asignacion(Instruccion):

    def __init__(self, identificador:Identificador, expresion):
        self.identificador = identificador
        self.expresion = expresion


        # cambio de entorno
        self.puntero_entorno_nuevo = ""
        self.ejecuta_en_funcion = False

        # declaración en HEAP
        self.declarar_en_instancia = False
   
    def ejecutar3D(self, entorno):
        
        CODIGO_SALIDA = ""

        tamanioEntorno = entorno.tamanio
        simbolo = entorno.obtenerSimbolo(self.identificador)
        PUNTERO_ENTORNO = "SP"
        SEGMENTO_MEMORIA = "Stack"


        if self.ejecuta_en_funcion:
            PUNTERO_ENTORNO = self.puntero_entorno_nuevo

        if self.declarar_en_instancia:
            PUNTERO_ENTORNO = self.puntero_entorno_nuevo
            SEGMENTO_MEMORIA = "Heap"



        #valorExpresion = self.expresion
        valorExpresion = self.expresion.obtener3D(entorno)
        temp1 = entorno.generador.obtenerTemporal()


        CODIGO_SALIDA += f"/* ASIGNACIÓN DE UNA VARIABLE   {self.identificador.nombre}*/\n"
        CODIGO_SALIDA += valorExpresion.codigo + '\n'
        CODIGO_SALIDA += f'    {temp1} = {PUNTERO_ENTORNO} + {simbolo.direccionRelativa}; \n'
        CODIGO_SALIDA += f'    {SEGMENTO_MEMORIA}[(int){temp1}] = {valorExpresion.temporal};\n'




        return CODIGO_SALIDA
