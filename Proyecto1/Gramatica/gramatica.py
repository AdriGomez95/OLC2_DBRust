
import re
from idlelib.multicall import r

import ply.yacc as yacc
import ply.lex as lex
from AST.Ast import Ast
from AST.Definicion.Asignacion import Asignacion

from AST.Definicion.Declaracion import Declaracion
from AST.Definicion.Objetos.CrearInstanciaObjeto import CrearInstanciaObjeto
from AST.Definicion.Objetos.GuardarClase import GuardarClase
from AST.Expresion.Acceso.AccesObjeto import AccesoObjeto
from AST.Expresion.Identificador import Identificador
from AST.Expresion.InstanciaObjeto.InstanciaObjeto import InstanciaObjeto
from AST.Expresion.Llamada import Llamada
from AST.Expresion.Operacion import TIPO_OPERACION, Operacion
from AST.Expresion.Primitivo import Primitivo
from AST.Sentencias.Break_Inst import Break_Inst
from AST.Sentencias.Continue_Inst import Continue_Inst
from AST.Sentencias.If_Inst import If_inst
from AST.Sentencias.Return_Instr import Return_Instr
from AST.Sentencias.While_Inst import While_inst
from Entorno.RetornoType import TIPO_DATO
from AST.Sentencias.Print import Print
from Entorno.Simbolos.Funcion import Funcion



#--------------------------------------------------------------------
#----------------- Definicion del analizador lexico -----------------
#--------------------------------------------------------------------

#PALABRAS RESERVADAS
reservadas = {
    #para funciones y struct
    'fn': 'FN',
    'return': 'RETURN',
    'break': 'BREAK',
    'continue': 'CONTINUE',

    #tipos de dato
    'i64': 'INT',
    'f64': 'FLOAT',
    #'to_string': 'BUFER1',
    #'to_owned': 'BUFER2',
    'string': 'STR1',
    'bool': 'BOOLEA',
    'char': 'CHAR',

    #para operaciones
    'true': 'TRUE',
    'false': 'FALSE',
    'pow': 'POW',
    'powf': 'POWF',

    #para declarar variables 
    'let': 'LET',
    'mut': 'MUT',

    #para sentencias de control
    'println': 'PRINT',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE'
}


tokens = [
    'PT',
    'DOBLEPT',
    'COMA',
    'PTCOMA',
    'PIZQ',
    'PDER',
    'LLAIZQ',
    'LLADER',
    'CIZQ',
    'CDER',

#logicas
    'AND',
    'OR',
    'NOT',

#relacionales
    'MAYORIGUAL',
    'MENOR',
    'MENORIGUAL',
    'MAYOR',
    'IGUALIGUAL',
    'DIFERENTE',
    'IGUAL',

#aritmeticas
    'MAS',
    'MENOS',
    'DIVISION',
    'MULTIPLICACION',
    'MODULO',

    'DECIMAL',
    'ENTERO',
    'ID',
    'CADENA',
    'STR2',
    'STRUCT',
    'TOSTRING',
    'TOOWNED'
] + list(reservadas.values())


#--------- DEFINICION DE TOKENS
t_PT = r'\.'
t_DOBLEPT = r'\:'
t_COMA = r'\,'
t_PTCOMA = r';'
t_PIZQ = r'\('
t_PDER = r'\)'
t_LLAIZQ = r'\{'
t_LLADER = r'\}'
t_CIZQ = r'\['
t_CDER = r'\]'

#logicas
t_AND = r'\&\&'
t_OR = r'\|\|'
t_NOT = r'\!'

#relacionales
t_MENOR = r'\<'
t_MAYOR = r'\>'
t_MAYORIGUAL = r'\>\='
t_MENORIGUAL = r'\<\='
t_IGUALIGUAL = r'\=\='
t_DIFERENTE = r'\!\='
t_IGUAL = r'\='

#aritmeticas
t_MAS = r'\+'
t_MENOS = r'-'
t_DIVISION = r'/'
t_MULTIPLICACION = r'\*'
t_MODULO = r'\%'




