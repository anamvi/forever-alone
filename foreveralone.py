import ply.lex as lex
import ply.yacc as yacc
from functions_table import FunctionsTable

DirFunc = FunctionsTable()
current_scope = ''
var_list = []
counter = 0

# PALABRAS RESERVADAS
reserved = {
    'programa' : 'PROGRAM',
    'var' : 'VAR',
    'funcion' : 'FUNC',
    'int' : 'INT',
    'float' : 'FLOAT',
    'char' : 'CHAR',
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
    'CTE_CHAR',
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
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_CTE_FLOAT(t):
    r'\d*\.[\d]+'
    t.value = float(t.value)
    return t

def t_CTE_INT(t):
    r'0|[1-9][0-9]*'
    t.value = int(t.value)
    return t

def t_CTE_CHAR(t):
    r'\'[\w\d\s.]?\''
    return t

def t_CTE_STR(t):
    r'\'[\w\d\s.]*\''
    return t

def t_ID(t):
    r'[a-zA-Z][\w\d]*'
    t.type = reserved.get(t.value, 'ID')
    return t

lexer = lex.lex()

def p_prog(p):
    '''
        prog : PROGRAM ID SEMICOLON variables prog_funcs func_princ
    '''
    global current_scope
    current_scope = 'global'
    for i in var_list:
        DirFunc.functions['global'].add_variable(i[0], i[1])
        
    var_list.clear()
    print(DirFunc)

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
def p_variables_2(p):
    '''
        variables_2 : tipo COLON lista_id SEMICOLON variables_rep
    '''
    global counter
    while counter>0:
        var_list[counter-1].append(p[1])
        counter-=1

def p_variables_rep(p):
    '''
        variables_rep : variables_2
        | empty
    '''

def p_lista_id(p):
    '''
        lista_id : ID dimension_var lista_id_rep
    '''
    global counter
    global var_list
    var_list.append([p[1]])
    counter+=1
    # DirFunc.functions[current_scope].add_var(p[1], current_type)

def p_lista_id_rep(p):
    '''
        lista_id_rep : COMMA lista_id
        | empty
    '''

def p_dimension_var(p):
    '''
        dimension_var : SQUAREL CTE_INT SQUARER
        | empty
    '''

def p_tipo(p):
    '''
        tipo : INT
        | FLOAT
        | CHAR
    '''

    p[0] = p[1]

def p_func_princ(p):
    '''
        func_princ : PRINCIPAL PARENTHESESL PARENTHESESR CURLYL estatuto_rep CURLYR
    '''

def p_funcion(p):
    '''
        funcion : FUNC tipo_func ID PARENTHESESL funcion_param PARENTHESESR SEMICOLON variables CURLYL estatuto_rep CURLYR
    '''
def p_tipo_func(p):
    '''
        tipo_func : tipo
        | VOID
    '''

def p_funcion_param(p):
    '''
        funcion_param : tipo ID funcion_param_rep
        | empty
    '''

def p_funcion_param_rep(p):
    '''
        funcion_param_rep : COMMA funcion_param
        | empty
    '''

def p_estatuto_rep(p):
    '''
        estatuto_rep : estatuto estatuto_rep
        | empty
    '''

def p_estatuto(p):
    '''
        estatuto : asignacion SEMICOLON
        | llamada SEMICOLON
        | retorno SEMICOLON
        | lectura SEMICOLON
        | escritura SEMICOLON
        | decision
        | rep_c
        | rep_nc
    '''

def p_asignacion(p):
    '''
        asignacion : ID dimension ASSIGN expresion
    '''
def p_dimension(p):
    '''
        dimension : SQUAREL expresion SQUARER
        | empty
    '''

def p_llamada(p):
    '''
        llamada : ID PARENTHESESL expresion_rep PARENTHESESR
    '''

def p_lectura(p):
    '''
        lectura : READ PARENTHESESL lista_lectura PARENTHESESR
    '''

def p_lista_lectura(p):
    '''
        lista_lectura : ID dimension COMMA lista_lectura
        | ID dimension
    '''

def p_escritura(p):
    '''
        escritura : PRINT PARENTHESESL lista_escritura PARENTHESESR
    '''

def p_lista_escritura(p):
    '''
        lista_escritura : letrero lista_escritura_rep
        | expresion lista_escritura_rep
    '''

def p_lista_escritura_rep(p):
    '''
        lista_escritura_rep : COMMA lista_escritura
        | empty
    '''

def p_decision(p):
    '''
        decision : IF PARENTHESESL expresion PARENTHESESR THEN CURLYL estatuto_rep CURLYR decision_alt
    '''

def p_decision_alt(p):
    '''
        decision_alt : ELSE CURLYL estatuto_rep CURLYR
        | empty
    '''

def p_rep_c(p):
    '''
        rep_c : WHILE PARENTHESESL expresion PARENTHESESR DO CURLYL estatuto_rep CURLYR
    '''

def p_rep_nc(p):
    '''
        rep_nc : FROM asignacion UNTIL expresion DO CURLYL estatuto_rep CURLYR
    '''

def p_expresion_rep(p):
    '''
        expresion_rep : expresion_rep_2
        | empty
    '''

def p_expresion_rep_2(p):
    '''
        expresion_rep_2 : expresion COMMA expresion_rep_2
        | expresion
    '''

def p_retorno(p):
    '''
        retorno : RETURN PARENTHESESL expresion PARENTHESESR
    '''

def p_expresion(p):
    '''
        expresion : exp_comp expresion_2
    '''

def p_expresion_2(p):
    '''
        expresion_2 : AND expresion
        | OR expresion
        | empty
    '''

def p_exp_comp(p):
    '''
        exp_comp : exp_ar exp_comp_2
    '''
def p_exp_comp_2(p):
    '''
        exp_comp_2 : comp_sym exp_ar
        | empty
    '''

def p_comp_sym(p):
    '''
        comp_sym : LESSTHAN
        | GREATERTHAN
        | LESSEQUAL
        | GREATEREQUAL
        | EQUAL
        | NOTEQUAL
    '''

def p_exp_ar(p):
    '''
        exp_ar : termino exp_ar_2
    '''

def p_exp_ar_2(p):
    '''
        exp_ar_2 : PLUS exp_ar
        | MINUS exp_ar
        | empty
    '''
def p_termino(p):
    '''
        termino : factor termino_2
    '''

def p_termino_2(p):
    '''
        termino_2 : MULT termino
        | DIVIDE termino
        | empty
    '''

def p_factor(p):
    '''
        factor : const
        | ID dimension
        | PARENTHESESL expresion PARENTHESESR
        | llamada
    '''

def p_const(p):
    '''
        const : CTE_INT
        | CTE_CHAR
        | CTE_FLOAT
    '''

def p_letrero(p):
    '''
        letrero : CTE_STR
    '''

def p_empty(p):
    '''
        empty :
    '''

def p_error(p):
   print("Syntax error", p)

parser = yacc.yacc()

def main():
    try:
        arch_name = 'test_input.txt'
        arch = open(arch_name,'r')
        info = arch.read()
        arch.close()
    except EOFError:
        print(EF)
    parser.parse(info)

main()
