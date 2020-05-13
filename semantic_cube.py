class OperandDictionary:
    def __init__(self):
        pass

class SemanticCube:
    def __init__(self):
        comparison_ops = ['>', '<', '>=', '<=', '==']
        logic_ops = ['&', '|']
        aritmethic_ops = ['+', '-', '*']
        cube = {}
        for x in comparison_ops:
            cube[x]={
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
            cube[x]={
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
        for x in logic_ops:
            cube[x]={
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

        cube['/']={
            'int': {
                'int': 'float',
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
                
