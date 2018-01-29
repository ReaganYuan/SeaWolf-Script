
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftANDleftORleftISISNOTrightNOTleftTIMESDIVIDEleftEXPONENTIALOR NOT MINUS NUMBER ID PLUS IN AND FLOORDIV DIVIDE TIMES IS ISNOT GREATERTHENEQUAL LESSTHENEQUAL GREATERTHEN LESSTHEN ASSIGNVALUE EXPONENTIAL MOD LPAREN RPAREN STRING RBRACKET LBRACKET COMMA LCURLYBRACKET RCURLYBRACKET PRINT SEMICOLON WHILE IF ELSE FLOATprogram : LCURLYBRACKET function RCURLYBRACKET\n        function : code\n               | code function\n               | conditional\n               | conditional functionconditional : WHILE LPAREN operation RPAREN block conditional : IF LPAREN operation RPAREN block\n                   | IF LPAREN operation RPAREN block ELSE block\n                   | IF RPAREN operation LPAREN block ELSE block\n        code : statements\n                | statements code\n         code : blocks\n                 | blocks codeblocks : block blocks\n                  | blockblock : LCURLYBRACKET function RCURLYBRACKET\n                 | LCURLYBRACKET statements RCURLYBRACKETstatements : statement SEMICOLON statements\n                      | statement SEMICOLON\n\n        statement : operation\n                     | list\n                     | ID ASSIGNVALUE operation\n                     | ID ASSIGNVALUE list\n                     | list_id_string ASSIGNVALUE operation\n        statement : PRINT LPAREN operation RPAREN\n                     | PRINT LPAREN list RPARENlist_id_string : list LBRACKET expression RBRACKET\n                  | list LBRACKET list_id_string RBRACKET\n                  | list LBRACKET expression RBRACKET LBRACKET expression RBRACKET\n                  | LBRACKET list RBRACKET LBRACKET expression RBRACKET\n                  | LBRACKET expression RBRACKET LBRACKET expression RBRACKET\n                  | LBRACKET list RBRACKET LBRACKET ID RBRACKET\n                  | LBRACKET expression RBRACKET LBRACKET ID RBRACKET\n                   list_id_string : ID LBRACKET list_id_string RBRACKET\n                    |  ID LBRACKET expression RBRACKET\n                    | ID LBRACKET expression RBRACKET LBRACKET expression RBRACKET  list_id_string : STRING LBRACKET list_id_string RBRACKET\n                  | STRING LBRACKET expression RBRACKET\n                  | STRING LBRACKET expression RBRACKET LBRACKET expression RBRACKET\n        list : LBRACKET items RBRACKETitems : operation COMMA items\n                 | operation\n                 | list\n                 | list COMMA items\n                 operation : equal\n        equal : conditioncondition : expressionterm : factorexpression : termequal : NOT equal\n      operation : expression IN list\n                | operation OR equal\n                | operation AND equal\n        \n         expression : expression PLUS term\n                | expression MINUS term\n             term : term TIMES factor\n                | term DIVIDE factor\n                | term FLOORDIV factor\n                | term MOD factor\n              | term EXPONENTIAL factor\n                      condition : condition GREATERTHEN expression\n                | condition GREATERTHENEQUAL expression\n                | condition LESSTHENEQUAL expression\n                | condition LESSTHEN expression\n          equal   : equal IS condition\n                     | equal ISNOT conditionfactor : ID factor : NUMBERfactor : FLOAT factor : STRINGfactor : LPAREN operation RPARENfactor : list_id_string'
    
