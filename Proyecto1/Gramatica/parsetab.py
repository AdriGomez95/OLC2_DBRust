
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDnonassocMAYORMENORIGUALMENORMAYORIGUALIGUALIGUALDIFERENTEleftMASMENOSleftMULTIPLICACIONDIVISIONMODULOrightNOTUMENOSAND BOOLEA BREAK CADENA CDER CHAR CIZQ COMA CONTINUE DECIMAL DIFERENTE DIVISION DOBLEPT ELSE ENTERO FALSE FLOAT FN FOR ID IF IGUAL IGUALIGUAL IN INT LET LLADER LLAIZQ MAS MAYOR MAYORIGUAL MENOR MENORIGUAL MENOS MODULO MULTIPLICACION MUT NOT OR PDER PIZQ POW POWF PRINT PT PTCOMA RETURN STR1 STR2 STRUCT TOOWNED TOSTRING TRUE WHILEinit : clases_funciones clases_funciones : clases_funciones clase_funcion   clases_funciones : clase_funcion  clase_funcion : clase\n                      | funcion   clase : STRUCT ID LLAIZQ lista_parametros LLADER\n               | STRUCT ID LLAIZQ  LLADERfuncion : FN ID PIZQ lista_parametros PDER MENOS MAYOR tipo bloque\n               | FN ID PIZQ lista_parametros PDER bloque\n               | FN ID PIZQ PDER bloquelista_parametros : lista_parametros COMA parametroolista_parametros : parametrooparametroo : ID DOBLEPT tipobloque : LLAIZQ instrucciones LLADER\n              | LLAIZQ LLADERinstrucciones : instrucciones instruccioninstrucciones : instruccioninstruccion : llamada PTCOMA\n                   | variables PTCOMA\n                   | declaracion_objeto PTCOMA\n                   | print_instruccion PTCOMA\n                   | return_instruccion PTCOMA\n                   | break_instruccion PTCOMA\n                   | continue_instruccion PTCOMA\n                   | if_instruccion \n                   | while_instruccion \n                   | for_instruccion  declaracion_objeto : ID ID IGUAL instancia_objeto  instancia_objeto : ID LLAIZQ lista_expresiones LLADER\n                         | ID LLAIZQ LLADER llamada : ID PIZQ lista_expresiones PDER \n               | ID PIZQ PDER return_instruccion : RETURN expression\n                          | RETURN break_instruccion : BREAK continue_instruccion : CONTINUE variables : LET MUT ID DOBLEPT tipo IGUAL expression \n\t\t         | LET ID DOBLEPT tipo IGUAL expression \n\t\t         | LET MUT ID IGUAL expression \n\t\t         | LET ID IGUAL expression \n\t\t         | ID IGUAL expressiontipo : INT\n\t        | FLOAT\n\t        | STR1\n\t        | STR2\n\t        | BOOLEA\n\t        | CHARprint_instruccion : PRINT NOT PIZQ expression PDERif_instruccion : IF PIZQ expression PDER bloque\n                      | IF PIZQ expression PDER bloque ELSE bloque \n                      | IF PIZQ expression PDER bloque lista_else_if\n                      | IF PIZQ expression PDER bloque lista_else_if ELSE bloque lista_else_if : lista_else_if else_iflista_else_if : else_if else_if : ELSE IF PIZQ expression PDER bloque while_instruccion : WHILE expression bloque for_instruccion : FOR ID IN expression bloquelista_expresiones : lista_expresiones COMA expressionlista_expresiones : expressionexpression : expression OR expression\n                 | expression AND expression\n                 | NOT expression %prec NOTexpression : expression MENOR expression\n                 | expression MAYOR expression\n                 | expression MAYORIGUAL expression\n                 | expression MENORIGUAL expression\n                 | expression DIFERENTE expression\n                 | expression IGUALIGUAL expressionexpression : MENOS expression %prec UMENOS\n                 | expression MAS expression\n                 | expression MENOS expression\n                 | expression MULTIPLICACION expression\n                 | expression DIVISION expression\n                 | PIZQ expression PDER\n                 | expression MODULO expression\n                 | INT DOBLEPT DOBLEPT POW PIZQ expression COMA expression PDER\n                 | FLOAT DOBLEPT DOBLEPT POWF PIZQ expression COMA expression PDERexpression : expression TOSTRING PIZQ PDER\n                  | expression TOOWNED PIZQ PDERexpression : llamada\n                  | acceso_objeto_expresion expression : ENTERO\n                  | DECIMAL\n                  | ID\n                  | CADENA\n                  | CHAR\n                  | TRUE\n                  | FALSE acceso_objeto_expresion : acceso_objeto acceso_objeto : acceso_objeto PT expression acceso_objeto : expression'
    
