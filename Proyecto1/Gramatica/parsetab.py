
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDnonassocMAYORMENORIGUALMENORMAYORIGUALIGUALIGUALDIFERENTEleftMASMENOSleftMULTIPLICACIONDIVISIONMODULOrightNOTUMENOSAND BOOLEA BREAK CADENA CDER CHAR CIZQ COMA DECIMAL DIFERENTE DIVISION DOBLEPT ELSE ENTERO FALSE FLOAT FN ID IF IGUAL IGUALIGUAL INT LET LLADER LLAIZQ MAS MAYOR MAYORIGUAL MENOR MENORIGUAL MENOS MODULO MULTIPLICACION MUT NOT OR PDER PIZQ POW POWF PRINT PT PTCOMA RETURN STR1 STR2 STRUCT TOOWNED TOSTRING TRUE WHILEinit : clases_funciones clases_funciones : clases_funciones clase_funcion   clases_funciones : clase_funcion  clase_funcion : clase\n                      | funcion   clase : STRUCT ID LLAIZQ lista_parametros LLADER\n               | STRUCT ID LLAIZQ  LLADERfuncion : FN ID PIZQ lista_parametros PDER MENOS MAYOR tipo bloque\n               | FN ID PIZQ lista_parametros PDER bloque\n               | FN ID PIZQ PDER bloquelista_parametros : lista_parametros COMA parametroolista_parametros : parametrooparametroo : ID DOBLEPT tipobloque : LLAIZQ instrucciones LLADER\n              | LLAIZQ LLADERinstrucciones : instrucciones instruccioninstrucciones : instruccioninstruccion : llamada PTCOMA\n                   | variables PTCOMA\n                   | declaracion_objeto PTCOMA\n                   | print_instruccion PTCOMA\n                   | return_instruccion PTCOMA\n                   | break_instruccion PTCOMA\n                   | if_instruccion \n                   | while_instruccion  declaracion_objeto : ID ID IGUAL instancia_objeto  instancia_objeto : ID LLAIZQ lista_expresiones LLADER\n                         | ID LLAIZQ LLADER llamada : ID PIZQ lista_expresiones PDER \n               | ID PIZQ PDER return_instruccion : RETURN expression\n                          | RETURN break_instruccion : BREAK variables : LET MUT ID DOBLEPT tipo IGUAL expression \n\t\t         | LET ID DOBLEPT tipo IGUAL expression \n\t\t         | LET MUT ID IGUAL expression \n\t\t         | LET ID IGUAL expression \n\t\t         | ID IGUAL expressiontipo : INT\n\t        | FLOAT\n\t        | STR1\n\t        | STR2\n\t        | BOOLEA\n\t        | CHARprint_instruccion : PRINT NOT PIZQ expression PDERif_instruccion : IF PIZQ expression PDER bloque\n                      | IF PIZQ expression PDER bloque ELSE bloque \n                      | IF PIZQ expression PDER bloque lista_else_if\n                      | IF PIZQ expression PDER bloque lista_else_if ELSE bloque lista_else_if : lista_else_if else_iflista_else_if : else_if else_if : ELSE IF PIZQ expression PDER bloque while_instruccion : WHILE expression bloque lista_expresiones : lista_expresiones COMA expressionlista_expresiones : expressionexpression : expression OR expression\n                 | expression AND expression\n                 | NOT expression %prec NOTexpression : expression MENOR expression\n                 | expression MAYOR expression\n                 | expression MAYORIGUAL expression\n                 | expression MENORIGUAL expression\n                 | expression DIFERENTE expression\n                 | expression IGUALIGUAL expressionexpression : MENOS expression %prec UMENOS\n                 | expression MAS expression\n                 | expression MENOS expression\n                 | expression MULTIPLICACION expression\n                 | expression DIVISION expression\n                 | PIZQ expression PDER\n                 | expression MODULO expression\n                 | INT DOBLEPT DOBLEPT POW PIZQ expression COMA expression PDER\n                 | FLOAT DOBLEPT DOBLEPT POWF PIZQ expression COMA expression PDERexpression : expression TOSTRING PIZQ PDER\n                  | expression TOOWNED PIZQ PDERexpression : llamada\n                  | acceso_objeto_expresion expression : ENTERO\n                  | DECIMAL\n                  | ID\n                  | CADENA\n                  | CHAR\n                  | TRUE\n                  | FALSE acceso_objeto_expresion : acceso_objeto acceso_objeto : acceso_objeto PT expression acceso_objeto : expression'
    
