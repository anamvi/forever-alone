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
    # Base program syntax.

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
            # assign a virtual address
            dir = inter_code.mem.global_.add_value(i[0],i[2])
            # add to var table
            dir_func.functions['global'].add_variable(i[0], i[2], dir)
            # handle array dimensions if they exist
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
    # check for dimensions in variable and add constant in memory
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
    # base main function syntax.

def p_np_start_main_(p):
    '''
        np_start_main_ :
    '''
    global current_scope, current_type
    # declares scope and type
    current_scope = 'global'
    current_type = 'void'

    # fills start goto quadruple with the first quadruple of main function
    main = inter_code.jumps_stack.pop()
    inter_code.fill(main,len(inter_code.quadruples))

def p_np_end_program_(p):
    '''
        np_end_program_ :
    '''
    # Adds ENDProg quadruple and performs finishing functions
    inter_code.add_endprog_quad()
    # creates the output to be added to the obj file
    output = {
        'Constants': inter_code.mem.constant_.output(),
        'Quadruples': inter_code.quadruples,
        'DirFunc': dir_func.output()
    }
    inter_code.mem.constant_.reset_memory()
    # creates the object code file
    with open("fa.bigsheep","w+") as json_file:
        json.dump(output, json_file)

    # starts the instance of the virtual machine
    vm = VirtualMachine("fa.bigsheep")

def p_funcion(p):
    '''
        funcion : FUNC tipo_func ID np_set_scope_ PARENTHESESL funcion_param np_add_func_to_directory_ PARENTHESESR SEMICOLON variables np_add_vars_to_table_ CURLYL estatuto_rep CURLYR np_end_function_
    '''
    # basic function syntax
def p_tipo_func(p):
    '''
        tipo_func : tipo
        | VOID
    '''
    # return type
    p[0] = p[1]

def p_np_set_scope_(p):
    '''
        np_set_scope_ :
    '''
    # set function and its type as the current scope
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

    # check for parameters
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

            # check for dimensions and assign each of them a virtual address
            if i[1] is not None:
                dir_func.functions[current_scope].variables[i[0]].array_size = int(i[1])
                x=1
                while x < int(i[1]):
                    inter_code.mem.global_.add_value(i[0]+str(x),i[2])
                    x+=1

def p_np_end_function_(p):
    '''
        np_end_function_ :
    '''
    global current_scope, current_type
    # check if function is non-void and should have a return value
    if str(current_type) != 'void' and not inter_code.does_return:
        raise Exception('ReturnError: Function "'+str(current_scope)+'" should have a return value.')
    # add amount of temps to the space needed for a function
    temps = inter_code.mem.temp_.count_content()
    inter_code.add_endfunc()
    dir_func.functions[current_scope].space_temp = temps
    # delete the variable table for the function
    dir_func.functions[current_scope].variables.clear()

def p_funcion_param(p):
    '''
        funcion_param : tipo ID funcion_param_rep
        | empty
    '''
    # get the parameters for a function in a list
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
    # if function call was made as a statement, and not as part of an operation, remove the result from the stack as it was a void function.
    inter_code.variable_stack.pop()
    inter_code.type_stack.pop()

def p_np_quadruple_IO_(p):
    '''
        np_quadruple_IO_ :
    '''
    # create an input output quadruple
    if inter_code.operator_stack!= []:
        inter_code.add_IO_quadruple()

def p_np_push_var_(p):
    '''
        np_push_var_ :
    '''
    global current_scope
    # get the type and address for the current variable. Check first in local scope and then global.
    if dir_func.functions[current_scope].variable_exists(p[-1]):
        var_type = dir_func.functions[current_scope].variables[p[-1]].type
        var = dir_func.functions[current_scope].variables[p[-1]].dir
    elif dir_func.functions['global'].variable_exists(p[-1]):
        var_type = dir_func.functions['global'].variables[p[-1]].type
        var = dir_func.functions['global'].variables[p[-1]].dir
    else:
        raise Exception('Variable "'+ str(p[-1]) +'" does not exist')
    # append variable to stack
    inter_code.variable_stack.append(var)
    inter_code.type_stack.append(var_type)

def p_np_push_operator_(p):
    '''
        np_push_operator_ :
    '''
    # append operator to the operator stack
    inter_code.operator_stack.append(p[-1])

def p_np_pop_operator_(p):
    '''
        np_pop_operator_ :
    '''
    # discard operator from the stack (for input/output functions)
    inter_code.operator_stack.pop()

