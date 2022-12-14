from enum import Enum
#from multiprocessing.pool import INIT
from AST.Abstract.Expression import Expression
from AST.Errores.CustomError import CustomError
from Entorno.RetornoType import RetornoType, TIPO_DATO
import math

erroresL = []

class TIPO_OPERACION(Enum):
    SUMA = 1,
    RESTA = 2,
    MULTIPLICACION = 3,
    DIVISION = 4,
    MENOR = 5,
    MAYOR = 6,
    MENORIGUAL = 7,
    MAYORIGUAL = 8,
    DIFERENTE = 9,
    IGUALIGUAL = 10,
    AND = 11,
    OR = 12,
    NOT = 13,
    MODULO = 14,
    POW = 15,
    POWF = 16,

class Operacion(Expression):
    #1.ENTERO   2.DECIMAL   3.CADENA   4.BOOLEAN   5.VOID   8.NULL   7.&STR(CADENA2)  6.CHAR   9.FN
    #1.INTEGER	2.FLOAT		3.STRING   4.CHAR	5.BOOL	 6.&STRING	7.NULL


    sumaDominante = [
        [TIPO_DATO.ENTERO, TIPO_DATO.DECIMAL, TIPO_DATO.CADENA, TIPO_DATO.NULL, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.ENTERO, TIPO_DATO.NULL],
        [TIPO_DATO.DECIMAL, TIPO_DATO.DECIMAL, TIPO_DATO.CADENA, TIPO_DATO.NULL, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.DECIMAL, TIPO_DATO.NULL],
        [TIPO_DATO.CADENA, TIPO_DATO.CADENA, TIPO_DATO.CADENA, TIPO_DATO.CADENA, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.CADENA, TIPO_DATO.CADENA, TIPO_DATO.NULL],
        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.CADENA, TIPO_DATO.NULL, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL],
        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL],

        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL],
        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.CADENA, TIPO_DATO.NULL, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL],
        [TIPO_DATO.ENTERO, TIPO_DATO.DECIMAL, TIPO_DATO.CADENA, TIPO_DATO.NULL, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.ENTERO, TIPO_DATO.NULL],
        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL],
    ]

    restaMultiplicacionDivison = [
        [TIPO_DATO.ENTERO, TIPO_DATO.DECIMAL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.ENTERO, TIPO_DATO.NULL],
        [TIPO_DATO.DECIMAL, TIPO_DATO.DECIMAL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.DECIMAL, TIPO_DATO.NULL],
        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL],
        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL],
        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.ENTERO, TIPO_DATO.NULL],
        
        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL],
        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL],
        [TIPO_DATO.ENTERO, TIPO_DATO.DECIMAL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.ENTERO, TIPO_DATO.NULL],
        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL],
    ]

    RelacionalDominante = [
        [TIPO_DATO.ENTERO, TIPO_DATO.DECIMAL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.ENTERO, TIPO_DATO.NULL],
        [TIPO_DATO.DECIMAL, TIPO_DATO.DECIMAL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.DECIMAL, TIPO_DATO.NULL],
        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.CADENA, TIPO_DATO.NULL, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL],
        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL],
        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL],
           
        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL],
        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL],
        [TIPO_DATO.ENTERO, TIPO_DATO.DECIMAL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.ENTERO, TIPO_DATO.NULL],
        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL],
    ]

    PowDominante = [
        [TIPO_DATO.ENTERO, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL],
        [TIPO_DATO.NULL, TIPO_DATO.DECIMAL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL],
        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL],
        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL],
        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL],
             
        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL],
        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL],
        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL],
        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL],
    ]

    logicaDominante = [
        [TIPO_DATO.BOOLEAN, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL],
        [TIPO_DATO.NULL, TIPO_DATO.BOOLEAN, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL],
        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.BOOLEAN, TIPO_DATO.NULL, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL],
        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.BOOLEAN, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL],
        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL],

        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL],
        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.BOOLEAN, TIPO_DATO.NULL, TIPO_DATO.NULL],
        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.BOOLEAN, TIPO_DATO.NULL],
        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL,   TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL],
    ]

    def __init__(self, exprIzq, tipo_operacion, exprDer, unario = False):
        self.exprIzq = exprIzq
        self.tipo_operacion = tipo_operacion
        self.exprDer = exprDer
        self.unario = unario



    def obtenerValor(self, entorno):
        retornoIzq = RetornoType()
        retornoDer = RetornoType()
        retornoUnario = RetornoType()

        if self.unario:
            retornoUnario = self.exprIzq.obtenerValor(entorno)
        else:
            retornoIzq = self.exprIzq.obtenerValor(entorno)
            retornoDer = self.exprDer.obtenerValor(entorno)


