
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASSIGN COLON COMMA CTE_FLOAT CTE_INT CTE_STR CURLYL CURLYR DIVIDE DO ELSE EQUAL FLOAT FROM FUNC GREATEREQUAL GREATERTHAN ID IF INT LESSEQUAL LESSTHAN MINUS MULT NOTEQUAL OR PARENTHESESL PARENTHESESR PLUS PRINCIPAL PRINT PROGRAM READ RETURN SEMICOLON SQUAREL SQUARER STRING THEN UNTIL VAR VOID WHILE\n        prog : PROGRAM ID np_goto_ SEMICOLON variables np_push_global_vars_ prog_funcs func_princ\n    \n        np_goto_ :\n    \n        np_push_global_vars_ :\n    \n        prog_funcs : funcion prog_funcs\n        | empty\n    \n        variables : VAR variables_2\n        | empty\n    \n        variables_2 : tipo COLON lista_id SEMICOLON variables_rep\n    \n        variables_rep : variables_2\n        | empty\n    \n        lista_id : ID dimension_var lista_id_rep\n    \n        lista_id_rep : COMMA lista_id\n        | empty\n    \n        dimension_var : SQUAREL CTE_INT SQUARER\n        | empty\n    \n        tipo : INT\n        | FLOAT\n        | STRING\n    \n        func_princ : PRINCIPAL np_start_main_ PARENTHESESL PARENTHESESR CURLYL estatuto_rep CURLYR\n    \n        np_start_main_ :\n    \n        funcion : FUNC tipo_func ID np_set_scope_ PARENTHESESL funcion_param np_add_func_to_directory_ PARENTHESESR SEMICOLON variables np_add_vars_to_table_ CURLYL estatuto_rep CURLYR\n    \n        np_set_scope_ :\n    \n        np_add_func_to_directory_ :\n    \n        np_add_vars_to_table_ :\n    \n        tipo_func : tipo\n        | VOID\n    \n        funcion_param : tipo ID funcion_param_rep\n        | empty\n    \n        funcion_param_rep : COMMA funcion_param\n        | empty\n    \n        estatuto_rep : estatuto estatuto_rep\n        | empty\n    \n        estatuto : asignacion SEMICOLON\n        | llamada SEMICOLON\n        | retorno SEMICOLON\n        | lectura SEMICOLON\n        | escritura SEMICOLON\n        | decision\n        | rep_c\n        | rep_nc\n    \n        np_quadruple_assignment_ :\n    \n        np_quadruple_IO_ :\n    \n        np_push_var_ :\n    \n        np_push_operator_ :\n    \n        np_pop_operator_ :\n    \n        asignacion : ID np_push_var_ dimension ASSIGN np_push_operator_ expresion np_quadruple_assignment_\n    \n        dimension : SQUAREL np_verify_dimensions_ np_add_false_bottom_ expresion np_manage_array_ np_remove_false_bottom_ SQUARER\n        | empty\n    \n        np_verify_dimensions_ :\n    \n        np_manage_array_ :\n    \n        llamada : ID PARENTHESESL expresion_rep PARENTHESESR\n    \n        lectura : READ np_push_operator_ PARENTHESESL lista_lectura PARENTHESESR np_pop_operator_\n    \n        lista_lectura : ID np_push_var_ dimension np_quadruple_IO_ COMMA lista_lectura\n        | ID np_push_var_ dimension np_quadruple_IO_\n    \n        escritura : PRINT np_push_operator_ PARENTHESESL lista_escritura PARENTHESESR np_pop_operator_\n    \n        lista_escritura : letrero np_quadruple_IO_ lista_escritura_rep\n        | expresion np_quadruple_IO_ lista_escritura_rep\n    \n        lista_escritura_rep : COMMA lista_escritura\n        | empty\n    \n        decision : IF PARENTHESESL expresion PARENTHESESR np_gotoF_ THEN CURLYL estatuto_rep CURLYR decision_alt\n    \n        decision_alt : ELSE np_false_condition_ CURLYL estatuto_rep CURLYR np_end_if_actions\n        | empty np_end_if_actions\n    \n        np_gotoF_ :\n    \n        np_false_condition_ :\n    \n        np_end_if_actions :\n    \n        rep_c : WHILE np_push_jump_ PARENTHESESL expresion PARENTHESESR np_gotoF_ DO CURLYL estatuto_rep CURLYR np_end_while_actions_\n    \n        np_push_jump_ :\n    \n        np_end_while_actions_ :\n    \n        rep_nc : FROM expresion np_assign_temp_ UNTIL expresion np_quadruple_for_ np_gotoF_ DO CURLYL estatuto_rep CURLYR np_end_for_actions\n    \n        np_assign_temp_ :\n    \n        np_quadruple_for_ : np_push_jump_\n    \n        np_end_for_actions : np_increment_temp_ np_end_while_actions_\n    \n        np_increment_temp_ :\n    \n        expresion_rep : expresion_rep_2\n        | empty\n    \n        expresion_rep_2 : expresion COMMA expresion_rep_2\n        | expresion\n    \n        retorno : RETURN PARENTHESESL expresion PARENTHESESR np_quadruple_return_\n    \n        np_quadruple_return_ :\n    \n        expresion : exp_comp np_quadruple_logic_ expresion_2\n    \n        expresion_2 : AND np_push_operator_ expresion\n        | OR np_push_operator_ expresion\n        | empty\n    \n        np_quadruple_logic_ :\n    \n        exp_comp : exp_ar exp_comp_2\n    \n        exp_comp_2 : comp_sym np_push_operator_ exp_ar np_quadruple_compare_\n        | empty\n    \n        np_quadruple_compare_ :\n    \n        comp_sym : LESSTHAN\n        | GREATERTHAN\n        | LESSEQUAL\n        | GREATEREQUAL\n        | EQUAL\n        | NOTEQUAL\n    \n        exp_ar : termino np_quadruple_term exp_ar_2\n    \n        exp_ar_2 : PLUS np_push_operator_ exp_ar\n        | MINUS np_push_operator_ exp_ar\n        | empty\n    \n        np_quadruple_term :\n    \n        termino : unary np_quadruple_factor_ termino_2\n    \n        termino_2 : MULT np_push_operator_ termino\n        | DIVIDE np_push_operator_ termino\n        | empty\n    \n        np_quadruple_factor_ :\n    \n        unary : factor\n        | MINUS np_push_operator_ unary change_sign\n        | PLUS unary\n    \n        change_sign :\n    \n        factor : const\n        | ID np_push_var_ dimension\n        | PARENTHESESL np_add_false_bottom_ expresion PARENTHESESR np_remove_false_bottom_\n        | llamada\n    \n        np_add_false_bottom_ :\n    \n        np_remove_false_bottom_ :\n    \n        const : CTE_INT np_push_const_int_\n        | letrero\n        | CTE_FLOAT np_push_const_float_\n    \n        np_push_const_int_ :\n    \n        np_push_const_float_ :\n    \n        np_push_const_string_ :\n    \n        letrero : CTE_STR np_push_const_string_\n    \n        empty :\n    \n        np_check :\n    '
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,20,71,],[0,-1,-19,]),'ID':([2,12,13,14,19,23,24,25,40,47,49,52,59,60,61,68,73,74,75,76,77,79,80,83,91,92,95,106,113,114,116,120,122,123,124,125,126,127,130,133,139,140,142,151,153,154,156,158,159,162,163,169,170,181,182,184,185,186,187,197,212,217,222,224,229,231,232,234,235,238,239,240,241,242,243,245,246,247,],[3,-16,-17,-18,27,29,-25,-26,27,62,70,62,-38,-39,-40,94,-33,-34,-35,-36,-37,94,94,94,-44,94,-113,-49,145,94,94,-44,-89,-90,-91,-92,-93,-94,94,94,-44,-113,94,94,-44,-44,94,-44,-44,-44,-44,94,94,94,94,94,94,94,94,94,62,62,145,62,-122,62,-60,-65,-68,-62,-66,-73,62,-69,-68,-72,-65,-61,]),'SEMICOLON':([3,4,26,27,31,33,39,41,45,46,54,55,56,57,58,86,87,88,89,90,93,94,96,97,98,99,100,101,107,118,119,121,128,129,131,132,134,135,136,141,143,152,155,157,160,161,164,165,166,172,173,175,183,188,189,191,193,195,204,205,206,207,208,209,210,211,213,227,],[-2,5,30,-122,-122,-15,-11,-13,-12,-14,73,74,75,76,77,-84,-122,-99,-104,-105,-109,-43,-112,-118,-116,-119,-120,137,-48,-122,-85,-87,-122,-122,-107,-122,-115,-117,-121,-51,-79,-80,-83,-95,-98,-100,-103,-108,-110,-78,-45,-45,-88,-106,-114,-41,-52,-55,-81,-82,-86,-96,-97,-101,-102,-111,-46,-47,]),'VAR':([5,137,],[7,7,]),'FUNC':([5,6,8,9,10,16,30,36,37,38,226,],[-122,-3,-7,18,-6,18,-122,-8,-9,-10,-21,]),'PRINCIPAL':([5,6,8,9,10,15,16,17,22,30,36,37,38,226,],[-122,-3,-7,-122,-6,21,-122,-5,-4,-122,-8,-9,-10,-21,]),'INT':([7,18,30,44,103,],[12,12,12,12,12,]),'FLOAT':([7,18,30,44,103,],[13,13,13,13,13,]),'STRING':([7,18,30,44,103,],[14,14,14,14,14,]),'CURLYL':([8,10,30,36,37,38,43,137,168,190,200,218,225,233,237,],[-7,-6,-122,-8,-9,-10,47,-122,-24,212,217,224,231,-64,241,]),'COLON':([11,12,13,14,],[19,-16,-17,-18,]),'VOID':([18,],[25,]),'PARENTHESESL':([21,28,29,35,62,63,64,65,66,67,68,79,80,81,82,83,84,91,92,94,95,106,114,116,120,122,123,124,125,126,127,130,133,139,140,142,151,153,154,156,158,159,162,163,169,170,181,182,184,185,186,187,197,],[-20,34,-22,44,79,80,-44,-44,83,-67,95,95,95,113,114,95,116,-44,95,79,-113,-49,95,95,-44,-89,-90,-91,-92,-93,-94,95,95,-44,-113,95,95,-44,-44,95,-44,-44,-44,-44,95,95,95,95,95,95,95,95,95,]),'SQUAREL':([27,62,78,94,132,145,174,],[32,-43,106,-43,106,-43,106,]),'COMMA':([27,31,33,46,70,86,87,88,89,90,93,94,96,97,98,99,100,107,111,118,119,121,128,129,131,132,134,135,136,141,145,147,148,152,155,157,160,161,164,165,166,174,176,177,183,188,189,194,204,205,206,207,208,209,210,211,215,227,],[-122,40,-15,-14,103,-84,-122,-99,-104,-105,-109,-43,-112,-118,-116,-119,-120,-48,142,-122,-85,-87,-122,-122,-107,-122,-115,-117,-121,-51,-43,-42,-42,-80,-83,-95,-98,-100,-103,-108,-110,-122,197,197,-88,-106,-114,-42,-81,-82,-86,-96,-97,-101,-102,-111,222,-47,]),'CTE_INT':([32,68,79,80,83,91,92,95,106,114,116,120,122,123,124,125,126,127,130,133,139,140,142,151,153,154,156,158,159,162,163,169,170,181,182,184,185,186,187,197,],[42,97,97,97,97,-44,97,-113,-49,97,97,-44,-89,-90,-91,-92,-93,-94,97,97,-44,-113,97,97,-44,-44,97,-44,-44,-44,-44,97,97,97,97,97,97,97,97,97,]),'PARENTHESESR':([34,44,48,50,69,70,79,86,87,88,89,90,93,94,96,97,98,99,100,102,103,104,107,108,109,110,111,112,115,118,119,121,128,129,131,132,134,135,136,138,141,144,145,146,147,148,150,152,155,157,160,161,164,165,166,167,171,174,176,177,183,188,189,194,196,198,199,204,205,206,207,208,209,210,211,215,216,227,228,],[43,-122,-23,-28,101,-122,-122,-84,-122,-99,-104,-105,-109,-43,-112,-118,-116,-119,-120,-27,-122,-30,-48,141,-74,-75,-77,143,149,-122,-85,-87,-122,-122,-107,-122,-115,-117,-121,-29,-51,173,-43,175,-42,-42,179,-80,-83,-95,-98,-100,-103,-108,-110,189,-76,-122,-122,-122,-88,-106,-114,-42,-56,-59,-57,-81,-82,-86,-96,-97,-101,-102,-111,-54,-58,-47,-53,]),'SQUARER':([42,86,87,88,89,90,93,94,96,97,98,99,100,107,118,119,121,128,129,131,132,134,135,136,141,152,155,157,160,161,164,165,166,183,188,189,192,204,205,206,207,208,209,210,211,214,221,227,],[46,-84,-122,-99,-104,-105,-109,-43,-112,-118,-116,-119,-120,-48,-122,-85,-87,-122,-122,-107,-122,-115,-117,-121,-51,-80,-83,-95,-98,-100,-103,-108,-110,-88,-106,-114,-50,-81,-82,-86,-96,-97,-101,-102,-111,-114,227,-47,]),'CURLYR':([47,51,52,53,59,60,61,72,73,74,75,76,77,212,217,220,223,224,229,230,231,232,234,235,236,238,239,240,241,242,243,244,245,246,247,],[-122,71,-122,-32,-38,-39,-40,-31,-33,-34,-35,-36,-37,-122,-122,226,229,-122,-122,235,-122,-60,-65,-68,240,-62,-66,-73,-122,-69,-68,246,-72,-65,-61,]),'RETURN':([47,52,59,60,61,73,74,75,76,77,212,217,224,229,231,232,234,235,238,239,240,241,242,243,245,246,247,],[63,63,-38,-39,-40,-33,-34,-35,-36,-37,63,63,63,-122,63,-60,-65,-68,-62,-66,-73,63,-69,-68,-72,-65,-61,]),'READ':([47,52,59,60,61,73,74,75,76,77,212,217,224,229,231,232,234,235,238,239,240,241,242,243,245,246,247,],[64,64,-38,-39,-40,-33,-34,-35,-36,-37,64,64,64,-122,64,-60,-65,-68,-62,-66,-73,64,-69,-68,-72,-65,-61,]),'PRINT':([47,52,59,60,61,73,74,75,76,77,212,217,224,229,231,232,234,235,238,239,240,241,242,243,245,246,247,],[65,65,-38,-39,-40,-33,-34,-35,-36,-37,65,65,65,-122,65,-60,-65,-68,-62,-66,-73,65,-69,-68,-72,-65,-61,]),'IF':([47,52,59,60,61,73,74,75,76,77,212,217,224,229,231,232,234,235,238,239,240,241,242,243,245,246,247,],[66,66,-38,-39,-40,-33,-34,-35,-36,-37,66,66,66,-122,66,-60,-65,-68,-62,-66,-73,66,-69,-68,-72,-65,-61,]),'WHILE':([47,52,59,60,61,73,74,75,76,77,212,217,224,229,231,232,234,235,238,239,240,241,242,243,245,246,247,],[67,67,-38,-39,-40,-33,-34,-35,-36,-37,67,67,67,-122,67,-60,-65,-68,-62,-66,-73,67,-69,-68,-72,-65,-61,]),'FROM':([47,52,59,60,61,73,74,75,76,77,212,217,224,229,231,232,234,235,238,239,240,241,242,243,245,246,247,],[68,68,-38,-39,-40,-33,-34,-35,-36,-37,68,68,68,-122,68,-60,-65,-68,-62,-66,-73,68,-69,-68,-72,-65,-61,]),'ASSIGN':([62,78,105,107,227,],[-43,-122,139,-48,-47,]),'MINUS':([68,79,80,83,88,89,90,91,92,93,94,95,96,97,98,99,100,106,107,114,116,120,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,139,140,141,142,147,151,153,154,156,158,159,161,162,163,164,165,166,169,170,181,182,184,185,186,187,188,189,197,209,210,211,227,],[91,91,91,91,-99,-104,-105,-44,91,-109,-43,-113,-112,-118,-116,-119,-120,-49,-48,91,91,-44,-89,-90,-91,-92,-93,-94,159,-122,91,-107,-122,91,-115,-117,-121,-44,-113,-51,91,-116,91,-44,-44,91,-44,-44,-100,-44,-44,-103,-108,-110,91,91,91,91,91,91,91,91,-106,-114,91,-101,-102,-111,-47,]),'PLUS':([68,79,80,83,88,89,90,91,92,93,94,95,96,97,98,99,100,106,107,114,116,120,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,139,140,141,142,147,151,153,154,156,158,159,161,162,163,164,165,166,169,170,181,182,184,185,186,187,188,189,197,209,210,211,227,],[92,92,92,92,-99,-104,-105,-44,92,-109,-43,-113,-112,-118,-116,-119,-120,-49,-48,92,92,-44,-89,-90,-91,-92,-93,-94,158,-122,92,-107,-122,92,-115,-117,-121,-44,-113,-51,92,-116,92,-44,-44,92,-44,-44,-100,-44,-44,-103,-108,-110,92,92,92,92,92,92,92,92,-106,-114,92,-101,-102,-111,-47,]),'CTE_FLOAT':([68,79,80,83,91,92,95,106,114,116,120,122,123,124,125,126,127,130,133,139,140,142,151,153,154,156,158,159,162,163,169,170,181,182,184,185,186,187,197,],[99,99,99,99,-44,99,-113,-49,99,99,-44,-89,-90,-91,-92,-93,-94,99,99,-44,-113,99,99,-44,-44,99,-44,-44,-44,-44,99,99,99,99,99,99,99,99,99,]),'CTE_STR':([68,79,80,83,91,92,95,106,114,116,120,122,123,124,125,126,127,130,133,139,140,142,151,153,154,156,158,159,162,163,169,170,181,182,184,185,186,187,197,],[100,100,100,100,-44,100,-113,-49,100,100,-44,-89,-90,-91,-92,-93,-94,100,100,-44,-113,100,100,-44,-44,100,-44,-44,-44,-44,100,100,100,100,100,100,100,100,100,]),'UNTIL':([85,86,87,88,89,90,93,94,96,97,98,99,100,107,117,118,119,121,128,129,131,132,134,135,136,141,152,155,157,160,161,164,165,166,183,188,189,204,205,206,207,208,209,210,211,227,],[-70,-84,-122,-99,-104,-105,-109,-43,-112,-118,-116,-119,-120,-48,151,-122,-85,-87,-122,-122,-107,-122,-115,-117,-121,-51,-80,-83,-95,-98,-100,-103,-108,-110,-88,-106,-114,-81,-82,-86,-96,-97,-101,-102,-111,-47,]),'AND':([86,87,88,89,90,93,94,96,97,98,99,100,107,118,119,121,128,129,131,132,134,135,136,141,147,157,160,161,164,165,166,183,188,189,206,207,208,209,210,211,227,],[-84,-122,-99,-104,-105,-109,-43,-112,-118,-116,-119,-120,-48,153,-85,-87,-122,-122,-107,-122,-115,-117,-121,-51,-116,-95,-98,-100,-103,-108,-110,-88,-106,-114,-86,-96,-97,-101,-102,-111,-47,]),'OR':([86,87,88,89,90,93,94,96,97,98,99,100,107,118,119,121,128,129,131,132,134,135,136,141,147,157,160,161,164,165,166,183,188,189,206,207,208,209,210,211,227,],[-84,-122,-99,-104,-105,-109,-43,-112,-118,-116,-119,-120,-48,154,-85,-87,-122,-122,-107,-122,-115,-117,-121,-51,-116,-95,-98,-100,-103,-108,-110,-88,-106,-114,-86,-96,-97,-101,-102,-111,-47,]),'DO':([86,87,88,89,90,93,94,96,97,98,99,100,107,118,119,121,128,129,131,132,134,135,136,141,152,155,157,160,161,164,165,166,179,180,183,188,189,201,202,203,204,205,206,207,208,209,210,211,219,227,],[-84,-122,-99,-104,-105,-109,-43,-112,-118,-116,-119,-120,-48,-122,-85,-87,-122,-122,-107,-122,-115,-117,-121,-51,-80,-83,-95,-98,-100,-103,-108,-110,-63,-67,-88,-106,-114,218,-63,-71,-81,-82,-86,-96,-97,-101,-102,-111,225,-47,]),'LESSTHAN':([87,88,89,90,93,94,96,97,98,99,100,107,128,129,131,132,134,135,136,141,147,157,160,161,164,165,166,188,189,207,208,209,210,211,227,],[122,-99,-104,-105,-109,-43,-112,-118,-116,-119,-120,-48,-122,-122,-107,-122,-115,-117,-121,-51,-116,-95,-98,-100,-103,-108,-110,-106,-114,-96,-97,-101,-102,-111,-47,]),'GREATERTHAN':([87,88,89,90,93,94,96,97,98,99,100,107,128,129,131,132,134,135,136,141,147,157,160,161,164,165,166,188,189,207,208,209,210,211,227,],[123,-99,-104,-105,-109,-43,-112,-118,-116,-119,-120,-48,-122,-122,-107,-122,-115,-117,-121,-51,-116,-95,-98,-100,-103,-108,-110,-106,-114,-96,-97,-101,-102,-111,-47,]),'LESSEQUAL':([87,88,89,90,93,94,96,97,98,99,100,107,128,129,131,132,134,135,136,141,147,157,160,161,164,165,166,188,189,207,208,209,210,211,227,],[124,-99,-104,-105,-109,-43,-112,-118,-116,-119,-120,-48,-122,-122,-107,-122,-115,-117,-121,-51,-116,-95,-98,-100,-103,-108,-110,-106,-114,-96,-97,-101,-102,-111,-47,]),'GREATEREQUAL':([87,88,89,90,93,94,96,97,98,99,100,107,128,129,131,132,134,135,136,141,147,157,160,161,164,165,166,188,189,207,208,209,210,211,227,],[125,-99,-104,-105,-109,-43,-112,-118,-116,-119,-120,-48,-122,-122,-107,-122,-115,-117,-121,-51,-116,-95,-98,-100,-103,-108,-110,-106,-114,-96,-97,-101,-102,-111,-47,]),'EQUAL':([87,88,89,90,93,94,96,97,98,99,100,107,128,129,131,132,134,135,136,141,147,157,160,161,164,165,166,188,189,207,208,209,210,211,227,],[126,-99,-104,-105,-109,-43,-112,-118,-116,-119,-120,-48,-122,-122,-107,-122,-115,-117,-121,-51,-116,-95,-98,-100,-103,-108,-110,-106,-114,-96,-97,-101,-102,-111,-47,]),'NOTEQUAL':([87,88,89,90,93,94,96,97,98,99,100,107,128,129,131,132,134,135,136,141,147,157,160,161,164,165,166,188,189,207,208,209,210,211,227,],[127,-99,-104,-105,-109,-43,-112,-118,-116,-119,-120,-48,-122,-122,-107,-122,-115,-117,-121,-51,-116,-95,-98,-100,-103,-108,-110,-106,-114,-96,-97,-101,-102,-111,-47,]),'MULT':([89,90,93,94,96,97,98,99,100,107,129,131,132,134,135,136,141,147,165,166,188,189,211,227,],[-104,-105,-109,-43,-112,-118,-116,-119,-120,-48,162,-107,-122,-115,-117,-121,-51,-116,-108,-110,-106,-114,-111,-47,]),'DIVIDE':([89,90,93,94,96,97,98,99,100,107,129,131,132,134,135,136,141,147,165,166,188,189,211,227,],[-104,-105,-109,-43,-112,-118,-116,-119,-120,-48,163,-107,-122,-115,-117,-121,-51,-116,-108,-110,-106,-114,-111,-47,]),'THEN':([149,178,],[-63,200,]),'ELSE':([229,],[233,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'prog':([0,],[1,]),'np_goto_':([3,],[4,]),'variables':([5,137,],[6,168,]),'empty':([5,9,16,27,30,31,44,47,52,70,78,79,87,103,118,128,129,132,137,174,176,177,212,217,224,229,231,241,],[8,17,17,33,38,41,50,53,53,104,107,110,121,50,155,160,164,107,8,107,198,198,53,53,53,234,53,53,]),'np_push_global_vars_':([6,],[9,]),'variables_2':([7,30,],[10,37,]),'tipo':([7,18,30,44,103,],[11,24,11,49,49,]),'prog_funcs':([9,16,],[15,22,]),'funcion':([9,16,],[16,16,]),'func_princ':([15,],[20,]),'tipo_func':([18,],[23,]),'lista_id':([19,40,],[26,45,]),'np_start_main_':([21,],[28,]),'dimension_var':([27,],[31,]),'np_set_scope_':([29,],[35,]),'variables_rep':([30,],[36,]),'lista_id_rep':([31,],[39,]),'funcion_param':([44,103,],[48,138,]),'estatuto_rep':([47,52,212,217,224,231,241,],[51,72,220,223,230,236,244,]),'estatuto':([47,52,212,217,224,231,241,],[52,52,52,52,52,52,52,]),'asignacion':([47,52,212,217,224,231,241,],[54,54,54,54,54,54,54,]),'llamada':([47,52,68,79,80,83,92,114,116,130,133,142,151,156,169,170,181,182,184,185,186,187,197,212,217,224,231,241,],[55,55,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,55,55,55,55,55,]),'retorno':([47,52,212,217,224,231,241,],[56,56,56,56,56,56,56,]),'lectura':([47,52,212,217,224,231,241,],[57,57,57,57,57,57,57,]),'escritura':([47,52,212,217,224,231,241,],[58,58,58,58,58,58,58,]),'decision':([47,52,212,217,224,231,241,],[59,59,59,59,59,59,59,]),'rep_c':([47,52,212,217,224,231,241,],[60,60,60,60,60,60,60,]),'rep_nc':([47,52,212,217,224,231,241,],[61,61,61,61,61,61,61,]),'np_add_func_to_directory_':([48,],[69,]),'np_push_var_':([62,94,145,],[78,132,174,]),'np_push_operator_':([64,65,91,120,139,153,154,158,159,162,163,],[81,82,130,156,169,181,182,184,185,186,187,]),'np_push_jump_':([67,180,],[84,203,]),'expresion':([68,79,80,83,114,116,133,142,151,169,170,181,182,197,],[85,111,112,115,148,150,167,111,180,191,192,204,205,148,]),'exp_comp':([68,79,80,83,114,116,133,142,151,169,170,181,182,197,],[86,86,86,86,86,86,86,86,86,86,86,86,86,86,]),'exp_ar':([68,79,80,83,114,116,133,142,151,156,169,170,181,182,184,185,197,],[87,87,87,87,87,87,87,87,87,183,87,87,87,87,207,208,87,]),'termino':([68,79,80,83,114,116,133,142,151,156,169,170,181,182,184,185,186,187,197,],[88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,209,210,88,]),'unary':([68,79,80,83,92,114,116,130,133,142,151,156,169,170,181,182,184,185,186,187,197,],[89,89,89,89,131,89,89,165,89,89,89,89,89,89,89,89,89,89,89,89,89,]),'factor':([68,79,80,83,92,114,116,130,133,142,151,156,169,170,181,182,184,185,186,187,197,],[90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,]),'const':([68,79,80,83,92,114,116,130,133,142,151,156,169,170,181,182,184,185,186,187,197,],[93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,]),'letrero':([68,79,80,83,92,114,116,130,133,142,151,156,169,170,181,182,184,185,186,187,197,],[98,98,98,98,98,147,98,98,98,98,98,98,98,98,98,98,98,98,98,98,147,]),'funcion_param_rep':([70,],[102,]),'dimension':([78,132,174,],[105,166,194,]),'expresion_rep':([79,],[108,]),'expresion_rep_2':([79,142,],[109,171,]),'np_assign_temp_':([85,],[117,]),'np_quadruple_logic_':([86,],[118,]),'exp_comp_2':([87,],[119,]),'comp_sym':([87,],[120,]),'np_quadruple_term':([88,],[128,]),'np_quadruple_factor_':([89,],[129,]),'np_add_false_bottom_':([95,140,],[133,170,]),'np_push_const_int_':([97,],[134,]),'np_push_const_float_':([99,],[135,]),'np_push_const_string_':([100,],[136,]),'np_verify_dimensions_':([106,],[140,]),'lista_lectura':([113,222,],[144,228,]),'lista_escritura':([114,197,],[146,216,]),'expresion_2':([118,],[152,]),'exp_ar_2':([128,],[157,]),'termino_2':([129,],[161,]),'np_quadruple_return_':([143,],[172,]),'np_quadruple_IO_':([147,148,194,],[176,177,215,]),'np_gotoF_':([149,179,202,],[178,201,219,]),'change_sign':([165,],[188,]),'np_add_vars_to_table_':([168,],[190,]),'np_pop_operator_':([173,175,],[193,195,]),'lista_escritura_rep':([176,177,],[196,199,]),'np_quadruple_for_':([180,],[202,]),'np_quadruple_compare_':([183,],[206,]),'np_remove_false_bottom_':([189,214,],[211,221,]),'np_quadruple_assignment_':([191,],[213,]),'np_manage_array_':([192,],[214,]),'decision_alt':([229,],[232,]),'np_false_condition_':([233,],[237,]),'np_end_if_actions':([234,246,],[238,247,]),'np_end_while_actions_':([235,243,],[239,245,]),'np_end_for_actions':([240,],[242,]),'np_increment_temp_':([240,],[243,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> prog","S'",1,None,None,None),
  ('prog -> PROGRAM ID np_goto_ SEMICOLON variables np_push_global_vars_ prog_funcs func_princ','prog',8,'p_prog','foreveralone.py',117),
  ('np_goto_ -> <empty>','np_goto_',0,'p_np_goto_','foreveralone.py',129),
  ('np_push_global_vars_ -> <empty>','np_push_global_vars_',0,'p_np_push_global_vars_','foreveralone.py',137),
  ('prog_funcs -> funcion prog_funcs','prog_funcs',2,'p_prog_funcs','foreveralone.py',154),
  ('prog_funcs -> empty','prog_funcs',1,'p_prog_funcs','foreveralone.py',155),
  ('variables -> VAR variables_2','variables',2,'p_variables','foreveralone.py',160),
  ('variables -> empty','variables',1,'p_variables','foreveralone.py',161),
  ('variables_2 -> tipo COLON lista_id SEMICOLON variables_rep','variables_2',5,'p_variables_2','foreveralone.py',169),
  ('variables_rep -> variables_2','variables_rep',1,'p_variables_rep','foreveralone.py',183),
  ('variables_rep -> empty','variables_rep',1,'p_variables_rep','foreveralone.py',184),
  ('lista_id -> ID dimension_var lista_id_rep','lista_id',3,'p_lista_id','foreveralone.py',191),
  ('lista_id_rep -> COMMA lista_id','lista_id_rep',2,'p_lista_id_rep','foreveralone.py',204),
  ('lista_id_rep -> empty','lista_id_rep',1,'p_lista_id_rep','foreveralone.py',205),
  ('dimension_var -> SQUAREL CTE_INT SQUARER','dimension_var',3,'p_dimension_var','foreveralone.py',215),
  ('dimension_var -> empty','dimension_var',1,'p_dimension_var','foreveralone.py',216),
  ('tipo -> INT','tipo',1,'p_tipo','foreveralone.py',223),
  ('tipo -> FLOAT','tipo',1,'p_tipo','foreveralone.py',224),
  ('tipo -> STRING','tipo',1,'p_tipo','foreveralone.py',225),
  ('func_princ -> PRINCIPAL np_start_main_ PARENTHESESL PARENTHESESR CURLYL estatuto_rep CURLYR','func_princ',7,'p_func_princ','foreveralone.py',232),
  ('np_start_main_ -> <empty>','np_start_main_',0,'p_np_start_main_','foreveralone.py',236),
  ('funcion -> FUNC tipo_func ID np_set_scope_ PARENTHESESL funcion_param np_add_func_to_directory_ PARENTHESESR SEMICOLON variables np_add_vars_to_table_ CURLYL estatuto_rep CURLYR','funcion',14,'p_funcion','foreveralone.py',245),
  ('np_set_scope_ -> <empty>','np_set_scope_',0,'p_np_set_scope_','foreveralone.py',250),
  ('np_add_func_to_directory_ -> <empty>','np_add_func_to_directory_',0,'p_np_add_func_to_directory_','foreveralone.py',258),
  ('np_add_vars_to_table_ -> <empty>','np_add_vars_to_table_',0,'p_np_add_vars_to_table_','foreveralone.py',280),
  ('tipo_func -> tipo','tipo_func',1,'p_tipo_func','foreveralone.py',297),
  ('tipo_func -> VOID','tipo_func',1,'p_tipo_func','foreveralone.py',298),
  ('funcion_param -> tipo ID funcion_param_rep','funcion_param',3,'p_funcion_param','foreveralone.py',305),
  ('funcion_param -> empty','funcion_param',1,'p_funcion_param','foreveralone.py',306),
  ('funcion_param_rep -> COMMA funcion_param','funcion_param_rep',2,'p_funcion_param_rep','foreveralone.py',320),
  ('funcion_param_rep -> empty','funcion_param_rep',1,'p_funcion_param_rep','foreveralone.py',321),
  ('estatuto_rep -> estatuto estatuto_rep','estatuto_rep',2,'p_estatuto_rep','foreveralone.py',328),
  ('estatuto_rep -> empty','estatuto_rep',1,'p_estatuto_rep','foreveralone.py',329),
  ('estatuto -> asignacion SEMICOLON','estatuto',2,'p_estatuto','foreveralone.py',334),
  ('estatuto -> llamada SEMICOLON','estatuto',2,'p_estatuto','foreveralone.py',335),
  ('estatuto -> retorno SEMICOLON','estatuto',2,'p_estatuto','foreveralone.py',336),
  ('estatuto -> lectura SEMICOLON','estatuto',2,'p_estatuto','foreveralone.py',337),
  ('estatuto -> escritura SEMICOLON','estatuto',2,'p_estatuto','foreveralone.py',338),
  ('estatuto -> decision','estatuto',1,'p_estatuto','foreveralone.py',339),
  ('estatuto -> rep_c','estatuto',1,'p_estatuto','foreveralone.py',340),
  ('estatuto -> rep_nc','estatuto',1,'p_estatuto','foreveralone.py',341),
  ('np_quadruple_assignment_ -> <empty>','np_quadruple_assignment_',0,'p_np_quadruple_assignment_','foreveralone.py',346),
  ('np_quadruple_IO_ -> <empty>','np_quadruple_IO_',0,'p_np_quadruple_IO_','foreveralone.py',354),
  ('np_push_var_ -> <empty>','np_push_var_',0,'p_np_push_var_','foreveralone.py',362),
  ('np_push_operator_ -> <empty>','np_push_operator_',0,'p_np_push_operator_','foreveralone.py',382),
  ('np_pop_operator_ -> <empty>','np_pop_operator_',0,'p_np_pop_operator_','foreveralone.py',393),
  ('asignacion -> ID np_push_var_ dimension ASSIGN np_push_operator_ expresion np_quadruple_assignment_','asignacion',7,'p_asignacion','foreveralone.py',399),
  ('dimension -> SQUAREL np_verify_dimensions_ np_add_false_bottom_ expresion np_manage_array_ np_remove_false_bottom_ SQUARER','dimension',7,'p_dimension','foreveralone.py',406),
  ('dimension -> empty','dimension',1,'p_dimension','foreveralone.py',407),
  ('np_verify_dimensions_ -> <empty>','np_verify_dimensions_',0,'p_np_verify_dimensions_','foreveralone.py',412),
  ('np_manage_array_ -> <empty>','np_manage_array_',0,'p_np_manage_array_','foreveralone.py',441),
  ('llamada -> ID PARENTHESESL expresion_rep PARENTHESESR','llamada',4,'p_llamada','foreveralone.py',450),
  ('lectura -> READ np_push_operator_ PARENTHESESL lista_lectura PARENTHESESR np_pop_operator_','lectura',6,'p_lectura','foreveralone.py',455),
  ('lista_lectura -> ID np_push_var_ dimension np_quadruple_IO_ COMMA lista_lectura','lista_lectura',6,'p_lista_lectura','foreveralone.py',460),
  ('lista_lectura -> ID np_push_var_ dimension np_quadruple_IO_','lista_lectura',4,'p_lista_lectura','foreveralone.py',461),
  ('escritura -> PRINT np_push_operator_ PARENTHESESL lista_escritura PARENTHESESR np_pop_operator_','escritura',6,'p_escritura','foreveralone.py',466),
  ('lista_escritura -> letrero np_quadruple_IO_ lista_escritura_rep','lista_escritura',3,'p_lista_escritura','foreveralone.py',471),
  ('lista_escritura -> expresion np_quadruple_IO_ lista_escritura_rep','lista_escritura',3,'p_lista_escritura','foreveralone.py',472),
  ('lista_escritura_rep -> COMMA lista_escritura','lista_escritura_rep',2,'p_lista_escritura_rep','foreveralone.py',477),
  ('lista_escritura_rep -> empty','lista_escritura_rep',1,'p_lista_escritura_rep','foreveralone.py',478),
  ('decision -> IF PARENTHESESL expresion PARENTHESESR np_gotoF_ THEN CURLYL estatuto_rep CURLYR decision_alt','decision',10,'p_decision','foreveralone.py',483),
  ('decision_alt -> ELSE np_false_condition_ CURLYL estatuto_rep CURLYR np_end_if_actions','decision_alt',6,'p_decision_alt','foreveralone.py',488),
  ('decision_alt -> empty np_end_if_actions','decision_alt',2,'p_decision_alt','foreveralone.py',489),
  ('np_gotoF_ -> <empty>','np_gotoF_',0,'p_np_gotoF_','foreveralone.py',494),
  ('np_false_condition_ -> <empty>','np_false_condition_',0,'p_np_false_condition_','foreveralone.py',504),
  ('np_end_if_actions -> <empty>','np_end_if_actions',0,'p_np_end_if_actions','foreveralone.py',513),
  ('rep_c -> WHILE np_push_jump_ PARENTHESESL expresion PARENTHESESR np_gotoF_ DO CURLYL estatuto_rep CURLYR np_end_while_actions_','rep_c',11,'p_rep_c','foreveralone.py',520),
  ('np_push_jump_ -> <empty>','np_push_jump_',0,'p_np_push_jump_','foreveralone.py',525),
  ('np_end_while_actions_ -> <empty>','np_end_while_actions_',0,'p_np_end_while_actions_','foreveralone.py',531),
  ('rep_nc -> FROM expresion np_assign_temp_ UNTIL expresion np_quadruple_for_ np_gotoF_ DO CURLYL estatuto_rep CURLYR np_end_for_actions','rep_nc',12,'p_rep_nc','foreveralone.py',540),
  ('np_assign_temp_ -> <empty>','np_assign_temp_',0,'p_np_assign_temp_','foreveralone.py',545),
  ('np_quadruple_for_ -> np_push_jump_','np_quadruple_for_',1,'p_np_quadruple_for_','foreveralone.py',551),
  ('np_end_for_actions -> np_increment_temp_ np_end_while_actions_','np_end_for_actions',2,'p_np_end_for_actions','foreveralone.py',572),
  ('np_increment_temp_ -> <empty>','np_increment_temp_',0,'p_np_increment_temp_','foreveralone.py',577),
  ('expresion_rep -> expresion_rep_2','expresion_rep',1,'p_expresion_rep','foreveralone.py',583),
  ('expresion_rep -> empty','expresion_rep',1,'p_expresion_rep','foreveralone.py',584),
  ('expresion_rep_2 -> expresion COMMA expresion_rep_2','expresion_rep_2',3,'p_expresion_rep_2','foreveralone.py',589),
  ('expresion_rep_2 -> expresion','expresion_rep_2',1,'p_expresion_rep_2','foreveralone.py',590),
  ('retorno -> RETURN PARENTHESESL expresion PARENTHESESR np_quadruple_return_','retorno',5,'p_retorno','foreveralone.py',595),
  ('np_quadruple_return_ -> <empty>','np_quadruple_return_',0,'p_np_quadruple_return_','foreveralone.py',600),
  ('expresion -> exp_comp np_quadruple_logic_ expresion_2','expresion',3,'p_expresion','foreveralone.py',608),
  ('expresion_2 -> AND np_push_operator_ expresion','expresion_2',3,'p_expresion_2','foreveralone.py',619),
  ('expresion_2 -> OR np_push_operator_ expresion','expresion_2',3,'p_expresion_2','foreveralone.py',620),
  ('expresion_2 -> empty','expresion_2',1,'p_expresion_2','foreveralone.py',621),
  ('np_quadruple_logic_ -> <empty>','np_quadruple_logic_',0,'p_np_quadruple_logic_','foreveralone.py',626),
  ('exp_comp -> exp_ar exp_comp_2','exp_comp',2,'p_exp_comp','foreveralone.py',634),
  ('exp_comp_2 -> comp_sym np_push_operator_ exp_ar np_quadruple_compare_','exp_comp_2',4,'p_exp_comp_2','foreveralone.py',639),
  ('exp_comp_2 -> empty','exp_comp_2',1,'p_exp_comp_2','foreveralone.py',640),
  ('np_quadruple_compare_ -> <empty>','np_quadruple_compare_',0,'p_np_quadruple_compare_','foreveralone.py',645),
  ('comp_sym -> LESSTHAN','comp_sym',1,'p_comp_sym','foreveralone.py',655),
  ('comp_sym -> GREATERTHAN','comp_sym',1,'p_comp_sym','foreveralone.py',656),
  ('comp_sym -> LESSEQUAL','comp_sym',1,'p_comp_sym','foreveralone.py',657),
  ('comp_sym -> GREATEREQUAL','comp_sym',1,'p_comp_sym','foreveralone.py',658),
  ('comp_sym -> EQUAL','comp_sym',1,'p_comp_sym','foreveralone.py',659),
  ('comp_sym -> NOTEQUAL','comp_sym',1,'p_comp_sym','foreveralone.py',660),
  ('exp_ar -> termino np_quadruple_term exp_ar_2','exp_ar',3,'p_exp_ar','foreveralone.py',666),
  ('exp_ar_2 -> PLUS np_push_operator_ exp_ar','exp_ar_2',3,'p_exp_ar_2','foreveralone.py',671),
  ('exp_ar_2 -> MINUS np_push_operator_ exp_ar','exp_ar_2',3,'p_exp_ar_2','foreveralone.py',672),
  ('exp_ar_2 -> empty','exp_ar_2',1,'p_exp_ar_2','foreveralone.py',673),
  ('np_quadruple_term -> <empty>','np_quadruple_term',0,'p_np_quadruple_term','foreveralone.py',678),
  ('termino -> unary np_quadruple_factor_ termino_2','termino',3,'p_termino','foreveralone.py',686),
  ('termino_2 -> MULT np_push_operator_ termino','termino_2',3,'p_termino_2','foreveralone.py',691),
  ('termino_2 -> DIVIDE np_push_operator_ termino','termino_2',3,'p_termino_2','foreveralone.py',692),
  ('termino_2 -> empty','termino_2',1,'p_termino_2','foreveralone.py',693),
  ('np_quadruple_factor_ -> <empty>','np_quadruple_factor_',0,'p_np_quadruple_factor_','foreveralone.py',698),
  ('unary -> factor','unary',1,'p_unary','foreveralone.py',707),
  ('unary -> MINUS np_push_operator_ unary change_sign','unary',4,'p_unary','foreveralone.py',708),
  ('unary -> PLUS unary','unary',2,'p_unary','foreveralone.py',709),
  ('change_sign -> <empty>','change_sign',0,'p_change_sign','foreveralone.py',715),
  ('factor -> const','factor',1,'p_factor','foreveralone.py',722),
  ('factor -> ID np_push_var_ dimension','factor',3,'p_factor','foreveralone.py',723),
  ('factor -> PARENTHESESL np_add_false_bottom_ expresion PARENTHESESR np_remove_false_bottom_','factor',5,'p_factor','foreveralone.py',724),
  ('factor -> llamada','factor',1,'p_factor','foreveralone.py',725),
  ('np_add_false_bottom_ -> <empty>','np_add_false_bottom_',0,'p_np_add_false_bottom_','foreveralone.py',730),
  ('np_remove_false_bottom_ -> <empty>','np_remove_false_bottom_',0,'p_np_remove_false_bottom_','foreveralone.py',741),
  ('const -> CTE_INT np_push_const_int_','const',2,'p_const','foreveralone.py',755),
  ('const -> letrero','const',1,'p_const','foreveralone.py',756),
  ('const -> CTE_FLOAT np_push_const_float_','const',2,'p_const','foreveralone.py',757),
  ('np_push_const_int_ -> <empty>','np_push_const_int_',0,'p_np_push_const_int_','foreveralone.py',762),
  ('np_push_const_float_ -> <empty>','np_push_const_float_',0,'p_np_push_const_float_','foreveralone.py',775),
  ('np_push_const_string_ -> <empty>','np_push_const_string_',0,'p_np_push_const_string_','foreveralone.py',788),
  ('letrero -> CTE_STR np_push_const_string_','letrero',2,'p_letrero','foreveralone.py',801),
  ('empty -> <empty>','empty',0,'p_empty','foreveralone.py',806),
  ('np_check -> <empty>','np_check',0,'p_np_check','foreveralone.py',811),
]
