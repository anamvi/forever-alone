from semantic_cube import SemanticCube

temp_counter = 1
cont = 0

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
        self.quadruples = []
        self.operator_stack = []
        self.variable_stack = []
        self.type_stack = []
        self.jumps_stack = []
        self.semantic = SemanticCube()

    def add_operation_quadruple(self):
        global temp_counter
        op = self.operator_stack.pop()
        r_var = self.variable_stack.pop()
        r_var_type = self.type_stack.pop()
        l_var = self.variable_stack.pop()
        l_var_type = self.type_stack.pop()
        res = 't'+str(temp_counter)
        # print('operation quadruple -- ' + op + ' ' +str(l_var) + ' ' + str(r_var) + ' '+ res)

        res_type = self.semantic.cube[op][r_var_type][l_var_type]

        if res_type != 'error' :
            current_quad = Quadruple(op, l_var, r_var, res)
            temp_counter+=1
            self.quadruples.append(current_quad)
            self.variable_stack.append(res)
            self.type_stack.append(res_type)
            print(self.variable_stack)
            print(self.type_stack)
            print(self.operator_stack)
            print('\n')
            # print(self.operator_stack)
        else:
            raise Exception('ERROR type mismatch' + '\n right: ' + r_var_type + "     left: " + l_var_type)

    def add_return_quadruple(self):
        val = self.variable_stack.pop()
        value_type = self.type_stack.pop()
        print(self.variable_stack)
        print(self.type_stack)
        print(self.operator_stack)
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
        print('\n')
        # print(self.operator_stack)
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
        global temp_counter
        op = self.operator_stack.pop()
        num_type = self.type_stack.pop()
        num = self.variable_stack.pop()
        print(self.variable_stack)
        print(self.type_stack)
        print(self.operator_stack)
        print('\n')
        if self.semantic.cube[op][num_type][None] != 'error':
            res = 't'+str(temp_counter)
            current_quad = Quadruple(op,num,None,res)
            self.quadruples.append(current_quad)
            temp_counter+=1
            self.variable_stack.append(res)
            self.type_stack.append(num_type)
        else:
            raise Exception('ERROR type mismatch'+ '\n values of type '+ num_type + " cannot be made negative" )

    def add_assign_temp_quadruple(self):
        global temp_counter
        num_type = self.type_stack.pop()
        num = self.variable_stack.pop()
        print(self.variable_stack)
        print(self.type_stack)
        print(self.operator_stack)
        print('\n')
        res = 't'+str(temp_counter) # del tipo del num
        current_quad = Quadruple('=',num,None,res)
        self.quadruples.append(current_quad)
        temp_counter+=1
        self.variable_stack.append(res)
        self.type_stack.append(num_type)

    def add_self_increment_quadruple(self, increment):
        num_type = self.type_stack.pop()
        num = self.variable_stack.pop()
        res = 't'+str(temp_counter)
        # maybe make a += operator?
        current_quad = Quadruple('+',num,increment,res)
        self.quadruples.append(current_quad)
        current_quad = Quadruple('=',res,None,num)
        self.quadruples.append(current_quad)