def p_asignacion(p):
    '''
        asignacion : ID np_push_var_ dimension ASSIGN np_push_operator_ expresion np_quadruple_assignment_
    '''
    p[0]=p[6]

def p_np_quadruple_assignment_(p):
    '''
        np_quadruple_assignment_ :
    '''
    # call function to create an assignment quadruple
    if inter_code.operator_stack!= []:
        inter_code.add_assignment_quadruple()

def p_dimension(p):
    '''
        dimension : SQUAREL np_verify_dimensions_ np_add_false_bottom_ expresion np_manage_array_ np_remove_false_bottom_ SQUARER
        | empty
    '''

def p_np_verify_dimensions_(p):
    '''
        np_verify_dimensions_ :
    '''
    global current_scope
    # Get variable that wants to be assigned dimensions and its type
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
            raise Exception('TypeMismatch: The variable ' + id + ' is not an array.')
    else:
        if p[-1] != '[':
            raise Exception('TypeMismatch: The variable ' + id + ' is declared as an array.')
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
    # check that the dimension provided is an integer
    if inter_code.type_stack[-1]!='int':
        raise Exception('TypeMismatch: array dimesions must be integers.')
    # create quadruples to verify array bounds and add the base direction to the index
    inter_code.add_verify_limits_quadruple()
    inter_code.add_array_base_direction_quadruple()

def p_llamada(p):
    '''
        llamada : ID np_verify_function_ PARENTHESESL np_add_false_bottom_ np_create_era_ expresion_rep np_end_of_parameters_ PARENTHESESR np_remove_false_bottom_ np_create_gosub_
    '''
    # base structure for a call to a function.

def p_np_verify_function_(p):
    '''
        np_verify_function_ :
    '''
    global func_to_call
    func_to_call = p[-1]
    # verify that the function being called exists
    if not dir_func.function_exists(p[-1]):
        raise Exception('SyntaxError: function '+ func_to_call +' does not exist.')

def p_expresion_rep(p):
    '''
        expresion_rep : expresion_rep_2
        | empty
    '''
    # repeted expression for parameter declaration

def p_expresion_rep_2(p):
    '''
        expresion_rep_2 : expresion np_next_parameter_check_ np_verify_parameters_ COMMA expresion_rep_2
        | expresion np_next_parameter_check_ np_verify_parameters_
    '''

def p_np_verify_parameters_(p):
    '''
        np_verify_parameters_ :
    '''
    global func_to_call
    argument = inter_code.variable_stack.pop()
    arg_type = inter_code.type_stack.pop()
    # if the argument provided is of the same type as the argument expected, make the parameter quadruple
    if arg_type == dir_func.functions[func_to_call].parameters[inter_code.parameter_counter-1]:
        inter_code.add_parameter_quadruple(argument)
    else:
        raise Exception('TypeMismatch: Argument type does not match function parameter')

def p_np_next_parameter_check_(p):
    '''
        np_next_parameter_check_ :
    '''
    global func_to_call
    global current_scope
    # check that the parameters given are not more than those expected
    if len(dir_func.functions[func_to_call].parameters) < inter_code.parameter_counter:
        raise Exception('Number of arguments in call do not match parameters.')

def p_np_end_of_parameters_(p):
    '''
        np_end_of_parameters_ :
    '''
    global func_to_call
    global current_scope
    # Once the parameters given have ended, check that there are no more parameters expected.
    if len(dir_func.functions[func_to_call].parameters) >= inter_code.parameter_counter:
        raise Exception('Number of arguments in call do not match parameters.')

def p_np_create_era_(p):
    '''
        np_create_era_ :
    '''
    global func_to_call
    # create ERA quadruple with needed memory size
    inter_code.add_era_quadruple(func_to_call, dir_func.functions[func_to_call].space_local)

def p_np_create_gosub_(p):
    '''
        np_create_gosub_ :
    '''
    global func_to_call
    scope = dir_func.functions[func_to_call].quad
    inter_code.add_gosub_quadruple(func_to_call, scope)
    # if function has a return value, assign that address to a temporal in order to save the return in case of recursion
    ret_dir = dir_func.functions['global'].variables[func_to_call].dir
    if ret_dir is not None:
        ret_type = inter_code.mem.global_.check_type(ret_dir)
        inter_code.variable_stack.append(ret_dir)
        inter_code.type_stack.append(ret_type)
        inter_code.add_assign_temp_quadruple()
    else:
        inter_code.variable_stack.append(ret_dir)
        inter_code.type_stack.append(None)
    # reset function being called
    func_to_call = ''