#----------------------------------------------------------- ARITMETICAS ---------------------------

        if self.tipo_operacion == TIPO_OPERACION.SUMA:
            tipoResultante = Operacion.sumaDominante[retornoIzq.tipo][retornoDer.tipo]
            
            if tipoResultante == TIPO_DATO.ENTERO:
                return RetornoType(valor=(retornoIzq.valor + retornoDer.valor), tipo=tipoResultante)
            elif tipoResultante == TIPO_DATO.DECIMAL:
                return RetornoType(valor=(retornoIzq.valor + retornoDer.valor), tipo=tipoResultante)
            elif tipoResultante == TIPO_DATO.CADENA:
                return RetornoType(valor=(str(retornoIzq.valor) + str(retornoDer.valor)), tipo=tipoResultante)
            elif tipoResultante == TIPO_DATO.NULL:
                #erroresL.append(CustomError("Semantico", "imposible sumar, tipos incompatibles", self.linea, self.columna))
                print(f"Error semantico en suma, no se puede operar: {retornoIzq.tipo} con {retornoDer.tipo}")
                return RetornoType()



        elif self.tipo_operacion == TIPO_OPERACION.RESTA:
            if self.unario:
                return RetornoType(valor=(retornoUnario.valor * -1), tipo=retornoUnario.tipo)
            else:
                tipoResultante = Operacion.restaMultiplicacionDivison[retornoIzq.tipo][retornoDer.tipo]

                if tipoResultante == TIPO_DATO.ENTERO:
                    return RetornoType(valor=(retornoIzq.valor - retornoDer.valor), tipo=tipoResultante)
                elif tipoResultante == TIPO_DATO.DECIMAL:
                    return RetornoType(valor=(retornoIzq.valor - retornoDer.valor), tipo=tipoResultante)
                elif tipoResultante == TIPO_DATO.NULL:
                    print(f"Error semantico en resta, no se puede operar: {retornoIzq.tipo} con {retornoDer.tipo}")
                    return RetornoType()
        


        elif self.tipo_operacion == TIPO_OPERACION.MULTIPLICACION:
            tipoResultante = Operacion.restaMultiplicacionDivison[retornoIzq.tipo][retornoDer.tipo]
            if tipoResultante == TIPO_DATO.ENTERO:
                return RetornoType(valor=(retornoIzq.valor * retornoDer.valor), tipo=tipoResultante)
            elif tipoResultante == TIPO_DATO.DECIMAL:
                return RetornoType(valor=(retornoIzq.valor * retornoDer.valor), tipo=tipoResultante)
            elif tipoResultante == TIPO_DATO.NULL:
                print(f"Error semantico en multiplicacion, no se puede operar: {retornoIzq.tipo} con {retornoDer.tipo}")
                return RetornoType()
        


        elif self.tipo_operacion == TIPO_OPERACION.DIVISION:
            tipoResultante = Operacion.restaMultiplicacionDivison[retornoIzq.tipo][retornoDer.tipo]
            if tipoResultante == TIPO_DATO.ENTERO:
                return RetornoType(valor=(retornoIzq.valor / retornoDer.valor), tipo=tipoResultante)
            elif tipoResultante == TIPO_DATO.DECIMAL:
                return RetornoType(valor=(retornoIzq.valor / retornoDer.valor), tipo=tipoResultante)
            elif tipoResultante == TIPO_DATO.NULL:
                print(f"Error semantico en division, no se puede operar: {retornoIzq.tipo} con {retornoDer.tipo}")
                return RetornoType()
        


        elif self.tipo_operacion == TIPO_OPERACION.MODULO:
            tipoResultante = Operacion.PowDominante[retornoIzq.tipo][retornoDer.tipo]
            if tipoResultante == TIPO_DATO.ENTERO:
                return RetornoType(valor=(retornoIzq.valor % retornoDer.valor), tipo=tipoResultante)
            elif tipoResultante == TIPO_DATO.DECIMAL:
                return RetornoType(valor=(retornoIzq.valor % retornoDer.valor), tipo=tipoResultante)
            elif tipoResultante == TIPO_DATO.NULL:
                print(f"Error semantico en modulo, no se puede operar: {retornoIzq.tipo} con {retornoDer.tipo}")
                return RetornoType()
        


        elif self.tipo_operacion == TIPO_OPERACION.POW:
            tipoResultante = Operacion.PowDominante[retornoIzq.tipo][retornoDer.tipo]
            if tipoResultante == TIPO_DATO.ENTERO:
                return RetornoType(valor=(int(math.pow(retornoIzq.valor,retornoDer.valor))), tipo=tipoResultante)
            else:
                print(f"Error semantico en pow, no se puede operar: {retornoIzq.tipo} con {retornoDer.tipo}")
                return RetornoType()
        


        elif self.tipo_operacion == TIPO_OPERACION.POWF:
            tipoResultante = Operacion.PowDominante[retornoIzq.tipo][retornoDer.tipo]
            if tipoResultante == TIPO_DATO.DECIMAL:
                return RetornoType(valor=(int(math.pow(retornoIzq.valor,retornoDer.valor))), tipo=tipoResultante)
            else:
                print(f"Error semantico en powf, no se puede operar: {retornoIzq.tipo} con {retornoDer.tipo}")
                return RetornoType()









                
