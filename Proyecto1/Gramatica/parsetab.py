
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDnonassocMAYORMENORIGUALMENORMAYORIGUALIGUALIGUALDIFERENTEleftMASMENOSleftMULTIPLICACIONDIVISIONleftMODULOrightNOTUMENOSAND CADENA COMA CORDER CORIZQ DECIMAL DIFERENTE DIVISION DOBLEPT ENTERO FALSE FLOAT ID IGUAL IGUALIGUAL INT INTT LET MAS MAYOR MAYORIGUAL MENOR MENORIGUAL MENOS MODULO MULTIPLICACION MUT NOT OR PDER PIZQ POW POWF PRINT PTCOMA TRUEinit : instruccionesinstrucciones : instrucciones instruccioninstrucciones : instruccioninstruccion : print_instruccion\n                   | variables\n                   | declaracion declaracion : INTT ID  IGUAL expression  PTCOMA\n                    | INTT ID PTCOMAvariables : LET MUT ID DOBLEPT tipo IGUAL expression PTCOMA\n\t\t         | LET ID DOBLEPT tipo IGUAL expression PTCOMA\n\t\t         | LET MUT ID IGUAL expression PTCOMA\n\t\t         | LET ID IGUAL expression PTCOMA\n\t\t         | ID IGUAL expression PTCOMAtipo : INT\n\t        | FLOATprint_instruccion : PRINT NOT PIZQ expression PDER PTCOMAexpression : expression OR expression\n                 | expression AND expression\n                 | NOT expression %prec NOTexpression : expression MENOR expression\n                 | expression MAYOR expression\n                 | expression MAYORIGUAL expression\n                 | expression MENORIGUAL expression\n                 | expression DIFERENTE expression\n                 | expression IGUALIGUAL expressionexpression : MENOS expression %prec UMENOS\n                 | expression MAS expression\n                 | expression MENOS expression\n                 | expression MULTIPLICACION expression\n                 | expression DIVISION expression\n                 | PIZQ expression PDER\n                 | expression MODULO expression\n                 | INT DOBLEPT DOBLEPT POW PIZQ expression COMA expression PDER\n                 | FLOAT DOBLEPT DOBLEPT POWF PIZQ expression COMA expression PDERexpression : ENTERO\n                  | DECIMAL\n                  | ID\n                  | CADENA\n                  | TRUE\n                  | FALSE'
    