def t_DECIMAL(t):
    r"""\d+\.\d+"""
    try:
        t.value = float(t.value)
    except ValueError:
        t.value = 0.0
    return t

def t_ENTERO(t):
    r"""\d+"""
    try:
        t.value = int(t.value)
    except ValueError:
        t.value = 0
    return t

def t_TOOWNED(t):
    r""".to_owned"""
    t.type = reservadas.get(t.value.lower(), 'TOOWNED')
    return t

def t_TOSTRING(t):
    r""".to_string"""
    t.type = reservadas.get(t.value.lower(), 'TOSTRING')
    return t

def t_STRUCT(t):
    r"""struct"""
    t.type = reservadas.get(t.value.lower(), 'STRUCT')
    return t

def t_STR2(t):
    r"""&str"""
    t.type = reservadas.get(t.value.lower(), 'STR2')
    return t

def t_ID(t):
    r"""[a-zA-Z_][a-zA-Z0-9_]*"""
    t.type = reservadas.get(t.value.lower(), 'ID')
    return t

def t_CADENA(t):  
    """\".*?\""""
    t.value = t.value[1:-1]  # Eliminar las comillas dobles
    return  t

def t_CHAR(t):  
    """\'.*?\'"""
    t.value = t.value[1:-1]  # Eliminar las comillas simples
    return  t

def t_newLine(t):
    r"""\n+"""
    t.lexer.lineno += t.value.count('\n')


def t_COMENTARIOUNILINEA(t):
    r'\#.*\n'
    t.lexer.lineno += 1


t_ignore = " \t\r"


def t_error(t):
    print(f"Se encontro un error lexico {t.value[0]}")
    t.lexer.skip(1)



#CREANDO EL LEXER 
lexer = lex.lex(reflags=re.IGNORECASE)
#lexer = lex.lex()










#------------------------------------------------------------------------
#----------------- Definicion del analizador sintactico -----------------
#------------------------------------------------------------------------

precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('nonassoc', 'MAYOR', 'MENORIGUAL', 'MENOR', 'MAYORIGUAL', 'IGUALIGUAL', 'DIFERENTE'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'MULTIPLICACION', 'DIVISION', 'MODULO'),
    ('right', 'NOT', 'UMENOS')
)


#def p_init(t):
#    """init : instrucciones"""
#    t[0] = t[1]


def p_init(t):
    """init : clases_funciones"""
    t[0] = Ast(t[1])

def p_clases_funciones(t):
    """ clases_funciones : clases_funciones clase_funcion  """
    t[1].append(t[2])
    t[0] = t[1]

def p_clases_funciones_corte(t):
    """ clases_funciones : clase_funcion """
    t[0] = [t[1]]

def p_clase_funcion(t):
    """ clase_funcion : clase
                      | funcion """
    t[0] = t[1]






######## CLASES (STRUCTS) ########
def p_clase(t):
    """  clase : STRUCT ID LLAIZQ lista_parametros LLADER
               | STRUCT ID LLAIZQ  LLADER"""
    if len(t) == 6:
        t[0] = GuardarClase(idClase=t[2], listaInstrucciones=t[4])
    else:
        t[0] = GuardarClase(idClase=t[2], listaInstrucciones=[])






######## FUNCIONES ########
def p_funcion(t):
    """funcion : FN ID PIZQ lista_parametros PDER MENOS MAYOR tipo bloque
               | FN ID PIZQ lista_parametros PDER bloque
               | FN ID PIZQ PDER bloque"""
    if len(t) == 10:    #funcion con tipo definido
            t[0] = Funcion(t[2], t[4], t[9], t[8])
    else:
        if t[4] == ')': #es funcion main
            if t[2] == 'main':
                t[0] = Funcion(t[2],[], t[5], TIPO_DATO.FN)
            else:
                t[0] = Funcion(t[2],[], t[5], TIPO_DATO.NULL)

        else:   #es funcion normal pero sin tipo definido
            t[0] = Funcion(t[2],t[4],t[6], TIPO_DATO.NULL)



def p_lista_parametros(t):
    """lista_parametros : lista_parametros COMA parametroo"""
    t[1].append(t[3])
    t[0] = t[1]