_lr_action_items = {'STRUCT':([0,2,3,4,5,8,15,20,23,34,36,58,126,],[6,6,-3,-4,-5,-2,-7,-6,-10,-9,-15,-14,-8,]),'FN':([0,2,3,4,5,8,15,20,23,34,36,58,126,],[7,7,-3,-4,-5,-2,-7,-6,-10,-9,-15,-14,-8,]),'$end':([1,2,3,4,5,8,15,20,23,34,36,58,126,],[0,-1,-3,-4,-5,-2,-7,-6,-10,-9,-15,-14,-8,]),'ID':([6,7,11,12,21,24,35,36,37,45,46,47,48,49,51,55,56,58,59,60,61,62,63,64,65,66,68,69,70,74,75,76,89,93,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,122,124,125,130,132,157,161,167,168,171,173,174,176,177,183,185,186,187,188,189,196,],[9,10,13,13,13,48,48,-15,-17,-25,-26,-27,67,71,83,83,91,-14,-16,-18,-19,-20,-21,-22,-23,-24,83,83,98,83,83,83,83,127,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,-56,83,83,83,83,83,-49,-57,83,83,83,-51,-54,-50,-53,83,83,83,-52,-55,]),'LLAIZQ':([9,18,22,26,27,28,29,30,31,79,80,81,82,83,84,85,86,87,88,90,92,95,117,118,127,129,136,137,138,139,140,141,142,143,144,145,146,147,148,151,154,155,156,163,164,175,184,193,194,195,],[11,24,24,-42,-43,-44,-45,-46,-47,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,24,24,-32,-62,-69,157,-31,-60,-61,-63,-64,-65,-66,-67,-68,-70,-71,-72,-73,-75,-74,-90,24,24,-78,-79,24,24,-76,-77,24,]),'PIZQ':([10,48,51,54,55,68,69,72,74,75,76,83,89,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,122,125,130,132,157,161,165,166,171,173,174,182,186,187,188,],[12,68,76,89,76,76,76,101,76,76,76,68,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,149,150,76,76,76,76,76,76,173,174,76,76,76,188,76,76,76,]),'LLADER':([11,14,16,24,25,26,27,28,29,30,31,32,35,36,37,45,46,47,58,59,60,61,62,63,64,65,66,79,80,81,82,83,84,85,86,87,88,95,96,117,118,124,129,136,137,138,139,140,141,142,143,144,145,146,147,148,151,154,157,158,163,164,167,168,169,176,177,183,185,189,193,194,196,],[15,20,-12,36,-13,-42,-43,-44,-45,-46,-47,-11,58,-15,-17,-25,-26,-27,-14,-16,-18,-19,-20,-21,-22,-23,-24,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,-32,-59,-62,-69,-56,-31,-60,-61,-63,-64,-65,-66,-67,-68,-70,-71,-72,-73,-75,-74,-90,170,-58,-78,-79,-49,-57,178,-51,-54,-50,-53,-52,-76,-77,-55,]),'PDER':([12,16,17,25,26,27,28,29,30,31,32,68,79,80,81,82,83,84,85,86,87,88,94,95,96,117,118,119,123,129,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,154,158,163,164,190,191,192,193,194,],[18,-12,22,-13,-42,-43,-44,-45,-46,-47,-11,95,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,129,-32,-59,-62,-69,151,155,-31,162,-60,-61,-63,-64,-65,-66,-67,-68,-70,-71,-72,-73,-75,163,164,-74,-90,-58,-78,-79,193,194,195,-76,-77,]),'DOBLEPT':([13,71,77,78,98,120,121,],[19,99,120,121,131,152,153,]),'COMA':([14,16,17,25,26,27,28,29,30,31,32,79,80,81,82,83,84,85,86,87,88,94,95,96,117,118,129,136,137,138,139,140,141,142,143,144,145,146,147,148,151,154,158,163,164,169,180,181,193,194,],[21,-12,21,-13,-42,-43,-44,-45,-46,-47,-11,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,130,-32,-59,-62,-69,-31,-60,-61,-63,-64,-65,-66,-67,-68,-70,-71,-72,-73,-75,-74,-90,-58,-78,-79,130,186,187,-76,-77,]),'INT':([19,51,55,57,68,69,74,75,76,89,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,122,125,130,131,132,157,161,171,173,174,186,187,188,],[26,77,77,26,77,77,77,77,77,77,26,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,26,77,77,77,77,77,77,77,77,77,]),'FLOAT':([19,51,55,57,68,69,74,75,76,89,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,122,125,130,131,132,157,161,171,173,174,186,187,188,],[27,78,78,27,78,78,78,78,78,78,27,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,27,78,78,78,78,78,78,78,78,78,]),'STR1':([19,57,99,131,],[28,28,28,28,]),'STR2':([19,57,99,131,],[29,29,29,29,]),'BOOLEA':([19,57,99,131,],[30,30,30,30,]),'CHAR':([19,51,55,57,68,69,74,75,76,89,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,122,125,130,131,132,157,161,171,173,174,186,187,188,],[31,85,85,31,85,85,85,85,85,85,31,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,31,85,85,85,85,85,85,85,85,85,]),'MENOS':([22,51,55,68,69,73,74,75,76,79,80,81,82,83,84,85,86,87,88,89,90,95,96,97,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,117,118,119,122,123,125,129,130,132,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,151,154,156,157,158,160,161,163,164,171,172,173,174,179,180,181,186,187,188,190,191,192,193,194,],[33,75,75,75,75,111,75,75,75,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,75,111,-32,111,111,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,-62,-69,111,75,111,75,-31,75,75,111,111,111,111,111,111,111,111,111,111,-70,-71,-72,-73,-75,-74,111,111,75,111,111,75,-78,-79,75,111,75,75,111,111,111,75,75,75,111,111,111,-76,-77,]),'LET':([24,35,36,37,45,46,47,58,59,60,61,62,63,64,65,66,124,167,168,176,177,183,185,189,196,],[49,49,-15,-17,-25,-26,-27,-14,-16,-18,-19,-20,-21,-22,-23,-24,-56,-49,-57,-51,-54,-50,-53,-52,-55,]),'PRINT':([24,35,36,37,45,46,47,58,59,60,61,62,63,64,65,66,124,167,168,176,177,183,185,189,196,],[50,50,-15,-17,-25,-26,-27,-14,-16,-18,-19,-20,-21,-22,-23,-24,-56,-49,-57,-51,-54,-50,-53,-52,-55,]),'RETURN':([24,35,36,37,45,46,47,58,59,60,61,62,63,64,65,66,124,167,168,176,177,183,185,189,196,],[51,51,-15,-17,-25,-26,-27,-14,-16,-18,-19,-20,-21,-22,-23,-24,-56,-49,-57,-51,-54,-50,-53,-52,-55,]),'BREAK':([24,35,36,37,45,46,47,58,59,60,61,62,63,64,65,66,124,167,168,176,177,183,185,189,196,],[52,52,-15,-17,-25,-26,-27,-14,-16,-18,-19,-20,-21,-22,-23,-24,-56,-49,-57,-51,-54,-50,-53,-52,-55,]),'CONTINUE':([24,35,36,37,45,46,47,58,59,60,61,62,63,64,65,66,124,167,168,176,177,183,185,189,196,],[53,53,-15,-17,-25,-26,-27,-14,-16,-18,-19,-20,-21,-22,-23,-24,-56,-49,-57,-51,-54,-50,-53,-52,-55,]),'IF':([24,35,36,37,45,46,47,58,59,60,61,62,63,64,65,66,124,167,168,175,176,177,183,184,185,189,196,],[54,54,-15,-17,-25,-26,-27,-14,-16,-18,-19,-20,-21,-22,-23,-24,-56,-49,-57,182,-51,-54,-50,182,-53,-52,-55,]),'WHILE':([24,35,36,37,45,46,47,58,59,60,61,62,63,64,65,66,124,167,168,176,177,183,185,189,196,],[55,55,-15,-17,-25,-26,-27,-14,-16,-18,-19,-20,-21,-22,-23,-24,-56,-49,-57,-51,-54,-50,-53,-52,-55,]),'FOR':([24,35,36,37,45,46,47,58,59,60,61,62,63,64,65,66,124,167,168,176,177,183,185,189,196,],[56,56,-15,-17,-25,-26,-27,-14,-16,-18,-19,-20,-21,-22,-23,-24,-56,-49,-57,-51,-54,-50,-53,-52,-55,]),'IGUAL':([26,27,28,29,30,31,48,67,71,98,133,159,],[-42,-43,-44,-45,-46,-47,69,93,100,132,161,171,]),'MAYOR':([33,73,79,80,81,82,83,84,85,86,87,88,90,95,96,97,117,118,119,123,129,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,151,154,156,158,160,163,164,172,179,180,181,190,191,192,193,194,],[57,105,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,105,-32,105,105,-62,-69,105,105,-31,105,105,105,105,-91,-91,-91,-91,-91,-91,-70,-71,-72,-73,-75,-74,105,105,105,105,-78,-79,105,105,105,105,105,105,105,-76,-77,]),'ELSE':([36,58,167,176,177,185,196,],[-15,-14,175,184,-54,-53,-55,]),'PTCOMA':([38,39,40,41,42,43,44,51,52,53,73,79,80,81,82,83,84,85,86,87,88,95,97,117,118,128,129,134,136,137,138,139,140,141,142,143,144,145,146,147,148,151,154,160,162,163,164,170,172,178,179,193,194,],[60,61,62,63,64,65,66,-34,-35,-36,-33,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,-32,-41,-62,-69,-28,-31,-40,-60,-61,-63,-64,-65,-66,-67,-68,-70,-71,-72,-73,-75,-74,-90,-39,-48,-78,-79,-30,-38,-29,-37,-76,-77,]),'MUT':([49,],[70,]),'NOT':([50,51,55,68,69,74,75,76,89,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,122,125,130,132,157,161,171,173,174,186,187,188,],[72,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,]),'ENTERO':([51,55,68,69,74,75,76,89,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,122,125,130,132,157,161,171,173,174,186,187,188,],[81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,]),'DECIMAL':([51,55,68,69,74,75,76,89,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,122,125,130,132,157,161,171,173,174,186,187,188,],[82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,]),'CADENA':([51,55,68,69,74,75,76,89,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,122,125,130,132,157,161,171,173,174,186,187,188,],[84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,]),'TRUE':([51,55,68,69,74,75,76,89,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,122,125,130,132,157,161,171,173,174,186,187,188,],[86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,]),'FALSE':([51,55,68,69,74,75,76,89,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,122,125,130,132,157,161,171,173,174,186,187,188,],[87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,]),'OR':([73,79,80,81,82,83,84,85,86,87,88,90,95,96,97,117,118,119,123,129,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,151,154,156,158,160,163,164,172,179,180,181,190,191,192,193,194,],[102,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,102,-32,102,102,-62,-69,102,102,-31,102,102,-60,-61,-63,-64,-65,-66,-67,-68,-70,-71,-72,-73,-75,-74,102,102,102,102,-78,-79,102,102,102,102,102,102,102,-76,-77,]),'AND':([73,79,80,81,82,83,84,85,86,87,88,90,95,96,97,117,118,119,123,129,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,151,154,156,158,160,163,164,172,179,180,181,190,191,192,193,194,],[103,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,103,-32,103,103,-62,-69,103,103,-31,103,103,103,-61,-63,-64,-65,-66,-67,-68,-70,-71,-72,-73,-75,-74,103,103,103,103,-78,-79,103,103,103,103,103,103,103,-76,-77,]),'MENOR':([73,79,80,81,82,83,84,85,86,87,88,90,95,96,97,117,118,119,123,129,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,151,154,156,158,160,163,164,172,179,180,181,190,191,192,193,194,],[104,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,104,-32,104,104,-62,-69,104,104,-31,104,104,104,104,-91,-91,-91,-91,-91,-91,-70,-71,-72,-73,-75,-74,104,104,104,104,-78,-79,104,104,104,104,104,104,104,-76,-77,]),'MAYORIGUAL':([73,79,80,81,82,83,84,85,86,87,88,90,95,96,97,117,118,119,123,129,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,151,154,156,158,160,163,164,172,179,180,181,190,191,192,193,194,],[106,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,106,-32,106,106,-62,-69,106,106,-31,106,106,106,106,-91,-91,-91,-91,-91,-91,-70,-71,-72,-73,-75,-74,106,106,106,106,-78,-79,106,106,106,106,106,106,106,-76,-77,]),'MENORIGUAL':([73,79,80,81,82,83,84,85,86,87,88,90,95,96,97,117,118,119,123,129,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,151,154,156,158,160,163,164,172,179,180,181,190,191,192,193,194,],[107,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,107,-32,107,107,-62,-69,107,107,-31,107,107,107,107,-91,-91,-91,-91,-91,-91,-70,-71,-72,-73,-75,-74,107,107,107,107,-78,-79,107,107,107,107,107,107,107,-76,-77,]),'DIFERENTE':([73,79,80,81,82,83,84,85,86,87,88,90,95,96,97,117,118,119,123,129,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,151,154,156,158,160,163,164,172,179,180,181,190,191,192,193,194,],[108,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,108,-32,108,108,-62,-69,108,108,-31,108,108,108,108,-91,-91,-91,-91,-91,-91,-70,-71,-72,-73,-75,-74,108,108,108,108,-78,-79,108,108,108,108,108,108,108,-76,-77,]),'IGUALIGUAL':([73,79,80,81,82,83,84,85,86,87,88,90,95,96,97,117,118,119,123,129,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,151,154,156,158,160,163,164,172,179,180,181,190,191,192,193,194,],[109,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,109,-32,109,109,-62,-69,109,109,-31,109,109,109,109,-91,-91,-91,-91,-91,-91,-70,-71,-72,-73,-75,-74,109,109,109,109,-78,-79,109,109,109,109,109,109,109,-76,-77,]),'MAS':([73,79,80,81,82,83,84,85,86,87,88,90,95,96,97,117,118,119,123,129,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,151,154,156,158,160,163,164,172,179,180,181,190,191,192,193,194,],[110,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,110,-32,110,110,-62,-69,110,110,-31,110,110,110,110,110,110,110,110,110,110,-70,-71,-72,-73,-75,-74,110,110,110,110,-78,-79,110,110,110,110,110,110,110,-76,-77,]),'MULTIPLICACION':([73,79,80,81,82,83,84,85,86,87,88,90,95,96,97,117,118,119,123,129,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,151,154,156,158,160,163,164,172,179,180,181,190,191,192,193,194,],[112,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,112,-32,112,112,-62,-69,112,112,-31,112,112,112,112,112,112,112,112,112,112,112,112,-72,-73,-75,-74,112,112,112,112,-78,-79,112,112,112,112,112,112,112,-76,-77,]),'DIVISION':([73,79,80,81,82,83,84,85,86,87,88,90,95,96,97,117,118,119,123,129,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,151,154,156,158,160,163,164,172,179,180,181,190,191,192,193,194,],[113,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,113,-32,113,113,-62,-69,113,113,-31,113,113,113,113,113,113,113,113,113,113,113,113,-72,-73,-75,-74,113,113,113,113,-78,-79,113,113,113,113,113,113,113,-76,-77,]),'MODULO':([73,79,80,81,82,83,84,85,86,87,88,90,95,96,97,117,118,119,123,129,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,151,154,156,158,160,163,164,172,179,180,181,190,191,192,193,194,],[114,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,114,-32,114,114,-62,-69,114,114,-31,114,114,114,114,114,114,114,114,114,114,114,114,-72,-73,-75,-74,114,114,114,114,-78,-79,114,114,114,114,114,114,114,-76,-77,]),'TOSTRING':([73,79,80,81,82,83,84,85,86,87,88,90,95,96,97,117,118,119,123,129,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,151,154,156,158,160,163,164,172,179,180,181,190,191,192,193,194,],[115,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,115,-32,115,115,-62,-69,115,115,-31,115,115,-60,-61,-63,-64,-65,-66,-67,-68,-70,-71,-72,-73,-75,-74,115,115,115,115,-78,-79,115,115,115,115,115,115,115,-76,-77,]),'TOOWNED':([73,79,80,81,82,83,84,85,86,87,88,90,95,96,97,117,118,119,123,129,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,151,154,156,158,160,163,164,172,179,180,181,190,191,192,193,194,],[116,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,116,-32,116,116,-62,-69,116,116,-31,116,116,-60,-61,-63,-64,-65,-66,-67,-68,-70,-71,-72,-73,-75,-74,116,116,116,116,-78,-79,116,116,116,116,116,116,116,-76,-77,]),'PT':([73,79,80,81,82,83,84,85,86,87,88,90,95,96,97,117,118,119,123,129,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,151,154,156,158,160,163,164,172,179,180,181,190,191,192,193,194,],[-91,-80,-81,-82,-83,-84,-85,-86,-87,-88,122,-91,-32,-91,-91,-62,-69,-91,-91,-31,-91,-91,-60,-61,-63,-64,-65,-66,-67,-68,-70,-71,-72,-73,-75,-74,-90,-91,-91,-91,-78,-79,-91,-91,-91,-91,-91,-91,-91,-76,-77,]),'IN':([91,],[125,]),'POW':([152,],[165,]),'POWF':([153,],[166,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'clases_funciones':([0,],[2,]),'clase_funcion':([0,2,],[3,8,]),'clase':([0,2,],[4,4,]),'funcion':([0,2,],[5,5,]),'lista_parametros':([11,12,],[14,17,]),'parametroo':([11,12,21,],[16,16,32,]),'bloque':([18,22,90,92,155,156,175,184,195,],[23,34,124,126,167,168,183,189,196,]),'tipo':([19,57,99,131,],[25,92,133,159,]),'instrucciones':([24,],[35,]),'instruccion':([24,35,],[37,59,]),'llamada':([24,35,51,55,68,69,74,75,76,89,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,122,125,130,132,157,161,171,173,174,186,187,188,],[38,38,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,]),'variables':([24,35,],[39,39,]),'declaracion_objeto':([24,35,],[40,40,]),'print_instruccion':([24,35,],[41,41,]),'return_instruccion':([24,35,],[42,42,]),'break_instruccion':([24,35,],[43,43,]),'continue_instruccion':([24,35,],[44,44,]),'if_instruccion':([24,35,],[45,45,]),'while_instruccion':([24,35,],[46,46,]),'for_instruccion':([24,35,],[47,47,]),'expression':([51,55,68,69,74,75,76,89,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,122,125,130,132,157,161,171,173,174,186,187,188,],[73,90,96,97,117,118,119,123,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,154,156,158,160,96,172,179,180,181,190,191,192,]),'acceso_objeto_expresion':([51,55,68,69,74,75,76,89,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,122,125,130,132,157,161,171,173,174,186,187,188,],[80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,]),'acceso_objeto':([51,55,68,69,74,75,76,89,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,122,125,130,132,157,161,171,173,174,186,187,188,],[88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,]),'lista_expresiones':([68,157,],[94,169,]),'instancia_objeto':([93,],[128,]),'lista_else_if':([167,],[176,]),'else_if':([167,176,],[177,185,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> clases_funciones','init',1,'p_init','gramatica.py',254),
  ('clases_funciones -> clases_funciones clase_funcion','clases_funciones',2,'p_clases_funciones','gramatica.py',258),
  ('clases_funciones -> clase_funcion','clases_funciones',1,'p_clases_funciones_corte','gramatica.py',263),
  ('clase_funcion -> clase','clase_funcion',1,'p_clase_funcion','gramatica.py',267),
  ('clase_funcion -> funcion','clase_funcion',1,'p_clase_funcion','gramatica.py',268),
  ('clase -> STRUCT ID LLAIZQ lista_parametros LLADER','clase',5,'p_clase','gramatica.py',278),
  ('clase -> STRUCT ID LLAIZQ LLADER','clase',4,'p_clase','gramatica.py',279),
  ('funcion -> FN ID PIZQ lista_parametros PDER MENOS MAYOR tipo bloque','funcion',9,'p_funcion','gramatica.py',292),
  ('funcion -> FN ID PIZQ lista_parametros PDER bloque','funcion',6,'p_funcion','gramatica.py',293),
  ('funcion -> FN ID PIZQ PDER bloque','funcion',5,'p_funcion','gramatica.py',294),
  ('lista_parametros -> lista_parametros COMA parametroo','lista_parametros',3,'p_lista_parametros','gramatica.py',310),
  ('lista_parametros -> parametroo','lista_parametros',1,'p_lista_parametros_corte','gramatica.py',315),
  ('parametroo -> ID DOBLEPT tipo','parametroo',3,'p_parametroo','gramatica.py',319),
  ('bloque -> LLAIZQ instrucciones LLADER','bloque',3,'p_bloque','gramatica.py',326),
  ('bloque -> LLAIZQ LLADER','bloque',2,'p_bloque','gramatica.py',327),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones','gramatica.py',347),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_instruccion','gramatica.py',353),
  ('instruccion -> llamada PTCOMA','instruccion',2,'p_instruccion','gramatica.py',360),
  ('instruccion -> variables PTCOMA','instruccion',2,'p_instruccion','gramatica.py',361),
  ('instruccion -> declaracion_objeto PTCOMA','instruccion',2,'p_instruccion','gramatica.py',362),
  ('instruccion -> print_instruccion PTCOMA','instruccion',2,'p_instruccion','gramatica.py',363),
  ('instruccion -> return_instruccion PTCOMA','instruccion',2,'p_instruccion','gramatica.py',364),
  ('instruccion -> break_instruccion PTCOMA','instruccion',2,'p_instruccion','gramatica.py',365),
  ('instruccion -> continue_instruccion PTCOMA','instruccion',2,'p_instruccion','gramatica.py',366),
  ('instruccion -> if_instruccion','instruccion',1,'p_instruccion','gramatica.py',367),
  ('instruccion -> while_instruccion','instruccion',1,'p_instruccion','gramatica.py',368),
  ('instruccion -> for_instruccion','instruccion',1,'p_instruccion','gramatica.py',369),
  ('declaracion_objeto -> ID ID IGUAL instancia_objeto','declaracion_objeto',4,'p_declaracion_objeto','gramatica.py',387),
  ('instancia_objeto -> ID LLAIZQ lista_expresiones LLADER','instancia_objeto',4,'p_instancia_objeto','gramatica.py',394),
  ('instancia_objeto -> ID LLAIZQ LLADER','instancia_objeto',3,'p_instancia_objeto','gramatica.py',395),
  ('llamada -> ID PIZQ lista_expresiones PDER','llamada',4,'p_llamada','gramatica.py',415),
  ('llamada -> ID PIZQ PDER','llamada',3,'p_llamada','gramatica.py',416),
  ('return_instruccion -> RETURN expression','return_instruccion',2,'p_return_instruccion','gramatica.py',423),
  ('return_instruccion -> RETURN','return_instruccion',1,'p_return_instruccion','gramatica.py',424),
  ('break_instruccion -> BREAK','break_instruccion',1,'p_break_instruccion','gramatica.py',432),
  ('continue_instruccion -> CONTINUE','continue_instruccion',1,'p_continue_instruccion','gramatica.py',436),
  ('variables -> LET MUT ID DOBLEPT tipo IGUAL expression','variables',7,'p_variables','gramatica.py',452),
  ('variables -> LET ID DOBLEPT tipo IGUAL expression','variables',6,'p_variables','gramatica.py',453),
  ('variables -> LET MUT ID IGUAL expression','variables',5,'p_variables','gramatica.py',454),
  ('variables -> LET ID IGUAL expression','variables',4,'p_variables','gramatica.py',455),
  ('variables -> ID IGUAL expression','variables',3,'p_variables','gramatica.py',456),
  ('tipo -> INT','tipo',1,'p_tipo','gramatica.py',471),
  ('tipo -> FLOAT','tipo',1,'p_tipo','gramatica.py',472),
  ('tipo -> STR1','tipo',1,'p_tipo','gramatica.py',473),
  ('tipo -> STR2','tipo',1,'p_tipo','gramatica.py',474),
  ('tipo -> BOOLEA','tipo',1,'p_tipo','gramatica.py',475),
  ('tipo -> CHAR','tipo',1,'p_tipo','gramatica.py',476),
  ('print_instruccion -> PRINT NOT PIZQ expression PDER','print_instruccion',5,'p_print','gramatica.py',506),
  ('if_instruccion -> IF PIZQ expression PDER bloque','if_instruccion',5,'p_if_instruccion','gramatica.py',513),
  ('if_instruccion -> IF PIZQ expression PDER bloque ELSE bloque','if_instruccion',7,'p_if_instruccion','gramatica.py',514),
  ('if_instruccion -> IF PIZQ expression PDER bloque lista_else_if','if_instruccion',6,'p_if_instruccion','gramatica.py',515),
  ('if_instruccion -> IF PIZQ expression PDER bloque lista_else_if ELSE bloque','if_instruccion',8,'p_if_instruccion','gramatica.py',516),
  ('lista_else_if -> lista_else_if else_if','lista_else_if',2,'p_lista_else_if','gramatica.py',528),
  ('lista_else_if -> else_if','lista_else_if',1,'p_else_if_corte','gramatica.py',533),
  ('else_if -> ELSE IF PIZQ expression PDER bloque','else_if',6,'p_else_if','gramatica.py',537),
  ('while_instruccion -> WHILE expression bloque','while_instruccion',3,'p_while_instruccion','gramatica.py',543),
  ('for_instruccion -> FOR ID IN expression bloque','for_instruccion',5,'p_for_instruccion','gramatica.py',549),
  ('lista_expresiones -> lista_expresiones COMA expression','lista_expresiones',3,'p_lista_expresiones','gramatica.py',567),
  ('lista_expresiones -> expression','lista_expresiones',1,'p_lista_expresiones_corte','gramatica.py',572),
  ('expression -> expression OR expression','expression',3,'p_expression_logica','gramatica.py',579),
  ('expression -> expression AND expression','expression',3,'p_expression_logica','gramatica.py',580),
  ('expression -> NOT expression','expression',2,'p_expression_logica','gramatica.py',581),
  ('expression -> expression MENOR expression','expression',3,'p_expression_relacional','gramatica.py',593),
  ('expression -> expression MAYOR expression','expression',3,'p_expression_relacional','gramatica.py',594),
  ('expression -> expression MAYORIGUAL expression','expression',3,'p_expression_relacional','gramatica.py',595),
  ('expression -> expression MENORIGUAL expression','expression',3,'p_expression_relacional','gramatica.py',596),
  ('expression -> expression DIFERENTE expression','expression',3,'p_expression_relacional','gramatica.py',597),
  ('expression -> expression IGUALIGUAL expression','expression',3,'p_expression_relacional','gramatica.py',598),
  ('expression -> MENOS expression','expression',2,'p_expression_aritmetica','gramatica.py',616),
  ('expression -> expression MAS expression','expression',3,'p_expression_aritmetica','gramatica.py',617),
  ('expression -> expression MENOS expression','expression',3,'p_expression_aritmetica','gramatica.py',618),
  ('expression -> expression MULTIPLICACION expression','expression',3,'p_expression_aritmetica','gramatica.py',619),
  ('expression -> expression DIVISION expression','expression',3,'p_expression_aritmetica','gramatica.py',620),
  ('expression -> PIZQ expression PDER','expression',3,'p_expression_aritmetica','gramatica.py',621),
  ('expression -> expression MODULO expression','expression',3,'p_expression_aritmetica','gramatica.py',622),
  ('expression -> INT DOBLEPT DOBLEPT POW PIZQ expression COMA expression PDER','expression',9,'p_expression_aritmetica','gramatica.py',623),
  ('expression -> FLOAT DOBLEPT DOBLEPT POWF PIZQ expression COMA expression PDER','expression',9,'p_expression_aritmetica','gramatica.py',624),
  ('expression -> expression TOSTRING PIZQ PDER','expression',4,'p_expression_nativa','gramatica.py',650),
  ('expression -> expression TOOWNED PIZQ PDER','expression',4,'p_expression_nativa','gramatica.py',651),
  ('expression -> llamada','expression',1,'p_otras_expresiones','gramatica.py',663),
  ('expression -> acceso_objeto_expresion','expression',1,'p_otras_expresiones','gramatica.py',664),
  ('expression -> ENTERO','expression',1,'p_expression_primitiva','gramatica.py',670),
  ('expression -> DECIMAL','expression',1,'p_expression_primitiva','gramatica.py',671),
  ('expression -> ID','expression',1,'p_expression_primitiva','gramatica.py',672),
  ('expression -> CADENA','expression',1,'p_expression_primitiva','gramatica.py',673),
  ('expression -> CHAR','expression',1,'p_expression_primitiva','gramatica.py',674),
  ('expression -> TRUE','expression',1,'p_expression_primitiva','gramatica.py',675),
  ('expression -> FALSE','expression',1,'p_expression_primitiva','gramatica.py',676),
  ('acceso_objeto_expresion -> acceso_objeto','acceso_objeto_expresion',1,'p_acceso_objeto_expresion','gramatica.py',702),
  ('acceso_objeto -> acceso_objeto PT expression','acceso_objeto',3,'p_acceso_objeto','gramatica.py',707),
  ('acceso_objeto -> expression','acceso_objeto',1,'p_acceso_objeto_cort','gramatica.py',713),
]