_lr_action_items = {'PRINT':([0,2,3,4,5,6,11,34,42,66,83,84,86,91,94,],[7,7,-3,-4,-5,-6,-2,-8,-13,-12,-7,-16,-11,-10,-9,]),'LET':([0,2,3,4,5,6,11,34,42,66,83,84,86,91,94,],[8,8,-3,-4,-5,-6,-2,-8,-13,-12,-7,-16,-11,-10,-9,]),'ID':([0,2,3,4,5,6,8,10,11,13,15,17,20,23,24,25,33,34,37,42,43,44,45,46,47,48,49,50,51,52,53,54,55,65,66,83,84,85,86,91,92,93,94,97,98,],[9,9,-3,-4,-5,-6,14,16,-2,18,21,21,21,21,21,21,21,-8,21,-13,21,21,21,21,21,21,21,21,21,21,21,21,21,21,-12,-7,-16,21,-11,-10,21,21,-9,21,21,]),'INTT':([0,2,3,4,5,6,11,34,42,66,83,84,86,91,94,],[10,10,-3,-4,-5,-6,-2,-8,-13,-12,-7,-16,-11,-10,-9,]),'$end':([1,2,3,4,5,6,11,34,42,66,83,84,86,91,94,],[0,-1,-3,-4,-5,-6,-2,-8,-13,-12,-7,-16,-11,-10,-9,]),'NOT':([7,15,17,20,23,24,25,33,37,43,44,45,46,47,48,49,50,51,52,53,54,55,65,85,92,93,97,98,],[12,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'MUT':([8,],[13,]),'IGUAL':([9,14,16,18,38,39,40,63,],[15,20,33,37,65,-14,-15,85,]),'PIZQ':([12,15,17,20,23,24,25,33,37,43,44,45,46,47,48,49,50,51,52,53,54,55,65,85,88,89,92,93,97,98,],[17,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,92,93,25,25,25,25,]),'DOBLEPT':([14,18,26,27,59,60,],[19,36,59,60,81,82,]),'MENOS':([15,17,20,21,22,23,24,25,28,29,30,31,32,33,35,37,41,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,61,64,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,85,87,90,92,93,95,96,97,98,99,100,101,102,],[24,24,24,-37,52,24,24,24,-35,-36,-38,-39,-40,24,52,24,52,24,24,24,24,24,24,24,24,24,24,24,24,24,-19,-26,52,52,52,24,52,52,52,52,52,52,52,52,-27,-28,-29,-30,-32,-31,24,52,52,24,24,52,52,24,24,52,52,-33,-34,]),'INT':([15,17,19,20,23,24,25,33,36,37,43,44,45,46,47,48,49,50,51,52,53,54,55,65,85,92,93,97,98,],[26,26,39,26,26,26,26,26,39,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'FLOAT':([15,17,19,20,23,24,25,33,36,37,43,44,45,46,47,48,49,50,51,52,53,54,55,65,85,92,93,97,98,],[27,27,40,27,27,27,27,27,40,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'ENTERO':([15,17,20,23,24,25,33,37,43,44,45,46,47,48,49,50,51,52,53,54,55,65,85,92,93,97,98,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'DECIMAL':([15,17,20,23,24,25,33,37,43,44,45,46,47,48,49,50,51,52,53,54,55,65,85,92,93,97,98,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'CADENA':([15,17,20,23,24,25,33,37,43,44,45,46,47,48,49,50,51,52,53,54,55,65,85,92,93,97,98,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'TRUE':([15,17,20,23,24,25,33,37,43,44,45,46,47,48,49,50,51,52,53,54,55,65,85,92,93,97,98,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'FALSE':([15,17,20,23,24,25,33,37,43,44,45,46,47,48,49,50,51,52,53,54,55,65,85,92,93,97,98,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'PTCOMA':([16,21,22,28,29,30,31,32,41,56,57,61,62,64,67,68,69,70,71,72,73,74,75,76,77,78,79,80,87,90,101,102,],[34,-37,42,-35,-36,-38,-39,-40,66,-19,-26,83,84,86,-17,-18,-20,-21,-22,-23,-24,-25,-27,-28,-29,-30,-32,-31,91,94,-33,-34,]),'OR':([21,22,28,29,30,31,32,35,41,56,57,58,61,64,67,68,69,70,71,72,73,74,75,76,77,78,79,80,87,90,95,96,99,100,101,102,],[-37,43,-35,-36,-38,-39,-40,43,43,-19,-26,43,43,43,-17,-18,-20,-21,-22,-23,-24,-25,-27,-28,-29,-30,-32,-31,43,43,43,43,43,43,-33,-34,]),'AND':([21,22,28,29,30,31,32,35,41,56,57,58,61,64,67,68,69,70,71,72,73,74,75,76,77,78,79,80,87,90,95,96,99,100,101,102,],[-37,44,-35,-36,-38,-39,-40,44,44,-19,-26,44,44,44,44,-18,-20,-21,-22,-23,-24,-25,-27,-28,-29,-30,-32,-31,44,44,44,44,44,44,-33,-34,]),'MENOR':([21,22,28,29,30,31,32,35,41,56,57,58,61,64,67,68,69,70,71,72,73,74,75,76,77,78,79,80,87,90,95,96,99,100,101,102,],[-37,45,-35,-36,-38,-39,-40,45,45,-19,-26,45,45,45,45,45,None,None,None,None,None,None,-27,-28,-29,-30,-32,-31,45,45,45,45,45,45,-33,-34,]),'MAYOR':([21,22,28,29,30,31,32,35,41,56,57,58,61,64,67,68,69,70,71,72,73,74,75,76,77,78,79,80,87,90,95,96,99,100,101,102,],[-37,46,-35,-36,-38,-39,-40,46,46,-19,-26,46,46,46,46,46,None,None,None,None,None,None,-27,-28,-29,-30,-32,-31,46,46,46,46,46,46,-33,-34,]),'MAYORIGUAL':([21,22,28,29,30,31,32,35,41,56,57,58,61,64,67,68,69,70,71,72,73,74,75,76,77,78,79,80,87,90,95,96,99,100,101,102,],[-37,47,-35,-36,-38,-39,-40,47,47,-19,-26,47,47,47,47,47,None,None,None,None,None,None,-27,-28,-29,-30,-32,-31,47,47,47,47,47,47,-33,-34,]),'MENORIGUAL':([21,22,28,29,30,31,32,35,41,56,57,58,61,64,67,68,69,70,71,72,73,74,75,76,77,78,79,80,87,90,95,96,99,100,101,102,],[-37,48,-35,-36,-38,-39,-40,48,48,-19,-26,48,48,48,48,48,None,None,None,None,None,None,-27,-28,-29,-30,-32,-31,48,48,48,48,48,48,-33,-34,]),'DIFERENTE':([21,22,28,29,30,31,32,35,41,56,57,58,61,64,67,68,69,70,71,72,73,74,75,76,77,78,79,80,87,90,95,96,99,100,101,102,],[-37,49,-35,-36,-38,-39,-40,49,49,-19,-26,49,49,49,49,49,None,None,None,None,None,None,-27,-28,-29,-30,-32,-31,49,49,49,49,49,49,-33,-34,]),'IGUALIGUAL':([21,22,28,29,30,31,32,35,41,56,57,58,61,64,67,68,69,70,71,72,73,74,75,76,77,78,79,80,87,90,95,96,99,100,101,102,],[-37,50,-35,-36,-38,-39,-40,50,50,-19,-26,50,50,50,50,50,None,None,None,None,None,None,-27,-28,-29,-30,-32,-31,50,50,50,50,50,50,-33,-34,]),'MAS':([21,22,28,29,30,31,32,35,41,56,57,58,61,64,67,68,69,70,71,72,73,74,75,76,77,78,79,80,87,90,95,96,99,100,101,102,],[-37,51,-35,-36,-38,-39,-40,51,51,-19,-26,51,51,51,51,51,51,51,51,51,51,51,-27,-28,-29,-30,-32,-31,51,51,51,51,51,51,-33,-34,]),'MULTIPLICACION':([21,22,28,29,30,31,32,35,41,56,57,58,61,64,67,68,69,70,71,72,73,74,75,76,77,78,79,80,87,90,95,96,99,100,101,102,],[-37,53,-35,-36,-38,-39,-40,53,53,-19,-26,53,53,53,53,53,53,53,53,53,53,53,53,53,-29,-30,-32,-31,53,53,53,53,53,53,-33,-34,]),'DIVISION':([21,22,28,29,30,31,32,35,41,56,57,58,61,64,67,68,69,70,71,72,73,74,75,76,77,78,79,80,87,90,95,96,99,100,101,102,],[-37,54,-35,-36,-38,-39,-40,54,54,-19,-26,54,54,54,54,54,54,54,54,54,54,54,54,54,-29,-30,-32,-31,54,54,54,54,54,54,-33,-34,]),'MODULO':([21,22,28,29,30,31,32,35,41,56,57,58,61,64,67,68,69,70,71,72,73,74,75,76,77,78,79,80,87,90,95,96,99,100,101,102,],[-37,55,-35,-36,-38,-39,-40,55,55,-19,-26,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,-32,-31,55,55,55,55,55,55,-33,-34,]),'PDER':([21,28,29,30,31,32,35,56,57,58,67,68,69,70,71,72,73,74,75,76,77,78,79,80,99,100,101,102,],[-37,-35,-36,-38,-39,-40,62,-19,-26,80,-17,-18,-20,-21,-22,-23,-24,-25,-27,-28,-29,-30,-32,-31,101,102,-33,-34,]),'COMA':([21,28,29,30,31,32,56,57,67,68,69,70,71,72,73,74,75,76,77,78,79,80,95,96,101,102,],[-37,-35,-36,-38,-39,-40,-19,-26,-17,-18,-20,-21,-22,-23,-24,-25,-27,-28,-29,-30,-32,-31,97,98,-33,-34,]),'POW':([81,],[88,]),'POWF':([82,],[89,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'instrucciones':([0,],[2,]),'instruccion':([0,2,],[3,11,]),'print_instruccion':([0,2,],[4,4,]),'variables':([0,2,],[5,5,]),'declaracion':([0,2,],[6,6,]),'expression':([15,17,20,23,24,25,33,37,43,44,45,46,47,48,49,50,51,52,53,54,55,65,85,92,93,97,98,],[22,35,41,56,57,58,61,64,67,68,69,70,71,72,73,74,75,76,77,78,79,87,90,95,96,99,100,]),'tipo':([19,36,],[38,63,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> instrucciones','init',1,'p_init','gramatica.py',180),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones','gramatica.py',186),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_instruccion','gramatica.py',191),
  ('instruccion -> print_instruccion','instruccion',1,'p_instruccion','gramatica.py',198),
  ('instruccion -> variables','instruccion',1,'p_instruccion','gramatica.py',199),
  ('instruccion -> declaracion','instruccion',1,'p_instruccion','gramatica.py',200),
  ('declaracion -> INTT ID IGUAL expression PTCOMA','declaracion',5,'p_declaracion','gramatica.py',204),
  ('declaracion -> INTT ID PTCOMA','declaracion',3,'p_declaracion','gramatica.py',205),
  ('variables -> LET MUT ID DOBLEPT tipo IGUAL expression PTCOMA','variables',8,'p_variables','gramatica.py',216),
  ('variables -> LET ID DOBLEPT tipo IGUAL expression PTCOMA','variables',7,'p_variables','gramatica.py',217),
  ('variables -> LET MUT ID IGUAL expression PTCOMA','variables',6,'p_variables','gramatica.py',218),
  ('variables -> LET ID IGUAL expression PTCOMA','variables',5,'p_variables','gramatica.py',219),
  ('variables -> ID IGUAL expression PTCOMA','variables',4,'p_variables','gramatica.py',220),
  ('tipo -> INT','tipo',1,'p_tipo','gramatica.py',234),
  ('tipo -> FLOAT','tipo',1,'p_tipo','gramatica.py',235),
  ('print_instruccion -> PRINT NOT PIZQ expression PDER PTCOMA','print_instruccion',6,'p_print','gramatica.py',249),
  ('expression -> expression OR expression','expression',3,'p_expression_logica','gramatica.py',262),
  ('expression -> expression AND expression','expression',3,'p_expression_logica','gramatica.py',263),
  ('expression -> NOT expression','expression',2,'p_expression_logica','gramatica.py',264),
  ('expression -> expression MENOR expression','expression',3,'p_expression_relacional','gramatica.py',274),
  ('expression -> expression MAYOR expression','expression',3,'p_expression_relacional','gramatica.py',275),
  ('expression -> expression MAYORIGUAL expression','expression',3,'p_expression_relacional','gramatica.py',276),
  ('expression -> expression MENORIGUAL expression','expression',3,'p_expression_relacional','gramatica.py',277),
  ('expression -> expression DIFERENTE expression','expression',3,'p_expression_relacional','gramatica.py',278),
  ('expression -> expression IGUALIGUAL expression','expression',3,'p_expression_relacional','gramatica.py',279),
  ('expression -> MENOS expression','expression',2,'p_expression_aritmetica','gramatica.py',297),
  ('expression -> expression MAS expression','expression',3,'p_expression_aritmetica','gramatica.py',298),
  ('expression -> expression MENOS expression','expression',3,'p_expression_aritmetica','gramatica.py',299),
  ('expression -> expression MULTIPLICACION expression','expression',3,'p_expression_aritmetica','gramatica.py',300),
  ('expression -> expression DIVISION expression','expression',3,'p_expression_aritmetica','gramatica.py',301),
  ('expression -> PIZQ expression PDER','expression',3,'p_expression_aritmetica','gramatica.py',302),
  ('expression -> expression MODULO expression','expression',3,'p_expression_aritmetica','gramatica.py',303),
  ('expression -> INT DOBLEPT DOBLEPT POW PIZQ expression COMA expression PDER','expression',9,'p_expression_aritmetica','gramatica.py',304),
  ('expression -> FLOAT DOBLEPT DOBLEPT POWF PIZQ expression COMA expression PDER','expression',9,'p_expression_aritmetica','gramatica.py',305),
  ('expression -> ENTERO','expression',1,'p_expression_primitiva','gramatica.py',331),
  ('expression -> DECIMAL','expression',1,'p_expression_primitiva','gramatica.py',332),
  ('expression -> ID','expression',1,'p_expression_primitiva','gramatica.py',333),
  ('expression -> CADENA','expression',1,'p_expression_primitiva','gramatica.py',334),
  ('expression -> TRUE','expression',1,'p_expression_primitiva','gramatica.py',335),
  ('expression -> FALSE','expression',1,'p_expression_primitiva','gramatica.py',336),
]