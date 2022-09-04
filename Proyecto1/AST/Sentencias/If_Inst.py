from AST.Abstract.Instruccion import Instruccion
from AST.Errores.CustomError import CustomError
from Entorno.RetornoType import TIPO_DATO, RetornoType
#errorL = []

class If_inst(Instruccion):

    def __init__(self, condicion, listaInstrucionPrincipal, listaelseif, bloqueInstElse):
        self.condicion = condicion
        self.listaInstrucionPrincipal = listaInstrucionPrincipal
        self.listaelseif = listaelseif
        self.bloqueInstElse = bloqueInstElse
        #self.erroresL = erroresL

    def ejecutarInstruccion(self, entorno):

        condicionPrincipal = self.condicion.obtenerValor(entorno)

        if condicionPrincipal.tipo != TIPO_DATO.BOOLEAN:
            print(f"Error semantico en el if, tipo de dato a comparar no valido")
            #self.erroresL.append(CustomError("Semantico", "Error semantico en el if, tipo de dato a comparar no valido", 0,0))
            return RetornoType()
        else:

            if condicionPrincipal.valor == True:
                for instr in self.listaInstrucionPrincipal:
                    valorRetorno =  instr.ejecutarInstruccion(entorno)

                    if valorRetorno is not None:
                        if isinstance(valorRetorno, RetornoType):
                            return valorRetorno
                return

            else:
                # ejecutar instruccion else if
                for elseif in self.listaelseif:
                    condicionElseIf = elseif.condicion.obtenerValor(entorno)

                    if condicionPrincipal.tipo != TIPO_DATO.BOOLEAN:
                        print(f"Error semantico en el else if, tipo de dato a comparar no valido")
                        #self.erroresL.append(CustomError("Semantico", "Error semantico en el else if, tipo de dato a comparar no valido", 0,0))
                        return RetornoType()
                    else:
                        if condicionElseIf.valor == True:
                            for instr in elseif.listaInstrucionPrincipal:
                                valorRetorno = instr.ejecutarInstruccion(entorno)

                                if valorRetorno is not None:
                                    if isinstance(valorRetorno, RetornoType):
                                        return valorRetorno
                            return


                for instr in self.bloqueInstElse:
                    valorRetorno = instr.ejecutarInstruccion(entorno)

                    if valorRetorno is not None:
                        if isinstance(valorRetorno, RetornoType):
                            return valorRetorno

