import ply.lex as lex
import ply.yacc as yacc
import sys
import json
from virtual_machine import VirtualMachine
from functions_table import FunctionsTable
from intermediate_code import InterCode

dir_func = FunctionsTable()
inter_code = InterCode()
current_scope = 'global'
current_type = ''
func_to_call = ''

# PALABRAS RESERVADAS
reserved = {
    'programa' : 'PROGRAM',
    'var' : 'VAR',
    'funcion' : 'FUNC',
    'int' : 'INT',
    'float' : 'FLOAT',
    'string' : 'STRING',
    'void' : 'VOID',
    'principal' : 'PRINCIPAL',
    'regresa'   : 'RETURN',
    'escribe'   : 'PRINT',
    'lee'       : 'READ',
    'mientras'  : 'WHILE',
    'desde'     : 'FROM',
    'hasta'     : 'UNTIL',
    'hacer'     : 'DO',
    'si'        : 'IF',
    'entonces'  : 'THEN',
    'sino'      : 'ELSE'
}

# TOKENS
tokens = [
    'ID',
    'SEMICOLON',
    'COLON',
    'COMMA',
    'CTE_INT',
    'CTE_FLOAT',
    'CTE_STR',
    'CURLYL',
    'CURLYR',
    'PARENTHESESL',
    'PARENTHESESR',
    'SQUAREL',
    'SQUARER',
    'PLUS',
    'MINUS',
    'MULT',
    'DIVIDE',
    'ASSIGN',
    'NOTEQUAL',
    'LESSTHAN',
    'GREATERTHAN',
    'LESSEQUAL',
    'GREATEREQUAL',
    'EQUAL',
    'AND',
    'OR'
] + list(reserved.values())

t_SEMICOLON = r';'
t_COLON = r':'
t_COMMA = r','
t_CURLYL = r'\{'
t_CURLYR = r'}'
t_PARENTHESESL = r'\('
t_PARENTHESESR = r'\)'
t_SQUAREL = r'\['
t_SQUARER = r'\]'
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULT = r'\*'
t_DIVIDE = r'/'
t_ASSIGN = r'='
t_NOTEQUAL = r'!='
t_LESSTHAN = r'<'
t_GREATERTHAN = r'>'
t_LESSEQUAL = r'<='
t_GREATEREQUAL = r'>='
t_EQUAL = r'=='
t_AND = r'\&'
t_OR = r'\|'

# caracteres ignorados (en blanco)
t_ignore  = ' \t\n'

# regla para manejar errores
def t_error(t):
    # print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_CTE_FLOAT(t):
    r'\d*\.[\d]+'
    t.value = float(t.value)
    return t

def t_CTE_INT(t):
    r'0|[1-9]\d*'
    t.value = int(t.value)
    return t

def t_CTE_STR(t):
    r'[\'][^\']*[\']|["][^"]*["]'
    return t

def t_ID(t):
    r'[a-zA-Z][\w\d]*'
    t.type = reserved.get(t.value, 'ID')
    return t

lexer = lex.lex()

def p_prog(p):
    '''
        prog : PROGRAM ID np_goto_ SEMICOLON variables np_push_global_vars_ prog_funcs func_princ np_end_program_
    '''

    # print(dir_func)
    # print(inter_code.mem)
    # counter = 0
    # for x in inter_code.quadruples:
    #     print(counter, " ",x)
    #     counter+=1

def p_np_goto_(p):
    '''
        np_goto_ :
    '''
    # Add empty goto quadruple
    inter_code.add_goto_quadruple(None)
    inter_code.push_jump(-1)

def p_np_push_global_vars_(p):
    '''
        np_push_global_vars_ :
    '''
    # Add variables to variable table for the global scope
    if p[-1] is not None:
        for i in p[-1]:
            dir = inter_code.mem.global_.add_value(i[0],i[2])
            dir_func.functions['global'].add_variable(i[0], i[2], dir)
            if i[1] is not None:
                dim = inter_code.mem.constant_.get_value(i[1])
                dir_func.functions['global'].variables[i[0]].array_size = i[1]
                x=1
                while x < dim:
                    inter_code.mem.global_.add_value(i[0]+str(x),i[2])
                    x+=1

