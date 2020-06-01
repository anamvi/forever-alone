import json
from memory import Memory
from execution_memory import ExecutionMemorySegment

class VirtualMachine():
    def __init__(self):
        with open("pleasedont.cry", 'r') as json_file:
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

    def check_overflow(self):
        local_size = []
        local_size.append(len(self.mem.local_.integers))
        local_size.append(len(self.mem.local_.floats))
        local_size.append(len(self.mem.local_.strings))
        local_size.append(len(self.mem.local_.bools))
        if self.local_memory_stack:
            for i in self.local_memory_stack:
                local_size[0]+= len(i.integers)
                local_size[1]+= len(i.floats)
                local_size[2]+= len(i.strings)
                local_size[3]+= len(i.bools)
        if any(local_size)>=2000:
            raise Exception('StackOverflow: local variable stack exceded.')
        temp_size = []
        temp_size.append(len(self.mem.temp_.integers))
        temp_size.append(len(self.mem.temp_.floats))
        temp_size.append(len(self.mem.temp_.strings))
        temp_size.append(len(self.mem.temp_.bools))
        if self.temp_memory_stack:
            for i in self.temp_memory_stack:
                temp_size[0]+= len(i.integers)
                temp_size[1]+= len(i.floats)
                temp_size[2]+= len(i.strings)
                temp_size[3]+= len(i.bools)
        if any(temp_size)>=2000:
            raise Exception('StackOverflow: temporal values stack exceded.')

        # if self.mem._BASE_LOCAL<= dir < self.mem._BASE_TEMP:
        #     if self.mem.local_._BASE_INT <= dir-self.mem._BASE_LOCAL < self.mem.local_._BASE_FLOAT:
        #         if self.mem_used_local[0]>=2000:
        #             raise Exception("StackOverflow: too many stored values of type int")
        #         self.mem_used_local[0]+=1
        #     elif self.mem.local_._BASE_FLOAT <= dir-self.mem._BASE_LOCAL < self.mem.local_._BASE_STRING:
        #         if self.mem_used_local[1]>=2000:
        #             raise Exception("StackOverflow: too many stored values of type float")
        #         self.mem_used_local[1]+=1
        #     elif self.mem.local_._BASE_STRING <= dir-self.mem._BASE_LOCAL < self.mem.local_._BASE_BOOL:
        #         if self.mem_used_local[2]>=2000:
        #             raise Exception("StackOverflow: too many stored values of type string")
        #         self.mem_used_local[2]+=1
        #     elif self.mem.local_._BASE_BOOL <= dir-self.mem._BASE_LOCAL < self.mem.local_._BASE_PTR:
        #         if self.mem_used_local[3]>=2000:
        #             raise Exception("StackOverflow: too many stored values of type bool")
        #         self.mem_used_local[3]+=1
        #     elif self.mem.local_._BASE_PTR <= dir-self.mem._BASE_LOCAL:
        #         if self.mem_used_local[4]>=2000:
        #             raise Exception("StackOverflow: too many stored values of type pointer")
        #         self.mem_used_local[4]+=1
        # elif self.mem._BASE_TEMP<= dir < self.mem._BASE_CONSTANT:
        #     if self.mem.temp_._BASE_INT <= dir-self.mem._BASE_TEMP < self.mem.temp_._BASE_FLOAT:
        #         if self.mem_used_temp[0]>=2000:
        #             raise Exception("StackOverflow: too many stored values of type int")
        #         self.mem_used_temp[0]+=1
        #     elif self.mem.temp_._BASE_FLOAT <= dir-self.mem._BASE_TEMP < self.mem.temp_._BASE_STRING:
        #         if self.mem_used_temp[1]>=2000:
        #             raise Exception("StackOverflow: too many stored values of type float")
        #         self.mem_used_temp[1]+=1
        #     elif self.mem.temp_._BASE_STRING <= dir-self.mem._BASE_TEMP < self.mem.temp_._BASE_BOOL:
        #         if self.mem_used_temp[2]>=2000:
        #             raise Exception("StackOverflow: too many stored values of type string")
        #         self.mem_used_temp[2]+=1
        #     elif self.mem.temp_._BASE_BOOL <= dir-self.mem._BASE_TEMP < self.mem.temp_._BASE_PTR:
        #         if self.mem_used_temp[3]>=2000:
        #             raise Exception("StackOverflow: too many stored values of type bool")
        #         self.mem_used_temp[3]+=1
        #     elif self.mem.temp_._BASE_PTR <= dir-self.mem._BASE_TEMP:
        #         if self.mem_used_temp[4]>=2000:
        #             raise Exception("StackOverflow: too many stored values of type pointer")
        #         self.mem_used_temp[4]+=1


    def add_constants(self):
        for i in self.inter_code['Constants']:
            self.mem.constant_.load_value(i["value"], i["address"])

    def check_exists(self, dir):
        var = self.mem.get_value(int(dir))
        if var is None:
            # sacar el nombre de la variable de la tabla de variables
            raise NameError('Variable referenced before assignment.')
        return var

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

    def handle_pointer(self, val):
        if val is not None and not isinstance(val, str):
            if self.mem.check_type(int(val))=='ptr':
                return self.mem.get_value(int(val))
        return val
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

    def read_obj_code(self):
        x=self.inter_code['Quadruples']
        IP = 0
        while True:
            quad = x[IP]
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
                self.mem.load_value(self.compare_input_type(val,res),res) #CHECAR SI ESTO ESTA BIEN???????
                IP+=1
            elif quad['operator'] == 'return':
                # go to the next function (endfunc)
                if quad['result'] is not None:
                    res = self.handle_pointer(quad['result'])
                    self.mem.load_value(self.check_exists(left),res)
                self.mem.local_.reset_memory()
                self.mem.temp_.reset_memory()
                self.mem.local_ = self.local_memory_stack.pop()
                self.mem.temp_ = self.temp_memory_stack.pop()
                IP = self.context_stack.pop()
            elif quad['operator'] == 'ver':
                res = self.handle_pointer(quad['result'])
                if self.check_exists(left) >= self.check_exists(res):
                    raise Exception("Limits of array out of bounds."+str(left)+str(res))
                IP+=1
            elif quad['operator'] == 'ERA':
                self.current_func = quad['result']
                IP+=1
            elif quad['operator'] == 'PARAM':
                if self.mem.check_type(left) != self.inter_code['DirFunc'][self.current_func]['parameters'][int(quad['result'])-1]:
                    raise TypeError('The parameter in call does not match the function type for ' + str(self.current_func))
                self.parameters.append(self.mem.get_value(left))
                IP+=1
            elif quad['operator'] == 'GOSUB':
                self.context_stack.append(IP+1)
                self.local_memory_stack.append(self.mem.local_)
                self.temp_memory_stack.append(self.mem.temp_)
                self.mem.local_ = ExecutionMemorySegment(self.mem._BASE_LOCAL)
                self.mem.temp_ = ExecutionMemorySegment(self.mem._BASE_TEMP)
                self.assign_parameters(self.inter_code['DirFunc'][self.current_func]['parameters'])
                self.parameters.clear()
                IP = quad['result']
            elif quad['operator'] == 'ENDFunc':
                # hacer salto con pila de contextos
                self.mem.local_.reset_memory()
                self.mem.temp_.reset_memory()
                self.mem.local_ = self.local_memory_stack.pop()
                self.mem.temp_ = self.temp_memory_stack.pop()
                IP = self.context_stack.pop()
            elif quad['operator'] == 'ENDProg':
                break
            else:
                IP+=1
            self.check_overflow()