#----------------------------------------------------------- RELACIONALES ---------------------------

        elif self.tipo_operacion == TIPO_OPERACION.MENOR:
            tipoResultante = Operacion.RelacionalDominante[retornoIzq.tipo][retornoDer.tipo]
            if tipoResultante == TIPO_DATO.ENTERO:
                return RetornoType(valor=(retornoIzq.valor < retornoDer.valor), tipo=TIPO_DATO.BOOLEAN)
            elif tipoResultante == TIPO_DATO.DECIMAL:
                return RetornoType(valor=(retornoIzq.valor < retornoDer.valor), tipo=TIPO_DATO.BOOLEAN)
            elif tipoResultante == TIPO_DATO.CADENA:
                return RetornoType(valor=(retornoIzq.valor > retornoDer.valor), tipo=TIPO_DATO.BOOLEAN)
            elif tipoResultante == TIPO_DATO.NULL:
                print(f"Error semantico en relacional <, no se puede comparar: {retornoIzq.tipo} con {retornoDer.tipo}")
                return RetornoType()



        elif self.tipo_operacion == TIPO_OPERACION.MAYOR:
            tipoResultante = Operacion.RelacionalDominante[retornoIzq.tipo][retornoDer.tipo]
            if tipoResultante == TIPO_DATO.ENTERO:
                return RetornoType(valor=(retornoIzq.valor > retornoDer.valor), tipo=TIPO_DATO.BOOLEAN)
            elif tipoResultante == TIPO_DATO.DECIMAL:
                return RetornoType(valor=(retornoIzq.valor > retornoDer.valor), tipo=TIPO_DATO.BOOLEAN)
            elif tipoResultante == TIPO_DATO.CADENA:
                return RetornoType(valor=(retornoIzq.valor > retornoDer.valor), tipo=TIPO_DATO.BOOLEAN)
            elif tipoResultante == TIPO_DATO.NULL:
                print(f"Error semantico en relacional >, no se puede comparar: {retornoIzq.tipo} con {retornoDer.tipo}")
                return RetornoType()



        elif self.tipo_operacion == TIPO_OPERACION.MENORIGUAL:
            tipoResultante = Operacion.RelacionalDominante[retornoIzq.tipo][retornoDer.tipo]
            if tipoResultante == TIPO_DATO.ENTERO:
                return RetornoType(valor=(retornoIzq.valor <= retornoDer.valor), tipo=TIPO_DATO.BOOLEAN)
            elif tipoResultante == TIPO_DATO.DECIMAL:
                return RetornoType(valor=(retornoIzq.valor <= retornoDer.valor), tipo=TIPO_DATO.BOOLEAN)
            elif tipoResultante == TIPO_DATO.CADENA:
                return RetornoType(valor=(retornoIzq.valor <= retornoDer.valor), tipo=TIPO_DATO.BOOLEAN)
            elif tipoResultante == TIPO_DATO.NULL:
                print(f"Error semantico en relacional <=, no se puede comparar: {retornoIzq.tipo} con {retornoDer.tipo}")
                return RetornoType()



        elif self.tipo_operacion == TIPO_OPERACION.MAYORIGUAL:
            tipoResultante = Operacion.RelacionalDominante[retornoIzq.tipo][retornoDer.tipo]
            if tipoResultante == TIPO_DATO.ENTERO:
                return RetornoType(valor=(retornoIzq.valor >= retornoDer.valor), tipo=TIPO_DATO.BOOLEAN)
            elif tipoResultante == TIPO_DATO.DECIMAL:
                return RetornoType(valor=(retornoIzq.valor >= retornoDer.valor), tipo=TIPO_DATO.BOOLEAN)
            elif tipoResultante == TIPO_DATO.CADENA:
                return RetornoType(valor=(retornoIzq.valor >= retornoDer.valor), tipo=TIPO_DATO.BOOLEAN)
            elif tipoResultante == TIPO_DATO.NULL:
                print(f"Error semantico en relacional >=, no se puede comparar: {retornoIzq.tipo} con {retornoDer.tipo}")
                return RetornoType()



        elif self.tipo_operacion == TIPO_OPERACION.DIFERENTE:
            tipoResultante = Operacion.RelacionalDominante[retornoIzq.tipo][retornoDer.tipo]
            if tipoResultante == TIPO_DATO.ENTERO:
                return RetornoType(valor=(retornoIzq.valor != retornoDer.valor), tipo=TIPO_DATO.BOOLEAN)
            elif tipoResultante == TIPO_DATO.DECIMAL:
                return RetornoType(valor=(retornoIzq.valor != retornoDer.valor), tipo=TIPO_DATO.BOOLEAN)
            elif tipoResultante == TIPO_DATO.CADENA:
                return RetornoType(valor=(retornoIzq.valor != retornoDer.valor), tipo=TIPO_DATO.BOOLEAN)
            elif tipoResultante == TIPO_DATO.NULL:
                print(f"Error semantico en relacional !=, no se puede comparar: {retornoIzq.tipo} con {retornoDer.tipo}")
                return RetornoType()



        elif self.tipo_operacion == TIPO_OPERACION.IGUALIGUAL:
            tipoResultante = Operacion.RelacionalDominante[retornoIzq.tipo][retornoDer.tipo]
            if tipoResultante == TIPO_DATO.ENTERO:
                return RetornoType(valor=(retornoIzq.valor == retornoDer.valor), tipo=TIPO_DATO.BOOLEAN)
            elif tipoResultante == TIPO_DATO.DECIMAL:
                return RetornoType(valor=(retornoIzq.valor == retornoDer.valor), tipo=TIPO_DATO.BOOLEAN)
            elif tipoResultante == TIPO_DATO.CADENA:
                return RetornoType(valor=(retornoIzq.valor == retornoDer.valor), tipo=TIPO_DATO.BOOLEAN)
            elif tipoResultante == TIPO_DATO.NULL:
                print(f"Error semantico en relacional ==, no se puede comparar: {retornoIzq.tipo} con {retornoDer.tipo}")
                return RetornoType()









                
             
