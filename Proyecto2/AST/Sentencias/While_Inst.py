from AST.Abstract.Instruccion import Instruccion
from Entorno.EntornoTabla import EntornoTabla
from Entorno.RetornoType import TIPO_DATO, RetornoType


class While_inst(Instruccion):

    def __init__(self, condicion, instruccion):
        self.condicion = condicion
        self.instruccion = instruccion

    
    def ejecutar3D(self, entorno):
        CODIGO_SALIDA = ""


        #etiqueta de inicio para el ciclo
        ETIQUETA_INICIO = entorno.generador.obtenerEtiqueta()


        #defino etiqueta falsa y verdadera para que tome el flujo correcto
        self.condicion.etiquetaVerdadera = entorno.generador.obtenerEtiqueta()
        self.condicion.etiquetaFalsa  = entorno.generador.obtenerEtiqueta()

        #recupero el c3d de la expresion
        expresionCondicion = self.condicion.obtener3D(entorno)
        


        #aqui ya el cd3 del while
        CODIGO_SALIDA += "/* INSTRUCCION WHILE */\n"
        CODIGO_SALIDA += f'    {ETIQUETA_INICIO}: \n'
        CODIGO_SALIDA += expresionCondicion.codigo
        CODIGO_SALIDA += f'    {expresionCondicion.etiquetaV}: \n'

        for instrWhile in self.instruccion:
            expresionSubCondion = instrWhile.ejecutar3D(entorno)
            CODIGO_SALIDA += "\n\n"
            CODIGO_SALIDA +=     expresionSubCondion



        CODIGO_SALIDA += f'    goto {ETIQUETA_INICIO}; \n'
        CODIGO_SALIDA += f'    {expresionCondicion.etiquetaF}: \n'

        return CODIGO_SALIDA

                



    def generarC3DInstrucciones(self,entorno,lista):

        CODIGO_SALIDA = ""
        for intrs in lista :
            CODIGO_SALIDA += intrs.ejecutar3D(entorno)

        return CODIGO_SALIDA

