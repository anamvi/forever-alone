import json
import copy
from memory import Memory
from execution_memory import ExecutionMemorySegment

'''
    Máquina virtual: maneja el código intermedio recibido de la etapa de compilación y
    hace las revisiones necesarias para hacer los cálculos que se piden. Tiene acceso a la
    memoria de ejecución
'''

class VirtualMachine():
    def __init__(self, file_name):
        with open(file_name, 'r') as json_file:
            self.inter_code = json.load(json_file)
        self.mem = Memory('execution')
        self.add_constants()
        self.context_stack =[]
        self.local_memory_stack =[]
        self.temp_memory_stack =[]
        self.parameters = []
        self.current_func = ''
        parameters = []
        self.read_obj_code()

    '''
    allocate_memory:

    verifica que haya espacio para el segmento de código de la llamada
    '''
    def allocate_memory(self,locals,temps):
        if self.mem.local_.prev_size+locals >= 8000:
            raise Exception('StackOverflow: local variable stack exceded.')
        else:
            self.local_size = self.mem.local_.prev_size+locals
        if self.mem.temp_.prev_size+temps >= 10000:
            raise Exception('StackOverflow: temporal values stack exceded.')
        else:
            self.temp_size = self.mem.temp_.prev_size+temps

    '''
    add_constants:
    agrega las constantes del archivo de código intermedio a la memoria de constantes
    '''
    def add_constants(self):
        for i in self.inter_code['Constants']:
            self.mem.constant_.load_value(i["value"], i["address"])

    '''
    check_exists:
    revisa que la variable ya haya sido cargada a memoria de ejecución
    '''
    def check_exists(self, dir):
        var = self.mem.get_value(int(dir))
        if var is None:
            raise NameError('Variable referenced before assignment.')
        return var

    '''
    compare_input_type:
    revisa que el valor y la dirección tengan el mismo tipo
    '''
    def compare_input_type(self, val, address):
        type = self.mem.check_type(address)
        if type == 'int':
            try:
                val = int(val)
            except:
                raise TypeError("The value provided ("+val+") should be an integer.")
        elif type == 'float':
            try:
                val = float(val)
            except:
                raise TypeError("The value provided (" +val+ ") should be a float.")
        return val

    '''
    handle_pointer:
    revisar si el dato que recibimos es un pointer y de ser así obtener la dirección a la que apunta.
    '''
    def handle_pointer(self, val):
        if val is not None and not isinstance(val, str):
            if self.mem.check_type(int(val))=='ptr':
                return self.mem.get_value(int(val))
        return val

    '''
    assign_parameters:
    cargar los parámetros a la dirección de memoria correspondiente
    '''
    def assign_parameters(self, param_types):
        if self.parameters:
            base = self.mem._BASE_LOCAL
            for i,x in enumerate(self.parameters):
                if param_types[i] == 'int':
                    base_type = self.mem.local_._BASE_INT
                elif param_types[i] == 'float':
                    base_type = self.mem.local_._BASE_FLOAT
                elif param_types[i] == 'string':
                    base_type = self.mem.local_._BASE_STRING
                self.mem.load_value(x,base+base_type+i)

    '''
    read_obj_code:
    Lee el código obj recibido de la compilación
    '''
    def read_obj_code(self):
        x=self.inter_code['Quadruples']
        IP = 0
        while True:
            quad = x[IP]
            if quad['result'] != 'ERA':
                left = self.handle_pointer(quad['left_operand'])
                right = self.handle_pointer(quad['right_operand'])

            if quad['operator'] == 'GOTO':
                IP = quad['result']
            elif quad['operator'] == 'GOTOF':
                if self.mem.get_value(left) == False:
                    IP = quad['result']
                else:
                    IP+=1
            elif quad['operator'] == 'GOTOV':
                if self.mem.get_value(left) == True:
                    IP = quad['result']
                else:
                    IP+=1
            elif quad['operator'] == '+':
                if quad['right_operand'] is None:
                    op = 0 + self.check_exists(left)
                else:
                    op = self.check_exists(left) + self.check_exists(right)
                self.mem.load_value(op, quad['result'])
                IP+=1
            elif quad['operator'] == '-':
                if quad['right_operand'] is None:
                    op = 0 - self.check_exists(left)
                else:
                    op = self.check_exists(left) - self.check_exists(right)
                self.mem.load_value(op, quad['result'])
                IP+=1
            elif quad['operator'] == '*':
                op = self.check_exists(left) * self.check_exists(right)
                self.mem.load_value(op, quad['result'])
                IP+=1
            elif quad['operator'] == '/':
                op = self.check_exists(left) // self.check_exists(right)
                self.mem.load_value(op, quad['result'])
                IP+=1
            elif quad['operator'] == '==':
                op = self.check_exists(left) == self.check_exists(right)
                self.mem.load_value(op, quad['result'])
                IP+=1
            elif quad['operator'] == '!=':
                op = self.check_exists(left) != self.check_exists(right)
                self.mem.load_value(op, quad['result'])
                IP+=1
            elif quad['operator'] == '>=':
                op = self.check_exists(left) >= self.check_exists(right)
                self.mem.load_value(op, quad['result'])
                IP+=1
            elif quad['operator'] == '<=':
                op = self.check_exists(left) <= self.check_exists(right)
                self.mem.load_value(op, quad['result'])
                IP+=1
            elif quad['operator'] == '<':
                op = self.check_exists(left) < self.check_exists(right)
                self.mem.load_value(op, quad['result'])
                IP+=1
            elif quad['operator'] == '>':
                op = self.check_exists(left) > self.check_exists(right)
                self.mem.load_value(op, quad['result'])
                IP+=1
            elif quad['operator'] == '&':
                op = self.check_exists(left) and self.check_exists(right)
                self.mem.load_value(op, quad['result'])
                IP+=1
            elif quad['operator'] == '|':
                op = self.check_exists(left) or self.check_exists(right)
                self.mem.load_value(op, quad['result'])
                IP+=1
            elif quad['operator'] == '=':
                res = self.handle_pointer(quad['result'])
                self.mem.load_value(self.check_exists(left),res)
                IP+=1
            elif quad['operator'] == 'escribe':
                res = self.handle_pointer(quad['result'])
                if "/endl" == str(self.check_exists(res)) :
                    print("")
                else:
                    print(self.check_exists(res), end = '')
                IP+=1
            elif quad['operator'] == 'lee':
                res = self.handle_pointer(quad['result'])
                val = input()
                self.mem.load_value(self.compare_input_type(val,res),res)
                IP+=1
            elif quad['operator'] == 'return':
                if quad['result'] is not None:
                    res = self.handle_pointer(quad['result'])
                    self.mem.load_value(self.check_exists(left),res)
                self.mem.local_.reset_memory()
                self.mem.temp_.reset_memory()
                del self.mem.local_
                del self.mem.temp_
                self.mem.local_ = self.local_memory_stack.pop()
                self.mem.temp_ = self.temp_memory_stack.pop()
                IP = self.context_stack.pop()
            elif quad['operator'] == 'ver':
                res = self.handle_pointer(quad['result'])
                if self.check_exists(left) >= self.check_exists(res):
                    raise Exception("Limits of array out of bounds.")
                IP+=1
            elif quad['operator'] == 'ERA':
                self.allocate_memory(quad['left_operand'],quad['right_operand'])
                self.current_func = quad['result']

                IP+=1
            elif quad['operator'] == 'PARAM':
                if self.mem.check_type(left) != self.inter_code['DirFunc'][self.current_func]['parameters'][int(quad['result'])-1]:
                    raise TypeError('The parameter in call does not match the function type for ' + str(self.current_func))
                self.parameters.append(self.mem.get_value(left))
                IP+=1
            elif quad['operator'] == 'GOSUB':
                # guarda el instruction pointer (cont) en la pila de contextos
                self.context_stack.append(IP+1)
                # guarda las memorias local y temporal en las pilas de memorias
                self.local_memory_stack.append(copy.copy(self.mem.local_))
                self.temp_memory_stack.append(copy.copy(self.mem.temp_))
                del self.mem.local_
                del self.mem.temp_
                # crea un nuevo segmento de memoria local y temporal y los asigna a la variable que se está utilizando
                self.mem.local_ = ExecutionMemorySegment(self.mem._BASE_LOCAL, self.local_size)
                self.mem.temp_ = ExecutionMemorySegment(self.mem._BASE_TEMP, self.temp_size)
                # asigna los parámetros que se habían leido con el cuádruplo PARAM, a las direcciones de memoria correspondientes a los tipos
                self.assign_parameters(self.inter_code['DirFunc'][self.current_func]['parameters'])
                self.parameters.clear()
                IP = quad['result']
            elif quad['operator'] == 'ENDFunc':
                # se borran las memorias temporal y local
                self.mem.local_.reset_memory()
                self.mem.temp_.reset_memory()
                del self.mem.local_
                del self.mem.temp_
                # se hace un pop a la pila de memorias y se asignan a la variable que se está utilizando
                self.mem.local_ = self.local_memory_stack.pop()
                self.mem.temp_ = self.temp_memory_stack.pop()
                self.local_size = self.mem.local_.prev_size
                self.temp_size = self.mem.temp_.prev_size
                # se cambia el IP al guardado en la pila de contextos
                IP = self.context_stack.pop()
            elif quad['operator'] == 'ENDProg':
                break
            else:
                IP+=1
