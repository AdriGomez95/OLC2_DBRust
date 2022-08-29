
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDnonassocMAYORMENORIGUALMENORMAYORIGUALIGUALIGUALDIFERENTEleftMASMENOSleftMULTIPLICACIONDIVISIONMODULOrightNOTUMENOSAND BOOLEA BUFER1 BUFER2 CADENA CHAR COMA DECIMAL DIFERENTE DIVISION DOBLEPT ELSE ENTERO FALSE FLOAT FN ID IF IGUAL IGUALIGUAL INT LET LLADER LLAIZQ MAS MAYOR MAYORIGUAL MENOR MENORIGUAL MENOS MODULO MULTIPLICACION MUT NOT OR PDER PIZQ POW POWF PRINT PT PTCOMA RETURN STR1 STR2 STRUCT TRUE WHILEinit : clases_funciones clases_funciones : clases_funciones clase_funcion   clases_funciones : clase_funcion  clase_funcion : clase\n                      | funcion   clase : STRUCT ID bloqueClase bloqueClase : LLAIZQ instrs_clase LLADER\n                    | LLAIZQ  LLADERfuncion : FN ID PIZQ lista_parametros PDER MENOS MAYOR tipo bloque\n               | FN ID PIZQ lista_parametros PDER bloque\n               | FN ID PIZQ PDER bloquelista_parametros : lista_parametros COMA parametroolista_parametros : parametroobloque : LLAIZQ instrucciones LLADER\n              | LLAIZQ LLADER instrs_clase : instrs_clase COMA parametroo  instrs_clase :  parametroo  instr : parametrooparametroo : ID DOBLEPT tipoinstrucciones : instrucciones instruccioninstrucciones : instruccioninstruccion : llamada PTCOMA\n                   | variables PTCOMA\n                   | declaracion_objeto PTCOMA\n                   | print_instruccion PTCOMA\n                   | return_instruccion PTCOMA\n                   | if_instruccion \n                   | while_instruccion  declaracion_objeto : ID ID IGUAL expression llamada : ID PIZQ lista_expresiones PDER \n               | ID PIZQ PDER return_instruccion : RETURN expression\n                          | RETURN variables : LET MUT ID DOBLEPT tipo IGUAL expression \n\t\t         | LET ID DOBLEPT tipo IGUAL expression \n\t\t         | LET MUT ID IGUAL expression \n\t\t         | LET ID IGUAL expression \n\t\t         | ID IGUAL expressiontipo : INT\n\t        | FLOAT\n\t        | STR1\n\t        | STR2\n\t        | BOOLEA\n\t        | CHARprint_instruccion : PRINT NOT PIZQ expression PDERif_instruccion : IF PIZQ expression PDER bloque\n                      | IF PIZQ expression PDER bloque ELSE bloque \n                      | IF PIZQ expression PDER bloque lista_else_if\n                      | IF PIZQ expression PDER bloque lista_else_if ELSE bloque lista_else_if : lista_else_if else_iflista_else_if : else_if else_if : ELSE IF PIZQ expression PDER bloque while_instruccion : WHILE expression bloque lista_expresiones : lista_expresiones COMA expressionlista_expresiones : expressionexpression : expression OR expression\n                 | expression AND expression\n                 | NOT expression %prec NOTexpression : expression MENOR expression\n                 | expression MAYOR expression\n                 | expression MAYORIGUAL expression\n                 | expression MENORIGUAL expression\n                 | expression DIFERENTE expression\n                 | expression IGUALIGUAL expressionexpression : MENOS expression %prec UMENOS\n                 | expression MAS expression\n                 | expression MENOS expression\n                 | expression MULTIPLICACION expression\n                 | expression DIVISION expression\n                 | PIZQ expression PDER\n                 | expression MODULO expression\n                 | INT DOBLEPT DOBLEPT POW PIZQ expression COMA expression PDER\n                 | FLOAT DOBLEPT DOBLEPT POWF PIZQ expression COMA expression PDERexpression : expression PT BUFER1 PIZQ PDER\n                  | expression PT BUFER2 PIZQ PDERexpression : llamada\n                  | acceso_objeto_expresion\n                  | instancia_objeto expression : ENTERO\n                  | DECIMAL\n                  | ID\n                  | CADENA\n                  | CHAR\n                  | TRUE\n                  | FALSE instancia_objeto : ID PIZQ lista_expresiones PDER\n                         | ID PIZQ PDER  acceso_objeto_expresion : acceso_objeto acceso_objeto : acceso_objeto PT expression acceso_objeto : expression'
    