def p_lectura(p):
    '''
        lectura : READ np_push_operator_ PARENTHESESL lista_lectura PARENTHESESR np_pop_operator_
    '''
    # basic structure of read (input) function

def p_lista_lectura(p):
    '''
        lista_lectura : ID np_push_var_ dimension np_quadruple_IO_ COMMA lista_lectura
        | ID np_push_var_ dimension np_quadruple_IO_
    '''
    # list of variables to be read, separated by commas

def p_escritura(p):
    '''
        escritura : PRINT np_push_operator_ PARENTHESESL lista_escritura PARENTHESESR np_pop_operator_
    '''
    # basic structure of write (output) function

def p_lista_escritura(p):
    '''
        lista_escritura : expresion np_quadruple_IO_ lista_escritura_rep
    '''
    # list of variables to be printed, separated by commas

def p_lista_escritura_rep(p):
    '''
        lista_escritura_rep : COMMA lista_escritura
        | empty
    '''

def p_decision(p):
    '''
        decision : IF PARENTHESESL expresion PARENTHESESR np_gotoF_ THEN CURLYL estatuto_rep CURLYR decision_alt
    '''
    # basic structure of decision statement (if...then...else)

def p_decision_alt(p):
    '''
        decision_alt : ELSE np_false_condition_ CURLYL estatuto_rep CURLYR np_end_if_actions
        | empty np_end_if_actions
    '''
    # optional "else" section

def p_np_gotoF_(p):
    '''
        np_gotoF_ :
    '''
    # if the condition is false, jump to another quadruple
    exp_type = inter_code.type_stack.pop()
    if exp_type != 'bool':
        raise Exception('TypeMismatch: condition must be boolean and obtained type ' + exp_type )
    else :
        inter_code.add_gotof_quadruple(None)

def p_np_false_condition_(p):
    '''
        np_false_condition_ :
    '''
    # if there is an 'else' statement
    # - adds goto in order to jump if the true option has already been done
    inter_code.add_goto_quadruple(None)
    false = inter_code.jumps_stack.pop()
    # - fills gotoF jump with the start of else quadruples
    inter_code.push_jump(-1)
    inter_code.fill(false, len(inter_code.quadruples))

def p_np_end_if_actions(p):
    '''
        np_end_if_actions :
    '''
    # fill the last jump quadruple with end of the decision statement
    end = inter_code.jumps_stack.pop()
    inter_code.fill(end,len(inter_code.quadruples))

def p_rep_c(p):
    '''
        rep_c : WHILE np_push_jump_ PARENTHESESL expresion PARENTHESESR np_gotoF_ DO CURLYL estatuto_rep CURLYR np_end_while_actions_
    '''
    # basic syntax for conditional repetition (while) statement

def p_np_push_jump_(p):
    '''
        np_push_jump_ :
    '''
    # pushes current quadruple counter to the stack in order to be able to return to it
    inter_code.push_jump(0)

def p_np_end_while_actions_(p):
    '''
        np_end_while_actions_ :
    '''
    # create a goto quadruple that returns to the condition to see if it gets back into the loop
    end = inter_code.jumps_stack.pop()
    ret = inter_code.jumps_stack.pop()
    inter_code.add_goto_quadruple(ret)
    inter_code.fill(end, len(inter_code.quadruples))

def p_rep_nc(p):
    '''
        rep_nc : FROM ID np_push_var_ dimension ASSIGN expresion np_assign_loop_ UNTIL expresion np_quadruple_for_ np_gotoF_ DO CURLYL estatuto_rep CURLYR np_end_for_actions
    '''
    # basic syntax of non conditional (from..until) repetition

def p_np_assign_loop_(p):
    '''
        np_assign_loop_ :
    '''
    # makes assignment
    inter_code.add_assign_loop_quadruple()

def p_np_quadruple_for_(p):
    '''
        np_quadruple_for_ : np_push_jump_
    '''
    # Check that both expressions on either side are integers and create quadruple to compare them
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
        raise Exception('TypeMismatch: Only values of type int are supported in a non-conditional cycle.')

def p_np_end_for_actions(p):
    '''
        np_end_for_actions : np_increment_temp_ np_end_while_actions_
    '''