_lr_action_items = {'LCURLYBRACKET':([0,2,3,5,6,7,8,12,30,34,35,45,48,75,76,83,116,117,118,132,133,142,143,151,152,],[2,3,3,3,3,3,3,3,3,-11,-13,-14,-19,-16,-17,-18,3,3,3,-6,-7,3,3,-8,-9,]),'$end':([1,31,],[0,-1,]),'WHILE':([2,3,5,6,7,8,12,30,34,35,45,48,75,76,83,132,133,151,152,],[9,9,9,9,-10,-12,-15,-10,-11,-13,-14,-19,-16,-17,-18,-6,-7,-8,-9,]),'IF':([2,3,5,6,7,8,12,30,34,35,45,48,75,76,83,132,133,151,152,],[13,13,13,13,-10,-12,-15,-10,-11,-13,-14,-19,-16,-17,-18,-6,-7,-8,-9,]),'ID':([2,3,5,6,7,8,10,12,21,24,30,34,35,36,42,43,44,45,46,47,48,49,50,51,52,53,54,55,57,58,63,64,65,66,67,70,71,72,73,74,75,76,83,97,102,104,126,128,132,133,135,136,141,151,152,],[16,16,16,16,16,16,39,-15,39,39,16,-11,-13,39,39,39,39,-14,39,39,16,86,39,86,39,39,39,39,39,39,86,39,39,39,39,39,39,39,39,39,-16,-17,-18,39,39,39,138,140,-6,-7,39,39,39,-8,-9,]),'PRINT':([2,3,5,6,7,8,12,30,34,35,45,48,75,76,83,132,133,151,152,],[18,18,18,18,18,18,-15,18,-11,-13,-14,18,-16,-17,-18,-6,-7,-8,-9,]),'LBRACKET':([2,3,5,6,7,8,10,12,15,16,21,22,24,30,34,35,36,38,39,40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,60,63,64,65,66,67,70,71,72,73,74,75,76,83,86,88,93,97,100,101,102,103,104,119,122,125,126,128,131,132,133,135,136,138,140,141,151,152,],[21,21,21,21,21,21,42,-15,49,51,21,63,42,21,-11,-13,42,49,51,63,21,42,42,-14,42,42,21,42,21,42,42,21,42,42,97,42,42,49,42,42,42,42,42,42,42,42,42,42,-16,-17,-18,51,49,49,21,-40,126,21,128,21,135,136,49,42,42,141,-6,-7,42,42,51,51,42,-8,-9,]),'STRING':([2,3,5,6,7,8,10,12,21,24,30,34,35,36,42,43,44,45,46,47,48,49,50,51,52,53,54,55,57,58,63,64,65,66,67,70,71,72,73,74,75,76,83,97,102,104,126,128,132,133,135,136,141,151,152,],[22,22,22,22,22,22,40,-15,40,40,22,-11,-13,40,40,40,40,-14,40,40,22,22,40,22,40,40,40,40,40,40,22,40,40,40,40,40,40,40,40,40,-16,-17,-18,40,40,40,40,40,-6,-7,40,40,40,-8,-9,]),'NOT':([2,3,5,6,7,8,10,12,21,24,30,34,35,36,42,43,44,45,46,47,48,50,52,53,75,76,83,97,102,104,132,133,151,152,],[24,24,24,24,24,24,24,-15,24,24,24,-11,-13,24,24,24,24,-14,24,24,24,24,24,24,-16,-17,-18,24,24,24,-6,-7,-8,-9,]),'NUMBER':([2,3,5,6,7,8,10,12,21,24,30,34,35,36,42,43,44,45,46,47,48,49,50,51,52,53,54,55,57,58,63,64,65,66,67,70,71,72,73,74,75,76,83,97,102,104,126,128,132,133,135,136,141,151,152,],[27,27,27,27,27,27,27,-15,27,27,27,-11,-13,27,27,27,27,-14,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,-16,-17,-18,27,27,27,27,27,-6,-7,27,27,27,-8,-9,]),'FLOAT':([2,3,5,6,7,8,10,12,21,24,30,34,35,36,42,43,44,45,46,47,48,49,50,51,52,53,54,55,57,58,63,64,65,66,67,70,71,72,73,74,75,76,83,97,102,104,126,128,132,133,135,136,141,151,152,],[28,28,28,28,28,28,28,-15,28,28,28,-11,-13,28,28,28,28,-14,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,-16,-17,-18,28,28,28,28,28,-6,-7,28,28,28,-8,-9,]),'LPAREN':([2,3,5,6,7,8,9,10,12,13,18,19,20,21,23,24,25,26,27,28,30,34,35,36,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,57,58,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,82,83,94,95,96,97,98,99,100,102,104,107,108,109,110,111,112,113,114,115,119,120,121,122,126,128,130,131,132,133,135,136,141,146,147,148,149,151,152,153,154,155,],[10,10,10,10,10,10,36,10,-15,46,53,-45,-47,10,-46,10,-49,-48,-68,-69,10,-11,-13,10,-67,-70,-72,10,10,10,-14,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,-50,-47,10,10,10,10,10,-16,-17,-71,-52,-53,118,-18,-65,-66,-51,10,-54,-55,-40,10,10,-61,-62,-63,-64,-56,-57,-58,-59,-60,-27,-28,-34,-35,10,10,-37,-38,-6,-7,10,10,10,-30,-32,-31,-33,-8,-9,-29,-36,-39,]),'RCURLYBRACKET':([4,5,6,7,8,12,29,30,32,33,34,35,45,48,75,76,83,132,133,151,152,],[31,-2,-4,-10,-12,-15,75,76,-3,-5,-11,-13,-14,-19,-16,-17,-18,-6,-7,-8,-9,]),'SEMICOLON':([11,14,15,16,17,19,20,22,23,25,26,27,28,39,40,41,68,69,78,79,80,87,88,91,94,95,96,98,99,100,107,108,109,110,111,112,113,114,115,119,120,121,122,123,124,130,131,146,147,148,149,153,154,155,],[-20,48,-21,-67,-72,-45,-47,-70,-46,-49,-48,-68,-69,-67,-70,-72,-50,-47,-71,-52,-53,-22,-23,-24,-65,-66,-51,-54,-55,-40,-61,-62,-63,-64,-56,-57,-58,-59,-60,-27,-28,-34,-35,-25,-26,-37,-38,-30,-32,-31,-33,-29,-36,-39,]),'OR':([11,16,17,19,20,22,23,25,26,27,28,37,39,40,41,61,62,68,69,77,78,79,80,81,82,87,91,92,94,95,96,98,99,100,107,108,109,110,111,112,113,114,115,119,120,121,122,130,131,146,147,148,149,153,154,155,],[43,-67,-72,-45,-47,-70,-46,-49,-48,-68,-69,43,-67,-70,-72,-47,43,-50,-47,43,-71,-52,-53,43,43,43,43,43,-65,-66,-51,-54,-55,-40,-61,-62,-63,-64,-56,-57,-58,-59,-60,-27,-28,-34,-35,-37,-38,-30,-32,-31,-33,-29,-36,-39,]),'AND':([11,16,17,19,20,22,23,25,26,27,28,37,39,40,41,61,62,68,69,77,78,79,80,81,82,87,91,92,94,95,96,98,99,100,107,108,109,110,111,112,113,114,115,119,120,121,122,130,131,146,147,148,149,153,154,155,],[44,-67,-72,-45,-47,-70,-46,-49,-48,-68,-69,44,-67,-70,-72,-47,44,-50,-47,44,-71,-52,-53,44,44,44,44,44,-65,-66,-51,-54,-55,-40,-61,-62,-63,-64,-56,-57,-58,-59,-60,-27,-28,-34,-35,-37,-38,-30,-32,-31,-33,-29,-36,-39,]),'RPAREN':([13,19,20,23,25,26,27,28,37,39,40,41,68,69,77,78,79,80,81,92,93,94,95,96,98,99,100,107,108,109,110,111,112,113,114,115,119,120,121,122,130,131,146,147,148,149,153,154,155,],[47,-45,-47,-46,-49,-48,-68,-69,78,-67,-70,-72,-50,-47,116,-71,-52,-53,117,123,124,-65,-66,-51,-54,-55,-40,-61,-62,-63,-64,-56,-57,-58,-59,-60,-27,-28,-34,-35,-37,-38,-30,-32,-31,-33,-29,-36,-39,]),'ASSIGNVALUE':([16,17,119,120,121,122,130,131,146,147,148,149,153,154,155,],[50,52,-27,-28,-34,-35,-37,-38,-30,-32,-31,-33,-29,-36,-39,]),'TIMES':([16,17,22,25,26,27,28,39,40,41,78,85,86,89,98,99,105,111,112,113,114,115,119,120,121,122,130,131,138,140,146,147,148,149,153,154,155,],[-67,-72,-70,70,-48,-68,-69,-67,-70,-72,-71,-72,-67,-72,70,70,-72,-56,-57,-58,-59,-60,-27,-28,-34,-35,-37,-38,-67,-67,-30,-32,-31,-33,-29,-36,-39,]),'DIVIDE':([16,17,22,25,26,27,28,39,40,41,78,85,86,89,98,99,105,111,112,113,114,115,119,120,121,122,130,131,138,140,146,147,148,149,153,154,155,],[-67,-72,-70,71,-48,-68,-69,-67,-70,-72,-71,-72,-67,-72,71,71,-72,-56,-57,-58,-59,-60,-27,-28,-34,-35,-37,-38,-67,-67,-30,-32,-31,-33,-29,-36,-39,]),'FLOORDIV':([16,17,22,25,26,27,28,39,40,41,78,85,86,89,98,99,105,111,112,113,114,115,119,120,121,122,130,131,138,140,146,147,148,149,153,154,155,],[-67,-72,-70,72,-48,-68,-69,-67,-70,-72,-71,-72,-67,-72,72,72,-72,-56,-57,-58,-59,-60,-27,-28,-34,-35,-37,-38,-67,-67,-30,-32,-31,-33,-29,-36,-39,]),'MOD':([16,17,22,25,26,27,28,39,40,41,78,85,86,89,98,99,105,111,112,113,114,115,119,120,121,122,130,131,138,140,146,147,148,149,153,154,155,],[-67,-72,-70,73,-48,-68,-69,-67,-70,-72,-71,-72,-67,-72,73,73,-72,-56,-57,-58,-59,-60,-27,-28,-34,-35,-37,-38,-67,-67,-30,-32,-31,-33,-29,-36,-39,]),'EXPONENTIAL':([16,17,22,25,26,27,28,39,40,41,78,85,86,89,98,99,105,111,112,113,114,115,119,120,121,122,130,131,138,140,146,147,148,149,153,154,155,],[-67,-72,-70,74,-48,-68,-69,-67,-70,-72,-71,-72,-67,-72,74,74,-72,-56,-57,-58,-59,-60,-27,-28,-34,-35,-37,-38,-67,-67,-30,-32,-31,-33,-29,-36,-39,]),'IN':([16,17,20,22,25,26,27,28,39,40,41,61,78,98,99,111,112,113,114,115,119,120,121,122,130,131,146,147,148,149,153,154,155,],[-67,-72,56,-70,-49,-48,-68,-69,-67,-70,-72,56,-71,-54,-55,-56,-57,-58,-59,-60,-27,-28,-34,-35,-37,-38,-30,-32,-31,-33,-29,-36,-39,]),'PLUS':([16,17,20,22,25,26,27,28,39,40,41,61,69,78,84,85,86,89,90,98,99,105,106,107,108,109,110,111,112,113,114,115,119,120,121,122,130,131,137,138,139,140,144,145,146,147,148,149,150,153,154,155,],[-67,-72,57,-70,-49,-48,-68,-69,-67,-70,-72,57,57,-71,57,-72,-67,-72,57,-54,-55,-72,57,57,57,57,57,-56,-57,-58,-59,-60,-27,-28,-34,-35,-37,-38,57,-67,57,-67,57,57,-30,-32,-31,-33,57,-29,-36,-39,]),'MINUS':([16,17,20,22,25,26,27,28,39,40,41,61,69,78,84,85,86,89,90,98,99,105,106,107,108,109,110,111,112,113,114,115,119,120,121,122,130,131,137,138,139,140,144,145,146,147,148,149,150,153,154,155,],[-67,-72,58,-70,-49,-48,-68,-69,-67,-70,-72,58,58,-71,58,-72,-67,-72,58,-54,-55,-72,58,58,58,58,58,-56,-57,-58,-59,-60,-27,-28,-34,-35,-37,-38,58,-67,58,-67,58,58,-30,-32,-31,-33,58,-29,-36,-39,]),'GREATERTHEN':([16,17,20,22,23,25,26,27,28,39,40,41,61,69,78,94,95,98,99,107,108,109,110,111,112,113,114,115,119,120,121,122,130,131,146,147,148,149,153,154,155,],[-67,-72,-47,-70,64,-49,-48,-68,-69,-67,-70,-72,-47,-47,-71,64,64,-54,-55,-61,-62,-63,-64,-56,-57,-58,-59,-60,-27,-28,-34,-35,-37,-38,-30,-32,-31,-33,-29,-36,-39,]),'GREATERTHENEQUAL':([16,17,20,22,23,25,26,27,28,39,40,41,61,69,78,94,95,98,99,107,108,109,110,111,112,113,114,115,119,120,121,122,130,131,146,147,148,149,153,154,155,],[-67,-72,-47,-70,65,-49,-48,-68,-69,-67,-70,-72,-47,-47,-71,65,65,-54,-55,-61,-62,-63,-64,-56,-57,-58,-59,-60,-27,-28,-34,-35,-37,-38,-30,-32,-31,-33,-29,-36,-39,]),'LESSTHENEQUAL':([16,17,20,22,23,25,26,27,28,39,40,41,61,69,78,94,95,98,99,107,108,109,110,111,112,113,114,115,119,120,121,122,130,131,146,147,148,149,153,154,155,],[-67,-72,-47,-70,66,-49,-48,-68,-69,-67,-70,-72,-47,-47,-71,66,66,-54,-55,-61,-62,-63,-64,-56,-57,-58,-59,-60,-27,-28,-34,-35,-37,-38,-30,-32,-31,-33,-29,-36,-39,]),'LESSTHEN':([16,17,20,22,23,25,26,27,28,39,40,41,61,69,78,94,95,98,99,107,108,109,110,111,112,113,114,115,119,120,121,122,130,131,146,147,148,149,153,154,155,],[-67,-72,-47,-70,67,-49,-48,-68,-69,-67,-70,-72,-47,-47,-71,67,67,-54,-55,-61,-62,-63,-64,-56,-57,-58,-59,-60,-27,-28,-34,-35,-37,-38,-30,-32,-31,-33,-29,-36,-39,]),'IS':([16,17,19,20,22,23,25,26,27,28,39,40,41,61,68,69,78,79,80,94,95,98,99,107,108,109,110,111,112,113,114,115,119,120,121,122,130,131,146,147,148,149,153,154,155,],[-67,-72,54,-47,-70,-46,-49,-48,-68,-69,-67,-70,-72,-47,-50,-47,-71,54,54,-65,-66,-54,-55,-61,-62,-63,-64,-56,-57,-58,-59,-60,-27,-28,-34,-35,-37,-38,-30,-32,-31,-33,-29,-36,-39,]),'ISNOT':([16,17,19,20,22,23,25,26,27,28,39,40,41,61,68,69,78,79,80,94,95,98,99,107,108,109,110,111,112,113,114,115,119,120,121,122,130,131,146,147,148,149,153,154,155,],[-67,-72,55,-47,-70,-46,-49,-48,-68,-69,-67,-70,-72,-47,-50,-47,-71,55,55,-65,-66,-54,-55,-61,-62,-63,-64,-56,-57,-58,-59,-60,-27,-28,-34,-35,-37,-38,-30,-32,-31,-33,-29,-36,-39,]),'COMMA':([19,20,23,25,26,27,28,39,40,41,60,61,62,68,69,78,79,80,94,95,96,98,99,100,107,108,109,110,111,112,113,114,115,119,120,121,122,125,130,131,146,147,148,149,153,154,155,],[-45,-47,-46,-49,-48,-68,-69,-67,-70,-72,102,-47,104,-50,-47,-71,-52,-53,-65,-66,-51,-54,-55,-40,-61,-62,-63,-64,-56,-57,-58,-59,-60,-27,-28,-34,-35,102,-37,-38,-30,-32,-31,-33,-29,-36,-39,]),'RBRACKET':([19,20,22,23,25,26,27,28,39,40,41,59,60,61,62,68,69,78,79,80,84,85,86,89,90,94,95,96,98,99,100,105,106,107,108,109,110,111,112,113,114,115,119,120,121,122,125,127,129,130,131,137,138,139,140,144,145,146,147,148,149,150,153,154,155,],[-45,-47,-70,-46,-49,-48,-68,-69,-67,-70,-72,100,101,103,-42,-50,-47,-71,-52,-53,119,120,-67,121,122,-65,-66,-51,-54,-55,-40,130,131,-61,-62,-63,-64,-56,-57,-58,-59,-60,-27,-28,-34,-35,-43,-44,-41,-37,-38,146,147,148,149,153,154,-30,-32,-31,-33,155,-29,-36,-39,]),'ELSE':([75,76,133,134,],[-16,-17,142,143,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'function':([2,3,5,6,],[4,29,32,33,]),'code':([2,3,5,6,7,8,30,],[5,5,5,5,34,35,34,]),'conditional':([2,3,5,6,],[6,6,6,6,]),'statements':([2,3,5,6,7,8,30,48,],[7,30,7,7,7,7,7,83,]),'blocks':([2,3,5,6,7,8,12,30,],[8,8,8,8,8,8,45,8,]),'operation':([2,3,5,6,7,8,10,21,30,36,42,46,47,48,50,52,53,97,102,104,],[11,11,11,11,11,11,37,62,11,77,62,81,82,11,87,91,92,62,62,62,]),'block':([2,3,5,6,7,8,12,30,116,117,118,142,143,],[12,12,12,12,12,12,12,12,132,133,134,151,152,]),'statement':([2,3,5,6,7,8,30,48,],[14,14,14,14,14,14,14,14,]),'list':([2,3,5,6,7,8,10,21,24,30,36,42,43,44,46,47,48,49,50,51,52,53,54,55,56,57,58,63,64,65,66,67,70,71,72,73,74,97,102,104,126,128,135,136,141,],[15,15,15,15,15,15,38,60,38,15,38,60,38,38,38,38,15,38,88,38,38,93,38,38,96,38,38,38,38,38,38,38,38,38,38,38,38,125,125,125,38,38,38,38,38,]),'list_id_string':([2,3,5,6,7,8,10,21,24,30,36,42,43,44,46,47,48,49,50,51,52,53,54,55,57,58,63,64,65,66,67,70,71,72,73,74,97,102,104,126,128,135,136,141,],[17,17,17,17,17,17,41,41,41,17,41,41,41,41,41,41,17,85,41,89,41,41,41,41,41,41,105,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'equal':([2,3,5,6,7,8,10,21,24,30,36,42,43,44,46,47,48,50,52,53,97,102,104,],[19,19,19,19,19,19,19,19,68,19,19,19,79,80,19,19,19,19,19,19,19,19,19,]),'expression':([2,3,5,6,7,8,10,21,24,30,36,42,43,44,46,47,48,49,50,51,52,53,54,55,63,64,65,66,67,97,102,104,126,128,135,136,141,],[20,20,20,20,20,20,20,61,69,20,20,61,69,69,20,20,20,84,20,90,20,20,69,69,106,107,108,109,110,20,20,20,137,139,144,145,150,]),'condition':([2,3,5,6,7,8,10,21,24,30,36,42,43,44,46,47,48,50,52,53,54,55,97,102,104,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,94,95,23,23,23,]),'term':([2,3,5,6,7,8,10,21,24,30,36,42,43,44,46,47,48,49,50,51,52,53,54,55,57,58,63,64,65,66,67,97,102,104,126,128,135,136,141,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,98,99,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'factor':([2,3,5,6,7,8,10,21,24,30,36,42,43,44,46,47,48,49,50,51,52,53,54,55,57,58,63,64,65,66,67,70,71,72,73,74,97,102,104,126,128,135,136,141,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,111,112,113,114,115,26,26,26,26,26,26,26,26,]),'items':([21,42,97,102,104,],[59,59,59,127,129,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> LCURLYBRACKET function RCURLYBRACKET','program',3,'p_program','main.py',377),
  ('function -> code','function',1,'p_function','main.py',382),
  ('function -> code function','function',2,'p_function','main.py',383),
  ('function -> conditional','function',1,'p_function','main.py',384),
  ('function -> conditional function','function',2,'p_function','main.py',385),
  ('conditional -> WHILE LPAREN operation RPAREN block','conditional',5,'p_conditional_while','main.py',397),
  ('conditional -> IF LPAREN operation RPAREN block','conditional',5,'p_conditional_if','main.py',404),
  ('conditional -> IF LPAREN operation RPAREN block ELSE block','conditional',7,'p_conditional_if','main.py',405),
  ('conditional -> IF RPAREN operation LPAREN block ELSE block','conditional',7,'p_conditional_if','main.py',406),
  ('code -> statements','code',1,'p_code','main.py',423),
  ('code -> statements code','code',2,'p_code','main.py',424),
  ('code -> blocks','code',1,'p_code_blocks','main.py',438),
  ('code -> blocks code','code',2,'p_code_blocks','main.py',439),
  ('blocks -> block blocks','blocks',2,'p_blocks','main.py',450),
  ('blocks -> block','blocks',1,'p_blocks','main.py',451),
  ('block -> LCURLYBRACKET function RCURLYBRACKET','block',3,'p_block','main.py',459),
  ('block -> LCURLYBRACKET statements RCURLYBRACKET','block',3,'p_block','main.py',460),
  ('statements -> statement SEMICOLON statements','statements',3,'p_statements','main.py',465),
  ('statements -> statement SEMICOLON','statements',2,'p_statements','main.py',466),
  ('statement -> operation','statement',1,'p_statement','main.py',476),
  ('statement -> list','statement',1,'p_statement','main.py',477),
  ('statement -> ID ASSIGNVALUE operation','statement',3,'p_statement','main.py',478),
  ('statement -> ID ASSIGNVALUE list','statement',3,'p_statement','main.py',479),
  ('statement -> list_id_string ASSIGNVALUE operation','statement',3,'p_statement','main.py',480),
  ('statement -> PRINT LPAREN operation RPAREN','statement',4,'p_statement_print','main.py',491),
  ('statement -> PRINT LPAREN list RPAREN','statement',4,'p_statement_print','main.py',492),
  ('list_id_string -> list LBRACKET expression RBRACKET','list_id_string',4,'p_list_id_string','main.py',500),
  ('list_id_string -> list LBRACKET list_id_string RBRACKET','list_id_string',4,'p_list_id_string','main.py',501),
  ('list_id_string -> list LBRACKET expression RBRACKET LBRACKET expression RBRACKET','list_id_string',7,'p_list_id_string','main.py',502),
  ('list_id_string -> LBRACKET list RBRACKET LBRACKET expression RBRACKET','list_id_string',6,'p_list_id_string','main.py',503),
  ('list_id_string -> LBRACKET expression RBRACKET LBRACKET expression RBRACKET','list_id_string',6,'p_list_id_string','main.py',504),
  ('list_id_string -> LBRACKET list RBRACKET LBRACKET ID RBRACKET','list_id_string',6,'p_list_id_string','main.py',505),
  ('list_id_string -> LBRACKET expression RBRACKET LBRACKET ID RBRACKET','list_id_string',6,'p_list_id_string','main.py',506),
  ('list_id_string -> ID LBRACKET list_id_string RBRACKET','list_id_string',4,'p_list_id_string_ID','main.py',518),
  ('list_id_string -> ID LBRACKET expression RBRACKET','list_id_string',4,'p_list_id_string_ID','main.py',519),
  ('list_id_string -> ID LBRACKET expression RBRACKET LBRACKET expression RBRACKET','list_id_string',7,'p_list_id_string_ID','main.py',520),
  ('list_id_string -> STRING LBRACKET list_id_string RBRACKET','list_id_string',4,'p_list_id_string_string','main.py',530),
  ('list_id_string -> STRING LBRACKET expression RBRACKET','list_id_string',4,'p_list_id_string_string','main.py',531),
  ('list_id_string -> STRING LBRACKET expression RBRACKET LBRACKET expression RBRACKET','list_id_string',7,'p_list_id_string_string','main.py',532),
  ('list -> LBRACKET items RBRACKET','list',3,'p_list','main.py',543),
  ('items -> operation COMMA items','items',3,'p_items','main.py',547),
  ('items -> operation','items',1,'p_items','main.py',548),
  ('items -> list','items',1,'p_items','main.py',549),
  ('items -> list COMMA items','items',3,'p_items','main.py',550),
  ('operation -> equal','operation',1,'p_operations_equal','main.py',558),
  ('equal -> condition','equal',1,'p_eq_condition','main.py',563),
  ('condition -> expression','condition',1,'p_cond_expression','main.py',567),
  ('term -> factor','term',1,'p_term_factor','main.py',571),
  ('expression -> term','expression',1,'p_expr_term','main.py',575),
  ('equal -> NOT equal','equal',2,'p_not','main.py',579),
  ('operation -> expression IN list','operation',3,'p_binops_operation','main.py',585),
  ('operation -> operation OR equal','operation',3,'p_binops_operation','main.py',586),
  ('operation -> operation AND equal','operation',3,'p_binops_operation','main.py',587),
  ('expression -> expression PLUS term','expression',3,'p_binop_expression','main.py',593),
  ('expression -> expression MINUS term','expression',3,'p_binop_expression','main.py',594),
  ('term -> term TIMES factor','term',3,'p_binops_term','main.py',599),
  ('term -> term DIVIDE factor','term',3,'p_binops_term','main.py',600),
  ('term -> term FLOORDIV factor','term',3,'p_binops_term','main.py',601),
  ('term -> term MOD factor','term',3,'p_binops_term','main.py',602),
  ('term -> term EXPONENTIAL factor','term',3,'p_binops_term','main.py',603),
  ('condition -> condition GREATERTHEN expression','condition',3,'p_binops_condition','main.py',608),
  ('condition -> condition GREATERTHENEQUAL expression','condition',3,'p_binops_condition','main.py',609),
  ('condition -> condition LESSTHENEQUAL expression','condition',3,'p_binops_condition','main.py',610),
  ('condition -> condition LESSTHEN expression','condition',3,'p_binops_condition','main.py',611),
  ('equal -> equal IS condition','equal',3,'p_binops_equal','main.py',618),
  ('equal -> equal ISNOT condition','equal',3,'p_binops_equal','main.py',619),
  ('factor -> ID','factor',1,'p_factor_id','main.py',624),
  ('factor -> NUMBER','factor',1,'p_factor_number','main.py',627),
  ('factor -> FLOAT','factor',1,'p_factor_float','main.py',630),
  ('factor -> STRING','factor',1,'p_factor_string','main.py',633),
  ('factor -> LPAREN operation RPAREN','factor',3,'p_factor_expression','main.py',636),
  ('factor -> list_id_string','factor',1,'p_factor_list_id_string','main.py',640),
]
