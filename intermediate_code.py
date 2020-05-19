from semantic_cube import SemanticCube

counter = 1

class Quadruple:
    def __init__(self, operator, left_operand, right_operand, result):
        self.operator = operator
        self.left_operand = left_operand
        self.right_operand = right_operand
        self.result = result

    def __str__(self):
        output = "Quad --> " + self.operator + " " + str(self.left_operand) + " "+ str(self.right_operand) + " "+ self.result + "\n"
        return output

class InterCode:
    def __init__(self):
        self.quadruples = []
        self.operator_stack = []
        self.variable_stack = []
        self.type_stack = []
        self.semantic = SemanticCube()

    def add_operation_quadruple(self):
        global counter
        op = self.operator_stack.pop()
        r_var = self.variable_stack.pop()
        r_var_type = self.type_stack.pop()
        l_var = self.variable_stack.pop()
        l_var_type = self.type_stack.pop()
        res = 't'+str(counter)
        print('operation quadruple -- ' + op + ' ' +str(l_var) + ' ' + str(r_var) + ' '+ res)

        res_type = self.semantic.cube[op][r_var_type][l_var_type]

        if res_type != 'error' :
            current_quad = Quadruple(op, l_var, r_var, res)
            counter+=1
            self.quadruples.append(current_quad)
            self.variable_stack.append(res)
            self.type_stack.append(res_type)
            print(self.variable_stack)
            print(self.type_stack)
            print(self.operator_stack)
        else:
            raise Exception('ERROR type mismatch' + '\n right: ' + r_var_type + "     left: " + l_var_type)

    def add_assignment_quadruple(self):
        global counter

        op = self.operator_stack.pop()
        val = self.variable_stack.pop()
        value_type = self.type_stack.pop()
        var = self.variable_stack.pop()
        variable_type = self.type_stack.pop()
        print('assignment quadruple -- ' + op + ' ' +str(val) + ' ' + str(var))
        print(self.variable_stack)
        print(self.type_stack)
        print(self.operator_stack)
        if self.semantic.cube[op][value_type][variable_type] != 'error' :
            current_quad = Quadruple(op, val, None, var)
            counter+=1
            self.quadruples.append(current_quad)
        else:
            raise Exception('ERROR type mismatch'+ '\n value: '+ str(val) + " | "+ value_type + "     variable: " + str(var) + " | " +variable_type)
