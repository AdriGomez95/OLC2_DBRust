
from idlelib.multicall import r

import ply.yacc as yacc
import ply.lex as lex

from AST.Definicion.Declaracion import Declaracion
from AST.Expresion.Identificador import Identificador
from AST.Expresion.Operacion import TIPO_OPERACION, Operacion
from AST.Expresion.Primitivo import Primitivo
from Entorno.RetornoType import TIPO_DATO
from AST.Sentencias.Print import Print



#--------------------------------------------------------------------
#----------------- Definicion del analizador lexico -----------------
#--------------------------------------------------------------------

#PALABRAS RESERVADAS
reservadas = {
    #tipos de dato
    'int': 'INTT',
    'i64': 'INT',
    'f64': 'FLOAT',

    #para operaciones
    'true': 'TRUE',
    'false': 'FALSE',
    'pow': 'POW',
    'powf': 'POWF',

    #para declarar variables
    'let': 'LET',
    'mut': 'MUT',

    #para sentencias de control
    'print': 'PRINT'
}


tokens = [
    'DOBLEPT',
    'COMA',
    'PTCOMA',
    'PIZQ',
    'PDER',
    'CORIZQ',
    'CORDER',

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
    'CADENA'
] + list(reservadas.values())


#--------- DEFINICION DE TOKENS
t_DOBLEPT = r'\:'
t_COMA = r'\,'
t_PTCOMA = r';'
t_PIZQ = r'\('
t_PDER = r'\)'
t_CORIZQ = r'\['
t_CORDER = r'\]'

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

def t_ID(t):
    r"""[a-zA-Z_][a-zA-Z0-9_]*"""
    t.type = reservadas.get(t.value.lower(), 'ID')
    return t

def t_CADENA(t):  
    """\".*?\""""
    t.value = t.value[1:-1]  # Eliminar las comillas dobles
    return  t

def t_newLine(t):
    r"""\n+"""
    t.lexer.lineno += t.value.count('\n')


t_ignore = " \t\r"


def t_error(t):
    print(f"Se encontro un error lexico {t.value[0]}")
    t.lexer.skip(1)



#CREANDO EL LEXER 
lexer = lex.lex()










#------------------------------------------------------------------------
#----------------- Definicion del analizador sintactico -----------------
#------------------------------------------------------------------------

precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('nonassoc', 'MAYOR', 'MENORIGUAL', 'MENOR', 'MAYORIGUAL', 'IGUALIGUAL', 'DIFERENTE'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'MULTIPLICACION', 'DIVISION'),
    ('left', 'MODULO'),
    ('right', 'NOT', 'UMENOS')
)


def p_init(t):
    """init : instrucciones"""
    t[0] = t[1]


######## LISTA DE INSTRUCCIONES ########
def p_instrucciones(t):
    """instrucciones : instrucciones instruccion"""
    t[1].append(t[2])
    t[0] = t[1]

def p_instrucciones_instruccion(t):
    """instrucciones : instruccion"""
    t[0] = [t[1]]

######## FIN DE LISTA DE INSTRUCCIONES ########
######## TIPOS DE INSTRUCCION ########

def p_instruccion(t):
    """instruccion : print_instruccion
                   | variables
                   | declaracion """
    t[0] = t[1]

def p_declaracion(t):
    """declaracion : INTT ID  IGUAL expression  PTCOMA
                    | INTT ID PTCOMA"""
    t[0] = Declaracion(Identificador(t[2]), t[4] , TIPO_DATO.ENTERO)







######## DECLARACION DE VARIABLES ########
def p_variables(t):
    """variables : LET MUT ID DOBLEPT tipo IGUAL expression PTCOMA
		         | LET ID DOBLEPT tipo IGUAL expression PTCOMA
		         | LET MUT ID IGUAL expression PTCOMA
		         | LET ID IGUAL expression PTCOMA
		         | ID IGUAL expression PTCOMA"""
    if t[3] == ':':
        t[0] = Declaracion(Identificador(t[2]), t[6] , t[4])
    elif t[3] == '=':
        t[0] = Declaracion(Identificador(t[2]), t[4] , TIPO_DATO.ENTERO)
    else:
        if t[4] == ':':
            t[0] = Declaracion(Identificador(t[3]), t[7] , t[5])
        elif t[4] == '=':
            t[0] = Declaracion(Identificador(t[3]), t[5] , TIPO_DATO.ENTERO)
        #else: #t[2]=='=' es una asignacion


def p_tipo(t):
    """tipo : INT
	        | FLOAT"""
    if t.slice[1].type == 'INT':
        t[0] = TIPO_DATO.ENTERO
    elif t.slice[1].type == 'FLOAT':
        t[0] = TIPO_DATO.DECIMAL







######## SENTENCIAS DE CONTROL ########
def p_print(t):
    """print_instruccion : PRINT NOT PIZQ expression PDER PTCOMA"""
    instr = Print(t[4])
    t[0] = instr








######## EXPRESIONES ########
def p_expression_logica(t):
    """expression : expression OR expression
                 | expression AND expression
                 | NOT expression %prec NOT"""

    if t[2] == '&&':
        t[0] = Operacion(t[1], TIPO_OPERACION.AND, t[3])
    if t[2] == '||':
        t[0] = Operacion(t[1], TIPO_OPERACION.OR, t[3])



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



def p_expression_primitiva(t):
    """expression : ENTERO
                  | DECIMAL
                  | ID
                  | CADENA
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
    elif t.slice[1].type == 'TRUE':
        t[0] = Primitivo(True, TIPO_DATO.BOOLEAN)
    elif t.slice[1].type == 'FALSE':
        t[0] = Primitivo(False, TIPO_DATO.BOOLEAN)



def p_error(t):
    print(f'Se encontro un error sintactico{t.value[0]}')






#---------------------------------------------------------
#----------------- Definicion del parser -----------------
#---------------------------------------------------------

parser = yacc.yacc()
def parse(input):
    global lexer
    lexer = lex.lex()
    return parser.parse(input)