def p_lista_parametros_corte(t):
    """lista_parametros : parametroo"""
    t[0] = [t[1]]

def p_parametroo(t): 
    """parametroo : ID DOBLEPT tipo"""
    id = Identificador(t[1])
    t[0] = Declaracion(id, None, t[3], "true")



def p_bloque(t):
    """bloque : LLAIZQ instrucciones LLADER
              | LLAIZQ LLADER"""
    if len(t) == 4:
        t[0] = t[2]
    else:
        t[0] = []













######## LISTA DE INSTRUCCIONES ########
def p_instrucciones(t):
    """instrucciones : instrucciones instruccion"""
    if t[2] != -1:
        t[1].append(t[2])
    t[0] = t[1]

def p_instrucciones_instruccion(t):
    """instrucciones : instruccion"""
    t[0] = [t[1]]

######## FIN DE LISTA DE INSTRUCCIONES ########
######## TIPOS DE INSTRUCCION ########

def p_instruccion(t):
    """instruccion : llamada PTCOMA
                   | variables PTCOMA
                   | declaracion_objeto PTCOMA
                   | print_instruccion PTCOMA
                   | return_instruccion PTCOMA
                   | break_instruccion PTCOMA
                   | continue_instruccion PTCOMA
                   | if_instruccion 
                   | while_instruccion """
    t[0] = t[1]














######## DECLARACION OBJETO ########
def p_declaracion_objeto(t):
    """ declaracion_objeto : ID ID IGUAL instancia_objeto """
    t[0] = CrearInstanciaObjeto(idClase=t[1], idInstancia=t[2], expresion=t[4])



# INSTANCIA OBJETO -------------------------
def p_instancia_objeto(t):
    """ instancia_objeto : ID LLAIZQ lista_expresiones LLADER
                         | ID LLAIZQ LLADER """
    if len(t) == 5:
        t[0] = InstanciaObjeto(idClase=t[1], listaExpresiones=t[3])
    else:
        t[0] = InstanciaObjeto(idClase=t[1], listaExpresiones=[])













######## LLAMADA DE FUNCIONES Y RETURN ########
def p_llamada(t):
    """llamada : ID PIZQ lista_expresiones PDER 
               | ID PIZQ PDER """
    if len(t) == 5:
        t[0] = Llamada(t[1], t[3])
    else:
        t[0] = Llamada(t[1], [])

def p_return_instruccion(t):
    """return_instruccion : RETURN expression
                          | RETURN """
    if len(t) == 3: #cuando viene una expresion, se le manda tipo de dato null porque
                    #la expresion al compilarla, ya trae su tipo
        t[0] = Return_Instr(TIPO_DATO.NULL, t[2])
    else:
        t[0] = Return_Instr(TIPO_DATO.FN, None)

def p_break_instruccion(t):
    """break_instruccion : BREAK """
    t[0] = Break_Inst(TIPO_DATO.BREAK)

def p_continue_instruccion(t):
    """continue_instruccion : CONTINUE """
    t[0] = Continue_Inst(TIPO_DATO.CONTINUE_STR)












######## DECLARACION DE VARIABLES ########
def p_variables(t):
    """variables : LET MUT ID DOBLEPT tipo IGUAL expression 
		         | LET ID DOBLEPT tipo IGUAL expression 
		         | LET MUT ID IGUAL expression 
		         | LET ID IGUAL expression 
		         | ID IGUAL expression"""
                 
    if len(t) == 8:
        t[0] = Declaracion(Identificador(t[3]), t[7] , t[5], "true")
    elif len(t) == 7:#variables inmutables
        t[0] = Declaracion(Identificador(t[2]), t[6] , t[4], "false")
    elif len(t) == 6:
        t[0] = Declaracion(Identificador(t[3]), t[5] , TIPO_DATO.ENTERO, "true")
    elif len(t) == 5:#variables inmutables
        t[0] = Declaracion(Identificador(t[2]), t[4] , TIPO_DATO.ENTERO, "false")
    else:#es asignacion
        t[0] = Asignacion(Identificador(t[1]), t[3])
    

