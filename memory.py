class Memory:
    def __init__(self, dir):
        self.initial_dir = dir
        self.integers = {}
        self.floats = {}
        self.strings = {}
        self.bools = {}

        # Direccion base
        _BASE_INT = 0
        _BASE_FLOAT = 4000
        _BASE_STRING = 8000
        _BASE_BOOL = 12000