def p_prog_funcs(p):
    '''
        prog_funcs : funcion prog_funcs
        | empty
    '''

def p_variables(p):
    '''
        variables : VAR variables_2
        | empty
    '''
    # if there are variables, return the list
    if p[1] == 'var':
        p[0] = p[2]

def p_variables_2(p):
    '''
        variables_2 : tipo COLON lista_id SEMICOLON variables_rep
    '''
    # add the current type to each ID in the list
    for i in p[3]:
        i.append(p[1])
    # add the result of the recursion to the list
    if p[5] is not None:
        for j in p[5]:
            p[3].append(j)
    # return the list
    p[0] = p[3]

def p_variables_rep(p):
    '''
        variables_rep : variables_2
        | empty
    '''
    # Call recursion
    p[0] = p[1]

def p_lista_id(p):
    '''
        lista_id : ID dimension_var lista_id_rep
    '''
    # create a list of IDs, appending the new ID in each recursion
    p[0] = []
    #       Appends current ID
    p[0].append([p[1],p[2]])
    #       Appends result of recursion
    if p[3] is not None:
        for x in p[3]:
            p[0].append(x)

def p_lista_id_rep(p):
    '''
        lista_id_rep : COMMA lista_id
        | empty
    '''
    # if there is a comma, call the function to get the next ID
    if p[1] == ',':
        p[0] = p[2]
    else:
        p[0] = None

def p_dimension_var(p):
    '''
        dimension_var : SQUAREL CTE_INT SQUARER
        | empty
    '''
    if p[1] is not None:
        p[0] = inter_code.mem.constant_.add_value(int(p[2]),'int')

def p_tipo(p):
    '''
        tipo : INT
        | FLOAT
        | STRING
    '''

    p[0] = p[1]

def p_func_princ(p):
    '''
        func_princ : PRINCIPAL np_start_main_ PARENTHESESL PARENTHESESR CURLYL estatuto_rep CURLYR
    '''
def p_np_start_main_(p):
    '''
        np_start_main_ :
    '''
    global current_scope, current_type
    current_scope = 'global'
    current_type = 'void'
    main = inter_code.jumps_stack.pop()
    inter_code.fill(main,len(inter_code.quadruples))

def p_np_end_program_(p):
    '''
        np_end_program_ :
    '''
    inter_code.add_endprog_quad()
    output = {
        'Constants': inter_code.mem.constant_.output(),
        'Quadruples': inter_code.quadruples,
        'DirFunc': dir_func.output()
    }
    inter_code.mem.constant_.reset_memory()
    with open("pleasedont.cry","w+") as json_file:
        json.dump(output, json_file)

    vm = VirtualMachine()

def p_funcion(p):
    '''
        funcion : FUNC tipo_func ID np_set_scope_ PARENTHESESL funcion_param np_add_func_to_directory_ PARENTHESESR SEMICOLON variables np_add_vars_to_table_ CURLYL estatuto_rep CURLYR np_end_function_
    '''

def p_np_end_function_(p):
    '''
        np_end_function_ :
    '''
    global current_scope, current_type
    if str(current_type) != 'void' and not inter_code.does_return:
        raise Exception('Function "'+str(current_scope)+'" should have a return value.')
    temps = inter_code.mem.temp_.count_content()
    inter_code.add_endfunc()
    dir_func.functions[current_scope].space_needed += temps

def p_np_set_scope_(p):
    '''
        np_set_scope_ :
    '''
    global current_scope, current_type
    current_scope = p[-1]
    current_type = p[-2]

def p_np_add_func_to_directory_(p):
    '''
        np_add_func_to_directory_ :
    '''
    global current_scope, current_type
    temp = []

    # Add function to global variable table, and include the virtual address of the return value
    if current_type == 'void':
        faddr = None
    else:
        faddr = inter_code.mem.global_.add_value(current_scope,current_type)
    dir_func.functions['global'].add_variable(current_scope,current_type,faddr)

    if p[-1] is not None:
        for i in p[-1]:
            temp.append(i[1])
    # Add function to functions directory
    dir_func.add_function(current_scope, current_type, temp)

    # Add parameters to variable table for current function
    if p[-1] is not None:
        for i in p[-1]:
            dir = inter_code.mem.local_.add_value(i[0],i[1])
            dir_func.functions[current_scope].add_variable(i[0], i[1], dir)

    # Add start quadruple to function
    dir_func.functions[current_scope].quad = len(inter_code.quadruples)

