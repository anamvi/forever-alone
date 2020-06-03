
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASSIGN COLON COMMA CTE_FLOAT CTE_INT CTE_STR CURLYL CURLYR DIVIDE DO ELSE EQUAL FLOAT FROM FUNC GREATEREQUAL GREATERTHAN ID IF INT LESSEQUAL LESSTHAN MINUS MULT NOTEQUAL OR PARENTHESESL PARENTHESESR PLUS PRINCIPAL PRINT PROGRAM READ RETURN SEMICOLON SQUAREL SQUARER STRING THEN UNTIL VAR VOID WHILE\n        prog : PROGRAM ID np_goto_ SEMICOLON variables np_push_global_vars_ prog_funcs func_princ np_end_program_\n    \n        np_goto_ :\n    \n        np_push_global_vars_ :\n    \n        prog_funcs : funcion prog_funcs\n        | empty\n    \n        variables : VAR variables_2\n        | empty\n    \n        variables_2 : tipo COLON lista_id SEMICOLON variables_rep\n    \n        variables_rep : variables_2\n        | empty\n    \n        lista_id : ID dimension_var lista_id_rep\n    \n        lista_id_rep : COMMA lista_id\n        | empty\n    \n        dimension_var : SQUAREL CTE_INT SQUARER\n        | empty\n    \n        tipo : INT\n        | FLOAT\n        | STRING\n    \n        func_princ : PRINCIPAL np_start_main_ PARENTHESESL PARENTHESESR CURLYL estatuto_rep CURLYR\n    \n        np_start_main_ :\n    \n        np_end_program_ :\n    \n        funcion : FUNC tipo_func ID np_set_scope_ PARENTHESESL funcion_param np_add_func_to_directory_ PARENTHESESR SEMICOLON variables np_add_vars_to_table_ CURLYL estatuto_rep CURLYR np_end_function_\n    \n        tipo_func : tipo\n        | VOID\n    \n        np_set_scope_ :\n    \n        np_add_func_to_directory_ :\n    \n        np_add_vars_to_table_ :\n    \n        np_end_function_ :\n    \n        funcion_param : tipo ID funcion_param_rep\n        | empty\n    \n        funcion_param_rep : COMMA funcion_param\n        | empty\n    \n        estatuto_rep : estatuto estatuto_rep\n        | empty\n    \n        estatuto : asignacion SEMICOLON\n        | llamada SEMICOLON np_llamada_void_\n        | retorno SEMICOLON\n        | lectura SEMICOLON\n        | escritura SEMICOLON\n        | decision\n        | rep_c\n        | rep_nc\n    \n        np_llamada_void_ :\n    \n        np_quadruple_IO_ :\n    \n        np_push_var_ :\n    \n        np_push_operator_ :\n    \n        np_pop_operator_ :\n    \n        asignacion : ID np_push_var_ dimension ASSIGN np_push_operator_ expresion np_quadruple_assignment_\n    \n        np_quadruple_assignment_ :\n    \n        dimension : SQUAREL np_verify_dimensions_ np_add_false_bottom_ expresion np_manage_array_ np_remove_false_bottom_ SQUARER\n        | empty\n    \n        np_verify_dimensions_ :\n    \n        np_manage_array_ :\n    \n        llamada : ID np_verify_function_ PARENTHESESL np_add_false_bottom_ np_create_era_ expresion_rep np_end_of_parameters_ PARENTHESESR np_remove_false_bottom_ np_create_gosub_\n    \n        np_verify_function_ :\n    \n        expresion_rep : expresion_rep_2\n        | empty\n    \n        expresion_rep_2 : expresion np_next_parameter_check_ np_verify_parameters_ COMMA expresion_rep_2\n        | expresion np_next_parameter_check_ np_verify_parameters_\n    \n        np_verify_parameters_ :\n    \n        np_next_parameter_check_ :\n    \n        np_end_of_parameters_ :\n    \n        np_create_era_ :\n    \n        np_create_gosub_ :\n    \n        lectura : READ np_push_operator_ PARENTHESESL lista_lectura PARENTHESESR np_pop_operator_\n    \n        lista_lectura : ID np_push_var_ dimension np_quadruple_IO_ COMMA lista_lectura\n        | ID np_push_var_ dimension np_quadruple_IO_\n    \n        escritura : PRINT np_push_operator_ PARENTHESESL lista_escritura PARENTHESESR np_pop_operator_\n    \n        lista_escritura : expresion np_quadruple_IO_ lista_escritura_rep\n    \n        lista_escritura_rep : COMMA lista_escritura\n        | empty\n    \n        decision : IF PARENTHESESL expresion PARENTHESESR np_gotoF_ THEN CURLYL estatuto_rep CURLYR decision_alt\n    \n        decision_alt : ELSE np_false_condition_ CURLYL estatuto_rep CURLYR np_end_if_actions\n        | empty np_end_if_actions\n    \n        np_gotoF_ :\n    \n        np_false_condition_ :\n    \n        np_end_if_actions :\n    \n        rep_c : WHILE np_push_jump_ PARENTHESESL expresion PARENTHESESR np_gotoF_ DO CURLYL estatuto_rep CURLYR np_end_while_actions_\n    \n        np_push_jump_ :\n    \n        np_end_while_actions_ :\n    \n        rep_nc : FROM ID np_push_var_ dimension ASSIGN expresion np_assign_loop_ UNTIL expresion np_quadruple_for_ np_gotoF_ DO CURLYL estatuto_rep CURLYR np_end_for_actions\n    \n        np_assign_loop_ :\n    \n        np_quadruple_for_ : np_push_jump_\n    \n        np_end_for_actions : np_increment_temp_ np_end_while_actions_\n    \n        np_increment_temp_ :\n    \n        retorno : RETURN PARENTHESESL expresion PARENTHESESR np_quadruple_return_\n        | RETURN PARENTHESESL PARENTHESESR np_quadruple_empty_return_\n    \n        np_quadruple_return_ :\n    \n        np_quadruple_empty_return_ :\n    \n        expresion : exp_comp np_quadruple_logic_ expresion_2\n    \n        expresion_2 : AND np_push_operator_ expresion\n        | OR np_push_operator_ expresion\n        | empty\n    \n        np_quadruple_logic_ :\n    \n        exp_comp : exp_ar exp_comp_2\n    \n        exp_comp_2 : comp_sym np_push_operator_ exp_ar np_quadruple_compare_\n        | empty\n    \n        np_quadruple_compare_ :\n    \n        comp_sym : LESSTHAN\n        | GREATERTHAN\n        | LESSEQUAL\n        | GREATEREQUAL\n        | EQUAL\n        | NOTEQUAL\n    \n        exp_ar : termino np_quadruple_term exp_ar_2\n    \n        exp_ar_2 : PLUS np_push_operator_ exp_ar\n        | MINUS np_push_operator_ exp_ar\n        | empty\n    \n        np_quadruple_term :\n    \n        termino : unary np_quadruple_factor_ termino_2\n    \n        termino_2 : MULT np_push_operator_ termino\n        | DIVIDE np_push_operator_ termino\n        | empty\n    \n        np_quadruple_factor_ :\n    \n        unary : factor\n        | MINUS np_push_operator_ unary change_sign\n        | PLUS unary\n    \n        change_sign :\n    \n        factor : const\n        | ID np_push_var_ dimension\n        | PARENTHESESL np_add_false_bottom_ expresion PARENTHESESR np_remove_false_bottom_\n        | llamada\n    \n        np_add_false_bottom_ :\n    \n        np_remove_false_bottom_ :\n    \n        const : CTE_INT np_push_const_int_\n        | CTE_STR np_push_const_string_\n        | CTE_FLOAT np_push_const_float_\n    \n        np_push_const_int_ :\n    \n        np_push_const_float_ :\n    \n        np_push_const_string_ :\n    \n        empty :\n    '
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,20,28,72,],[0,-21,-1,-19,]),'ID':([2,12,13,14,19,23,24,25,41,48,50,53,60,61,62,69,74,75,76,77,78,81,84,91,93,95,96,104,105,112,113,115,119,120,121,122,127,129,130,131,132,133,134,137,151,152,153,157,158,160,162,163,166,167,177,186,187,189,190,191,192,198,203,218,225,227,228,232,234,240,242,243,247,248,250,253,254,256,257,258,259,260,],[3,-16,-17,-18,27,30,-23,-24,27,63,71,63,-40,-41,-42,86,-35,-43,-37,-38,-39,107,107,-36,-52,-123,-123,-46,107,144,107,107,-46,-123,-63,107,-46,-99,-100,-101,-102,-103,-104,107,107,107,107,-46,-46,107,-46,-46,-46,-46,107,107,107,107,107,107,107,107,63,63,144,63,107,107,-131,-72,-77,-80,-74,-78,63,63,-77,-73,-85,-81,-80,-84,]),'SEMICOLON':([3,4,26,27,32,34,40,42,46,47,55,56,57,58,59,87,94,98,99,100,101,102,103,106,107,108,109,110,111,123,124,125,126,128,135,136,138,139,140,141,142,155,156,159,161,164,165,168,169,170,171,173,179,185,188,193,194,196,204,208,209,210,211,212,213,214,215,223,230,231,238,],[-2,5,31,-131,-131,-15,-11,-13,-12,-14,74,75,76,77,78,117,-51,-89,-94,-131,-109,-114,-115,-119,-45,-122,-128,-130,-129,-88,-87,-131,-95,-97,-131,-131,-117,-131,-125,-126,-127,-86,-90,-93,-105,-108,-110,-113,-118,-120,-47,-47,-49,-124,-98,-116,-65,-68,-48,-121,-91,-92,-96,-106,-107,-111,-112,-124,-50,-64,-54,]),'VAR':([5,117,],[7,7,]),'FUNC':([5,6,8,9,10,16,31,37,38,39,229,237,],[-131,-3,-7,18,-6,18,-131,-8,-9,-10,-28,-22,]),'PRINCIPAL':([5,6,8,9,10,15,16,17,22,31,37,38,39,229,237,],[-131,-3,-7,-131,-6,21,-131,-5,-4,-131,-8,-9,-10,-28,-22,]),'INT':([7,18,31,45,89,],[12,12,12,12,12,]),'FLOAT':([7,18,31,45,89,],[13,13,13,13,13,]),'STRING':([7,18,31,45,89,],[14,14,14,14,14,]),'CURLYL':([8,10,31,37,38,39,44,117,150,178,200,219,241,246,251,],[-7,-6,-131,-8,-9,-10,48,-131,-27,203,218,227,-76,250,253,]),'COLON':([11,12,13,14,],[19,-16,-17,-18,]),'VOID':([18,],[25,]),'PARENTHESESL':([21,29,30,36,63,64,65,66,67,68,80,81,82,83,84,85,93,95,96,104,105,107,113,115,119,120,121,122,127,129,130,131,132,133,134,137,151,152,153,157,158,160,162,163,166,167,177,186,187,189,190,191,192,198,228,232,],[-20,35,-25,45,-55,81,-46,-46,84,-79,95,96,112,113,96,115,-52,-123,-123,-46,96,-55,96,96,-46,-123,-63,96,-46,-99,-100,-101,-102,-103,-104,96,96,96,96,-46,-46,96,-46,-46,-46,-46,96,96,96,96,96,96,96,96,96,96,]),'SQUAREL':([27,63,79,86,107,116,139,144,172,],[33,-45,93,-45,-45,93,93,-45,93,]),'COMMA':([27,32,34,47,71,94,99,100,101,102,103,106,107,108,109,110,111,125,126,128,135,136,138,139,140,141,142,144,146,156,159,161,164,165,168,169,170,172,174,184,185,188,193,195,207,208,209,210,211,212,213,214,215,216,223,224,230,231,238,],[-131,41,-15,-14,89,-51,-94,-131,-109,-114,-115,-119,-45,-122,-128,-130,-129,-131,-95,-97,-131,-131,-117,-131,-125,-126,-127,-45,-44,-90,-93,-105,-108,-110,-113,-118,-120,-131,198,-61,-124,-98,-116,-44,-60,-121,-91,-92,-96,-106,-107,-111,-112,225,-124,232,-50,-64,-54,]),'CTE_INT':([33,81,84,93,95,96,104,105,113,115,119,120,121,122,127,129,130,131,132,133,134,137,151,152,153,157,158,160,162,163,166,167,177,186,187,189,190,191,192,198,228,232,],[43,109,109,-52,-123,-123,-46,109,109,109,-46,-123,-63,109,-46,-99,-100,-101,-102,-103,-104,109,109,109,109,-46,-46,109,-46,-46,-46,-46,109,109,109,109,109,109,109,109,109,109,]),'PARENTHESESR':([35,45,49,51,70,71,81,88,89,90,94,95,97,99,100,101,102,103,106,107,108,109,110,111,114,118,121,125,126,128,135,136,138,139,140,141,142,143,144,145,146,148,153,154,156,159,161,164,165,168,169,170,172,174,181,182,183,184,185,188,193,195,197,199,206,207,208,209,210,211,212,213,214,215,216,217,223,224,230,231,233,238,239,],[44,-131,-26,-30,87,-131,98,-29,-131,-32,-51,-123,123,-94,-131,-109,-114,-115,-119,-45,-122,-128,-130,-129,147,-31,-63,-131,-95,-97,-131,-131,-117,-131,-125,-126,-127,171,-45,173,-44,176,-131,185,-90,-93,-105,-108,-110,-113,-118,-120,-131,-131,-62,-56,-57,-61,-124,-98,-116,-44,-69,-71,223,-60,-121,-91,-92,-96,-106,-107,-111,-112,-67,-70,-124,-59,-50,-64,-66,-54,-58,]),'SQUARER':([43,94,99,100,101,102,103,106,107,108,109,110,111,125,126,128,135,136,138,139,140,141,142,156,159,161,164,165,168,169,170,180,185,188,193,205,208,209,210,211,212,213,214,215,222,223,230,231,238,],[47,-51,-94,-131,-109,-114,-115,-119,-45,-122,-128,-130,-129,-131,-95,-97,-131,-131,-117,-131,-125,-126,-127,-90,-93,-105,-108,-110,-113,-118,-120,-53,-124,-98,-116,-124,-121,-91,-92,-96,-106,-107,-111,-112,230,-124,-50,-64,-54,]),'CURLYR':([48,52,53,54,60,61,62,73,74,75,76,77,78,91,203,218,221,226,227,234,235,240,242,243,247,248,250,252,253,254,255,256,257,258,259,260,],[-131,72,-131,-34,-40,-41,-42,-33,-35,-43,-37,-38,-39,-36,-131,-131,229,234,-131,-131,243,-72,-77,-80,-74,-78,-131,254,-131,-77,257,-73,-85,-81,-80,-84,]),'RETURN':([48,53,60,61,62,74,75,76,77,78,91,203,218,227,234,240,242,243,247,248,250,253,254,256,257,258,259,260,],[64,64,-40,-41,-42,-35,-43,-37,-38,-39,-36,64,64,64,-131,-72,-77,-80,-74,-78,64,64,-77,-73,-85,-81,-80,-84,]),'READ':([48,53,60,61,62,74,75,76,77,78,91,203,218,227,234,240,242,243,247,248,250,253,254,256,257,258,259,260,],[65,65,-40,-41,-42,-35,-43,-37,-38,-39,-36,65,65,65,-131,-72,-77,-80,-74,-78,65,65,-77,-73,-85,-81,-80,-84,]),'PRINT':([48,53,60,61,62,74,75,76,77,78,91,203,218,227,234,240,242,243,247,248,250,253,254,256,257,258,259,260,],[66,66,-40,-41,-42,-35,-43,-37,-38,-39,-36,66,66,66,-131,-72,-77,-80,-74,-78,66,66,-77,-73,-85,-81,-80,-84,]),'IF':([48,53,60,61,62,74,75,76,77,78,91,203,218,227,234,240,242,243,247,248,250,253,254,256,257,258,259,260,],[67,67,-40,-41,-42,-35,-43,-37,-38,-39,-36,67,67,67,-131,-72,-77,-80,-74,-78,67,67,-77,-73,-85,-81,-80,-84,]),'WHILE':([48,53,60,61,62,74,75,76,77,78,91,203,218,227,234,240,242,243,247,248,250,253,254,256,257,258,259,260,],[68,68,-40,-41,-42,-35,-43,-37,-38,-39,-36,68,68,68,-131,-72,-77,-80,-74,-78,68,68,-77,-73,-85,-81,-80,-84,]),'FROM':([48,53,60,61,62,74,75,76,77,78,91,203,218,227,234,240,242,243,247,248,250,253,254,256,257,258,259,260,],[69,69,-40,-41,-42,-35,-43,-37,-38,-39,-36,69,69,69,-131,-72,-77,-80,-74,-78,69,69,-77,-73,-85,-81,-80,-84,]),'ASSIGN':([63,79,86,92,94,116,149,230,],[-45,-131,-45,119,-51,-131,177,-50,]),'MINUS':([81,84,93,94,95,96,101,102,103,104,105,106,107,108,109,110,111,113,115,119,120,121,122,127,129,130,131,132,133,134,135,136,137,138,139,140,141,142,151,152,153,157,158,160,162,163,165,166,167,168,169,170,177,185,186,187,189,190,191,192,193,198,208,214,215,223,228,230,231,232,238,],[104,104,-52,-51,-123,-123,-109,-114,-115,-46,104,-119,-45,-122,-128,-130,-129,104,104,-46,-123,-63,104,-46,-99,-100,-101,-102,-103,-104,163,-131,104,-117,-131,-125,-126,-127,104,104,104,-46,-46,104,-46,-46,-110,-46,-46,-113,-118,-120,104,-124,104,104,104,104,104,104,-116,104,-121,-111,-112,-124,104,-50,-64,104,-54,]),'PLUS':([81,84,93,94,95,96,101,102,103,104,105,106,107,108,109,110,111,113,115,119,120,121,122,127,129,130,131,132,133,134,135,136,137,138,139,140,141,142,151,152,153,157,158,160,162,163,165,166,167,168,169,170,177,185,186,187,189,190,191,192,193,198,208,214,215,223,228,230,231,232,238,],[105,105,-52,-51,-123,-123,-109,-114,-115,-46,105,-119,-45,-122,-128,-130,-129,105,105,-46,-123,-63,105,-46,-99,-100,-101,-102,-103,-104,162,-131,105,-117,-131,-125,-126,-127,105,105,105,-46,-46,105,-46,-46,-110,-46,-46,-113,-118,-120,105,-124,105,105,105,105,105,105,-116,105,-121,-111,-112,-124,105,-50,-64,105,-54,]),'CTE_STR':([81,84,93,95,96,104,105,113,115,119,120,121,122,127,129,130,131,132,133,134,137,151,152,153,157,158,160,162,163,166,167,177,186,187,189,190,191,192,198,228,232,],[110,110,-52,-123,-123,-46,110,110,110,-46,-123,-63,110,-46,-99,-100,-101,-102,-103,-104,110,110,110,110,-46,-46,110,-46,-46,-46,-46,110,110,110,110,110,110,110,110,110,110,]),'CTE_FLOAT':([81,84,93,95,96,104,105,113,115,119,120,121,122,127,129,130,131,132,133,134,137,151,152,153,157,158,160,162,163,166,167,177,186,187,189,190,191,192,198,228,232,],[111,111,-52,-123,-123,-46,111,111,111,-46,-123,-63,111,-46,-99,-100,-101,-102,-103,-104,111,111,111,111,-46,-46,111,-46,-46,-46,-46,111,111,111,111,111,111,111,111,111,111,]),'MULT':([94,102,103,106,107,108,109,110,111,136,138,139,140,141,142,169,170,185,193,208,223,230,231,238,],[-51,-114,-115,-119,-45,-122,-128,-130,-129,166,-117,-131,-125,-126,-127,-118,-120,-124,-116,-121,-124,-50,-64,-54,]),'DIVIDE':([94,102,103,106,107,108,109,110,111,136,138,139,140,141,142,169,170,185,193,208,223,230,231,238,],[-51,-114,-115,-119,-45,-122,-128,-130,-129,167,-117,-131,-125,-126,-127,-118,-120,-124,-116,-121,-124,-50,-64,-54,]),'LESSTHAN':([94,100,101,102,103,106,107,108,109,110,111,135,136,138,139,140,141,142,161,164,165,168,169,170,185,193,208,212,213,214,215,223,230,231,238,],[-51,129,-109,-114,-115,-119,-45,-122,-128,-130,-129,-131,-131,-117,-131,-125,-126,-127,-105,-108,-110,-113,-118,-120,-124,-116,-121,-106,-107,-111,-112,-124,-50,-64,-54,]),'GREATERTHAN':([94,100,101,102,103,106,107,108,109,110,111,135,136,138,139,140,141,142,161,164,165,168,169,170,185,193,208,212,213,214,215,223,230,231,238,],[-51,130,-109,-114,-115,-119,-45,-122,-128,-130,-129,-131,-131,-117,-131,-125,-126,-127,-105,-108,-110,-113,-118,-120,-124,-116,-121,-106,-107,-111,-112,-124,-50,-64,-54,]),'LESSEQUAL':([94,100,101,102,103,106,107,108,109,110,111,135,136,138,139,140,141,142,161,164,165,168,169,170,185,193,208,212,213,214,215,223,230,231,238,],[-51,131,-109,-114,-115,-119,-45,-122,-128,-130,-129,-131,-131,-117,-131,-125,-126,-127,-105,-108,-110,-113,-118,-120,-124,-116,-121,-106,-107,-111,-112,-124,-50,-64,-54,]),'GREATEREQUAL':([94,100,101,102,103,106,107,108,109,110,111,135,136,138,139,140,141,142,161,164,165,168,169,170,185,193,208,212,213,214,215,223,230,231,238,],[-51,132,-109,-114,-115,-119,-45,-122,-128,-130,-129,-131,-131,-117,-131,-125,-126,-127,-105,-108,-110,-113,-118,-120,-124,-116,-121,-106,-107,-111,-112,-124,-50,-64,-54,]),'EQUAL':([94,100,101,102,103,106,107,108,109,110,111,135,136,138,139,140,141,142,161,164,165,168,169,170,185,193,208,212,213,214,215,223,230,231,238,],[-51,133,-109,-114,-115,-119,-45,-122,-128,-130,-129,-131,-131,-117,-131,-125,-126,-127,-105,-108,-110,-113,-118,-120,-124,-116,-121,-106,-107,-111,-112,-124,-50,-64,-54,]),'NOTEQUAL':([94,100,101,102,103,106,107,108,109,110,111,135,136,138,139,140,141,142,161,164,165,168,169,170,185,193,208,212,213,214,215,223,230,231,238,],[-51,134,-109,-114,-115,-119,-45,-122,-128,-130,-129,-131,-131,-117,-131,-125,-126,-127,-105,-108,-110,-113,-118,-120,-124,-116,-121,-106,-107,-111,-112,-124,-50,-64,-54,]),'AND':([94,99,100,101,102,103,106,107,108,109,110,111,125,126,128,135,136,138,139,140,141,142,161,164,165,168,169,170,185,188,193,208,211,212,213,214,215,223,230,231,238,],[-51,-94,-131,-109,-114,-115,-119,-45,-122,-128,-130,-129,157,-95,-97,-131,-131,-117,-131,-125,-126,-127,-105,-108,-110,-113,-118,-120,-124,-98,-116,-121,-96,-106,-107,-111,-112,-124,-50,-64,-54,]),'OR':([94,99,100,101,102,103,106,107,108,109,110,111,125,126,128,135,136,138,139,140,141,142,161,164,165,168,169,170,185,188,193,208,211,212,213,214,215,223,230,231,238,],[-51,-94,-131,-109,-114,-115,-119,-45,-122,-128,-130,-129,158,-95,-97,-131,-131,-117,-131,-125,-126,-127,-105,-108,-110,-113,-118,-120,-124,-98,-116,-121,-96,-106,-107,-111,-112,-124,-50,-64,-54,]),'UNTIL':([94,99,100,101,102,103,106,107,108,109,110,111,125,126,128,135,136,138,139,140,141,142,156,159,161,164,165,168,169,170,185,188,193,202,208,209,210,211,212,213,214,215,220,223,230,231,238,],[-51,-94,-131,-109,-114,-115,-119,-45,-122,-128,-130,-129,-131,-95,-97,-131,-131,-117,-131,-125,-126,-127,-90,-93,-105,-108,-110,-113,-118,-120,-124,-98,-116,-82,-121,-91,-92,-96,-106,-107,-111,-112,228,-124,-50,-64,-54,]),'DO':([94,99,100,101,102,103,106,107,108,109,110,111,125,126,128,135,136,138,139,140,141,142,156,159,161,164,165,168,169,170,176,185,188,193,201,208,209,210,211,212,213,214,215,223,230,231,236,238,244,245,249,],[-51,-94,-131,-109,-114,-115,-119,-45,-122,-128,-130,-129,-131,-95,-97,-131,-131,-117,-131,-125,-126,-127,-90,-93,-105,-108,-110,-113,-118,-120,-75,-124,-98,-116,219,-121,-91,-92,-96,-106,-107,-111,-112,-124,-50,-64,-79,-54,-75,-83,251,]),'THEN':([147,175,],[-75,200,]),'ELSE':([234,],[241,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'prog':([0,],[1,]),'np_goto_':([3,],[4,]),'variables':([5,117,],[6,150,]),'empty':([5,9,16,27,31,32,45,48,53,71,79,89,100,116,117,125,135,136,139,153,172,174,203,218,227,234,250,253,],[8,17,17,34,39,42,51,54,54,90,94,51,128,94,8,159,164,168,94,183,94,199,54,54,54,242,54,54,]),'np_push_global_vars_':([6,],[9,]),'variables_2':([7,31,],[10,38,]),'tipo':([7,18,31,45,89,],[11,24,11,50,50,]),'prog_funcs':([9,16,],[15,22,]),'funcion':([9,16,],[16,16,]),'func_princ':([15,],[20,]),'tipo_func':([18,],[23,]),'lista_id':([19,41,],[26,46,]),'np_end_program_':([20,],[28,]),'np_start_main_':([21,],[29,]),'dimension_var':([27,],[32,]),'np_set_scope_':([30,],[36,]),'variables_rep':([31,],[37,]),'lista_id_rep':([32,],[40,]),'funcion_param':([45,89,],[49,118,]),'estatuto_rep':([48,53,203,218,227,250,253,],[52,73,221,226,235,252,255,]),'estatuto':([48,53,203,218,227,250,253,],[53,53,53,53,53,53,53,]),'asignacion':([48,53,203,218,227,250,253,],[55,55,55,55,55,55,55,]),'llamada':([48,53,81,84,105,113,115,122,137,151,152,153,160,177,186,187,189,190,191,192,198,203,218,227,228,232,250,253,],[56,56,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,56,56,56,108,108,56,56,]),'retorno':([48,53,203,218,227,250,253,],[57,57,57,57,57,57,57,]),'lectura':([48,53,203,218,227,250,253,],[58,58,58,58,58,58,58,]),'escritura':([48,53,203,218,227,250,253,],[59,59,59,59,59,59,59,]),'decision':([48,53,203,218,227,250,253,],[60,60,60,60,60,60,60,]),'rep_c':([48,53,203,218,227,250,253,],[61,61,61,61,61,61,61,]),'rep_nc':([48,53,203,218,227,250,253,],[62,62,62,62,62,62,62,]),'np_add_func_to_directory_':([49,],[70,]),'np_push_var_':([63,86,107,144,],[79,116,139,172,]),'np_verify_function_':([63,107,],[80,80,]),'np_push_operator_':([65,66,104,119,127,157,158,162,163,166,167,],[82,83,137,151,160,186,187,189,190,191,192,]),'np_push_jump_':([68,236,],[85,245,]),'funcion_param_rep':([71,],[88,]),'np_llamada_void_':([75,],[91,]),'dimension':([79,116,139,172,],[92,149,170,195,]),'expresion':([81,84,113,115,122,151,152,153,177,186,187,198,228,232,],[97,114,146,148,154,179,180,184,202,209,210,146,236,184,]),'exp_comp':([81,84,113,115,122,151,152,153,177,186,187,198,228,232,],[99,99,99,99,99,99,99,99,99,99,99,99,99,99,]),'exp_ar':([81,84,113,115,122,151,152,153,160,177,186,187,189,190,198,228,232,],[100,100,100,100,100,100,100,100,188,100,100,100,212,213,100,100,100,]),'termino':([81,84,113,115,122,151,152,153,160,177,186,187,189,190,191,192,198,228,232,],[101,101,101,101,101,101,101,101,101,101,101,101,101,101,214,215,101,101,101,]),'unary':([81,84,105,113,115,122,137,151,152,153,160,177,186,187,189,190,191,192,198,228,232,],[102,102,138,102,102,102,169,102,102,102,102,102,102,102,102,102,102,102,102,102,102,]),'factor':([81,84,105,113,115,122,137,151,152,153,160,177,186,187,189,190,191,192,198,228,232,],[103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,]),'const':([81,84,105,113,115,122,137,151,152,153,160,177,186,187,189,190,191,192,198,228,232,],[106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,]),'np_verify_dimensions_':([93,],[120,]),'np_add_false_bottom_':([95,96,120,],[121,122,152,]),'np_quadruple_empty_return_':([98,],[124,]),'np_quadruple_logic_':([99,],[125,]),'exp_comp_2':([100,],[126,]),'comp_sym':([100,],[127,]),'np_quadruple_term':([101,],[135,]),'np_quadruple_factor_':([102,],[136,]),'np_push_const_int_':([109,],[140,]),'np_push_const_string_':([110,],[141,]),'np_push_const_float_':([111,],[142,]),'lista_lectura':([112,225,],[143,233,]),'lista_escritura':([113,198,],[145,217,]),'np_create_era_':([121,],[153,]),'np_quadruple_return_':([123,],[155,]),'expresion_2':([125,],[156,]),'exp_ar_2':([135,],[161,]),'termino_2':([136,],[165,]),'np_quadruple_IO_':([146,195,],[174,216,]),'np_gotoF_':([147,176,244,],[175,201,249,]),'np_add_vars_to_table_':([150,],[178,]),'expresion_rep':([153,],[181,]),'expresion_rep_2':([153,232,],[182,239,]),'change_sign':([169,],[193,]),'np_pop_operator_':([171,173,],[194,196,]),'lista_escritura_rep':([174,],[197,]),'np_quadruple_assignment_':([179,],[204,]),'np_manage_array_':([180,],[205,]),'np_end_of_parameters_':([181,],[206,]),'np_next_parameter_check_':([184,],[207,]),'np_remove_false_bottom_':([185,205,223,],[208,222,231,]),'np_quadruple_compare_':([188,],[211,]),'np_assign_loop_':([202,],[220,]),'np_verify_parameters_':([207,],[224,]),'np_end_function_':([229,],[237,]),'np_create_gosub_':([231,],[238,]),'decision_alt':([234,],[240,]),'np_quadruple_for_':([236,],[244,]),'np_false_condition_':([241,],[246,]),'np_end_if_actions':([242,254,],[247,256,]),'np_end_while_actions_':([243,259,],[248,260,]),'np_end_for_actions':([257,],[258,]),'np_increment_temp_':([257,],[259,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> prog","S'",1,None,None,None),
  ('prog -> PROGRAM ID np_goto_ SEMICOLON variables np_push_global_vars_ prog_funcs func_princ np_end_program_','prog',9,'p_prog','foreveralone.py',120),
  ('np_goto_ -> <empty>','np_goto_',0,'p_np_goto_','foreveralone.py',126),
  ('np_push_global_vars_ -> <empty>','np_push_global_vars_',0,'p_np_push_global_vars_','foreveralone.py',134),
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
  ('tipo -> INT','tipo',1,'p_tipo','foreveralone.py',224),
  ('tipo -> FLOAT','tipo',1,'p_tipo','foreveralone.py',225),
  ('tipo -> STRING','tipo',1,'p_tipo','foreveralone.py',226),
  ('func_princ -> PRINCIPAL np_start_main_ PARENTHESESL PARENTHESESR CURLYL estatuto_rep CURLYR','func_princ',7,'p_func_princ','foreveralone.py',232),
  ('np_start_main_ -> <empty>','np_start_main_',0,'p_np_start_main_','foreveralone.py',238),
  ('np_end_program_ -> <empty>','np_end_program_',0,'p_np_end_program_','foreveralone.py',251),
  ('funcion -> FUNC tipo_func ID np_set_scope_ PARENTHESESL funcion_param np_add_func_to_directory_ PARENTHESESR SEMICOLON variables np_add_vars_to_table_ CURLYL estatuto_rep CURLYR np_end_function_','funcion',15,'p_funcion','foreveralone.py',271),
  ('tipo_func -> tipo','tipo_func',1,'p_tipo_func','foreveralone.py',276),
  ('tipo_func -> VOID','tipo_func',1,'p_tipo_func','foreveralone.py',277),
  ('np_set_scope_ -> <empty>','np_set_scope_',0,'p_np_set_scope_','foreveralone.py',284),
  ('np_add_func_to_directory_ -> <empty>','np_add_func_to_directory_',0,'p_np_add_func_to_directory_','foreveralone.py',293),
  ('np_add_vars_to_table_ -> <empty>','np_add_vars_to_table_',0,'p_np_add_vars_to_table_','foreveralone.py',323),
  ('np_end_function_ -> <empty>','np_end_function_',0,'p_np_end_function_','foreveralone.py',342),
  ('funcion_param -> tipo ID funcion_param_rep','funcion_param',3,'p_funcion_param','foreveralone.py',357),
  ('funcion_param -> empty','funcion_param',1,'p_funcion_param','foreveralone.py',358),
  ('funcion_param_rep -> COMMA funcion_param','funcion_param_rep',2,'p_funcion_param_rep','foreveralone.py',373),
  ('funcion_param_rep -> empty','funcion_param_rep',1,'p_funcion_param_rep','foreveralone.py',374),
  ('estatuto_rep -> estatuto estatuto_rep','estatuto_rep',2,'p_estatuto_rep','foreveralone.py',381),
  ('estatuto_rep -> empty','estatuto_rep',1,'p_estatuto_rep','foreveralone.py',382),
  ('estatuto -> asignacion SEMICOLON','estatuto',2,'p_estatuto','foreveralone.py',387),
  ('estatuto -> llamada SEMICOLON np_llamada_void_','estatuto',3,'p_estatuto','foreveralone.py',388),
  ('estatuto -> retorno SEMICOLON','estatuto',2,'p_estatuto','foreveralone.py',389),
  ('estatuto -> lectura SEMICOLON','estatuto',2,'p_estatuto','foreveralone.py',390),
  ('estatuto -> escritura SEMICOLON','estatuto',2,'p_estatuto','foreveralone.py',391),
  ('estatuto -> decision','estatuto',1,'p_estatuto','foreveralone.py',392),
  ('estatuto -> rep_c','estatuto',1,'p_estatuto','foreveralone.py',393),
  ('estatuto -> rep_nc','estatuto',1,'p_estatuto','foreveralone.py',394),
  ('np_llamada_void_ -> <empty>','np_llamada_void_',0,'p_np_llamada_void_','foreveralone.py',399),
  ('np_quadruple_IO_ -> <empty>','np_quadruple_IO_',0,'p_np_quadruple_IO_','foreveralone.py',407),
  ('np_push_var_ -> <empty>','np_push_var_',0,'p_np_push_var_','foreveralone.py',415),
  ('np_push_operator_ -> <empty>','np_push_operator_',0,'p_np_push_operator_','foreveralone.py',433),
  ('np_pop_operator_ -> <empty>','np_pop_operator_',0,'p_np_pop_operator_','foreveralone.py',440),
  ('asignacion -> ID np_push_var_ dimension ASSIGN np_push_operator_ expresion np_quadruple_assignment_','asignacion',7,'p_asignacion','foreveralone.py',447),
  ('np_quadruple_assignment_ -> <empty>','np_quadruple_assignment_',0,'p_np_quadruple_assignment_','foreveralone.py',453),
  ('dimension -> SQUAREL np_verify_dimensions_ np_add_false_bottom_ expresion np_manage_array_ np_remove_false_bottom_ SQUARER','dimension',7,'p_dimension','foreveralone.py',461),
  ('dimension -> empty','dimension',1,'p_dimension','foreveralone.py',462),
  ('np_verify_dimensions_ -> <empty>','np_verify_dimensions_',0,'p_np_verify_dimensions_','foreveralone.py',467),
  ('np_manage_array_ -> <empty>','np_manage_array_',0,'p_np_manage_array_','foreveralone.py',497),
  ('llamada -> ID np_verify_function_ PARENTHESESL np_add_false_bottom_ np_create_era_ expresion_rep np_end_of_parameters_ PARENTHESESR np_remove_false_bottom_ np_create_gosub_','llamada',10,'p_llamada','foreveralone.py',508),
  ('np_verify_function_ -> <empty>','np_verify_function_',0,'p_np_verify_function_','foreveralone.py',514),
  ('expresion_rep -> expresion_rep_2','expresion_rep',1,'p_expresion_rep','foreveralone.py',524),
  ('expresion_rep -> empty','expresion_rep',1,'p_expresion_rep','foreveralone.py',525),
  ('expresion_rep_2 -> expresion np_next_parameter_check_ np_verify_parameters_ COMMA expresion_rep_2','expresion_rep_2',5,'p_expresion_rep_2','foreveralone.py',531),
  ('expresion_rep_2 -> expresion np_next_parameter_check_ np_verify_parameters_','expresion_rep_2',3,'p_expresion_rep_2','foreveralone.py',532),
  ('np_verify_parameters_ -> <empty>','np_verify_parameters_',0,'p_np_verify_parameters_','foreveralone.py',537),
  ('np_next_parameter_check_ -> <empty>','np_next_parameter_check_',0,'p_np_next_parameter_check_','foreveralone.py',550),
  ('np_end_of_parameters_ -> <empty>','np_end_of_parameters_',0,'p_np_end_of_parameters_','foreveralone.py',560),
  ('np_create_era_ -> <empty>','np_create_era_',0,'p_np_create_era_','foreveralone.py',570),
  ('np_create_gosub_ -> <empty>','np_create_gosub_',0,'p_np_create_gosub_','foreveralone.py',578),
  ('lectura -> READ np_push_operator_ PARENTHESESL lista_lectura PARENTHESESR np_pop_operator_','lectura',6,'p_lectura','foreveralone.py',598),
  ('lista_lectura -> ID np_push_var_ dimension np_quadruple_IO_ COMMA lista_lectura','lista_lectura',6,'p_lista_lectura','foreveralone.py',604),
  ('lista_lectura -> ID np_push_var_ dimension np_quadruple_IO_','lista_lectura',4,'p_lista_lectura','foreveralone.py',605),
  ('escritura -> PRINT np_push_operator_ PARENTHESESL lista_escritura PARENTHESESR np_pop_operator_','escritura',6,'p_escritura','foreveralone.py',611),
  ('lista_escritura -> expresion np_quadruple_IO_ lista_escritura_rep','lista_escritura',3,'p_lista_escritura','foreveralone.py',617),
  ('lista_escritura_rep -> COMMA lista_escritura','lista_escritura_rep',2,'p_lista_escritura_rep','foreveralone.py',623),
  ('lista_escritura_rep -> empty','lista_escritura_rep',1,'p_lista_escritura_rep','foreveralone.py',624),
  ('decision -> IF PARENTHESESL expresion PARENTHESESR np_gotoF_ THEN CURLYL estatuto_rep CURLYR decision_alt','decision',10,'p_decision','foreveralone.py',629),
  ('decision_alt -> ELSE np_false_condition_ CURLYL estatuto_rep CURLYR np_end_if_actions','decision_alt',6,'p_decision_alt','foreveralone.py',635),
  ('decision_alt -> empty np_end_if_actions','decision_alt',2,'p_decision_alt','foreveralone.py',636),
  ('np_gotoF_ -> <empty>','np_gotoF_',0,'p_np_gotoF_','foreveralone.py',642),
  ('np_false_condition_ -> <empty>','np_false_condition_',0,'p_np_false_condition_','foreveralone.py',653),
  ('np_end_if_actions -> <empty>','np_end_if_actions',0,'p_np_end_if_actions','foreveralone.py',665),
  ('rep_c -> WHILE np_push_jump_ PARENTHESESL expresion PARENTHESESR np_gotoF_ DO CURLYL estatuto_rep CURLYR np_end_while_actions_','rep_c',11,'p_rep_c','foreveralone.py',673),
  ('np_push_jump_ -> <empty>','np_push_jump_',0,'p_np_push_jump_','foreveralone.py',679),
  ('np_end_while_actions_ -> <empty>','np_end_while_actions_',0,'p_np_end_while_actions_','foreveralone.py',686),
  ('rep_nc -> FROM ID np_push_var_ dimension ASSIGN expresion np_assign_loop_ UNTIL expresion np_quadruple_for_ np_gotoF_ DO CURLYL estatuto_rep CURLYR np_end_for_actions','rep_nc',16,'p_rep_nc','foreveralone.py',696),
  ('np_assign_loop_ -> <empty>','np_assign_loop_',0,'p_np_assign_loop_','foreveralone.py',702),
  ('np_quadruple_for_ -> np_push_jump_','np_quadruple_for_',1,'p_np_quadruple_for_','foreveralone.py',709),
  ('np_end_for_actions -> np_increment_temp_ np_end_while_actions_','np_end_for_actions',2,'p_np_end_for_actions','foreveralone.py',730),
  ('np_increment_temp_ -> <empty>','np_increment_temp_',0,'p_np_increment_temp_','foreveralone.py',735),
  ('retorno -> RETURN PARENTHESESL expresion PARENTHESESR np_quadruple_return_','retorno',5,'p_retorno','foreveralone.py',742),
  ('retorno -> RETURN PARENTHESESL PARENTHESESR np_quadruple_empty_return_','retorno',4,'p_retorno','foreveralone.py',743),
  ('np_quadruple_return_ -> <empty>','np_quadruple_return_',0,'p_np_quadruple_return_','foreveralone.py',748),
  ('np_quadruple_empty_return_ -> <empty>','np_quadruple_empty_return_',0,'p_np_quadruple_empty_return_','foreveralone.py',762),
  ('expresion -> exp_comp np_quadruple_logic_ expresion_2','expresion',3,'p_expresion','foreveralone.py',773),
  ('expresion_2 -> AND np_push_operator_ expresion','expresion_2',3,'p_expresion_2','foreveralone.py',778),
  ('expresion_2 -> OR np_push_operator_ expresion','expresion_2',3,'p_expresion_2','foreveralone.py',779),
  ('expresion_2 -> empty','expresion_2',1,'p_expresion_2','foreveralone.py',780),
  ('np_quadruple_logic_ -> <empty>','np_quadruple_logic_',0,'p_np_quadruple_logic_','foreveralone.py',786),
  ('exp_comp -> exp_ar exp_comp_2','exp_comp',2,'p_exp_comp','foreveralone.py',795),
  ('exp_comp_2 -> comp_sym np_push_operator_ exp_ar np_quadruple_compare_','exp_comp_2',4,'p_exp_comp_2','foreveralone.py',800),
  ('exp_comp_2 -> empty','exp_comp_2',1,'p_exp_comp_2','foreveralone.py',801),
  ('np_quadruple_compare_ -> <empty>','np_quadruple_compare_',0,'p_np_quadruple_compare_','foreveralone.py',807),
  ('comp_sym -> LESSTHAN','comp_sym',1,'p_comp_sym','foreveralone.py',816),
  ('comp_sym -> GREATERTHAN','comp_sym',1,'p_comp_sym','foreveralone.py',817),
  ('comp_sym -> LESSEQUAL','comp_sym',1,'p_comp_sym','foreveralone.py',818),
  ('comp_sym -> GREATEREQUAL','comp_sym',1,'p_comp_sym','foreveralone.py',819),
  ('comp_sym -> EQUAL','comp_sym',1,'p_comp_sym','foreveralone.py',820),
  ('comp_sym -> NOTEQUAL','comp_sym',1,'p_comp_sym','foreveralone.py',821),
  ('exp_ar -> termino np_quadruple_term exp_ar_2','exp_ar',3,'p_exp_ar','foreveralone.py',827),
  ('exp_ar_2 -> PLUS np_push_operator_ exp_ar','exp_ar_2',3,'p_exp_ar_2','foreveralone.py',832),
  ('exp_ar_2 -> MINUS np_push_operator_ exp_ar','exp_ar_2',3,'p_exp_ar_2','foreveralone.py',833),
  ('exp_ar_2 -> empty','exp_ar_2',1,'p_exp_ar_2','foreveralone.py',834),
  ('np_quadruple_term -> <empty>','np_quadruple_term',0,'p_np_quadruple_term','foreveralone.py',840),
  ('termino -> unary np_quadruple_factor_ termino_2','termino',3,'p_termino','foreveralone.py',849),
  ('termino_2 -> MULT np_push_operator_ termino','termino_2',3,'p_termino_2','foreveralone.py',854),
  ('termino_2 -> DIVIDE np_push_operator_ termino','termino_2',3,'p_termino_2','foreveralone.py',855),
  ('termino_2 -> empty','termino_2',1,'p_termino_2','foreveralone.py',856),
  ('np_quadruple_factor_ -> <empty>','np_quadruple_factor_',0,'p_np_quadruple_factor_','foreveralone.py',862),
  ('unary -> factor','unary',1,'p_unary','foreveralone.py',871),
  ('unary -> MINUS np_push_operator_ unary change_sign','unary',4,'p_unary','foreveralone.py',872),
  ('unary -> PLUS unary','unary',2,'p_unary','foreveralone.py',873),
  ('change_sign -> <empty>','change_sign',0,'p_change_sign','foreveralone.py',880),
  ('factor -> const','factor',1,'p_factor','foreveralone.py',886),
  ('factor -> ID np_push_var_ dimension','factor',3,'p_factor','foreveralone.py',887),
  ('factor -> PARENTHESESL np_add_false_bottom_ expresion PARENTHESESR np_remove_false_bottom_','factor',5,'p_factor','foreveralone.py',888),
  ('factor -> llamada','factor',1,'p_factor','foreveralone.py',889),
  ('np_add_false_bottom_ -> <empty>','np_add_false_bottom_',0,'p_np_add_false_bottom_','foreveralone.py',895),
  ('np_remove_false_bottom_ -> <empty>','np_remove_false_bottom_',0,'p_np_remove_false_bottom_','foreveralone.py',901),
  ('const -> CTE_INT np_push_const_int_','const',2,'p_const','foreveralone.py',907),
  ('const -> CTE_STR np_push_const_string_','const',2,'p_const','foreveralone.py',908),
  ('const -> CTE_FLOAT np_push_const_float_','const',2,'p_const','foreveralone.py',909),
  ('np_push_const_int_ -> <empty>','np_push_const_int_',0,'p_np_push_const_int_','foreveralone.py',914),
  ('np_push_const_float_ -> <empty>','np_push_const_float_',0,'p_np_push_const_float_','foreveralone.py',923),
  ('np_push_const_string_ -> <empty>','np_push_const_string_',0,'p_np_push_const_string_','foreveralone.py',931),
  ('empty -> <empty>','empty',0,'p_empty','foreveralone.py',940),
]