#----------------------------------------------------------- LOGICA ---------------------------

        elif self.tipo_operacion == TIPO_OPERACION.AND:
            tipoResultante = Operacion.logicaDominante[retornoIzq.tipo][retornoDer.tipo]
            if tipoResultante == TIPO_DATO.BOOLEAN:
                return RetornoType(valor=(bool(retornoIzq.valor) and bool(retornoDer.valor)), tipo=tipoResultante)
            elif tipoResultante == TIPO_DATO.NULL:
                print(f"Error semantico en logica &&, no se puede comparar: {retornoIzq.tipo} con {retornoDer.tipo}")
                return RetornoType()


        elif self.tipo_operacion == TIPO_OPERACION.OR:
            tipoResultante = Operacion.logicaDominante[retornoIzq.tipo][retornoDer.tipo]
            if tipoResultante == TIPO_DATO.BOOLEAN:
                return RetornoType(valor=(bool(retornoIzq.valor) or bool(retornoDer.valor)), tipo=tipoResultante)
            elif tipoResultante == TIPO_DATO.NULL:
                print(f"Error semantico en logica || no se puede comparar: {retornoIzq.tipo} con {retornoDer.tipo}")
                return RetornoType()


        elif self.tipo_operacion == TIPO_OPERACION.NOT:
            if retornoIzq.tipo == TIPO_DATO.ENTERO:
                return RetornoType(valor=(-1*retornoIzq.valor), tipo= retornoIzq.tipo)
            if retornoIzq.tipo == TIPO_DATO.DECIMAL:
                return RetornoType(valor=(-1*retornoIzq.valor), tipo= retornoIzq.tipo)
            elif retornoIzq.tipo == TIPO_DATO.NULL:
                print(f"Error semantico en logica ! no se puede operar")
                return RetornoType()
                