def p_np_add_vars_to_table_(p):
    '''
        np_add_vars_to_table_ :
    '''
    global current_scope
    # add variables to variable table
    if p[-1] is not None:
        for i in p[-1]:
            dir = inter_code.mem.local_.add_value(i[0],i[2])
            dir_func.functions[current_scope].add_variable(i[0], i[2],dir)
            if i[1] is not None:
                dir_func.functions[current_scope].variables[i[0]].array_size = int(i[1])
                x=1
                while x < int(i[1]):
                    inter_code.mem.global_.add_value(i[0]+str(x),i[2])
                    x+=1

def p_tipo_func(p):
    '''
        tipo_func : tipo
        | VOID
    '''
    # return type
    p[0] = p[1]

def p_funcion_param(p):
    '''
        funcion_param : tipo ID funcion_param_rep
        | empty
    '''
    temp = []
    if p[1] is not None:
        # Append current id and its type
        temp.append([p[2], p[1]])
        # Append result of recursion
        if p[3] is not None:
            for x in p[3]:
                temp.append(x)
        p[0] = temp

def p_funcion_param_rep(p):
    '''
        funcion_param_rep : COMMA funcion_param
        | empty
    '''
    if p[1] is not None:
        p[0] = p[2]

def p_estatuto_rep(p):
    '''
        estatuto_rep : estatuto estatuto_rep
        | empty
    '''

def p_estatuto(p):
    '''
        estatuto : asignacion SEMICOLON
        | llamada SEMICOLON np_llamada_void_
        | retorno SEMICOLON
        | lectura SEMICOLON
        | escritura SEMICOLON
        | decision
        | rep_c
        | rep_nc
    '''

def p_np_llamada_void_(p):
    '''
        np_llamada_void_ :
    '''
    inter_code.variable_stack.pop()
    inter_code.type_stack.pop()

def p_np_quadruple_assignment_(p):
    '''
        np_quadruple_assignment_ :
    '''
    # llamar a func de crear quad de asignacion dentro de inter_code
    if inter_code.operator_stack!= []:
        inter_code.add_assignment_quadruple()

def p_np_quadruple_IO_(p):
    '''
        np_quadruple_IO_ :
    '''
    # llamar a func de crear quad de asignacion dentro de inter_code
    if inter_code.operator_stack!= []:
        inter_code.add_IO_quadruple()

def p_np_push_var_(p):
    '''
        np_push_var_ :
    '''
    global current_scope
    if dir_func.functions[current_scope].variable_exists(p[-1]):
        var_type = dir_func.functions[current_scope].variables[p[-1]].type
        var = dir_func.functions[current_scope].variables[p[-1]].dir
    elif dir_func.functions['global'].variable_exists(p[-1]):
        var_type = dir_func.functions['global'].variables[p[-1]].type
        var = dir_func.functions['global'].variables[p[-1]].dir
    else:
        raise Exception('Variable "'+ str(p[-1]) +'" does not exist')
    inter_code.variable_stack.append(var)
    inter_code.type_stack.append(var_type)
    # print(inter_code.variable_stack)
    # print(inter_code.type_stack)
    # print(inter_code.operator_stack)
    # print(inter_code.jumps_stack)
    # print('\n')

def p_np_push_operator_(p):
    '''
        np_push_operator_ :
    '''
    inter_code.operator_stack.append(p[-1])
    # print(inter_code.variable_stack)
    # print(inter_code.type_stack)
    # print(inter_code.operator_stack)
    # print(inter_code.jumps_stack)
    # print('\n')

def p_np_pop_operator_(p):
    '''
        np_pop_operator_ :
    '''
    inter_code.operator_stack.pop()

def p_asignacion(p):
    '''
        asignacion : ID np_push_var_ dimension ASSIGN np_push_operator_ expresion np_quadruple_assignment_
    '''
    p[0]=p[6]
    # dejar igual, solo después de dimension hacer un pop al stack del resultado de la variable dimensionada y otro push de eso nuevo usando el mismo np

