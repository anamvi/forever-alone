class SemanticCube:
    def __init__(self):
        comparison_ops = ['>', '<', '>=', '<=']
        logic_ops = ['&', '|']
        aritmethic_ops_unary = ['+', '-']
        aritmethic_ops = ['+', '-','*', '/']
        self.cube = {}
        for x in comparison_ops:
            self.cube[x]={
                'int': {
                    'int': 'bool',
                    'float': 'bool',
                    'char': 'error',
                    'bool': 'error',
                    'string': 'error',
                    None : 'error'
                },
                'float': {
                    'int': 'bool',
                    'float': 'bool',
                    'char': 'error',
                    'bool': 'error',
                    'string': 'error',
                    None : 'error'
                },
                'char': {
                    'int': 'error',
                    'float': 'error',
                    'char': 'bool',
                    'bool': 'error',
                    'string': 'error',
                    None : 'error'
                },
                'bool': {
                    'int': 'error',
                    'float': 'error',
                    'char': 'error',
                    'bool': 'error',
                    'string': 'error',
                    None : 'error'
                },
                'string': {
                    'int': 'error',
                    'float': 'error',
                    'char': 'error',
                    'bool': 'error',
                    'string': 'bool',
                    None : 'error'
                }
            }
        for x in aritmethic_ops:
            self.cube[x]={
                'int': {
                    'int': 'int',
                    'float': 'float',
                    'char': 'error',
                    'bool': 'error',
                    'string': 'error',
                    None : 'error'
                },
                'float': {
                    'int': 'float',
                    'float': 'float',
                    'char': 'error',
                    'bool': 'error',
                    'string': 'error',
                    None : 'error'
                },
                'char': {
                    'int': 'error',
                    'float': 'error',
                    'char': 'error',
                    'bool': 'error',
                    'string': 'error',
                    None : 'error'
                },
                'bool': {
                    'int': 'error',
                    'float': 'error',
                    'char': 'error',
                    'bool': 'error',
                    'string': 'error',
                    None : 'error'
                },
                'string': {
                    'int': 'error',
                    'float': 'error',
                    'char': 'error',
                    'bool': 'error',
                    'string': 'error',
                    None : 'error'
                }
            }
        for x in aritmethic_ops_unary:
            self.cube[x]['int'][None] = 'int'
            self.cube[x]['float'][None] = 'float'
        for x in logic_ops:
            self.cube[x]={
                'int': {
                    'int': 'error',
                    'float': 'error',
                    'char': 'error',
                    'bool': 'error',
                    'string': 'error',
                    None : 'error'
                },
                'float': {
                    'int': 'error',
                    'float': 'error',
                    'char': 'error',
                    'bool': 'error',
                    'string': 'error',
                    None : 'error'
                },
                'char': {
                    'int': 'error',
                    'float': 'error',
                    'char': 'error',
                    'bool': 'error',
                    'string': 'error',
                    None : 'error'
                },
                'bool': {
                    'int': 'error',
                    'float': 'error',
                    'char': 'error',
                    'bool': 'bool',
                    'string': 'error',
                    None : 'error'
                },
                'string': {
                    'int': 'error',
                    'float': 'error',
                    'char': 'error',
                    'bool': 'error',
                    'string': 'error',
                    None : 'error'
                }
            }

        self.cube['==']={
            'int': {
                'int': 'bool',
                'float': 'error',
                'char': 'error',
                'bool': 'error',
                'string': 'error',
                None : 'error'
            },
            'float': {
                'int': 'error',
                'float': 'bool',
                'char': 'error',
                'bool': 'error',
                'string': 'error',
                None : 'error'
            },
            'char': {
                'int': 'error',
                'float': 'error',
                'char': 'bool',
                'bool': 'error',
                'string': 'error',
                None : 'error'
            },
            'bool': {
                'int': 'error',
                'float': 'error',
                'char': 'error',
                'bool': 'bool',
                'string': 'error',
                None : 'error'
            },
            'string': {
                'int': 'error',
                'float': 'error',
                'char': 'error',
                'bool': 'error',
                'string': 'bool',
                None : 'error'
            }
        }
        self.cube['=']={
            'int': {
                'int': 'int',
                'float': 'error',
                'char': 'error',
                'bool': 'error',
                'string': 'error',
                None : 'error'
            },
            'float': {
                'int': 'error',
                'float': 'float',
                'char': 'error',
                'bool': 'error',
                'string': 'error',
                None : 'error'
            },
            'char': {
                'int': 'error',
                'float': 'error',
                'char': 'char',
                'bool': 'error',
                'string': 'error',
                None : 'error'
            },
            'bool': {
                'int': 'error',
                'float': 'error',
                'char': 'error',
                'bool': 'bool',
                'string': 'error',
                None : 'error'
            },
            'string': {
                'int': 'error',
                'float': 'error',
                'char': 'error',
                'bool': 'error',
                'string': 'string',
                None : 'error'
            }
        }

    def __str__(self):
        output = "------------ semantic cube -------------\n"
        for i in self.cube:
            output +=  i + " : " + "\n"
            for j in self.cube[i]:
                output += "-----> " + j + "\n"
                for k in self.cube[i][j]:
                    output += "             " +j +i+  k + " = " + self.cube[i][j][k] + "\n"
            output += "\n"
        return output
