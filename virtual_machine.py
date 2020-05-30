import json
from memory import Memory

class VirtualMachine():
    def __init__(self):
        with open("inter.cry", 'r') as json_file:
            self.inter_code = json.load(json_file)
        self.mem = Memory()
        self.add_constants()
        self.read_obj_code()
        # print(self.mem)

    def add_constants(self):
        for i in self.inter_code['Constants']:
            self.mem.constant_.load_value(i["value"], i["address"])


    def read_obj_code(self):
        x=self.inter_code['Quadruples']
        IP = 0
        while True:
            quad = x[IP]
            if quad['operator'] == 'GOTO':
                IP = quad['result']
            elif quad['operator'] == 'GOTOF':
                if self.mem.get_value(quad['left_operand']) == False:
                    IP = quad['result']
                else:
                    IP+=1
            elif quad['operator'] == 'GOTOV':
                if self.mem.get_value(quad['left_operand']) == True:
                    IP = quad['result']
                else:
                    IP+=1
            elif quad['operator'] == '+':
                op = self.mem.get_value(quad['left_operand']) + self.mem.get_value(quad['right_operand'])
                self.mem.load_value(op, quad['result'])
                IP+=1
            elif quad['operator'] == '-':
                op = self.mem.get_value(quad['left_operand']) - self.mem.get_value(quad['right_operand'])
                self.mem.load_value(op, quad['result'])
                IP+=1
            elif quad['operator'] == '*':
                op = self.mem.get_value(quad['left_operand']) * self.mem.get_value(quad['right_operand'])
                self.mem.load_value(op, quad['result'])
                IP+=1
            elif quad['operator'] == '/':
                op = self.mem.get_value(quad['left_operand']) // self.mem.get_value(quad['right_operand'])
                self.mem.load_value(op, quad['result'])
                IP+=1
            elif quad['operator'] == '==':
                op = self.mem.get_value(quad['left_operand']) == self.mem.get_value(quad['right_operand'])
                self.mem.load_value(op, quad['result'])
                IP+=1
            elif quad['operator'] == '>=':
                op = self.mem.get_value(quad['left_operand']) >= self.mem.get_value(quad['right_operand'])
                self.mem.load_value(op, quad['result'])
                IP+=1
            elif quad['operator'] == '<=':
                op = self.mem.get_value(quad['left_operand']) <= self.mem.get_value(quad['right_operand'])
                self.mem.load_value(op, quad['result'])
                IP+=1
            elif quad['operator'] == '<':
                op = self.mem.get_value(quad['left_operand']) < self.mem.get_value(quad['right_operand'])
                self.mem.load_value(op, quad['result'])
                IP+=1
            elif quad['operator'] == '>':
                op = self.mem.get_value(quad['left_operand']) > self.mem.get_value(quad['right_operand'])
                self.mem.load_value(op, quad['result'])
                IP+=1
            elif quad['operator'] == '=':
                self.mem.load_value(self.mem.get_value(quad['left_operand']),quad['result'])
                IP+=1
            elif quad['operator'] == 'escribe':
                print(self.mem.get_value(quad['result']))
                IP+=1
            elif quad['operator'] == 'ENDProg':
                break
            else:
                IP+=1
