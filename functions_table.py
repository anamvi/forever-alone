class Variable:
    def __init__(self, name, type):
        self.name = name
        self.type = type

class Function(object):
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.variables = {}
        # agregar parámetros a arreglo de parámetros

    def add_variable(self, name, type):
        if name in self.variables:
            raise Exception("La variable ya existe en este contexto.")
        self.variables[name] = Variable(name, type)

    def check_variable_exists(self, name):
        if name in self.variables:
            return True
        return False

class FunctionsTable:
    def __init__(self):
        self.functions = {}
        self.add_function("global", 'void', {})

    def add_function(self, name, type):
        if name in self.functions:
            raise Exception("La función ya existe.")
        else:
            self.functions[name] = Function(name, type)

    def check_function_exists(self, name):
        if name in self.functions:
            return True
        return False
