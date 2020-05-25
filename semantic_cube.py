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
                    'string': 'error'
                },
                'float': {
                    'int': 'bool',
                    'float': 'bool',
                    'char': 'error',
                    'bool': 'error',
                    'string': 'error'
                },
                'char': {
                    'int': 'error',
                    'float': 'error',
                    'char': 'bool',
                    'bool': 'error',
                    'string': 'error'
                },
                'bool': {
                    'int': 'error',
                    'float': 'error',
                    'char': 'error',
                    'bool': 'error',
                    'string': 'error'
                },
                'string': {
                    'int': 'error',
                    'float': 'error',
                    'char': 'error',
                    'bool': 'error',
                    'string': 'bool'
                }
            }
        for x in aritmethic_ops:
            self.cube[x]={
                'int': {
                    'int': 'int',
                    'float': 'float',
                    'char': 'error',
                    'bool': 'error',
                    'string': 'error'
                },
                'float': {
                    'int': 'float',
                    'float': 'float',
                    'char': 'error',
                    'bool': 'error',
                    'string': 'error'
                },
                'char': {
                    'int': 'error',
                    'float': 'error',
                    'char': 'error',
                    'bool': 'error',
                    'string': 'error'
                },
                'bool': {
                    'int': 'error',
                    'float': 'error',
                    'char': 'error',
                    'bool': 'error',
                    'string': 'error'
                },
                'string': {
                    'int': 'error',
                    'float': 'error',
                    'char': 'error',
                    'bool': 'error',
                    'string': 'error'
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
                    'string': 'error'
                },
                'float': {
                    'int': 'error',
                    'float': 'error',
                    'char': 'error',
                    'bool': 'error',
                    'string': 'error'
                },
                'char': {
                    'int': 'error',
                    'float': 'error',
                    'char': 'error',
                    'bool': 'error',
                    'string': 'error'
                },
                'bool': {
                    'int': 'error',
                    'float': 'error',
                    'char': 'error',
                    'bool': 'bool',
                    'string': 'error'
                },
                'string': {
                    'int': 'error',
                    'float': 'error',
                    'char': 'error',
                    'bool': 'error',
                    'string': 'error'
                }
            }

        self.cube['==']={
            'int': {
                'int': 'bool',
                'float': 'error',
                'char': 'error',
                'bool': 'error',
                'string': 'error'
            },
            'float': {
                'int': 'error',
                'float': 'bool',
                'char': 'error',
                'bool': 'error',
                'string': 'error'
            },
            'char': {
                'int': 'error',
                'float': 'error',
                'char': 'bool',
                'bool': 'error',
                'string': 'error'
            },
            'bool': {
                'int': 'error',
                'float': 'error',
                'char': 'error',
                'bool': 'bool',
                'string': 'error'
            },
            'string': {
                'int': 'error',
                'float': 'error',
                'char': 'error',
                'bool': 'error',
                'string': 'bool'
            }
        }
        self.cube['=']={
            'int': {
                'int': 'int',
                'float': 'error',
                'char': 'error',
                'bool': 'error',
                'string': 'error'
            },
            'float': {
                'int': 'error',
                'float': 'float',
                'char': 'error',
                'bool': 'error',
                'string': 'error'
            },
            'char': {
                'int': 'error',
                'float': 'error',
                'char': 'char',
                'bool': 'error',
                'string': 'error'
            },
            'bool': {
                'int': 'error',
                'float': 'error',
                'char': 'error',
                'bool': 'bool',
                'string': 'error'
            },
            'string': {
                'int': 'error',
                'float': 'error',
                'char': 'error',
                'bool': 'error',
                'string': 'string'
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