def p_dimension(p):
    '''
        dimension : SQUAREL np_verify_dimensions_ np_add_false_bottom_ expresion np_manage_array_ np_remove_false_bottom_ SQUARER
        | empty
    '''
    # p[0] = dirección de p[-1] + dirección de expresion
def p_np_verify_dimensions_(p):
    '''
        np_verify_dimensions_ :
    '''
    global current_scope
    # Get variable and its type
    id_dir = inter_code.variable_stack.pop()
    type = inter_code.type_stack.pop()
    # check if it's a local or global variable, and get the name. Then get the size from the correct variable table.
    if id_dir < inter_code.mem._BASE_LOCAL:
        id = inter_code.mem.global_.get_value(id_dir)
        size = dir_func.functions['global'].variables[str(id)].array_size
    else:
        id = inter_code.mem.local_.get_value(id_dir)
        size = dir_func.functions[current_scope].variables[str(id)].array_size

    # Verify if the variable has dimensions
    if size == 0:
        if p[-1] == '[':
            raise Exception('Type mismatch: The variable ' + id + ' is not an array.')
    else:
        if p[-1] != '[':
            raise Exception('Type mismatch: The variable ' + id + ' is declared as an array.')
        # add the virtual address as a constant in order to use it for quadruple operations
        initial_dir = inter_code.mem.constant_.add_value(int(id_dir),'int')
        # adds the address as a constant and the limit of the array to the variable stack, as well as the variable type.
        inter_code.variable_stack.append(initial_dir)
        inter_code.type_stack.append(type)
        inter_code.variable_stack.append(size)

def p_np_manage_array_(p):
    '''
        np_manage_array_ :
    '''
    if inter_code.type_stack[-1]!='int':
        raise Exception('Type mismatch: array dimesions must be integers.')
    inter_code.add_verify_limits_quadruple()
    inter_code.add_array_base_direction_quadruple()

def p_llamada(p):
    '''
        llamada : ID np_verify_function_ PARENTHESESL np_add_false_bottom_ np_create_era_ expresion_rep np_end_of_parameters_ PARENTHESESR np_remove_false_bottom_ np_create_gosub_
    '''

def p_expresion_rep(p):
    '''
        expresion_rep : expresion_rep_2
        | empty
    '''

def p_expresion_rep_2(p):
    '''
        expresion_rep_2 : expresion np_verify_parameters_ COMMA np_next_parameter_check_ expresion_rep_2
        | expresion np_check np_verify_parameters_
    '''

def p_np_verify_function_(p):
    '''
        np_verify_function_ :
    '''
    global func_to_call
    if not dir_func.function_exists(p[-1]):
        raise Exception('Syntax error: function '+ func_to_call +' does not exist.')
    func_to_call = p[-1]
    # inter_code.variable_stack.append(p[-1])

def p_np_verify_parameters_(p):
    '''
        np_verify_parameters_ :
    '''
    global func_to_call
    argument = inter_code.variable_stack.pop()
    arg_type = inter_code.type_stack.pop()
    # print('lo que esta en el varstack es '+ str(inter_code.variable_stack[-1]) + " osea " + str(inter_code.mem.get_value(inter_code.variable_stack[-1])))
    if arg_type == dir_func.functions[func_to_call].parameters[inter_code.parameter_counter-1]:
        inter_code.add_parameter_quadruple(argument)
    else:
        raise Exception('Type mismatch: Argument type does not match function parameter')

def p_np_next_parameter_check_(p):
    '''
        np_next_parameter_check_ :
    '''
    global func_to_call
    global current_scope
    if len(dir_func.functions[func_to_call].parameters) < inter_code.parameter_counter:
        raise Exception('Number of arguments in call do not match parameters.')

def p_np_end_of_parameters_(p):
    '''
        np_end_of_parameters_ :
    '''
    global func_to_call
    global current_scope
    if len(dir_func.functions[func_to_call].parameters) >= inter_code.parameter_counter:
        raise Exception('Number of arguments in call do not match parameters ('+str(len(dir_func.functions[func_to_call].parameters))+') vs ('+str(inter_code.parameter_counter)+').')