_lr_action_items = {'STRUCT':([0,2,3,4,5,8,15,20,23,34,36,54,119,],[6,6,-3,-4,-5,-2,-7,-6,-10,-9,-15,-14,-8,]),'FN':([0,2,3,4,5,8,15,20,23,34,36,54,119,],[7,7,-3,-4,-5,-2,-7,-6,-10,-9,-15,-14,-8,]),'$end':([1,2,3,4,5,8,15,20,23,34,36,54,119,],[0,-1,-3,-4,-5,-2,-7,-6,-10,-9,-15,-14,-8,]),'ID':([6,7,11,12,21,24,35,36,37,44,45,46,47,49,52,54,55,56,57,58,59,60,61,63,64,65,69,70,71,84,87,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,116,118,123,125,149,153,159,162,164,165,167,168,174,176,177,178,179,180,187,],[9,10,13,13,13,46,46,-15,-17,-24,-25,62,66,78,78,-14,-16,-18,-19,-20,-21,-22,-23,78,78,92,78,78,78,78,120,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,-53,78,78,78,78,-46,78,78,78,-48,-51,-47,-50,78,78,78,-49,-52,]),'LLAIZQ':([9,18,22,26,27,28,29,30,31,74,75,76,77,78,79,80,81,82,83,85,86,89,111,112,120,122,129,130,131,132,133,134,135,136,137,138,139,140,141,144,147,148,155,156,166,175,184,185,186,],[11,24,24,-39,-40,-41,-42,-43,-44,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,24,24,-30,-58,-65,149,-29,-56,-57,-59,-60,-61,-62,-63,-64,-66,-67,-68,-69,-71,-70,-86,24,-74,-75,24,24,-72,-73,24,]),'PIZQ':([10,46,49,51,52,63,64,67,69,70,71,78,84,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,116,123,125,149,153,157,158,162,164,165,173,177,178,179,],[12,63,71,84,71,71,71,95,71,71,71,63,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,142,143,71,71,71,71,71,164,165,71,71,71,179,71,71,71,]),'LLADER':([11,14,16,24,25,26,27,28,29,30,31,32,35,36,37,44,45,54,55,56,57,58,59,60,61,74,75,76,77,78,79,80,81,82,83,89,90,111,112,118,122,129,130,131,132,133,134,135,136,137,138,139,140,141,144,147,149,150,155,156,159,160,167,168,174,176,180,184,185,187,],[15,20,-12,36,-13,-39,-40,-41,-42,-43,-44,-11,54,-15,-17,-24,-25,-14,-16,-18,-19,-20,-21,-22,-23,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-30,-55,-58,-65,-53,-29,-56,-57,-59,-60,-61,-62,-63,-64,-66,-67,-68,-69,-71,-70,-86,161,-54,-74,-75,-46,169,-48,-51,-47,-50,-49,-72,-73,-52,]),'PDER':([12,16,17,25,26,27,28,29,30,31,32,63,74,75,76,77,78,79,80,81,82,83,88,89,90,111,112,113,117,122,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,147,150,155,156,181,182,183,184,185,],[18,-12,22,-13,-39,-40,-41,-42,-43,-44,-11,89,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,122,-30,-55,-58,-65,144,148,-29,154,-56,-57,-59,-60,-61,-62,-63,-64,-66,-67,-68,-69,-71,155,156,-70,-86,-54,-74,-75,184,185,186,-72,-73,]),'DOBLEPT':([13,66,72,73,92,114,115,],[19,93,114,115,124,145,146,]),'COMA':([14,16,17,25,26,27,28,29,30,31,32,74,75,76,77,78,79,80,81,82,83,88,89,90,111,112,122,129,130,131,132,133,134,135,136,137,138,139,140,141,144,147,150,155,156,160,171,172,184,185,],[21,-12,21,-13,-39,-40,-41,-42,-43,-44,-11,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,123,-30,-55,-58,-65,-29,-56,-57,-59,-60,-61,-62,-63,-64,-66,-67,-68,-69,-71,-70,-86,-54,-74,-75,123,177,178,-72,-73,]),'INT':([19,49,52,53,63,64,69,70,71,84,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,116,123,124,125,149,153,162,164,165,177,178,179,],[26,72,72,26,72,72,72,72,72,72,26,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,26,72,72,72,72,72,72,72,72,72,]),'FLOAT':([19,49,52,53,63,64,69,70,71,84,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,116,123,124,125,149,153,162,164,165,177,178,179,],[27,73,73,27,73,73,73,73,73,73,27,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,27,73,73,73,73,73,73,73,73,73,]),'STR1':([19,53,93,124,],[28,28,28,28,]),'STR2':([19,53,93,124,],[29,29,29,29,]),'BOOLEA':([19,53,93,124,],[30,30,30,30,]),'CHAR':([19,49,52,53,63,64,69,70,71,84,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,116,123,124,125,149,153,162,164,165,177,178,179,],[31,80,80,31,80,80,80,80,80,80,31,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,31,80,80,80,80,80,80,80,80,80,]),'MENOS':([22,49,52,63,64,68,69,70,71,74,75,76,77,78,79,80,81,82,83,84,85,89,90,91,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,111,112,113,116,117,122,123,125,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,144,147,149,150,152,153,155,156,162,163,164,165,170,171,172,177,178,179,181,182,183,184,185,],[33,70,70,70,70,105,70,70,70,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,70,105,-30,105,105,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,-58,-65,105,70,105,-29,70,70,105,105,105,105,105,105,105,105,105,105,-66,-67,-68,-69,-71,-70,105,70,105,105,70,-74,-75,70,105,70,70,105,105,105,70,70,70,105,105,105,-72,-73,]),'LET':([24,35,36,37,44,45,54,55,56,57,58,59,60,61,118,159,167,168,174,176,180,187,],[47,47,-15,-17,-24,-25,-14,-16,-18,-19,-20,-21,-22,-23,-53,-46,-48,-51,-47,-50,-49,-52,]),'PRINT':([24,35,36,37,44,45,54,55,56,57,58,59,60,61,118,159,167,168,174,176,180,187,],[48,48,-15,-17,-24,-25,-14,-16,-18,-19,-20,-21,-22,-23,-53,-46,-48,-51,-47,-50,-49,-52,]),'RETURN':([24,35,36,37,44,45,54,55,56,57,58,59,60,61,118,159,167,168,174,176,180,187,],[49,49,-15,-17,-24,-25,-14,-16,-18,-19,-20,-21,-22,-23,-53,-46,-48,-51,-47,-50,-49,-52,]),'BREAK':([24,35,36,37,44,45,54,55,56,57,58,59,60,61,118,159,167,168,174,176,180,187,],[50,50,-15,-17,-24,-25,-14,-16,-18,-19,-20,-21,-22,-23,-53,-46,-48,-51,-47,-50,-49,-52,]),'IF':([24,35,36,37,44,45,54,55,56,57,58,59,60,61,118,159,166,167,168,174,175,176,180,187,],[51,51,-15,-17,-24,-25,-14,-16,-18,-19,-20,-21,-22,-23,-53,-46,173,-48,-51,-47,173,-50,-49,-52,]),'WHILE':([24,35,36,37,44,45,54,55,56,57,58,59,60,61,118,159,167,168,174,176,180,187,],[52,52,-15,-17,-24,-25,-14,-16,-18,-19,-20,-21,-22,-23,-53,-46,-48,-51,-47,-50,-49,-52,]),'IGUAL':([26,27,28,29,30,31,46,62,66,92,126,151,],[-39,-40,-41,-42,-43,-44,64,87,94,125,153,162,]),'MAYOR':([33,68,74,75,76,77,78,79,80,81,82,83,85,89,90,91,111,112,113,117,122,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,144,147,150,152,155,156,163,170,171,172,181,182,183,184,185,],[53,99,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,99,-30,99,99,-58,-65,99,99,-29,99,99,99,99,-87,-87,-87,-87,-87,-87,-66,-67,-68,-69,-71,-70,99,99,99,-74,-75,99,99,99,99,99,99,99,-72,-73,]),'ELSE':([36,54,159,167,168,176,187,],[-15,-14,166,175,-51,-50,-52,]),'PTCOMA':([38,39,40,41,42,43,49,50,68,74,75,76,77,78,79,80,81,82,83,89,91,111,112,121,122,127,129,130,131,132,133,134,135,136,137,138,139,140,141,144,147,152,154,155,156,161,163,169,170,184,185,],[56,57,58,59,60,61,-32,-33,-31,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-30,-38,-58,-65,-26,-29,-37,-56,-57,-59,-60,-61,-62,-63,-64,-66,-67,-68,-69,-71,-70,-86,-36,-45,-74,-75,-28,-35,-27,-34,-72,-73,]),'MUT':([47,],[65,]),'NOT':([48,49,52,63,64,69,70,71,84,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,116,123,125,149,153,162,164,165,177,178,179,],[67,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,]),'ENTERO':([49,52,63,64,69,70,71,84,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,116,123,125,149,153,162,164,165,177,178,179,],[76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,]),'DECIMAL':([49,52,63,64,69,70,71,84,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,116,123,125,149,153,162,164,165,177,178,179,],[77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,]),'CADENA':([49,52,63,64,69,70,71,84,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,116,123,125,149,153,162,164,165,177,178,179,],[79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,]),'TRUE':([49,52,63,64,69,70,71,84,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,116,123,125,149,153,162,164,165,177,178,179,],[81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,]),'FALSE':([49,52,63,64,69,70,71,84,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,116,123,125,149,153,162,164,165,177,178,179,],[82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,]),'OR':([68,74,75,76,77,78,79,80,81,82,83,85,89,90,91,111,112,113,117,122,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,144,147,150,152,155,156,163,170,171,172,181,182,183,184,185,],[96,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,96,-30,96,96,-58,-65,96,96,-29,96,96,-56,-57,-59,-60,-61,-62,-63,-64,-66,-67,-68,-69,-71,-70,96,96,96,-74,-75,96,96,96,96,96,96,96,-72,-73,]),'AND':([68,74,75,76,77,78,79,80,81,82,83,85,89,90,91,111,112,113,117,122,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,144,147,150,152,155,156,163,170,171,172,181,182,183,184,185,],[97,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,97,-30,97,97,-58,-65,97,97,-29,97,97,97,-57,-59,-60,-61,-62,-63,-64,-66,-67,-68,-69,-71,-70,97,97,97,-74,-75,97,97,97,97,97,97,97,-72,-73,]),'MENOR':([68,74,75,76,77,78,79,80,81,82,83,85,89,90,91,111,112,113,117,122,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,144,147,150,152,155,156,163,170,171,172,181,182,183,184,185,],[98,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,98,-30,98,98,-58,-65,98,98,-29,98,98,98,98,-87,-87,-87,-87,-87,-87,-66,-67,-68,-69,-71,-70,98,98,98,-74,-75,98,98,98,98,98,98,98,-72,-73,]),'MAYORIGUAL':([68,74,75,76,77,78,79,80,81,82,83,85,89,90,91,111,112,113,117,122,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,144,147,150,152,155,156,163,170,171,172,181,182,183,184,185,],[100,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,100,-30,100,100,-58,-65,100,100,-29,100,100,100,100,-87,-87,-87,-87,-87,-87,-66,-67,-68,-69,-71,-70,100,100,100,-74,-75,100,100,100,100,100,100,100,-72,-73,]),'MENORIGUAL':([68,74,75,76,77,78,79,80,81,82,83,85,89,90,91,111,112,113,117,122,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,144,147,150,152,155,156,163,170,171,172,181,182,183,184,185,],[101,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,101,-30,101,101,-58,-65,101,101,-29,101,101,101,101,-87,-87,-87,-87,-87,-87,-66,-67,-68,-69,-71,-70,101,101,101,-74,-75,101,101,101,101,101,101,101,-72,-73,]),'DIFERENTE':([68,74,75,76,77,78,79,80,81,82,83,85,89,90,91,111,112,113,117,122,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,144,147,150,152,155,156,163,170,171,172,181,182,183,184,185,],[102,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,102,-30,102,102,-58,-65,102,102,-29,102,102,102,102,-87,-87,-87,-87,-87,-87,-66,-67,-68,-69,-71,-70,102,102,102,-74,-75,102,102,102,102,102,102,102,-72,-73,]),'IGUALIGUAL':([68,74,75,76,77,78,79,80,81,82,83,85,89,90,91,111,112,113,117,122,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,144,147,150,152,155,156,163,170,171,172,181,182,183,184,185,],[103,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,103,-30,103,103,-58,-65,103,103,-29,103,103,103,103,-87,-87,-87,-87,-87,-87,-66,-67,-68,-69,-71,-70,103,103,103,-74,-75,103,103,103,103,103,103,103,-72,-73,]),'MAS':([68,74,75,76,77,78,79,80,81,82,83,85,89,90,91,111,112,113,117,122,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,144,147,150,152,155,156,163,170,171,172,181,182,183,184,185,],[104,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,104,-30,104,104,-58,-65,104,104,-29,104,104,104,104,104,104,104,104,104,104,-66,-67,-68,-69,-71,-70,104,104,104,-74,-75,104,104,104,104,104,104,104,-72,-73,]),'MULTIPLICACION':([68,74,75,76,77,78,79,80,81,82,83,85,89,90,91,111,112,113,117,122,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,144,147,150,152,155,156,163,170,171,172,181,182,183,184,185,],[106,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,106,-30,106,106,-58,-65,106,106,-29,106,106,106,106,106,106,106,106,106,106,106,106,-68,-69,-71,-70,106,106,106,-74,-75,106,106,106,106,106,106,106,-72,-73,]),'DIVISION':([68,74,75,76,77,78,79,80,81,82,83,85,89,90,91,111,112,113,117,122,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,144,147,150,152,155,156,163,170,171,172,181,182,183,184,185,],[107,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,107,-30,107,107,-58,-65,107,107,-29,107,107,107,107,107,107,107,107,107,107,107,107,-68,-69,-71,-70,107,107,107,-74,-75,107,107,107,107,107,107,107,-72,-73,]),'MODULO':([68,74,75,76,77,78,79,80,81,82,83,85,89,90,91,111,112,113,117,122,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,144,147,150,152,155,156,163,170,171,172,181,182,183,184,185,],[108,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,108,-30,108,108,-58,-65,108,108,-29,108,108,108,108,108,108,108,108,108,108,108,108,-68,-69,-71,-70,108,108,108,-74,-75,108,108,108,108,108,108,108,-72,-73,]),'TOSTRING':([68,74,75,76,77,78,79,80,81,82,83,85,89,90,91,111,112,113,117,122,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,144,147,150,152,155,156,163,170,171,172,181,182,183,184,185,],[109,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,109,-30,109,109,-58,-65,109,109,-29,109,109,-56,-57,-59,-60,-61,-62,-63,-64,-66,-67,-68,-69,-71,-70,109,109,109,-74,-75,109,109,109,109,109,109,109,-72,-73,]),'TOOWNED':([68,74,75,76,77,78,79,80,81,82,83,85,89,90,91,111,112,113,117,122,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,144,147,150,152,155,156,163,170,171,172,181,182,183,184,185,],[110,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,110,-30,110,110,-58,-65,110,110,-29,110,110,-56,-57,-59,-60,-61,-62,-63,-64,-66,-67,-68,-69,-71,-70,110,110,110,-74,-75,110,110,110,110,110,110,110,-72,-73,]),'PT':([68,74,75,76,77,78,79,80,81,82,83,85,89,90,91,111,112,113,117,122,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,144,147,150,152,155,156,163,170,171,172,181,182,183,184,185,],[-87,-76,-77,-78,-79,-80,-81,-82,-83,-84,116,-87,-30,-87,-87,-58,-65,-87,-87,-29,-87,-87,-56,-57,-59,-60,-61,-62,-63,-64,-66,-67,-68,-69,-71,-70,-86,-87,-87,-74,-75,-87,-87,-87,-87,-87,-87,-87,-72,-73,]),'POW':([145,],[157,]),'POWF':([146,],[158,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'clases_funciones':([0,],[2,]),'clase_funcion':([0,2,],[3,8,]),'clase':([0,2,],[4,4,]),'funcion':([0,2,],[5,5,]),'lista_parametros':([11,12,],[14,17,]),'parametroo':([11,12,21,],[16,16,32,]),'bloque':([18,22,85,86,148,166,175,186,],[23,34,118,119,159,174,180,187,]),'tipo':([19,53,93,124,],[25,86,126,151,]),'instrucciones':([24,],[35,]),'instruccion':([24,35,],[37,55,]),'llamada':([24,35,49,52,63,64,69,70,71,84,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,116,123,125,149,153,162,164,165,177,178,179,],[38,38,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,]),'variables':([24,35,],[39,39,]),'declaracion_objeto':([24,35,],[40,40,]),'print_instruccion':([24,35,],[41,41,]),'return_instruccion':([24,35,],[42,42,]),'break_instruccion':([24,35,],[43,43,]),'if_instruccion':([24,35,],[44,44,]),'while_instruccion':([24,35,],[45,45,]),'expression':([49,52,63,64,69,70,71,84,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,116,123,125,149,153,162,164,165,177,178,179,],[68,85,90,91,111,112,113,117,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,147,150,152,90,163,170,171,172,181,182,183,]),'acceso_objeto_expresion':([49,52,63,64,69,70,71,84,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,116,123,125,149,153,162,164,165,177,178,179,],[75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,]),'acceso_objeto':([49,52,63,64,69,70,71,84,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,116,123,125,149,153,162,164,165,177,178,179,],[83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,]),'lista_expresiones':([63,149,],[88,160,]),'instancia_objeto':([87,],[121,]),'lista_else_if':([159,],[167,]),'else_if':([159,167,],[168,176,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> clases_funciones','init',1,'p_init','gramatica.py',250),
  ('clases_funciones -> clases_funciones clase_funcion','clases_funciones',2,'p_clases_funciones','gramatica.py',254),
  ('clases_funciones -> clase_funcion','clases_funciones',1,'p_clases_funciones_corte','gramatica.py',259),
  ('clase_funcion -> clase','clase_funcion',1,'p_clase_funcion','gramatica.py',263),
  ('clase_funcion -> funcion','clase_funcion',1,'p_clase_funcion','gramatica.py',264),
  ('clase -> STRUCT ID LLAIZQ lista_parametros LLADER','clase',5,'p_clase','gramatica.py',274),
  ('clase -> STRUCT ID LLAIZQ LLADER','clase',4,'p_clase','gramatica.py',275),
  ('funcion -> FN ID PIZQ lista_parametros PDER MENOS MAYOR tipo bloque','funcion',9,'p_funcion','gramatica.py',288),
  ('funcion -> FN ID PIZQ lista_parametros PDER bloque','funcion',6,'p_funcion','gramatica.py',289),
  ('funcion -> FN ID PIZQ PDER bloque','funcion',5,'p_funcion','gramatica.py',290),
  ('lista_parametros -> lista_parametros COMA parametroo','lista_parametros',3,'p_lista_parametros','gramatica.py',306),
  ('lista_parametros -> parametroo','lista_parametros',1,'p_lista_parametros_corte','gramatica.py',311),
  ('parametroo -> ID DOBLEPT tipo','parametroo',3,'p_parametroo','gramatica.py',315),
  ('bloque -> LLAIZQ instrucciones LLADER','bloque',3,'p_bloque','gramatica.py',322),
  ('bloque -> LLAIZQ LLADER','bloque',2,'p_bloque','gramatica.py',323),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones','gramatica.py',343),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_instruccion','gramatica.py',349),
  ('instruccion -> llamada PTCOMA','instruccion',2,'p_instruccion','gramatica.py',356),
  ('instruccion -> variables PTCOMA','instruccion',2,'p_instruccion','gramatica.py',357),
  ('instruccion -> declaracion_objeto PTCOMA','instruccion',2,'p_instruccion','gramatica.py',358),
  ('instruccion -> print_instruccion PTCOMA','instruccion',2,'p_instruccion','gramatica.py',359),
  ('instruccion -> return_instruccion PTCOMA','instruccion',2,'p_instruccion','gramatica.py',360),
  ('instruccion -> break_instruccion PTCOMA','instruccion',2,'p_instruccion','gramatica.py',361),
  ('instruccion -> if_instruccion','instruccion',1,'p_instruccion','gramatica.py',362),
  ('instruccion -> while_instruccion','instruccion',1,'p_instruccion','gramatica.py',363),
  ('declaracion_objeto -> ID ID IGUAL instancia_objeto','declaracion_objeto',4,'p_declaracion_objeto','gramatica.py',381),
  ('instancia_objeto -> ID LLAIZQ lista_expresiones LLADER','instancia_objeto',4,'p_instancia_objeto','gramatica.py',388),
  ('instancia_objeto -> ID LLAIZQ LLADER','instancia_objeto',3,'p_instancia_objeto','gramatica.py',389),
  ('llamada -> ID PIZQ lista_expresiones PDER','llamada',4,'p_llamada','gramatica.py',409),
  ('llamada -> ID PIZQ PDER','llamada',3,'p_llamada','gramatica.py',410),
  ('return_instruccion -> RETURN expression','return_instruccion',2,'p_return_instruccion','gramatica.py',417),
  ('return_instruccion -> RETURN','return_instruccion',1,'p_return_instruccion','gramatica.py',418),
  ('break_instruccion -> BREAK','break_instruccion',1,'p_break_instruccion','gramatica.py',426),
  ('variables -> LET MUT ID DOBLEPT tipo IGUAL expression','variables',7,'p_variables','gramatica.py',442),
  ('variables -> LET ID DOBLEPT tipo IGUAL expression','variables',6,'p_variables','gramatica.py',443),
  ('variables -> LET MUT ID IGUAL expression','variables',5,'p_variables','gramatica.py',444),
  ('variables -> LET ID IGUAL expression','variables',4,'p_variables','gramatica.py',445),
  ('variables -> ID IGUAL expression','variables',3,'p_variables','gramatica.py',446),
  ('tipo -> INT','tipo',1,'p_tipo','gramatica.py',461),
  ('tipo -> FLOAT','tipo',1,'p_tipo','gramatica.py',462),
  ('tipo -> STR1','tipo',1,'p_tipo','gramatica.py',463),
  ('tipo -> STR2','tipo',1,'p_tipo','gramatica.py',464),
  ('tipo -> BOOLEA','tipo',1,'p_tipo','gramatica.py',465),
  ('tipo -> CHAR','tipo',1,'p_tipo','gramatica.py',466),
  ('print_instruccion -> PRINT NOT PIZQ expression PDER','print_instruccion',5,'p_print','gramatica.py',496),
  ('if_instruccion -> IF PIZQ expression PDER bloque','if_instruccion',5,'p_if_instruccion','gramatica.py',503),
  ('if_instruccion -> IF PIZQ expression PDER bloque ELSE bloque','if_instruccion',7,'p_if_instruccion','gramatica.py',504),
  ('if_instruccion -> IF PIZQ expression PDER bloque lista_else_if','if_instruccion',6,'p_if_instruccion','gramatica.py',505),
  ('if_instruccion -> IF PIZQ expression PDER bloque lista_else_if ELSE bloque','if_instruccion',8,'p_if_instruccion','gramatica.py',506),
  ('lista_else_if -> lista_else_if else_if','lista_else_if',2,'p_lista_else_if','gramatica.py',518),
  ('lista_else_if -> else_if','lista_else_if',1,'p_else_if_corte','gramatica.py',523),
  ('else_if -> ELSE IF PIZQ expression PDER bloque','else_if',6,'p_else_if','gramatica.py',527),
  ('while_instruccion -> WHILE expression bloque','while_instruccion',3,'p_while_instruccion','gramatica.py',533),
  ('lista_expresiones -> lista_expresiones COMA expression','lista_expresiones',3,'p_lista_expresiones','gramatica.py',553),
  ('lista_expresiones -> expression','lista_expresiones',1,'p_lista_expresiones_corte','gramatica.py',558),
  ('expression -> expression OR expression','expression',3,'p_expression_logica','gramatica.py',565),
  ('expression -> expression AND expression','expression',3,'p_expression_logica','gramatica.py',566),
  ('expression -> NOT expression','expression',2,'p_expression_logica','gramatica.py',567),
  ('expression -> expression MENOR expression','expression',3,'p_expression_relacional','gramatica.py',579),
  ('expression -> expression MAYOR expression','expression',3,'p_expression_relacional','gramatica.py',580),
  ('expression -> expression MAYORIGUAL expression','expression',3,'p_expression_relacional','gramatica.py',581),
  ('expression -> expression MENORIGUAL expression','expression',3,'p_expression_relacional','gramatica.py',582),
  ('expression -> expression DIFERENTE expression','expression',3,'p_expression_relacional','gramatica.py',583),
  ('expression -> expression IGUALIGUAL expression','expression',3,'p_expression_relacional','gramatica.py',584),
  ('expression -> MENOS expression','expression',2,'p_expression_aritmetica','gramatica.py',602),
  ('expression -> expression MAS expression','expression',3,'p_expression_aritmetica','gramatica.py',603),
  ('expression -> expression MENOS expression','expression',3,'p_expression_aritmetica','gramatica.py',604),
  ('expression -> expression MULTIPLICACION expression','expression',3,'p_expression_aritmetica','gramatica.py',605),
  ('expression -> expression DIVISION expression','expression',3,'p_expression_aritmetica','gramatica.py',606),
  ('expression -> PIZQ expression PDER','expression',3,'p_expression_aritmetica','gramatica.py',607),
  ('expression -> expression MODULO expression','expression',3,'p_expression_aritmetica','gramatica.py',608),
  ('expression -> INT DOBLEPT DOBLEPT POW PIZQ expression COMA expression PDER','expression',9,'p_expression_aritmetica','gramatica.py',609),
  ('expression -> FLOAT DOBLEPT DOBLEPT POWF PIZQ expression COMA expression PDER','expression',9,'p_expression_aritmetica','gramatica.py',610),
  ('expression -> expression TOSTRING PIZQ PDER','expression',4,'p_expression_nativa','gramatica.py',636),
  ('expression -> expression TOOWNED PIZQ PDER','expression',4,'p_expression_nativa','gramatica.py',637),
  ('expression -> llamada','expression',1,'p_otras_expresiones','gramatica.py',649),
  ('expression -> acceso_objeto_expresion','expression',1,'p_otras_expresiones','gramatica.py',650),
  ('expression -> ENTERO','expression',1,'p_expression_primitiva','gramatica.py',656),
  ('expression -> DECIMAL','expression',1,'p_expression_primitiva','gramatica.py',657),
  ('expression -> ID','expression',1,'p_expression_primitiva','gramatica.py',658),
  ('expression -> CADENA','expression',1,'p_expression_primitiva','gramatica.py',659),
  ('expression -> CHAR','expression',1,'p_expression_primitiva','gramatica.py',660),
  ('expression -> TRUE','expression',1,'p_expression_primitiva','gramatica.py',661),
  ('expression -> FALSE','expression',1,'p_expression_primitiva','gramatica.py',662),
  ('acceso_objeto_expresion -> acceso_objeto','acceso_objeto_expresion',1,'p_acceso_objeto_expresion','gramatica.py',688),
  ('acceso_objeto -> acceso_objeto PT expression','acceso_objeto',3,'p_acceso_objeto','gramatica.py',693),
  ('acceso_objeto -> expression','acceso_objeto',1,'p_acceso_objeto_cort','gramatica.py',699),
]
