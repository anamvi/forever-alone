class Variable:
    def __init__(self, name, type, dir):
        self.name = name
        self.type = type
        self.dir = dir
        self.array_size = 0

class Function:
    def __init__(self, name, type, parameters):
        self.name = name
        self.type = type
        self.variables = {}
        self.parameters = parameters

    def add_variable(self, name, type, dir):
        if name in self.variables:
            raise Exception("La variable '"+name+"' ya existe en este contexto.")
        self.variables[name] = Variable(name, type, dir)

    def variable_exists(self, name):
        if name in self.variables:
            return True
        return False

class FunctionsTable:
    def __init__(self):
        self.functions = {}
        self.add_function("global", 'void', [])

    def __str__(self):
        output = "------------ functions -------------\n"
        for i in self.functions:
            func = self.functions[i]
            output += "-----> " + func.name + " : " + \
                str(func.type) + "\n"
            output += "PARAMETERS: " + str(func.parameters) + "\n\n"
            for j in self.functions[func.name].variables:
                variable = self.functions[func.name].variables[j]
                output += "NAME: " + variable.name + "\n"
                output += "TYPE: " + str(variable.type) + "\n"
                output += "DIRECTION: " + str(variable.dir) + "\n"
                output += "ARRAY: " + str(variable.array_size) + "\n\n"

            output += "\n"
        return output

    def add_function(self, name, type, parameters):
        if name in self.functions:
            raise Exception("La función ya existe.")
        else:
            self.functions[name] = Function(name, type, parameters)

    def function_exists(self, name):
        if name in self.functions:
            return True
        return False