def p_np_create_era_(p):
    '''
        np_create_era_ :
    '''
    global func_to_call
    inter_code.add_era_quadruple(func_to_call, dir_func.functions[func_to_call].space_needed)

def p_np_create_gosub_(p):
    '''
        np_create_gosub_ :
    '''
    global func_to_call
    scope = dir_func.functions[func_to_call].quad
    inter_code.add_gosub_quadruple(func_to_call, scope)
    # si tiene direccion vas aaaaaaaaaaaaaaaaaa ir por la direccion a la tabla de variables global y asignarle ese valor a un temporal del mismo tipo
    # asignar return value a un temporal
    ret_dir = dir_func.functions['global'].variables[func_to_call].dir
    if ret_dir is not None:
        ret_type = inter_code.mem.global_.check_type(ret_dir)
        inter_code.variable_stack.append(ret_dir)
        inter_code.type_stack.append(ret_type)
        inter_code.add_assign_temp_quadruple()
    else:
        inter_code.variable_stack.append(ret_dir)
        inter_code.type_stack.append(None)
    # print(inter_code.variable_stack)
    # print(inter_code.type_stack)
    # print(inter_code.operator_stack)
    # print(inter_code.jumps_stack)
    func_to_call = ''

def p_lectura(p):
    '''
        lectura : READ np_push_operator_ PARENTHESESL lista_lectura PARENTHESESR np_pop_operator_
    '''

def p_lista_lectura(p):
    '''
        lista_lectura : ID np_push_var_ dimension np_quadruple_IO_ COMMA lista_lectura
        | ID np_push_var_ dimension np_quadruple_IO_
    '''

def p_escritura(p):
    '''
        escritura : PRINT np_push_operator_ PARENTHESESL lista_escritura PARENTHESESR np_pop_operator_
    '''

def p_lista_escritura(p):
    '''
        lista_escritura : expresion np_quadruple_IO_ lista_escritura_rep
    '''

def p_lista_escritura_rep(p):
    '''
        lista_escritura_rep : COMMA lista_escritura
        | empty
    '''

def p_decision(p):
    '''
        decision : IF PARENTHESESL expresion PARENTHESESR np_gotoF_ THEN CURLYL estatuto_rep CURLYR decision_alt
    '''

def p_decision_alt(p):
    '''
        decision_alt : ELSE np_false_condition_ CURLYL estatuto_rep CURLYR np_end_if_actions
        | empty np_end_if_actions
    '''

def p_np_gotoF_(p):
    '''
        np_gotoF_ :
    '''
    exp_type = inter_code.type_stack.pop()
    if exp_type != 'bool':
        raise Exception('Type mismatch ', inter_code.variable_stack.pop()," ",exp_type )
    else :
        inter_code.add_gotof_quadruple(None)

def p_np_false_condition_(p):
    '''
        np_false_condition_ :
    '''
    inter_code.add_goto_quadruple(None)
    false = inter_code.jumps_stack.pop()
    inter_code.push_jump(-1)
    inter_code.fill(false, len(inter_code.quadruples))

def p_np_end_if_actions(p):
    '''
        np_end_if_actions :
    '''
    end = inter_code.jumps_stack.pop()
    inter_code.fill(end,len(inter_code.quadruples))

def p_rep_c(p):
    '''
        rep_c : WHILE np_push_jump_ PARENTHESESL expresion PARENTHESESR np_gotoF_ DO CURLYL estatuto_rep CURLYR np_end_while_actions_
    '''

def p_np_push_jump_(p):
    '''
        np_push_jump_ :
    '''
    inter_code.push_jump(0)

def p_np_end_while_actions_(p):
    '''
        np_end_while_actions_ :
    '''
    end = inter_code.jumps_stack.pop()
    ret = inter_code.jumps_stack.pop()
    inter_code.add_goto_quadruple(ret)
    inter_code.fill(end, len(inter_code.quadruples))

def p_rep_nc(p):
    '''
        rep_nc : FROM expresion np_assign_temp_ UNTIL expresion np_quadruple_for_ np_gotoF_ DO CURLYL estatuto_rep CURLYR np_end_for_actions
    '''

def p_np_assign_temp_(p):
    '''
        np_assign_temp_ :
    '''
    inter_code.add_assign_temp_quadruple()

