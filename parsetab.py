
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASSIGN COLON COMMA CTE_FLOAT CTE_INT CTE_STR CURLYL CURLYR DIVIDE DO ELSE EQUAL FLOAT FROM FUNC GREATEREQUAL GREATERTHAN ID IF INT LESSEQUAL LESSTHAN MINUS MULT NOTEQUAL OR PARENTHESESL PARENTHESESR PLUS PRINCIPAL PRINT PROGRAM READ RETURN SEMICOLON SQUAREL SQUARER STRING THEN UNTIL VAR VOID WHILE\n        prog : PROGRAM ID SEMICOLON variables np_push_global_vars_ prog_funcs func_princ\n    \n        np_push_global_vars_ :\n    \n        prog_funcs : funcion prog_funcs\n        | empty\n    \n        variables : VAR variables_2\n        | empty\n    \n        variables_2 : tipo COLON lista_id SEMICOLON variables_rep\n    \n        variables_rep : variables_2\n        | empty\n    \n        lista_id : ID dimension_var lista_id_rep\n    \n        lista_id_rep : COMMA lista_id\n        | empty\n    \n        dimension_var : SQUAREL CTE_INT SQUARER\n        | empty\n    \n        tipo : INT\n        | FLOAT\n        | STRING\n    \n        func_princ : PRINCIPAL PARENTHESESL PARENTHESESR CURLYL estatuto_rep CURLYR\n    \n        funcion : FUNC tipo_func ID np_set_scope_ PARENTHESESL funcion_param np_add_func_to_directory_ PARENTHESESR SEMICOLON variables np_add_vars_to_table_ CURLYL estatuto_rep CURLYR\n    \n        np_set_scope_ :\n    \n        np_add_func_to_directory_ :\n    \n        np_add_vars_to_table_ :\n    \n        tipo_func : tipo\n        | VOID\n    \n        funcion_param : tipo ID funcion_param_rep\n        | empty\n    \n        funcion_param_rep : COMMA funcion_param\n        | empty\n    \n        estatuto_rep : estatuto estatuto_rep\n        | empty\n    \n        estatuto : asignacion SEMICOLON\n        | llamada SEMICOLON\n        | retorno SEMICOLON\n        | lectura SEMICOLON\n        | escritura SEMICOLON\n        | decision\n        | rep_c\n        | rep_nc\n    \n        np_quadruple_assignment_ :\n    \n        np_quadruple_IO_ :\n    \n        np_push_var_ :\n    \n        np_push_operator_ :\n    \n        np_pop_operator_ :\n    \n        asignacion : ID np_push_var_ dimension ASSIGN np_push_operator_ expresion np_quadruple_assignment_\n    \n        dimension : SQUAREL np_add_false_bottom_ expresion np_pop_dimension_ np_remove_false_bottom_ SQUARER\n        | empty\n    \n        np_pop_dimension_ :\n    \n        llamada : ID PARENTHESESL expresion_rep PARENTHESESR\n    \n        lectura : READ np_push_operator_ PARENTHESESL lista_lectura PARENTHESESR np_pop_operator_\n    \n        lista_lectura : ID np_push_var_ dimension np_quadruple_IO_ COMMA lista_lectura\n        | ID np_push_var_ dimension np_quadruple_IO_\n    \n        escritura : PRINT np_push_operator_ PARENTHESESL lista_escritura PARENTHESESR np_pop_operator_\n    \n        lista_escritura : letrero np_quadruple_IO_ lista_escritura_rep\n        | expresion np_quadruple_IO_ lista_escritura_rep\n    \n        lista_escritura_rep : COMMA lista_escritura\n        | empty\n    \n        decision : IF PARENTHESESL expresion PARENTHESESR np_gotoF_ THEN CURLYL estatuto_rep CURLYR decision_alt\n    \n        decision_alt : ELSE np_false_condition_ CURLYL estatuto_rep CURLYR np_end_if_actions\n        | empty np_end_if_actions\n    \n        np_gotoF_ :\n    \n        np_false_condition_ :\n    \n        np_end_if_actions :\n    \n        rep_c : WHILE np_push_jump_ PARENTHESESL expresion PARENTHESESR np_gotoF_ DO CURLYL estatuto_rep CURLYR np_end_while_actions_\n    \n        np_push_jump_ :\n    \n        np_end_while_actions_ :\n    \n        rep_nc : FROM expresion np_assign_temp_ UNTIL expresion np_quadruple_for_ np_gotoF_ DO CURLYL estatuto_rep CURLYR np_end_for_actions\n    \n        np_assign_temp_ :\n    \n        np_quadruple_for_ : np_push_jump_\n    \n        np_end_for_actions : np_increment_temp_ np_end_while_actions_\n    \n        np_increment_temp_ :\n    \n        expresion_rep : expresion_rep_2\n        | empty\n    \n        expresion_rep_2 : expresion COMMA expresion_rep_2\n        | expresion\n    \n        retorno : RETURN PARENTHESESL expresion PARENTHESESR np_quadruple_return_\n    \n        np_quadruple_return_ :\n    \n        expresion : exp_comp np_quadruple_logic_ expresion_2\n    \n        expresion_2 : AND np_push_operator_ expresion\n        | OR np_push_operator_ expresion\n        | empty\n    \n        np_quadruple_logic_ :\n    \n        exp_comp : exp_ar exp_comp_2\n    \n        exp_comp_2 : comp_sym np_push_operator_ exp_ar np_quadruple_compare_\n        | empty\n    \n        np_quadruple_compare_ :\n    \n        comp_sym : LESSTHAN\n        | GREATERTHAN\n        | LESSEQUAL\n        | GREATEREQUAL\n        | EQUAL\n        | NOTEQUAL\n    \n        exp_ar : termino np_quadruple_term exp_ar_2\n    \n        exp_ar_2 : PLUS np_push_operator_ exp_ar\n        | MINUS np_push_operator_ exp_ar\n        | empty\n    \n        np_quadruple_term :\n    \n        termino : unary np_quadruple_factor_ termino_2\n    \n        termino_2 : MULT np_push_operator_ termino\n        | DIVIDE np_push_operator_ termino\n        | empty\n    \n        np_quadruple_factor_ :\n    \n        unary : factor\n        | MINUS np_push_operator_ unary change_sign\n        | PLUS unary\n    \n        change_sign :\n    \n        factor : const\n        | ID np_push_var_ dimension\n        | PARENTHESESL np_add_false_bottom_ expresion PARENTHESESR np_remove_false_bottom_\n        | llamada\n    \n        np_add_false_bottom_ :\n    \n        np_remove_false_bottom_ :\n    \n        const : CTE_INT np_push_const_int_\n        | letrero\n        | CTE_FLOAT np_push_const_float_\n    \n        np_push_const_int_ :\n    \n        np_push_const_char_ :\n    \n        np_push_const_float_ :\n    \n        np_push_const_string_ :\n    \n        letrero : CTE_STR np_push_const_string_\n    \n        empty :\n    \n        np_check :\n    '
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,19,67,],[0,-1,-18,]),'ID':([2,11,12,13,18,22,23,24,39,42,47,54,55,56,63,65,69,70,71,72,73,75,76,79,87,88,91,100,107,108,110,114,116,117,118,119,120,121,124,127,135,136,138,147,149,150,152,154,155,158,159,166,178,179,181,182,183,184,194,214,217,219,221,225,227,229,231,232,235,236,237,238,239,240,242,243,244,],[3,-15,-16,-17,26,28,-23,-24,26,57,57,-36,-37,-38,90,98,-31,-32,-33,-34,-35,90,90,90,-42,90,-110,-110,141,90,90,-42,-86,-87,-88,-89,-90,-91,90,90,-42,90,90,90,-42,-42,90,-42,-42,-42,-42,90,90,90,90,90,90,90,90,57,57,141,57,-120,57,-57,-62,-65,-59,-63,-70,57,-66,-65,-69,-62,-58,]),'SEMICOLON':([3,25,26,30,32,38,40,44,45,49,50,51,52,53,82,83,84,85,86,89,90,92,93,94,95,96,101,112,113,115,122,123,125,126,128,129,130,131,137,139,148,151,153,156,157,160,161,162,169,170,172,180,185,186,188,190,192,201,202,203,204,205,206,207,208,210,218,],[4,29,-120,-120,-14,-10,-12,-11,-13,69,70,71,72,73,-81,-120,-96,-101,-102,-106,-41,-109,-115,-113,-117,-118,-46,-120,-82,-84,-120,-120,-104,-120,-112,-114,-119,164,-48,-76,-77,-80,-92,-95,-97,-100,-105,-107,-75,-43,-43,-85,-103,-111,-39,-49,-52,-78,-79,-83,-93,-94,-98,-99,-108,-44,-45,]),'VAR':([4,164,],[6,6,]),'FUNC':([4,5,7,8,9,15,29,35,36,37,228,],[-120,-2,-6,17,-5,17,-120,-7,-8,-9,-19,]),'PRINCIPAL':([4,5,7,8,9,14,15,16,21,29,35,36,37,228,],[-120,-2,-6,-120,-5,20,-120,-4,-3,-120,-7,-8,-9,-19,]),'INT':([6,17,29,43,133,],[11,11,11,11,11,]),'FLOAT':([6,17,29,43,133,],[12,12,12,12,12,]),'STRING':([6,17,29,43,133,],[13,13,13,13,13,]),'CURLYL':([7,9,29,33,35,36,37,164,187,197,209,215,222,230,234,],[-6,-5,-120,42,-7,-8,-9,-120,-22,214,217,221,227,-61,238,]),'COLON':([10,11,12,13,],[18,-15,-16,-17,]),'VOID':([17,],[24,]),'PARENTHESESL':([20,28,34,57,58,59,60,61,62,63,75,76,77,78,79,80,87,88,90,91,100,108,110,114,116,117,118,119,120,121,124,127,135,136,138,147,149,150,152,154,155,158,159,166,178,179,181,182,183,184,194,],[27,-20,43,75,76,-42,-42,79,-64,91,91,91,107,108,91,110,-42,91,75,-110,-110,91,91,-42,-86,-87,-88,-89,-90,-91,91,91,-42,91,91,91,-42,-42,91,-42,-42,-42,-42,91,91,91,91,91,91,91,91,]),'SQUAREL':([26,57,74,90,126,141,171,],[31,-41,100,-41,100,-41,100,]),'COMMA':([26,30,32,45,82,83,84,85,86,89,90,92,93,94,95,96,98,101,105,112,113,115,122,123,125,126,128,129,130,137,141,143,144,148,151,153,156,157,160,161,162,171,173,174,180,185,186,191,201,202,203,204,205,206,207,208,212,218,],[-120,39,-14,-13,-81,-120,-96,-101,-102,-106,-41,-109,-115,-113,-117,-118,133,-46,138,-120,-82,-84,-120,-120,-104,-120,-112,-114,-119,-48,-41,-40,-40,-77,-80,-92,-95,-97,-100,-105,-107,-120,194,194,-85,-103,-111,-40,-78,-79,-83,-93,-94,-98,-99,-108,219,-45,]),'PARENTHESESR':([27,43,64,66,75,82,83,84,85,86,89,90,92,93,94,95,96,97,98,101,102,103,104,105,106,109,112,113,115,122,123,125,126,128,129,130,132,133,134,137,140,141,142,143,144,146,148,151,153,156,157,160,161,162,163,165,168,171,173,174,180,185,186,191,193,195,196,201,202,203,204,205,206,207,208,212,213,218,224,],[33,-120,-21,-26,-120,-81,-120,-96,-101,-102,-106,-41,-109,-115,-113,-117,-118,131,-120,-46,137,-71,-72,-74,139,145,-120,-82,-84,-120,-120,-104,-120,-112,-114,-119,-25,-120,-28,-48,170,-41,172,-40,-40,176,-77,-80,-92,-95,-97,-100,-105,-107,186,-27,-73,-120,-120,-120,-85,-103,-111,-40,-53,-56,-54,-78,-79,-83,-93,-94,-98,-99,-108,-51,-55,-45,-50,]),'CTE_INT':([31,63,75,76,79,87,88,91,100,108,110,114,116,117,118,119,120,121,124,127,135,136,138,147,149,150,152,154,155,158,159,166,178,179,181,182,183,184,194,],[41,93,93,93,93,-42,93,-110,-110,93,93,-42,-86,-87,-88,-89,-90,-91,93,93,-42,93,93,93,-42,-42,93,-42,-42,-42,-42,93,93,93,93,93,93,93,93,]),'SQUARER':([41,82,83,84,85,86,89,90,92,93,94,95,96,101,112,113,115,122,123,125,126,128,129,130,137,148,151,153,156,157,160,161,162,167,180,185,186,189,201,202,203,204,205,206,207,208,211,218,],[45,-81,-120,-96,-101,-102,-106,-41,-109,-115,-113,-117,-118,-46,-120,-82,-84,-120,-120,-104,-120,-112,-114,-119,-48,-77,-80,-92,-95,-97,-100,-105,-107,-47,-85,-103,-111,-111,-78,-79,-83,-93,-94,-98,-99,-108,218,-45,]),'CURLYR':([42,46,47,48,54,55,56,68,69,70,71,72,73,214,217,220,221,223,225,226,227,229,231,232,233,235,236,237,238,239,240,241,242,243,244,],[-120,67,-120,-30,-36,-37,-38,-29,-31,-32,-33,-34,-35,-120,-120,225,-120,228,-120,232,-120,-57,-62,-65,237,-59,-63,-70,-120,-66,-65,243,-69,-62,-58,]),'RETURN':([42,47,54,55,56,69,70,71,72,73,214,217,221,225,227,229,231,232,235,236,237,238,239,240,242,243,244,],[58,58,-36,-37,-38,-31,-32,-33,-34,-35,58,58,58,-120,58,-57,-62,-65,-59,-63,-70,58,-66,-65,-69,-62,-58,]),'READ':([42,47,54,55,56,69,70,71,72,73,214,217,221,225,227,229,231,232,235,236,237,238,239,240,242,243,244,],[59,59,-36,-37,-38,-31,-32,-33,-34,-35,59,59,59,-120,59,-57,-62,-65,-59,-63,-70,59,-66,-65,-69,-62,-58,]),'PRINT':([42,47,54,55,56,69,70,71,72,73,214,217,221,225,227,229,231,232,235,236,237,238,239,240,242,243,244,],[60,60,-36,-37,-38,-31,-32,-33,-34,-35,60,60,60,-120,60,-57,-62,-65,-59,-63,-70,60,-66,-65,-69,-62,-58,]),'IF':([42,47,54,55,56,69,70,71,72,73,214,217,221,225,227,229,231,232,235,236,237,238,239,240,242,243,244,],[61,61,-36,-37,-38,-31,-32,-33,-34,-35,61,61,61,-120,61,-57,-62,-65,-59,-63,-70,61,-66,-65,-69,-62,-58,]),'WHILE':([42,47,54,55,56,69,70,71,72,73,214,217,221,225,227,229,231,232,235,236,237,238,239,240,242,243,244,],[62,62,-36,-37,-38,-31,-32,-33,-34,-35,62,62,62,-120,62,-57,-62,-65,-59,-63,-70,62,-66,-65,-69,-62,-58,]),'FROM':([42,47,54,55,56,69,70,71,72,73,214,217,221,225,227,229,231,232,235,236,237,238,239,240,242,243,244,],[63,63,-36,-37,-38,-31,-32,-33,-34,-35,63,63,63,-120,63,-57,-62,-65,-59,-63,-70,63,-66,-65,-69,-62,-58,]),'ASSIGN':([57,74,99,101,218,],[-41,-120,135,-46,-45,]),'MINUS':([63,75,76,79,84,85,86,87,88,89,90,91,92,93,94,95,96,100,101,108,110,114,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,135,136,137,138,143,147,149,150,152,154,155,157,158,159,160,161,162,166,178,179,181,182,183,184,185,186,194,206,207,208,218,],[87,87,87,87,-96,-101,-102,-42,87,-106,-41,-110,-109,-115,-113,-117,-118,-110,-46,87,87,-42,-86,-87,-88,-89,-90,-91,155,-120,87,-104,-120,87,-112,-114,-119,-42,87,-48,87,-113,87,-42,-42,87,-42,-42,-97,-42,-42,-100,-105,-107,87,87,87,87,87,87,87,-103,-111,87,-98,-99,-108,-45,]),'PLUS':([63,75,76,79,84,85,86,87,88,89,90,91,92,93,94,95,96,100,101,108,110,114,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,135,136,137,138,143,147,149,150,152,154,155,157,158,159,160,161,162,166,178,179,181,182,183,184,185,186,194,206,207,208,218,],[88,88,88,88,-96,-101,-102,-42,88,-106,-41,-110,-109,-115,-113,-117,-118,-110,-46,88,88,-42,-86,-87,-88,-89,-90,-91,154,-120,88,-104,-120,88,-112,-114,-119,-42,88,-48,88,-113,88,-42,-42,88,-42,-42,-97,-42,-42,-100,-105,-107,88,88,88,88,88,88,88,-103,-111,88,-98,-99,-108,-45,]),'CTE_FLOAT':([63,75,76,79,87,88,91,100,108,110,114,116,117,118,119,120,121,124,127,135,136,138,147,149,150,152,154,155,158,159,166,178,179,181,182,183,184,194,],[95,95,95,95,-42,95,-110,-110,95,95,-42,-86,-87,-88,-89,-90,-91,95,95,-42,95,95,95,-42,-42,95,-42,-42,-42,-42,95,95,95,95,95,95,95,95,]),'CTE_STR':([63,75,76,79,87,88,91,100,108,110,114,116,117,118,119,120,121,124,127,135,136,138,147,149,150,152,154,155,158,159,166,178,179,181,182,183,184,194,],[96,96,96,96,-42,96,-110,-110,96,96,-42,-86,-87,-88,-89,-90,-91,96,96,-42,96,96,96,-42,-42,96,-42,-42,-42,-42,96,96,96,96,96,96,96,96,]),'UNTIL':([81,82,83,84,85,86,89,90,92,93,94,95,96,101,111,112,113,115,122,123,125,126,128,129,130,137,148,151,153,156,157,160,161,162,180,185,186,201,202,203,204,205,206,207,208,218,],[-67,-81,-120,-96,-101,-102,-106,-41,-109,-115,-113,-117,-118,-46,147,-120,-82,-84,-120,-120,-104,-120,-112,-114,-119,-48,-77,-80,-92,-95,-97,-100,-105,-107,-85,-103,-111,-78,-79,-83,-93,-94,-98,-99,-108,-45,]),'AND':([82,83,84,85,86,89,90,92,93,94,95,96,101,112,113,115,122,123,125,126,128,129,130,137,143,153,156,157,160,161,162,180,185,186,203,204,205,206,207,208,218,],[-81,-120,-96,-101,-102,-106,-41,-109,-115,-113,-117,-118,-46,149,-82,-84,-120,-120,-104,-120,-112,-114,-119,-48,-113,-92,-95,-97,-100,-105,-107,-85,-103,-111,-83,-93,-94,-98,-99,-108,-45,]),'OR':([82,83,84,85,86,89,90,92,93,94,95,96,101,112,113,115,122,123,125,126,128,129,130,137,143,153,156,157,160,161,162,180,185,186,203,204,205,206,207,208,218,],[-81,-120,-96,-101,-102,-106,-41,-109,-115,-113,-117,-118,-46,150,-82,-84,-120,-120,-104,-120,-112,-114,-119,-48,-113,-92,-95,-97,-100,-105,-107,-85,-103,-111,-83,-93,-94,-98,-99,-108,-45,]),'DO':([82,83,84,85,86,89,90,92,93,94,95,96,101,112,113,115,122,123,125,126,128,129,130,137,148,151,153,156,157,160,161,162,176,177,180,185,186,198,199,200,201,202,203,204,205,206,207,208,216,218,],[-81,-120,-96,-101,-102,-106,-41,-109,-115,-113,-117,-118,-46,-120,-82,-84,-120,-120,-104,-120,-112,-114,-119,-48,-77,-80,-92,-95,-97,-100,-105,-107,-60,-64,-85,-103,-111,215,-60,-68,-78,-79,-83,-93,-94,-98,-99,-108,222,-45,]),'LESSTHAN':([83,84,85,86,89,90,92,93,94,95,96,101,122,123,125,126,128,129,130,137,143,153,156,157,160,161,162,185,186,204,205,206,207,208,218,],[116,-96,-101,-102,-106,-41,-109,-115,-113,-117,-118,-46,-120,-120,-104,-120,-112,-114,-119,-48,-113,-92,-95,-97,-100,-105,-107,-103,-111,-93,-94,-98,-99,-108,-45,]),'GREATERTHAN':([83,84,85,86,89,90,92,93,94,95,96,101,122,123,125,126,128,129,130,137,143,153,156,157,160,161,162,185,186,204,205,206,207,208,218,],[117,-96,-101,-102,-106,-41,-109,-115,-113,-117,-118,-46,-120,-120,-104,-120,-112,-114,-119,-48,-113,-92,-95,-97,-100,-105,-107,-103,-111,-93,-94,-98,-99,-108,-45,]),'LESSEQUAL':([83,84,85,86,89,90,92,93,94,95,96,101,122,123,125,126,128,129,130,137,143,153,156,157,160,161,162,185,186,204,205,206,207,208,218,],[118,-96,-101,-102,-106,-41,-109,-115,-113,-117,-118,-46,-120,-120,-104,-120,-112,-114,-119,-48,-113,-92,-95,-97,-100,-105,-107,-103,-111,-93,-94,-98,-99,-108,-45,]),'GREATEREQUAL':([83,84,85,86,89,90,92,93,94,95,96,101,122,123,125,126,128,129,130,137,143,153,156,157,160,161,162,185,186,204,205,206,207,208,218,],[119,-96,-101,-102,-106,-41,-109,-115,-113,-117,-118,-46,-120,-120,-104,-120,-112,-114,-119,-48,-113,-92,-95,-97,-100,-105,-107,-103,-111,-93,-94,-98,-99,-108,-45,]),'EQUAL':([83,84,85,86,89,90,92,93,94,95,96,101,122,123,125,126,128,129,130,137,143,153,156,157,160,161,162,185,186,204,205,206,207,208,218,],[120,-96,-101,-102,-106,-41,-109,-115,-113,-117,-118,-46,-120,-120,-104,-120,-112,-114,-119,-48,-113,-92,-95,-97,-100,-105,-107,-103,-111,-93,-94,-98,-99,-108,-45,]),'NOTEQUAL':([83,84,85,86,89,90,92,93,94,95,96,101,122,123,125,126,128,129,130,137,143,153,156,157,160,161,162,185,186,204,205,206,207,208,218,],[121,-96,-101,-102,-106,-41,-109,-115,-113,-117,-118,-46,-120,-120,-104,-120,-112,-114,-119,-48,-113,-92,-95,-97,-100,-105,-107,-103,-111,-93,-94,-98,-99,-108,-45,]),'MULT':([85,86,89,90,92,93,94,95,96,101,123,125,126,128,129,130,137,143,161,162,185,186,208,218,],[-101,-102,-106,-41,-109,-115,-113,-117,-118,-46,158,-104,-120,-112,-114,-119,-48,-113,-105,-107,-103,-111,-108,-45,]),'DIVIDE':([85,86,89,90,92,93,94,95,96,101,123,125,126,128,129,130,137,143,161,162,185,186,208,218,],[-101,-102,-106,-41,-109,-115,-113,-117,-118,-46,159,-104,-120,-112,-114,-119,-48,-113,-105,-107,-103,-111,-108,-45,]),'THEN':([145,175,],[-60,197,]),'ELSE':([225,],[230,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'prog':([0,],[1,]),'variables':([4,164,],[5,187,]),'empty':([4,8,15,26,29,30,42,43,47,74,75,83,98,112,122,123,126,133,164,171,173,174,214,217,221,225,227,238,],[7,16,16,32,37,40,48,66,48,101,104,115,134,151,156,160,101,66,7,101,195,195,48,48,48,231,48,48,]),'np_push_global_vars_':([5,],[8,]),'variables_2':([6,29,],[9,36,]),'tipo':([6,17,29,43,133,],[10,23,10,65,65,]),'prog_funcs':([8,15,],[14,21,]),'funcion':([8,15,],[15,15,]),'func_princ':([14,],[19,]),'tipo_func':([17,],[22,]),'lista_id':([18,39,],[25,44,]),'dimension_var':([26,],[30,]),'np_set_scope_':([28,],[34,]),'variables_rep':([29,],[35,]),'lista_id_rep':([30,],[38,]),'estatuto_rep':([42,47,214,217,221,227,238,],[46,68,220,223,226,233,241,]),'estatuto':([42,47,214,217,221,227,238,],[47,47,47,47,47,47,47,]),'asignacion':([42,47,214,217,221,227,238,],[49,49,49,49,49,49,49,]),'llamada':([42,47,63,75,76,79,88,108,110,124,127,136,138,147,152,166,178,179,181,182,183,184,194,214,217,221,227,238,],[50,50,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,50,50,50,50,50,]),'retorno':([42,47,214,217,221,227,238,],[51,51,51,51,51,51,51,]),'lectura':([42,47,214,217,221,227,238,],[52,52,52,52,52,52,52,]),'escritura':([42,47,214,217,221,227,238,],[53,53,53,53,53,53,53,]),'decision':([42,47,214,217,221,227,238,],[54,54,54,54,54,54,54,]),'rep_c':([42,47,214,217,221,227,238,],[55,55,55,55,55,55,55,]),'rep_nc':([42,47,214,217,221,227,238,],[56,56,56,56,56,56,56,]),'funcion_param':([43,133,],[64,165,]),'np_push_var_':([57,90,141,],[74,126,171,]),'np_push_operator_':([59,60,87,114,135,149,150,154,155,158,159,],[77,78,124,152,166,178,179,181,182,183,184,]),'np_push_jump_':([62,177,],[80,200,]),'expresion':([63,75,76,79,108,110,127,136,138,147,166,178,179,194,],[81,105,106,109,144,146,163,167,105,177,188,201,202,144,]),'exp_comp':([63,75,76,79,108,110,127,136,138,147,166,178,179,194,],[82,82,82,82,82,82,82,82,82,82,82,82,82,82,]),'exp_ar':([63,75,76,79,108,110,127,136,138,147,152,166,178,179,181,182,194,],[83,83,83,83,83,83,83,83,83,83,180,83,83,83,204,205,83,]),'termino':([63,75,76,79,108,110,127,136,138,147,152,166,178,179,181,182,183,184,194,],[84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,206,207,84,]),'unary':([63,75,76,79,88,108,110,124,127,136,138,147,152,166,178,179,181,182,183,184,194,],[85,85,85,85,125,85,85,161,85,85,85,85,85,85,85,85,85,85,85,85,85,]),'factor':([63,75,76,79,88,108,110,124,127,136,138,147,152,166,178,179,181,182,183,184,194,],[86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,]),'const':([63,75,76,79,88,108,110,124,127,136,138,147,152,166,178,179,181,182,183,184,194,],[89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,]),'letrero':([63,75,76,79,88,108,110,124,127,136,138,147,152,166,178,179,181,182,183,184,194,],[94,94,94,94,94,143,94,94,94,94,94,94,94,94,94,94,94,94,94,94,143,]),'np_add_func_to_directory_':([64,],[97,]),'dimension':([74,126,171,],[99,162,191,]),'expresion_rep':([75,],[102,]),'expresion_rep_2':([75,138,],[103,168,]),'np_assign_temp_':([81,],[111,]),'np_quadruple_logic_':([82,],[112,]),'exp_comp_2':([83,],[113,]),'comp_sym':([83,],[114,]),'np_quadruple_term':([84,],[122,]),'np_quadruple_factor_':([85,],[123,]),'np_add_false_bottom_':([91,100,],[127,136,]),'np_push_const_int_':([93,],[128,]),'np_push_const_float_':([95,],[129,]),'np_push_const_string_':([96,],[130,]),'funcion_param_rep':([98,],[132,]),'lista_lectura':([107,219,],[140,224,]),'lista_escritura':([108,194,],[142,213,]),'expresion_2':([112,],[148,]),'exp_ar_2':([122,],[153,]),'termino_2':([123,],[157,]),'np_quadruple_return_':([139,],[169,]),'np_quadruple_IO_':([143,144,191,],[173,174,212,]),'np_gotoF_':([145,176,199,],[175,198,216,]),'change_sign':([161,],[185,]),'np_pop_dimension_':([167,],[189,]),'np_pop_operator_':([170,172,],[190,192,]),'lista_escritura_rep':([173,174,],[193,196,]),'np_quadruple_for_':([177,],[199,]),'np_quadruple_compare_':([180,],[203,]),'np_remove_false_bottom_':([186,189,],[208,211,]),'np_add_vars_to_table_':([187,],[209,]),'np_quadruple_assignment_':([188,],[210,]),'decision_alt':([225,],[229,]),'np_false_condition_':([230,],[234,]),'np_end_if_actions':([231,243,],[235,244,]),'np_end_while_actions_':([232,240,],[236,242,]),'np_end_for_actions':([237,],[239,]),'np_increment_temp_':([237,],[240,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> prog","S'",1,None,None,None),
  ('prog -> PROGRAM ID SEMICOLON variables np_push_global_vars_ prog_funcs func_princ','prog',7,'p_prog','foreveralone.py',117),
  ('np_push_global_vars_ -> <empty>','np_push_global_vars_',0,'p_np_push_global_vars_','foreveralone.py',128),
  ('prog_funcs -> funcion prog_funcs','prog_funcs',2,'p_prog_funcs','foreveralone.py',136),
  ('prog_funcs -> empty','prog_funcs',1,'p_prog_funcs','foreveralone.py',137),
  ('variables -> VAR variables_2','variables',2,'p_variables','foreveralone.py',142),
  ('variables -> empty','variables',1,'p_variables','foreveralone.py',143),
  ('variables_2 -> tipo COLON lista_id SEMICOLON variables_rep','variables_2',5,'p_variables_2','foreveralone.py',151),
  ('variables_rep -> variables_2','variables_rep',1,'p_variables_rep','foreveralone.py',165),
  ('variables_rep -> empty','variables_rep',1,'p_variables_rep','foreveralone.py',166),
  ('lista_id -> ID dimension_var lista_id_rep','lista_id',3,'p_lista_id','foreveralone.py',173),
  ('lista_id_rep -> COMMA lista_id','lista_id_rep',2,'p_lista_id_rep','foreveralone.py',186),
  ('lista_id_rep -> empty','lista_id_rep',1,'p_lista_id_rep','foreveralone.py',187),
  ('dimension_var -> SQUAREL CTE_INT SQUARER','dimension_var',3,'p_dimension_var','foreveralone.py',197),
  ('dimension_var -> empty','dimension_var',1,'p_dimension_var','foreveralone.py',198),
  ('tipo -> INT','tipo',1,'p_tipo','foreveralone.py',203),
  ('tipo -> FLOAT','tipo',1,'p_tipo','foreveralone.py',204),
  ('tipo -> STRING','tipo',1,'p_tipo','foreveralone.py',205),
  ('func_princ -> PRINCIPAL PARENTHESESL PARENTHESESR CURLYL estatuto_rep CURLYR','func_princ',6,'p_func_princ','foreveralone.py',212),
  ('funcion -> FUNC tipo_func ID np_set_scope_ PARENTHESESL funcion_param np_add_func_to_directory_ PARENTHESESR SEMICOLON variables np_add_vars_to_table_ CURLYL estatuto_rep CURLYR','funcion',14,'p_funcion','foreveralone.py',217),
  ('np_set_scope_ -> <empty>','np_set_scope_',0,'p_np_set_scope_','foreveralone.py',222),
  ('np_add_func_to_directory_ -> <empty>','np_add_func_to_directory_',0,'p_np_add_func_to_directory_','foreveralone.py',230),
  ('np_add_vars_to_table_ -> <empty>','np_add_vars_to_table_',0,'p_np_add_vars_to_table_','foreveralone.py',247),
  ('tipo_func -> tipo','tipo_func',1,'p_tipo_func','foreveralone.py',257),
  ('tipo_func -> VOID','tipo_func',1,'p_tipo_func','foreveralone.py',258),
  ('funcion_param -> tipo ID funcion_param_rep','funcion_param',3,'p_funcion_param','foreveralone.py',265),
  ('funcion_param -> empty','funcion_param',1,'p_funcion_param','foreveralone.py',266),
  ('funcion_param_rep -> COMMA funcion_param','funcion_param_rep',2,'p_funcion_param_rep','foreveralone.py',280),
  ('funcion_param_rep -> empty','funcion_param_rep',1,'p_funcion_param_rep','foreveralone.py',281),
  ('estatuto_rep -> estatuto estatuto_rep','estatuto_rep',2,'p_estatuto_rep','foreveralone.py',288),
  ('estatuto_rep -> empty','estatuto_rep',1,'p_estatuto_rep','foreveralone.py',289),
  ('estatuto -> asignacion SEMICOLON','estatuto',2,'p_estatuto','foreveralone.py',294),
  ('estatuto -> llamada SEMICOLON','estatuto',2,'p_estatuto','foreveralone.py',295),
  ('estatuto -> retorno SEMICOLON','estatuto',2,'p_estatuto','foreveralone.py',296),
  ('estatuto -> lectura SEMICOLON','estatuto',2,'p_estatuto','foreveralone.py',297),
  ('estatuto -> escritura SEMICOLON','estatuto',2,'p_estatuto','foreveralone.py',298),
  ('estatuto -> decision','estatuto',1,'p_estatuto','foreveralone.py',299),
  ('estatuto -> rep_c','estatuto',1,'p_estatuto','foreveralone.py',300),
  ('estatuto -> rep_nc','estatuto',1,'p_estatuto','foreveralone.py',301),
  ('np_quadruple_assignment_ -> <empty>','np_quadruple_assignment_',0,'p_np_quadruple_assignment_','foreveralone.py',306),
  ('np_quadruple_IO_ -> <empty>','np_quadruple_IO_',0,'p_np_quadruple_IO_','foreveralone.py',314),
  ('np_push_var_ -> <empty>','np_push_var_',0,'p_np_push_var_','foreveralone.py',322),
  ('np_push_operator_ -> <empty>','np_push_operator_',0,'p_np_push_operator_','foreveralone.py',339),
  ('np_pop_operator_ -> <empty>','np_pop_operator_',0,'p_np_pop_operator_','foreveralone.py',349),
  ('asignacion -> ID np_push_var_ dimension ASSIGN np_push_operator_ expresion np_quadruple_assignment_','asignacion',7,'p_asignacion','foreveralone.py',355),
  ('dimension -> SQUAREL np_add_false_bottom_ expresion np_pop_dimension_ np_remove_false_bottom_ SQUARER','dimension',6,'p_dimension','foreveralone.py',362),
  ('dimension -> empty','dimension',1,'p_dimension','foreveralone.py',363),
  ('np_pop_dimension_ -> <empty>','np_pop_dimension_',0,'p_np_pop_dimension_','foreveralone.py',368),
  ('llamada -> ID PARENTHESESL expresion_rep PARENTHESESR','llamada',4,'p_llamada','foreveralone.py',379),
  ('lectura -> READ np_push_operator_ PARENTHESESL lista_lectura PARENTHESESR np_pop_operator_','lectura',6,'p_lectura','foreveralone.py',384),
  ('lista_lectura -> ID np_push_var_ dimension np_quadruple_IO_ COMMA lista_lectura','lista_lectura',6,'p_lista_lectura','foreveralone.py',389),
  ('lista_lectura -> ID np_push_var_ dimension np_quadruple_IO_','lista_lectura',4,'p_lista_lectura','foreveralone.py',390),
  ('escritura -> PRINT np_push_operator_ PARENTHESESL lista_escritura PARENTHESESR np_pop_operator_','escritura',6,'p_escritura','foreveralone.py',395),
  ('lista_escritura -> letrero np_quadruple_IO_ lista_escritura_rep','lista_escritura',3,'p_lista_escritura','foreveralone.py',400),
  ('lista_escritura -> expresion np_quadruple_IO_ lista_escritura_rep','lista_escritura',3,'p_lista_escritura','foreveralone.py',401),
  ('lista_escritura_rep -> COMMA lista_escritura','lista_escritura_rep',2,'p_lista_escritura_rep','foreveralone.py',406),
  ('lista_escritura_rep -> empty','lista_escritura_rep',1,'p_lista_escritura_rep','foreveralone.py',407),
  ('decision -> IF PARENTHESESL expresion PARENTHESESR np_gotoF_ THEN CURLYL estatuto_rep CURLYR decision_alt','decision',10,'p_decision','foreveralone.py',412),
  ('decision_alt -> ELSE np_false_condition_ CURLYL estatuto_rep CURLYR np_end_if_actions','decision_alt',6,'p_decision_alt','foreveralone.py',417),
  ('decision_alt -> empty np_end_if_actions','decision_alt',2,'p_decision_alt','foreveralone.py',418),
  ('np_gotoF_ -> <empty>','np_gotoF_',0,'p_np_gotoF_','foreveralone.py',423),
  ('np_false_condition_ -> <empty>','np_false_condition_',0,'p_np_false_condition_','foreveralone.py',433),
  ('np_end_if_actions -> <empty>','np_end_if_actions',0,'p_np_end_if_actions','foreveralone.py',442),
  ('rep_c -> WHILE np_push_jump_ PARENTHESESL expresion PARENTHESESR np_gotoF_ DO CURLYL estatuto_rep CURLYR np_end_while_actions_','rep_c',11,'p_rep_c','foreveralone.py',449),
  ('np_push_jump_ -> <empty>','np_push_jump_',0,'p_np_push_jump_','foreveralone.py',454),
  ('np_end_while_actions_ -> <empty>','np_end_while_actions_',0,'p_np_end_while_actions_','foreveralone.py',460),
  ('rep_nc -> FROM expresion np_assign_temp_ UNTIL expresion np_quadruple_for_ np_gotoF_ DO CURLYL estatuto_rep CURLYR np_end_for_actions','rep_nc',12,'p_rep_nc','foreveralone.py',469),
  ('np_assign_temp_ -> <empty>','np_assign_temp_',0,'p_np_assign_temp_','foreveralone.py',474),
  ('np_quadruple_for_ -> np_push_jump_','np_quadruple_for_',1,'p_np_quadruple_for_','foreveralone.py',480),
  ('np_end_for_actions -> np_increment_temp_ np_end_while_actions_','np_end_for_actions',2,'p_np_end_for_actions','foreveralone.py',501),
  ('np_increment_temp_ -> <empty>','np_increment_temp_',0,'p_np_increment_temp_','foreveralone.py',506),
  ('expresion_rep -> expresion_rep_2','expresion_rep',1,'p_expresion_rep','foreveralone.py',512),
  ('expresion_rep -> empty','expresion_rep',1,'p_expresion_rep','foreveralone.py',513),
  ('expresion_rep_2 -> expresion COMMA expresion_rep_2','expresion_rep_2',3,'p_expresion_rep_2','foreveralone.py',518),
  ('expresion_rep_2 -> expresion','expresion_rep_2',1,'p_expresion_rep_2','foreveralone.py',519),
  ('retorno -> RETURN PARENTHESESL expresion PARENTHESESR np_quadruple_return_','retorno',5,'p_retorno','foreveralone.py',524),
  ('np_quadruple_return_ -> <empty>','np_quadruple_return_',0,'p_np_quadruple_return_','foreveralone.py',529),
  ('expresion -> exp_comp np_quadruple_logic_ expresion_2','expresion',3,'p_expresion','foreveralone.py',535),
  ('expresion_2 -> AND np_push_operator_ expresion','expresion_2',3,'p_expresion_2','foreveralone.py',546),
  ('expresion_2 -> OR np_push_operator_ expresion','expresion_2',3,'p_expresion_2','foreveralone.py',547),
  ('expresion_2 -> empty','expresion_2',1,'p_expresion_2','foreveralone.py',548),
  ('np_quadruple_logic_ -> <empty>','np_quadruple_logic_',0,'p_np_quadruple_logic_','foreveralone.py',553),
  ('exp_comp -> exp_ar exp_comp_2','exp_comp',2,'p_exp_comp','foreveralone.py',561),
  ('exp_comp_2 -> comp_sym np_push_operator_ exp_ar np_quadruple_compare_','exp_comp_2',4,'p_exp_comp_2','foreveralone.py',566),
  ('exp_comp_2 -> empty','exp_comp_2',1,'p_exp_comp_2','foreveralone.py',567),
  ('np_quadruple_compare_ -> <empty>','np_quadruple_compare_',0,'p_np_quadruple_compare_','foreveralone.py',572),
  ('comp_sym -> LESSTHAN','comp_sym',1,'p_comp_sym','foreveralone.py',582),
  ('comp_sym -> GREATERTHAN','comp_sym',1,'p_comp_sym','foreveralone.py',583),
  ('comp_sym -> LESSEQUAL','comp_sym',1,'p_comp_sym','foreveralone.py',584),
  ('comp_sym -> GREATEREQUAL','comp_sym',1,'p_comp_sym','foreveralone.py',585),
  ('comp_sym -> EQUAL','comp_sym',1,'p_comp_sym','foreveralone.py',586),
  ('comp_sym -> NOTEQUAL','comp_sym',1,'p_comp_sym','foreveralone.py',587),
  ('exp_ar -> termino np_quadruple_term exp_ar_2','exp_ar',3,'p_exp_ar','foreveralone.py',593),
  ('exp_ar_2 -> PLUS np_push_operator_ exp_ar','exp_ar_2',3,'p_exp_ar_2','foreveralone.py',598),
  ('exp_ar_2 -> MINUS np_push_operator_ exp_ar','exp_ar_2',3,'p_exp_ar_2','foreveralone.py',599),
  ('exp_ar_2 -> empty','exp_ar_2',1,'p_exp_ar_2','foreveralone.py',600),
  ('np_quadruple_term -> <empty>','np_quadruple_term',0,'p_np_quadruple_term','foreveralone.py',605),
  ('termino -> unary np_quadruple_factor_ termino_2','termino',3,'p_termino','foreveralone.py',613),
  ('termino_2 -> MULT np_push_operator_ termino','termino_2',3,'p_termino_2','foreveralone.py',618),
  ('termino_2 -> DIVIDE np_push_operator_ termino','termino_2',3,'p_termino_2','foreveralone.py',619),
  ('termino_2 -> empty','termino_2',1,'p_termino_2','foreveralone.py',620),
  ('np_quadruple_factor_ -> <empty>','np_quadruple_factor_',0,'p_np_quadruple_factor_','foreveralone.py',625),
  ('unary -> factor','unary',1,'p_unary','foreveralone.py',634),
  ('unary -> MINUS np_push_operator_ unary change_sign','unary',4,'p_unary','foreveralone.py',635),
  ('unary -> PLUS unary','unary',2,'p_unary','foreveralone.py',636),
  ('change_sign -> <empty>','change_sign',0,'p_change_sign','foreveralone.py',642),
  ('factor -> const','factor',1,'p_factor','foreveralone.py',649),
  ('factor -> ID np_push_var_ dimension','factor',3,'p_factor','foreveralone.py',650),
  ('factor -> PARENTHESESL np_add_false_bottom_ expresion PARENTHESESR np_remove_false_bottom_','factor',5,'p_factor','foreveralone.py',651),
  ('factor -> llamada','factor',1,'p_factor','foreveralone.py',652),
  ('np_add_false_bottom_ -> <empty>','np_add_false_bottom_',0,'p_np_add_false_bottom_','foreveralone.py',657),
  ('np_remove_false_bottom_ -> <empty>','np_remove_false_bottom_',0,'p_np_remove_false_bottom_','foreveralone.py',667),
  ('const -> CTE_INT np_push_const_int_','const',2,'p_const','foreveralone.py',680),
  ('const -> letrero','const',1,'p_const','foreveralone.py',681),
  ('const -> CTE_FLOAT np_push_const_float_','const',2,'p_const','foreveralone.py',682),
  ('np_push_const_int_ -> <empty>','np_push_const_int_',0,'p_np_push_const_int_','foreveralone.py',687),
  ('np_push_const_char_ -> <empty>','np_push_const_char_',0,'p_np_push_const_char_','foreveralone.py',698),
  ('np_push_const_float_ -> <empty>','np_push_const_float_',0,'p_np_push_const_float_','foreveralone.py',709),
  ('np_push_const_string_ -> <empty>','np_push_const_string_',0,'p_np_push_const_string_','foreveralone.py',720),
  ('letrero -> CTE_STR np_push_const_string_','letrero',2,'p_letrero','foreveralone.py',731),
  ('empty -> <empty>','empty',0,'p_empty','foreveralone.py',736),
  ('np_check -> <empty>','np_check',0,'p_np_check','foreveralone.py',741),
]