_lr_action_items = {'STRUCT':([0,2,3,4,5,8,11,15,21,26,37,40,56,121,],[6,6,-3,-4,-5,-2,-6,-8,-7,-11,-10,-15,-14,-9,]),'FN':([0,2,3,4,5,8,11,15,21,26,37,40,56,121,],[7,7,-3,-4,-5,-2,-6,-8,-7,-11,-10,-15,-14,-9,]),'$end':([1,2,3,4,5,8,11,15,21,26,37,40,56,121,],[0,-1,-3,-4,-5,-2,-6,-8,-7,-11,-10,-15,-14,-9,]),'ID':([6,7,12,13,22,25,27,39,40,41,47,48,49,50,52,54,56,57,58,59,60,61,62,64,65,66,70,71,72,86,89,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,117,118,120,124,126,155,162,163,167,168,170,171,176,178,179,180,181,182,189,],[9,10,17,17,17,17,49,49,-15,-21,-27,-28,63,67,80,80,-14,-20,-22,-23,-24,-25,-26,80,80,94,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,-53,80,80,80,-46,80,80,80,-48,-51,-47,-50,80,80,80,-49,-52,]),'LLAIZQ':([9,19,24,30,31,32,33,34,35,75,76,77,78,79,80,81,82,83,84,85,87,88,112,113,130,131,132,133,134,135,136,137,138,139,140,141,142,145,149,150,151,161,165,166,169,177,186,187,188,],[12,27,27,-39,-40,-41,-42,-43,-44,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-88,27,27,-58,-65,-56,-57,-59,-60,-61,-62,-63,-64,-66,-67,-68,-69,-71,-70,-31,-89,27,-30,-74,-75,27,27,-72,-73,27,]),'PIZQ':([10,49,52,53,54,64,65,68,70,71,72,80,86,89,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,117,118,124,126,143,144,155,159,160,163,167,168,175,179,180,181,],[13,64,72,86,72,72,72,97,72,72,72,117,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,157,158,72,167,168,72,72,72,181,72,72,72,]),'LLADER':([12,14,16,27,28,29,30,31,32,33,34,35,39,40,41,47,48,56,57,58,59,60,61,62,120,162,170,171,176,178,182,189,],[15,21,-17,40,-16,-19,-39,-40,-41,-42,-43,-44,56,-15,-21,-27,-28,-14,-20,-22,-23,-24,-25,-26,-53,-46,-48,-51,-47,-50,-49,-52,]),'PDER':([13,18,20,29,30,31,32,33,34,35,38,64,75,76,77,78,79,80,81,82,83,84,85,90,92,112,113,114,117,119,129,130,131,132,133,134,135,136,137,138,139,140,141,142,145,148,149,150,152,157,158,161,165,166,183,184,185,186,187,],[19,24,-13,-19,-39,-40,-41,-42,-43,-44,-12,91,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-88,123,-55,-58,-65,145,149,151,156,-56,-57,-59,-60,-61,-62,-63,-64,-66,-67,-68,-69,-71,-70,161,-31,-89,-54,165,166,-30,-74,-75,186,187,188,-72,-73,]),'COMA':([14,16,18,20,28,29,30,31,32,33,34,35,38,75,76,77,78,79,80,81,82,83,84,85,90,92,112,113,130,131,132,133,134,135,136,137,138,139,140,141,142,145,148,149,150,152,161,165,166,173,174,186,187,],[22,-17,25,-13,-16,-19,-39,-40,-41,-42,-43,-44,-12,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-88,124,-55,-58,-65,-56,-57,-59,-60,-61,-62,-63,-64,-66,-67,-68,-69,-71,-70,124,-31,-89,-54,-30,-74,-75,179,180,-72,-73,]),'DOBLEPT':([17,67,73,74,94,115,116,],[23,95,115,116,125,146,147,]),'INT':([23,52,54,55,64,65,70,71,72,86,89,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,117,118,124,125,126,155,163,167,168,179,180,181,],[30,73,73,30,73,73,73,73,73,73,73,30,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,30,73,73,73,73,73,73,73,73,]),'FLOAT':([23,52,54,55,64,65,70,71,72,86,89,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,117,118,124,125,126,155,163,167,168,179,180,181,],[31,74,74,31,74,74,74,74,74,74,74,31,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,31,74,74,74,74,74,74,74,74,]),'STR1':([23,55,95,125,],[32,32,32,32,]),'STR2':([23,55,95,125,],[33,33,33,33,]),'BOOLEA':([23,55,95,125,],[34,34,34,34,]),'CHAR':([23,52,54,55,64,65,70,71,72,86,89,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,117,118,124,125,126,155,163,167,168,179,180,181,],[35,82,82,35,82,82,82,82,82,82,82,35,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,35,82,82,82,82,82,82,82,82,]),'MENOS':([24,52,54,64,65,69,70,71,72,75,76,77,78,79,80,81,82,83,84,85,86,87,89,92,93,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,112,113,114,117,118,119,122,124,126,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,145,149,150,152,154,155,161,163,164,165,166,167,168,172,173,174,179,180,181,183,184,185,186,187,],[36,71,71,71,71,107,71,71,71,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-88,71,107,71,107,107,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,-58,-65,107,71,71,107,107,71,71,107,107,107,107,107,107,107,107,107,107,-66,-67,-68,-69,-71,-70,-31,107,107,107,71,-30,71,107,-74,-75,71,71,107,107,107,71,71,71,107,107,107,-72,-73,]),'LET':([27,39,40,41,47,48,56,57,58,59,60,61,62,120,162,170,171,176,178,182,189,],[50,50,-15,-21,-27,-28,-14,-20,-22,-23,-24,-25,-26,-53,-46,-48,-51,-47,-50,-49,-52,]),'PRINT':([27,39,40,41,47,48,56,57,58,59,60,61,62,120,162,170,171,176,178,182,189,],[51,51,-15,-21,-27,-28,-14,-20,-22,-23,-24,-25,-26,-53,-46,-48,-51,-47,-50,-49,-52,]),'RETURN':([27,39,40,41,47,48,56,57,58,59,60,61,62,120,162,170,171,176,178,182,189,],[52,52,-15,-21,-27,-28,-14,-20,-22,-23,-24,-25,-26,-53,-46,-48,-51,-47,-50,-49,-52,]),'IF':([27,39,40,41,47,48,56,57,58,59,60,61,62,120,162,169,170,171,176,177,178,182,189,],[53,53,-15,-21,-27,-28,-14,-20,-22,-23,-24,-25,-26,-53,-46,175,-48,-51,-47,175,-50,-49,-52,]),'WHILE':([27,39,40,41,47,48,56,57,58,59,60,61,62,120,162,170,171,176,178,182,189,],[54,54,-15,-21,-27,-28,-14,-20,-22,-23,-24,-25,-26,-53,-46,-48,-51,-47,-50,-49,-52,]),'IGUAL':([30,31,32,33,34,35,49,63,67,94,127,153,],[-39,-40,-41,-42,-43,-44,65,89,96,126,155,163,]),'MAYOR':([36,69,75,76,77,78,79,80,81,82,83,84,85,87,92,93,112,113,114,119,122,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,145,149,150,152,154,161,164,165,166,172,173,174,183,184,185,186,187,],[55,101,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-88,101,101,101,-58,-65,101,101,101,101,101,101,101,-90,-90,-90,-90,-90,-90,-66,-67,-68,-69,-71,-70,-31,101,101,101,-30,101,-74,-75,101,101,101,101,101,101,-72,-73,]),'ELSE':([40,56,162,170,171,178,189,],[-15,-14,169,177,-51,-50,-52,]),'PTCOMA':([42,43,44,45,46,52,69,75,76,77,78,79,80,81,82,83,84,85,91,93,112,113,122,123,128,130,131,132,133,134,135,136,137,138,139,140,141,142,145,149,150,154,156,161,164,165,166,172,186,187,],[58,59,60,61,62,-33,-32,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-88,-31,-38,-58,-65,-29,-30,-37,-56,-57,-59,-60,-61,-62,-63,-64,-66,-67,-68,-69,-71,-70,-31,-89,-36,-45,-30,-35,-74,-75,-34,-72,-73,]),'MUT':([50,],[66,]),'NOT':([51,52,54,64,65,70,71,72,86,89,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,117,118,124,126,155,163,167,168,179,180,181,],[68,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,]),'ENTERO':([52,54,64,65,70,71,72,86,89,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,117,118,124,126,155,163,167,168,179,180,181,],[78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,]),'DECIMAL':([52,54,64,65,70,71,72,86,89,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,117,118,124,126,155,163,167,168,179,180,181,],[79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,]),'CADENA':([52,54,64,65,70,71,72,86,89,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,117,118,124,126,155,163,167,168,179,180,181,],[81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,]),'TRUE':([52,54,64,65,70,71,72,86,89,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,117,118,124,126,155,163,167,168,179,180,181,],[83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,]),'FALSE':([52,54,64,65,70,71,72,86,89,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,117,118,124,126,155,163,167,168,179,180,181,],[84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,]),'OR':([69,75,76,77,78,79,80,81,82,83,84,85,87,92,93,112,113,114,119,122,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,145,149,150,152,154,161,164,165,166,172,173,174,183,184,185,186,187,],[98,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-88,98,98,98,-58,-65,98,98,98,98,98,-56,-57,-59,-60,-61,-62,-63,-64,-66,-67,-68,-69,-71,-70,-31,98,98,98,-30,98,-74,-75,98,98,98,98,98,98,-72,-73,]),'AND':([69,75,76,77,78,79,80,81,82,83,84,85,87,92,93,112,113,114,119,122,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,145,149,150,152,154,161,164,165,166,172,173,174,183,184,185,186,187,],[99,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-88,99,99,99,-58,-65,99,99,99,99,99,99,-57,-59,-60,-61,-62,-63,-64,-66,-67,-68,-69,-71,-70,-31,99,99,99,-30,99,-74,-75,99,99,99,99,99,99,-72,-73,]),'MENOR':([69,75,76,77,78,79,80,81,82,83,84,85,87,92,93,112,113,114,119,122,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,145,149,150,152,154,161,164,165,166,172,173,174,183,184,185,186,187,],[100,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-88,100,100,100,-58,-65,100,100,100,100,100,100,100,-90,-90,-90,-90,-90,-90,-66,-67,-68,-69,-71,-70,-31,100,100,100,-30,100,-74,-75,100,100,100,100,100,100,-72,-73,]),'MAYORIGUAL':([69,75,76,77,78,79,80,81,82,83,84,85,87,92,93,112,113,114,119,122,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,145,149,150,152,154,161,164,165,166,172,173,174,183,184,185,186,187,],[102,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-88,102,102,102,-58,-65,102,102,102,102,102,102,102,-90,-90,-90,-90,-90,-90,-66,-67,-68,-69,-71,-70,-31,102,102,102,-30,102,-74,-75,102,102,102,102,102,102,-72,-73,]),'MENORIGUAL':([69,75,76,77,78,79,80,81,82,83,84,85,87,92,93,112,113,114,119,122,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,145,149,150,152,154,161,164,165,166,172,173,174,183,184,185,186,187,],[103,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-88,103,103,103,-58,-65,103,103,103,103,103,103,103,-90,-90,-90,-90,-90,-90,-66,-67,-68,-69,-71,-70,-31,103,103,103,-30,103,-74,-75,103,103,103,103,103,103,-72,-73,]),'DIFERENTE':([69,75,76,77,78,79,80,81,82,83,84,85,87,92,93,112,113,114,119,122,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,145,149,150,152,154,161,164,165,166,172,173,174,183,184,185,186,187,],[104,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-88,104,104,104,-58,-65,104,104,104,104,104,104,104,-90,-90,-90,-90,-90,-90,-66,-67,-68,-69,-71,-70,-31,104,104,104,-30,104,-74,-75,104,104,104,104,104,104,-72,-73,]),'IGUALIGUAL':([69,75,76,77,78,79,80,81,82,83,84,85,87,92,93,112,113,114,119,122,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,145,149,150,152,154,161,164,165,166,172,173,174,183,184,185,186,187,],[105,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-88,105,105,105,-58,-65,105,105,105,105,105,105,105,-90,-90,-90,-90,-90,-90,-66,-67,-68,-69,-71,-70,-31,105,105,105,-30,105,-74,-75,105,105,105,105,105,105,-72,-73,]),'MAS':([69,75,76,77,78,79,80,81,82,83,84,85,87,92,93,112,113,114,119,122,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,145,149,150,152,154,161,164,165,166,172,173,174,183,184,185,186,187,],[106,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-88,106,106,106,-58,-65,106,106,106,106,106,106,106,106,106,106,106,106,106,-66,-67,-68,-69,-71,-70,-31,106,106,106,-30,106,-74,-75,106,106,106,106,106,106,-72,-73,]),'MULTIPLICACION':([69,75,76,77,78,79,80,81,82,83,84,85,87,92,93,112,113,114,119,122,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,145,149,150,152,154,161,164,165,166,172,173,174,183,184,185,186,187,],[108,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-88,108,108,108,-58,-65,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,-68,-69,-71,-70,-31,108,108,108,-30,108,-74,-75,108,108,108,108,108,108,-72,-73,]),'DIVISION':([69,75,76,77,78,79,80,81,82,83,84,85,87,92,93,112,113,114,119,122,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,145,149,150,152,154,161,164,165,166,172,173,174,183,184,185,186,187,],[109,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-88,109,109,109,-58,-65,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,-68,-69,-71,-70,-31,109,109,109,-30,109,-74,-75,109,109,109,109,109,109,-72,-73,]),'MODULO':([69,75,76,77,78,79,80,81,82,83,84,85,87,92,93,112,113,114,119,122,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,145,149,150,152,154,161,164,165,166,172,173,174,183,184,185,186,187,],[110,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-88,110,110,110,-58,-65,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,-68,-69,-71,-70,-31,110,110,110,-30,110,-74,-75,110,110,110,110,110,110,-72,-73,]),'PT':([69,75,76,77,78,79,80,81,82,83,84,85,87,92,93,112,113,114,119,122,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,145,149,150,152,154,161,164,165,166,172,173,174,183,184,185,186,187,],[111,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,118,111,111,111,-58,-65,111,111,111,111,111,-56,-57,-59,-60,-61,-62,-63,-64,-66,-67,-68,-69,-71,-70,-31,111,111,111,-30,111,-74,-75,111,111,111,111,111,111,-72,-73,]),'BUFER1':([111,],[143,]),'BUFER2':([111,],[144,]),'POW':([146,],[159,]),'POWF':([147,],[160,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'clases_funciones':([0,],[2,]),'clase_funcion':([0,2,],[3,8,]),'clase':([0,2,],[4,4,]),'funcion':([0,2,],[5,5,]),'bloqueClase':([9,],[11,]),'instrs_clase':([12,],[14,]),'parametroo':([12,13,22,25,],[16,20,28,38,]),'lista_parametros':([13,],[18,]),'bloque':([19,24,87,88,151,169,177,188,],[26,37,120,121,162,176,182,189,]),'tipo':([23,55,95,125,],[29,88,127,153,]),'instrucciones':([27,],[39,]),'instruccion':([27,39,],[41,57,]),'llamada':([27,39,52,54,64,65,70,71,72,86,89,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,117,118,124,126,155,163,167,168,179,180,181,],[42,42,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,]),'variables':([27,39,],[43,43,]),'declaracion_objeto':([27,39,],[44,44,]),'print_instruccion':([27,39,],[45,45,]),'return_instruccion':([27,39,],[46,46,]),'if_instruccion':([27,39,],[47,47,]),'while_instruccion':([27,39,],[48,48,]),'expression':([52,54,64,65,70,71,72,86,89,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,117,118,124,126,155,163,167,168,179,180,181,],[69,87,92,93,112,113,114,119,122,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,92,150,152,154,164,172,173,174,183,184,185,]),'acceso_objeto_expresion':([52,54,64,65,70,71,72,86,89,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,117,118,124,126,155,163,167,168,179,180,181,],[76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,]),'instancia_objeto':([52,54,64,65,70,71,72,86,89,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,117,118,124,126,155,163,167,168,179,180,181,],[77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,]),'acceso_objeto':([52,54,64,65,70,71,72,86,89,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,117,118,124,126,155,163,167,168,179,180,181,],[85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,]),'lista_expresiones':([64,117,],[90,148,]),'lista_else_if':([162,],[170,]),'else_if':([162,170,],[171,178,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> clases_funciones','init',1,'p_init','gramatica.py',228),
  ('clases_funciones -> clases_funciones clase_funcion','clases_funciones',2,'p_clases_funciones','gramatica.py',232),
  ('clases_funciones -> clase_funcion','clases_funciones',1,'p_clases_funciones_corte','gramatica.py',237),
  ('clase_funcion -> clase','clase_funcion',1,'p_clase_funcion','gramatica.py',241),
  ('clase_funcion -> funcion','clase_funcion',1,'p_clase_funcion','gramatica.py',242),
  ('clase -> STRUCT ID bloqueClase','clase',3,'p_clase','gramatica.py',250),
  ('bloqueClase -> LLAIZQ instrs_clase LLADER','bloqueClase',3,'p_bloque_clase','gramatica.py',254),
  ('bloqueClase -> LLAIZQ LLADER','bloqueClase',2,'p_bloque_clase','gramatica.py',255),
  ('funcion -> FN ID PIZQ lista_parametros PDER MENOS MAYOR tipo bloque','funcion',9,'p_funcion','gramatica.py',269),
  ('funcion -> FN ID PIZQ lista_parametros PDER bloque','funcion',6,'p_funcion','gramatica.py',270),
  ('funcion -> FN ID PIZQ PDER bloque','funcion',5,'p_funcion','gramatica.py',271),
  ('lista_parametros -> lista_parametros COMA parametroo','lista_parametros',3,'p_lista_parametros','gramatica.py',287),
  ('lista_parametros -> parametroo','lista_parametros',1,'p_lista_parametros_corte','gramatica.py',292),
  ('bloque -> LLAIZQ instrucciones LLADER','bloque',3,'p_bloque','gramatica.py',298),
  ('bloque -> LLAIZQ LLADER','bloque',2,'p_bloque','gramatica.py',299),
  ('instrs_clase -> instrs_clase COMA parametroo','instrs_clase',3,'p_instrs_clase','gramatica.py',311),
  ('instrs_clase -> parametroo','instrs_clase',1,'p_instrs_clase_corte','gramatica.py',317),
  ('instr -> parametroo','instr',1,'p_instr','gramatica.py',322),
  ('parametroo -> ID DOBLEPT tipo','parametroo',3,'p_parametroo','gramatica.py',331),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones','gramatica.py',345),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_instruccion','gramatica.py',351),
  ('instruccion -> llamada PTCOMA','instruccion',2,'p_instruccion','gramatica.py',358),
  ('instruccion -> variables PTCOMA','instruccion',2,'p_instruccion','gramatica.py',359),
  ('instruccion -> declaracion_objeto PTCOMA','instruccion',2,'p_instruccion','gramatica.py',360),
  ('instruccion -> print_instruccion PTCOMA','instruccion',2,'p_instruccion','gramatica.py',361),
  ('instruccion -> return_instruccion PTCOMA','instruccion',2,'p_instruccion','gramatica.py',362),
  ('instruccion -> if_instruccion','instruccion',1,'p_instruccion','gramatica.py',363),
  ('instruccion -> while_instruccion','instruccion',1,'p_instruccion','gramatica.py',364),
  ('declaracion_objeto -> ID ID IGUAL expression','declaracion_objeto',4,'p_declaracion_objeto','gramatica.py',382),
  ('llamada -> ID PIZQ lista_expresiones PDER','llamada',4,'p_llamada','gramatica.py',400),
  ('llamada -> ID PIZQ PDER','llamada',3,'p_llamada','gramatica.py',401),
  ('return_instruccion -> RETURN expression','return_instruccion',2,'p_return_instruccion','gramatica.py',408),
  ('return_instruccion -> RETURN','return_instruccion',1,'p_return_instruccion','gramatica.py',409),
  ('variables -> LET MUT ID DOBLEPT tipo IGUAL expression','variables',7,'p_variables','gramatica.py',431),
  ('variables -> LET ID DOBLEPT tipo IGUAL expression','variables',6,'p_variables','gramatica.py',432),
  ('variables -> LET MUT ID IGUAL expression','variables',5,'p_variables','gramatica.py',433),
  ('variables -> LET ID IGUAL expression','variables',4,'p_variables','gramatica.py',434),
  ('variables -> ID IGUAL expression','variables',3,'p_variables','gramatica.py',435),
  ('tipo -> INT','tipo',1,'p_tipo','gramatica.py',450),
  ('tipo -> FLOAT','tipo',1,'p_tipo','gramatica.py',451),
  ('tipo -> STR1','tipo',1,'p_tipo','gramatica.py',452),
  ('tipo -> STR2','tipo',1,'p_tipo','gramatica.py',453),
  ('tipo -> BOOLEA','tipo',1,'p_tipo','gramatica.py',454),
  ('tipo -> CHAR','tipo',1,'p_tipo','gramatica.py',455),
  ('print_instruccion -> PRINT NOT PIZQ expression PDER','print_instruccion',5,'p_print','gramatica.py',485),
  ('if_instruccion -> IF PIZQ expression PDER bloque','if_instruccion',5,'p_if_instruccion','gramatica.py',492),
  ('if_instruccion -> IF PIZQ expression PDER bloque ELSE bloque','if_instruccion',7,'p_if_instruccion','gramatica.py',493),
  ('if_instruccion -> IF PIZQ expression PDER bloque lista_else_if','if_instruccion',6,'p_if_instruccion','gramatica.py',494),
  ('if_instruccion -> IF PIZQ expression PDER bloque lista_else_if ELSE bloque','if_instruccion',8,'p_if_instruccion','gramatica.py',495),
  ('lista_else_if -> lista_else_if else_if','lista_else_if',2,'p_lista_else_if','gramatica.py',507),
  ('lista_else_if -> else_if','lista_else_if',1,'p_else_if_corte','gramatica.py',512),
  ('else_if -> ELSE IF PIZQ expression PDER bloque','else_if',6,'p_else_if','gramatica.py',516),
  ('while_instruccion -> WHILE expression bloque','while_instruccion',3,'p_while_instruccion','gramatica.py',522),
  ('lista_expresiones -> lista_expresiones COMA expression','lista_expresiones',3,'p_lista_expresiones','gramatica.py',542),
  ('lista_expresiones -> expression','lista_expresiones',1,'p_lista_expresiones_corte','gramatica.py',547),
  ('expression -> expression OR expression','expression',3,'p_expression_logica','gramatica.py',554),
  ('expression -> expression AND expression','expression',3,'p_expression_logica','gramatica.py',555),
  ('expression -> NOT expression','expression',2,'p_expression_logica','gramatica.py',556),
  ('expression -> expression MENOR expression','expression',3,'p_expression_relacional','gramatica.py',566),
  ('expression -> expression MAYOR expression','expression',3,'p_expression_relacional','gramatica.py',567),
  ('expression -> expression MAYORIGUAL expression','expression',3,'p_expression_relacional','gramatica.py',568),
  ('expression -> expression MENORIGUAL expression','expression',3,'p_expression_relacional','gramatica.py',569),
  ('expression -> expression DIFERENTE expression','expression',3,'p_expression_relacional','gramatica.py',570),
  ('expression -> expression IGUALIGUAL expression','expression',3,'p_expression_relacional','gramatica.py',571),
  ('expression -> MENOS expression','expression',2,'p_expression_aritmetica','gramatica.py',589),
  ('expression -> expression MAS expression','expression',3,'p_expression_aritmetica','gramatica.py',590),
  ('expression -> expression MENOS expression','expression',3,'p_expression_aritmetica','gramatica.py',591),
  ('expression -> expression MULTIPLICACION expression','expression',3,'p_expression_aritmetica','gramatica.py',592),
  ('expression -> expression DIVISION expression','expression',3,'p_expression_aritmetica','gramatica.py',593),
  ('expression -> PIZQ expression PDER','expression',3,'p_expression_aritmetica','gramatica.py',594),
  ('expression -> expression MODULO expression','expression',3,'p_expression_aritmetica','gramatica.py',595),
  ('expression -> INT DOBLEPT DOBLEPT POW PIZQ expression COMA expression PDER','expression',9,'p_expression_aritmetica','gramatica.py',596),
  ('expression -> FLOAT DOBLEPT DOBLEPT POWF PIZQ expression COMA expression PDER','expression',9,'p_expression_aritmetica','gramatica.py',597),
  ('expression -> expression PT BUFER1 PIZQ PDER','expression',5,'p_expression_nativa','gramatica.py',623),
  ('expression -> expression PT BUFER2 PIZQ PDER','expression',5,'p_expression_nativa','gramatica.py',624),
  ('expression -> llamada','expression',1,'p_otras_expresiones','gramatica.py',638),
  ('expression -> acceso_objeto_expresion','expression',1,'p_otras_expresiones','gramatica.py',639),
  ('expression -> instancia_objeto','expression',1,'p_otras_expresiones','gramatica.py',640),
  ('expression -> ENTERO','expression',1,'p_expression_primitiva','gramatica.py',646),
  ('expression -> DECIMAL','expression',1,'p_expression_primitiva','gramatica.py',647),
  ('expression -> ID','expression',1,'p_expression_primitiva','gramatica.py',648),
  ('expression -> CADENA','expression',1,'p_expression_primitiva','gramatica.py',649),
  ('expression -> CHAR','expression',1,'p_expression_primitiva','gramatica.py',650),
  ('expression -> TRUE','expression',1,'p_expression_primitiva','gramatica.py',651),
  ('expression -> FALSE','expression',1,'p_expression_primitiva','gramatica.py',652),
  ('instancia_objeto -> ID PIZQ lista_expresiones PDER','instancia_objeto',4,'p_instancia_objeto','gramatica.py',677),
  ('instancia_objeto -> ID PIZQ PDER','instancia_objeto',3,'p_instancia_objeto','gramatica.py',678),
  ('acceso_objeto_expresion -> acceso_objeto','acceso_objeto_expresion',1,'p_acceso_objeto_expresion','gramatica.py',688),
  ('acceso_objeto -> acceso_objeto PT expression','acceso_objeto',3,'p_acceso_objeto','gramatica.py',693),
  ('acceso_objeto -> expression','acceso_objeto',1,'p_acceso_objeto_cort','gramatica.py',699),
]