def p_np_quadruple_for_(p):
    '''
        np_quadruple_for_ : np_push_jump_
    '''
    # checar que las dos expresion es sean enteras
    val1_type = inter_code.type_stack.pop()
    val2_type = inter_code.type_stack.pop()
    val1 = inter_code.variable_stack.pop()
    val2 = inter_code.variable_stack.pop()
    if val1_type == 'int' and val2_type == 'int':
        inter_code.type_stack.append(val2_type)
        inter_code.type_stack.append(val2_type)
        inter_code.type_stack.append(val1_type)
        inter_code.variable_stack.append(val2)
        inter_code.variable_stack.append(val2)
        inter_code.variable_stack.append(val1)
        inter_code.operator_stack.append("<=")
        inter_code.add_operation_quadruple()
    else:
        raise Exception('ERROR type mismatch. Solo se pueden usar enteros en un ciclo no condicional.')

def p_np_end_for_actions(p):
    '''
        np_end_for_actions : np_increment_temp_ np_end_while_actions_
    '''

def p_np_increment_temp_(p):
    '''
        np_increment_temp_ :
    '''
    inter_code.add_self_increment_quadruple(1)

def p_retorno(p):
    '''
        retorno : RETURN PARENTHESESL expresion PARENTHESESR np_quadruple_return_
        | RETURN PARENTHESESL PARENTHESESR np_quadruple_empty_return_
    '''

def p_np_quadruple_return_(p):
    '''
        np_quadruple_return_ :
    '''
    global current_type, current_scope
    # get the virtual address of the function in order to leave the return value there
    func_addr = dir_func.functions['global'].variables[current_scope].dir
    if func_addr is None:
        raise Exception('Type mismatch: Void function cannot have a return value.')
    inter_code.variable_stack.append(func_addr)
    inter_code.type_stack.append(current_type)
    inter_code.add_return_quadruple()

def p_np_quadruple_empty_return_(p):
    '''
        np_quadruple_empty_return_ :
    '''
    global current_type, current_scope
    # get the virtual address of the function in order to leave the return value there
    func_addr = dir_func.functions['global'].variables[current_scope].dir
    if func_addr is not None:
        raise Exception('Type mismatch: non-void function has to have a return value.')
    inter_code.add_empty_return_quadruple()

def p_expresion(p):
    '''
        expresion : exp_comp np_quadruple_logic_ expresion_2
    '''
    # var = inter_code.variable_stack.pop()
    # var_type = inter_code.type_stack.pop()
    # if var_type = 'int':
    #     p[0]=var
    # inter_code.variable_stack.append(var)
    # inter_code.type_stack.append(var_type)

def p_expresion_2(p):
    '''
        expresion_2 : AND np_push_operator_ expresion
        | OR np_push_operator_ expresion
        | empty
    '''

def p_np_quadruple_logic_(p):
    '''
        np_quadruple_logic_ :
    '''
    if inter_code.operator_stack!= []:
        if inter_code.operator_stack[len(inter_code.operator_stack)-1] in ['&', '|']:
            inter_code.add_operation_quadruple()

def p_exp_comp(p):
    '''
        exp_comp : exp_ar exp_comp_2
    '''

def p_exp_comp_2(p):
    '''
        exp_comp_2 : comp_sym np_push_operator_ exp_ar np_quadruple_compare_
        | empty
    '''

def p_np_quadruple_compare_(p):
    '''
        np_quadruple_compare_ :
    '''
    if inter_code.operator_stack!= []:
        if inter_code.operator_stack[len(inter_code.operator_stack)-1] in ['<', '>', '>=', '<=','==', '!=']:
            inter_code.add_operation_quadruple()
        else:
            raise Exception('tronando como palomitas')

def p_comp_sym(p):
    '''
        comp_sym : LESSTHAN
        | GREATERTHAN
        | LESSEQUAL
        | GREATEREQUAL
        | EQUAL
        | NOTEQUAL
    '''
    p[0] = p[1]

def p_exp_ar(p):
    '''
        exp_ar : termino np_quadruple_term exp_ar_2
    '''