def p_tipo(t):
    """tipo : INT
	        | FLOAT
	        | STR1
	        | STR2
	        | BOOLEA
	        | CHAR"""
    if t.slice[1].type == 'INT':
        t[0] = TIPO_DATO.ENTERO
    elif t.slice[1].type == 'FLOAT':
        t[0] = TIPO_DATO.DECIMAL
    elif t.slice[1].type == 'STR1':
        t[0] = TIPO_DATO.CADENA
    elif t.slice[1].type == 'STR2':
        t[0] = TIPO_DATO.CADENA2
    elif t.slice[1].type == 'BOOLEA':
        t[0] = TIPO_DATO.BOOLEAN
    elif t.slice[1].type == 'CHAR':
        t[0] = TIPO_DATO.CHAR















######## SENTENCIAS DE CONTROL ########
def p_print(t):
    """print_instruccion : PRINT NOT PIZQ expression PDER"""
    instr = Print(t[4])
    t[0] = instr



def p_if_instruccion(t):
    """if_instruccion : IF PIZQ expression PDER bloque
                      | IF PIZQ expression PDER bloque ELSE bloque 
                      | IF PIZQ expression PDER bloque lista_else_if
                      | IF PIZQ expression PDER bloque lista_else_if ELSE bloque """

    if len(t) == 6:
        t[0] = If_inst(t[3], t[5], [],[])
    elif len(t) == 7:
        t[0] = If_inst(t[3], t[5], t[6],[])
    elif len(t) == 8:
        t[0] = If_inst(t[3], t[5], [],t[7])
    else:
        t[0] = If_inst(t[3], t[5], t[6],t[8])

def p_lista_else_if(t):
    """lista_else_if : lista_else_if else_if"""
    t[1].append(t[2])
    t[0] = t[1]

def p_else_if_corte(t):
    """lista_else_if : else_if """
    t[0] = [t[1]]

def p_else_if(t):
    """else_if : ELSE IF PIZQ expression PDER bloque """
    t[0] = If_inst(t[4],t[6], [],[])



def p_while_instruccion(t):
    """while_instruccion : WHILE expression bloque """
    t[0] = While_inst(t[2], t[3])
















######## LO USA LLAMADA Y OBJETOS DE ARRIBA ########
def p_lista_expresiones(t):
    """lista_expresiones : lista_expresiones COMA expression"""
    t[1].append(t[3])
    t[0] = t[1]

def p_lista_expresiones_corte(t):
    """lista_expresiones : expression"""
    t[0] = [t[1]]
######## FIN ########


######## EXPRESIONES ########
def p_expression_logica(t):
    """expression : expression OR expression
                 | expression AND expression
                 | NOT expression %prec NOT"""

    if t[2] == '&&':
        t[0] = Operacion(t[1], TIPO_OPERACION.AND, t[3])
    if t[2] == '||':
        t[0] = Operacion(t[1], TIPO_OPERACION.OR, t[3])
    if t[1] == '!':
        t[0] = Operacion(t[2], TIPO_OPERACION.NOT, [])



def p_expression_relacional(t):
    """expression : expression MENOR expression
                 | expression MAYOR expression
                 | expression MAYORIGUAL expression
                 | expression MENORIGUAL expression
                 | expression DIFERENTE expression
                 | expression IGUALIGUAL expression"""

    if t[2] == '<':
        t[0] = Operacion(t[1], TIPO_OPERACION.MENOR, t[3])
    if t[2] == '>':
        t[0] = Operacion(t[1], TIPO_OPERACION.MAYOR, t[3])
    if t[2] == '<=':
        t[0] = Operacion(t[1], TIPO_OPERACION.MENORIGUAL, t[3])
    if t[2] == '>=':
        t[0] = Operacion(t[1], TIPO_OPERACION.MAYORIGUAL, t[3])
    if t[2] == '==':
        t[0] = Operacion(t[1], TIPO_OPERACION.IGUALIGUAL, t[3])
    if t[2] == '!=':
        t[0] = Operacion(t[1], TIPO_OPERACION.DIFERENTE, t[3])



