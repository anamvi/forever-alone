class SemanticCube:
    def __init__(self):
        comparison_ops = ['>', '<', '>=', '<=', '==', '!=']
        equality_ops = ['==', '!=']
        logic_ops = ['&', '|']
        aritmethic_ops_unary = ['+', '-']
        aritmethic_ops = ['+', '-','*', '/']
        self.cube = {}
        for x in comparison_ops:
            self.cube[x]={
                'int': {
                    'int': 'bool',
                    'float': 'bool',
                    'bool': 'error',
                    'string': 'error',
                    'ptr': 'bool',
                    None : 'error'
                },
                'float': {
                    'int': 'bool',
                    'float': 'bool',
                    'bool': 'error',
                    'string': 'error',
                    'ptr': 'bool',
                    None : 'error'
                },
                'bool': {
                    'int': 'error',
                    'float': 'error',
                    'bool': 'error',
                    'string': 'error',
                    'ptr': 'error',
                    None : 'error'
                },
                'string': {
                    'int': 'error',
                    'float': 'error',
                    'bool': 'error',
                    'string': 'bool',
                    'ptr': 'bool',
                    None : 'error'
                },
                'ptr': {
                    'int': 'bool',
                    'float': 'bool',
                    'bool': 'error',
                    'string': 'bool',
                    'ptr': 'bool',
                    None : 'error'
                },
                None: {
                    'int': 'error',
                    'float': 'error',
                    'bool': 'error',
                    'string': 'error',
                    'ptr': 'error',
                    None : 'error'
                }
            }
        for x in equality_ops:
            self.cube[x]['bool']['bool'] = 'bool'
            self.cube[x]['ptr']['bool'] = 'bool'
            self.cube[x]['bool']['ptr'] = 'bool'
        for x in aritmethic_ops:
            self.cube[x]={
                'int': {
                    'int': 'int',
                    'float': 'float',
                    'bool': 'error',
                    'string': 'error',
                    'ptr': 'int',
                    None : 'error'
                },
                'float': {
                    'int': 'float',
                    'float': 'float',
                    'bool': 'error',
                    'string': 'error',
                    'ptr': 'float',
                    None : 'error'
                },
                'bool': {
                    'int': 'error',
                    'float': 'error',
                    'bool': 'error',
                    'string': 'error',
                    'ptr': 'error',
                    None : 'error'
                },
                'string': {
                    'int': 'error',
                    'float': 'error',
                    'bool': 'error',
                    'string': 'string',
                    'ptr': 'error',
                    None : 'error'
                },
                'ptr': {
                    'int': 'int',
                    'float': 'float',
                    'bool': 'error',
                    'string': 'error',
                    'ptr': 'ptr',
                    None : 'error'
                },
                None: {
                    'int': 'error',
                    'float': 'error',
                    'bool': 'error',
                    'string': 'error',
                    'ptr': 'error',
                    None : 'error'
                }
            }
        for x in aritmethic_ops_unary:
            self.cube[x]['int'][None] = 'int'
            self.cube[x]['float'][None] = 'float'
            self.cube[x][None]['int'] = 'int'
            self.cube[x][None]['float'] = 'float'
        for x in logic_ops:
            self.cube[x]={
                'int': {
                    'int': 'error',
                    'float': 'error',
                    'bool': 'error',
                    'string': 'error',
                    'ptr': 'error',
                    None : 'error'
                },
                'float': {
                    'int': 'error',
                    'float': 'error',
                    'bool': 'error',
                    'string': 'error',
                    'ptr': 'error',
                    None : 'error'
                },
                'bool': {
                    'int': 'error',
                    'float': 'error',
                    'bool': 'bool',
                    'string': 'error',
                    'ptr': 'bool',
                    None : 'error'
                },
                'string': {
                    'int': 'error',
                    'float': 'error',
                    'bool': 'error',
                    'string': 'error',
                    'ptr': 'error',
                    None : 'error'
                },
                'ptr': {
                    'int': 'error',
                    'float': 'error',
                    'bool': 'bool',
                    'string': 'error',
                    'ptr': 'bool',
                    None : 'error'
                },
                None: {
                    'int': 'error',
                    'float': 'error',
                    'bool': 'error',
                    'string': 'error',
                    'ptr': 'error',
                    None : 'error'
                }
            }
        self.cube['=']={
            'int': {
                'int': 'int',
                'float': 'error',
                'bool': 'error',
                'string': 'error',
                'ptr': 'int',
                None : 'error'
            },
            'float': {
                'int': 'error',
                'float': 'float',
                'bool': 'error',
                'string': 'error',
                'ptr': 'float',
                None : 'error'
            },
            'bool': {
                'int': 'error',
                'float': 'error',
                'bool': 'bool',
                'string': 'error',
                'ptr': 'bool',
                None : 'error'
            },
            'string': {
                'int': 'error',
                'float': 'error',
                'bool': 'error',
                'string': 'string',
                'ptr': 'string',
                None : 'error'
            },
            'ptr': {
                'int': 'int',
                'float': 'float',
                'bool': 'bool',
                'string': 'string',
                'ptr': 'ptr',
                None : 'error'
            },
            None: {
                'int': 'error',
                'float': 'error',
                'bool': 'error',
                'string': 'error',
                'ptr': 'error',
                None : 'error'
            }
        }

    def __str__(self):
        output = "------------ semantic cube -------------\n"
        for i in self.cube:
            output +=  i + " : " + "\n"
            for j in self.cube[i]:
                output += "-----> " + str(j) + "\n"
                for k in self.cube[i][j]:
                    if self.cube[i][j][k] != 'error':
                        output += "             " +str(j) +" "+str(i)+" "+str(k) + " = " + self.cube[i][j][k] + "\n"
            output += "\n"
        return output