def p_np_increment_temp_(p):
    '''
        np_increment_temp_ :
    '''
    # increment the initial value by 1
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
    # throws an error if the function was not supposed to have a return value
    if func_addr is None:
        raise Exception('ReturnError: Void function cannot have a return value.')
    inter_code.variable_stack.append(func_addr)
    inter_code.type_stack.append(current_type)
    inter_code.add_return_quadruple()

def p_np_quadruple_empty_return_(p):
    '''
        np_quadruple_empty_return_ :
    '''
    global current_type, current_scope
    func_addr = dir_func.functions['global'].variables[current_scope].dir
    # if the return is empty, check if it's a void function and throw an error if it was supposed to have a return
    if func_addr is not None:
        raise Exception('ReturnError: non-void function has to have a return value.')
    inter_code.add_empty_return_quadruple()

def p_expresion(p):
    '''
        expresion : exp_comp np_quadruple_logic_ expresion_2
    '''

def p_expresion_2(p):
    '''
        expresion_2 : AND np_push_operator_ expresion
        | OR np_push_operator_ expresion
        | empty
    '''
    # start of expression, compares using logic operators (AND or OR)

def p_np_quadruple_logic_(p):
    '''
        np_quadruple_logic_ :
    '''
    # Neural point to verify if the next operator is of the same priority
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
    # uses comparison operators (>, <, ==, etc.)

def p_np_quadruple_compare_(p):
    '''
        np_quadruple_compare_ :
    '''
    # Neural point to verify if the next operator is of the same priority
    if inter_code.operator_stack!= []:
        if inter_code.operator_stack[len(inter_code.operator_stack)-1] in ['<', '>', '>=', '<=','==', '!=']:
            inter_code.add_operation_quadruple()

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
    # adds or substracts from expression

def p_np_quadruple_term(p):
    '''
        np_quadruple_term :
    '''
    # Neural point to verify if the next operator is of the same priority
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
    # multiplies and divides

def p_np_quadruple_factor_(p):
    '''
        np_quadruple_factor_ :
    '''
    # Neural point to verify if the next operator is of the same priority
    if inter_code.operator_stack != []:
        if inter_code.operator_stack[len(inter_code.operator_stack)-1] in ['*', '/']:
            inter_code.add_operation_quadruple()

def p_unary(p):
    '''
        unary : factor
        | MINUS np_push_operator_ unary change_sign
        | PLUS unary
    '''
    p[0]=p[1]
    # creates unary operations (+ and -)

def p_change_sign(p):
    '''
        change_sign :
    '''
    inter_code.add_unary_quadruple()

def p_factor(p):
    '''
        factor : const
        | ID np_push_var_ dimension
        | PARENTHESESL np_add_false_bottom_ expresion PARENTHESESR np_remove_false_bottom_
        | llamada
    '''
    # syntax for base factor. Can be either a variable, constant, call, or expresion in parenthesis.

def p_np_add_false_bottom_(p):
    '''
        np_add_false_bottom_ :
    '''
    inter_code.operator_stack.append('(')

def p_np_remove_false_bottom_(p):
    '''
        np_remove_false_bottom_ :
    '''
    fb = inter_code.operator_stack.pop()

def p_const(p):
    '''
        const : CTE_INT np_push_const_int_
        | CTE_STR np_push_const_string_
        | CTE_FLOAT np_push_const_float_
    '''

def p_np_push_const_int_(p):
    '''
        np_push_const_int_ :
    '''
    # push a constant of type int to memory
    var = inter_code.mem.constant_.add_value(int(p[-1]),'int')
    inter_code.variable_stack.append(var)
    inter_code.type_stack.append('int')

def p_np_push_const_float_(p):
    '''
        np_push_const_float_ :
    '''
    # push a constant of type float to memory
    var = inter_code.mem.constant_.add_value(float(p[-1]),'float')
    inter_code.variable_stack.append(var)
    inter_code.type_stack.append('float')
def p_np_push_const_string_(p):
    '''
        np_push_const_string_ :
    '''
    # push a constant of type string to memory
    var = inter_code.mem.constant_.add_value(str(p[-1][1:-1]),'string')
    inter_code.variable_stack.append(var)
    inter_code.type_stack.append('string')

def p_empty(p):
    '''
        empty :
    '''

def p_error(p):
   print("Syntax error", p)

parser = yacc.yacc()

def main():
    arch_name = sys.argv[1]
    try:
        arch = open(arch_name,'r')
        info = arch.read()
        arch.close()
    except EOFError as error:
        print(error)
    parser.parse(info)

main()