def p_exp_ar_2(p):
    '''
        exp_ar_2 : PLUS np_push_operator_ exp_ar
        | MINUS np_push_operator_ exp_ar
        | empty
    '''

def p_np_quadruple_term(p):
    '''
        np_quadruple_term :
    '''
    if inter_code.operator_stack!= []:
        if inter_code.operator_stack[len(inter_code.operator_stack)-1] in ['+', '-']:
            inter_code.add_operation_quadruple()

def p_termino(p):
    '''
        termino : unary np_quadruple_factor_ termino_2
    '''

def p_termino_2(p):
    '''
        termino_2 : MULT np_push_operator_ termino
        | DIVIDE np_push_operator_ termino
        | empty
    '''

def p_np_quadruple_factor_(p):
    '''
        np_quadruple_factor_ :
    '''
    if inter_code.operator_stack != []:
        if inter_code.operator_stack[len(inter_code.operator_stack)-1] in ['*', '/']:
            inter_code.add_operation_quadruple()

# UNARY--------------------------------
def p_unary(p):
    '''
        unary : factor
        | MINUS np_push_operator_ unary change_sign
        | PLUS unary
    '''
    p[0]=p[1]

def p_change_sign(p):
    '''
        change_sign :
    '''
    inter_code.add_unary_quadruple()

# ---------------------------------------
def p_factor(p):
    '''
        factor : const
        | ID np_push_var_ dimension
        | PARENTHESESL np_add_false_bottom_ expresion PARENTHESESR np_remove_false_bottom_
        | llamada
    '''

def p_np_add_false_bottom_(p):
    '''
        np_add_false_bottom_ :
    '''
    inter_code.operator_stack.append('(')
    # print(inter_code.variable_stack)
    # print(inter_code.type_stack)
    # print(inter_code.operator_stack)
    # print(inter_code.jumps_stack)
    # print('\n')

def p_np_remove_false_bottom_(p):
    '''
        np_remove_false_bottom_ :
    '''
    fb = inter_code.operator_stack.pop()
    if fb != '(':
        raise Exception('el false bottom no jalo')

    # print(inter_code.variable_stack)
    # print(inter_code.type_stack)
    # print(inter_code.operator_stack)
    # print(inter_code.jumps_stack)
    # print('\n')

def p_const(p):
    '''
        const : CTE_INT np_push_const_int_
        | letrero
        | CTE_FLOAT np_push_const_float_
    '''

def p_np_push_const_int_(p):
    '''
        np_push_const_int_ :
    '''
    var = inter_code.mem.constant_.add_value(int(p[-1]),'int')
    inter_code.variable_stack.append(var)
    # print(inter_code.variable_stack)
    inter_code.type_stack.append('int')
    # print(inter_code.type_stack)
    # print(inter_code.operator_stack)
    # print(inter_code.jumps_stack)
    # print('\n')

def p_np_push_const_float_(p):
    '''
        np_push_const_float_ :
    '''
    var = inter_code.mem.constant_.add_value(float(p[-1]),'float')
    inter_code.variable_stack.append(var)
    # print(inter_code.variable_stack)
    inter_code.type_stack.append('float')
    # print(inter_code.type_stack)
    # print(inter_code.operator_stack)
    # print(inter_code.jumps_stack)
    # print('\n')

def p_np_push_const_string_(p):
    '''
        np_push_const_string_ :
    '''
    var = inter_code.mem.constant_.add_value(str(p[-1][1:-1]),'string')
    inter_code.variable_stack.append(var)
    # print(inter_code.variable_stack)
    inter_code.type_stack.append('string')
    # print(inter_code.type_stack)
    # print(inter_code.operator_stack)
    # print(inter_code.jumps_stack)
    # print('\n')

def p_letrero(p):
    '''
        letrero : CTE_STR np_push_const_string_
    '''

def p_empty(p):
    '''
        empty :
    '''

def p_np_check(p):
    '''
        np_check :
    '''
    # print('BEEP BEEP I AM HERE I AM CHECK')

def p_error(p):
   print("Syntax error", p)

parser = yacc.yacc()

def main():
    arch_name = sys.argv[1]
    try:
        arch = open(arch_name,'r')
        info = arch.read()
        arch.close()
    except EOFError:
        print(EF)
    parser.parse(info)

main()