def p_expression_aritmetica(t):
    """expression : MENOS expression %prec UMENOS
                 | expression MAS expression
                 | expression MENOS expression
                 | expression MULTIPLICACION expression
                 | expression DIVISION expression
                 | PIZQ expression PDER
                 | expression MODULO expression
                 | INT DOBLEPT DOBLEPT POW PIZQ expression COMA expression PDER
                 | FLOAT DOBLEPT DOBLEPT POWF PIZQ expression COMA expression PDER"""

    if len(t) == 3: #Coincide consimbolo y expresion, una operacion unaria
        t[0] = Operacion(t[2], TIPO_OPERACION.RESTA, None, True)
    elif t[1] == '(':
        t[0] = t[2]
    else:
        if t[2] == '+':
            t[0] = Operacion(t[1], TIPO_OPERACION.SUMA, t[3])
        elif t[2] == '-':
            t[0] = Operacion(t[1], TIPO_OPERACION.RESTA, t[3])
        elif t[2] == '*':
            t[0] = Operacion(t[1], TIPO_OPERACION.MULTIPLICACION, t[3])
        elif t[2] == '/':
            t[0] = Operacion(t[1], TIPO_OPERACION.DIVISION, t[3])
        elif t[2] == '%':
            t[0] = Operacion(t[1], TIPO_OPERACION.MODULO, t[3])
        else:
            if t[4] == 'pow':
                t[0] = Operacion(t[6], TIPO_OPERACION.POW, t[8])
            elif t[4] == 'powf':
                t[0] = Operacion(t[6], TIPO_OPERACION.POWF, t[8])



def p_expression_nativa(t):
    """expression : expression TOSTRING PIZQ PDER
                  | expression TOOWNED PIZQ PDER"""
    t[0] = t[1]
    #if t.slice[3].type == 'BUFER1':
    #    Nativa(t[1], TIPO_DATO.CADENA, 1)
    #    t[0] = t[1]
    #elif t.slice[3].type == 'BUFER2':
    #    Nativa(t[1], TIPO_DATO.CADENA, 1)
    #    t[0] = t[1]



def p_otras_expresiones(t):
    """expression : llamada
                  | acceso_objeto_expresion """
    t[0] = t[1]



def p_expression_primitiva(t):
    """expression : ENTERO
                  | DECIMAL
                  | ID
                  | CADENA
                  | CHAR
                  | TRUE
                  | FALSE"""

    if t.slice[1].type == 'ENTERO':
        t[0] = Primitivo(t[1], TIPO_DATO.ENTERO)
    elif t.slice[1].type == 'DECIMAL':
        t[0] = Primitivo(t[1], TIPO_DATO.DECIMAL)
    elif t.slice[1].type == 'ID':
        t[0] = Identificador(t[1])
    elif t.slice[1].type == 'CADENA':
        t[0] = Primitivo(t[1], TIPO_DATO.CADENA)
    elif t.slice[1].type == 'CHAR':
        t[0] = Primitivo(t[1], TIPO_DATO.CHAR)
    elif t.slice[1].type == 'TRUE':
        t[0] = Primitivo(True, TIPO_DATO.BOOLEAN)
    elif t.slice[1].type == 'FALSE':
        t[0] = Primitivo(False, TIPO_DATO.BOOLEAN)








# ACCESO A OBJETOS  ----------------------
def p_acceso_objeto_expresion(t):
    """ acceso_objeto_expresion : acceso_objeto"""
    t[0] = AccesoObjeto(listaExpresiones=t[1])


def p_acceso_objeto(t):
    """ acceso_objeto : acceso_objeto PT expression"""
    t[1].append(t[3])
    t[0] = t[1]


def p_acceso_objeto_cort(t):
    """ acceso_objeto : expression"""
    t[0] = [t[1]]













def p_error(t):
    print(f'Se encontro un error sintactico: {t.value[0]}')





#---------------------------------------------------------
#----------------- Definicion del parser -----------------
#---------------------------------------------------------

parser = yacc.yacc()
def parse(input):
    global lexer
    lexer = lex.lex()
    return parser.parse(input)