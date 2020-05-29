from semantic_cube import SemanticCube
from virtual_memory import VirtualMemory

class Quadruple:
    def __init__(self, operator, left_operand, right_operand, result):
        self.operator = operator
        self.left_operand = left_operand
        self.right_operand = right_operand
        self.result = result

    def __str__(self):
        output = "--> " + str(self.operator) + " " + str(self.left_operand) + " "+ str(self.right_operand) + " "+ str(self.result) + "\n"
        return output

class InterCode:
    def __init__(self):
        self.temp_counter = 1
        self.parameter_counter = 1
        self.quadruples = []
        self.operator_stack = []
        self.variable_stack = []
        self.type_stack = []
        self.jumps_stack = []
        self.semantic = SemanticCube()
        self.mem = VirtualMemory()

    def add_operation_quadruple(self):
        op = self.operator_stack.pop()
        r_var = self.variable_stack.pop()
        r_var_type = self.type_stack.pop()
        l_var = self.variable_stack.pop()
        l_var_type = self.type_stack.pop()
        # res = 't'+str(self.temp_counter)
        # print('operation quadruple -- ' + op + ' ' +str(l_var) + ' ' + str(r_var) + ' '+ res)

        res_type = self.semantic.cube[op][r_var_type][l_var_type]
        res = self.mem.temp_.add_value('t'+str(self.temp_counter),res_type)
        self.temp_counter+=1
        if res_type != 'error' :
            current_quad = Quadruple(op, l_var, r_var, res)
            self.quadruples.append(current_quad)
            self.variable_stack.append(res)
            self.type_stack.append(res_type)
            print(self.variable_stack)
            print(self.type_stack)
            print(self.operator_stack)
            print(self.jumps_stack)
            print('\n')
        else:
            raise Exception('ERROR type mismatch' + '\n right: ' + r_var_type + "     left: " + l_var_type)

    def add_return_quadruple(self):
        val = self.variable_stack.pop()
        value_type = self.type_stack.pop()
        print(self.variable_stack)
        print(self.type_stack)
        print(self.operator_stack)
        print(self.jumps_stack)
        print('\n')
        # ----------- check that the return value type is the same as the function type ------------------
        current_quad = Quadruple('return', None, None, val)
        self.quadruples.append(current_quad)

    def add_IO_quadruple(self):
        op = self.operator_stack.pop()
        val = self.variable_stack.pop()
        value_type = self.type_stack.pop()
        print(self.variable_stack)
        print(self.type_stack)
        print(self.operator_stack)
        print(self.jumps_stack)
        print('\n')
        current_quad = Quadruple(op, None, None, val)
        self.quadruples.append(current_quad)
        self.operator_stack.append(op)

    def add_assignment_quadruple(self):
        op = self.operator_stack.pop()
        val = self.variable_stack.pop()
        value_type = self.type_stack.pop()
        var = self.variable_stack.pop()
        variable_type = self.type_stack.pop()

        # print('assignment quadruple -- ' + op + ' ' +str(val) + ' ' + str(var))
        print(self.variable_stack)
        print(self.type_stack)
        print(self.operator_stack)
        print(self.jumps_stack)
        print('\n')
        if self.semantic.cube[op][value_type][variable_type] != 'error' :
            current_quad = Quadruple(op, val, None, var)
            self.quadruples.append(current_quad)
        else:
            raise Exception('ERROR type mismatch'+ '\n value: '+ str(val) + " | "+ value_type + "     variable: " + str(var) + " | " +variable_type)

    def add_gotof_quadruple(self, dest):
        result = self.variable_stack.pop()
        current_quad = Quadruple('GOTOF',result,None,dest)
        self.quadruples.append(current_quad)
        self.push_jump(-1)

    def add_goto_quadruple(self,dest):
        current_quad = Quadruple('GOTO',None,None,dest)
        self.quadruples.append(current_quad)

    def fill(self, quadruple_ptr, destination):
        self.quadruples[quadruple_ptr].result = destination

    def push_jump(self, offset):
        self.jumps_stack.append(len(self.quadruples)+offset)

    def add_unary_quadruple(self):
        op = self.operator_stack.pop()
        num_type = self.type_stack.pop()
        num = self.variable_stack.pop()
        print(self.variable_stack)
        print(self.type_stack)
        print(self.operator_stack)
        print(self.jumps_stack)
        print('\n')
        res_type=self.semantic.cube[op][num_type][None]
        if res_type != 'error':
            res = self.mem.temp_.add_value('t'+str(self.temp_counter),res_type)
            self.temp_counter+=1
            current_quad = Quadruple(op,num,None,res)
            self.quadruples.append(current_quad)
            self.variable_stack.append(res)
            self.type_stack.append(num_type)
        else:
            raise Exception('ERROR type mismatch'+ '\n values of type '+ num_type + " cannot be made negative" )

    def add_assign_temp_quadruple(self):
        num_type = self.type_stack.pop()
        num = self.variable_stack.pop()
        print(self.variable_stack)
        print(self.type_stack)
        print(self.operator_stack)
        print(self.jumps_stack)
        print('\n')
        res = self.mem.temp_.add_value('t'+str(self.temp_counter),num_type)
        self.temp_counter+=1
        current_quad = Quadruple('=',num,None,res)
        self.quadruples.append(current_quad)
        self.variable_stack.append(res)
        self.type_stack.append(num_type)

    def add_self_increment_quadruple(self, increment):
        num_type = self.type_stack.pop()
        num = self.variable_stack.pop()
        res = self.mem.temp_.add_value('t'+str(self.temp_counter),num_type)
        print(self.variable_stack)
        print(self.type_stack)
        print(self.operator_stack)
        print(self.jumps_stack)
        self.temp_counter+=1
        current_quad = Quadruple('+',num,increment,res)
        self.quadruples.append(current_quad)
        current_quad = Quadruple('=',res,None,num)
        self.quadruples.append(current_quad)


    def add_verify_limits_quadruple(self):
        dim = self.variable_stack.pop()
        limit = self.variable_stack.pop()
        type = self.type_stack.pop()
        print(self.variable_stack)
        print(self.type_stack)
        print(self.operator_stack)
        print(self.jumps_stack)
        current_quad = Quadruple('ver',dim,None,limit) #create a function in virtual memory that will be called by the virtual machine
        self.quadruples.append(current_quad)
        self.variable_stack.append(dim)

    def add_array_base_direction_quadruple(self):
        size = self.variable_stack.pop()
        dir = self.variable_stack.pop()
        type = self.type_stack.pop()
        print(self.variable_stack)
        print(self.type_stack)
        print(self.operator_stack)
        print(self.jumps_stack)
        res = self.mem.temp_.add_value('t'+str(self.temp_counter),'ptr')
        self.temp_counter+=1
        current_quad = Quadruple('+',size,dir,res)
        self.quadruples.append(current_quad)
        self.variable_stack.append(res)
        self.type_stack.append(type)

    def add_endfunc(self):
        current_quad = Quadruple('ENDFunc',None,None,None)
        self.quadruples.append(current_quad)

    def add_era_quadruple(self, dir, space):
        current_quad = Quadruple('ERA',space,None,dir)
        self.quadruples.append(current_quad)
