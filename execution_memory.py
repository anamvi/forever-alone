class ExecutionMemorySegment:
    def __init__(self, dir):
        self.initial_dir = dir
        self.integers = {}
        self.floats = {}
        self.strings = {}
        self.bools = {}
        self.pointers = {}

        # Offset for each data type
        self._BASE_INT = 0
        self._BASE_FLOAT = 2000
        self._BASE_STRING = 4000
        self._BASE_BOOL = 6000
        self._BASE_PTR = 8000

    def __str__(self):
        output = '-- Initial Direction: '+ str(self.initial_dir)
        output+= '\n        INTEGERS:'
        output+= '\n        -- start: ' + str(self.initial_dir+self._BASE_INT)
        output+= '\n        -- end: ' + str(self.initial_dir+self._BASE_INT+1999)
        output+= '\n        -- current: ' + str(self.initial_dir+self._BASE_INT+len(self.integers))
        output+= '\n        -- ' + str(self.integers)
        output+= '\n        FLOATS:'
        output+= '\n        -- start: ' + str(self.initial_dir+self._BASE_FLOAT)
        output+= '\n        -- end: ' + str(self.initial_dir+self._BASE_FLOAT+1999)
        output+= '\n        -- current: ' + str(self.initial_dir+self._BASE_FLOAT+len(self.floats))
        output+= '\n        -- ' + str(self.floats)
        output+= '\n        STRINGS:'
        output+= '\n        -- start: ' + str(self.initial_dir+self._BASE_STRING)
        output+= '\n        -- end: ' + str(self.initial_dir+self._BASE_STRING+1999)
        output+= '\n        -- current: ' + str(self.initial_dir+self._BASE_STRING+len(self.strings))
        output+= '\n        -- ' + str(self.strings)
        output+= '\n        BOOLS:'
        output+= '\n        -- start: ' + str(self.initial_dir+self._BASE_BOOL)
        output+= '\n        -- end: ' + str(self.initial_dir+self._BASE_BOOL+1999)
        output+= '\n        -- current: ' + str(self.initial_dir+self._BASE_BOOL+len(self.bools))
        output+= '\n        -- ' + str(self.bools)
        output+= '\n        POINTERS:'
        output+= '\n        -- start: ' + str(self.initial_dir+self._BASE_PTR)
        output+= '\n        -- end: ' + str(self.initial_dir+self._BASE_PTR+1999)
        output+= '\n        -- current: ' + str(self.initial_dir+self._BASE_PTR+len(self.pointers))
        output+= '\n        -- ' + str(self.pointers)
        output+= '\n\n'
        return output

    def reset_memory(self):
        self.integers.clear()
        self.floats.clear()
        self.strings.clear()
        self.bools.clear()
        self.pointers.clear()

    # -------------------------- ACCESS VALUES IN MEMORY --------------------------
    # def add_value(self, value, type):
    #     if type == 'int':
    #         if value not in self.integers:
    #             self.integers.append(value)
    #         return self.integers.index(value)+self._BASE_INT+self.initial_dir
    #     elif type == 'float':
    #         if value not in self.floats:
    #             self.floats.append(value)
    #         return self.floats.index(value)+self._BASE_FLOAT+self.initial_dir
    #     elif type == 'string':
    #         if value not in self.strings:
    #             self.strings.append(value)
    #         return self.strings.index(value)+self._BASE_STRING+self.initial_dir
    #     elif type == 'bool':
    #         if value not in self.bools:
    #             self.bools.append(value)
    #         return self.bools.index(value)+self._BASE_BOOL+self.initial_dir
    #     elif type == 'ptr':
    #         if value not in self.pointers:
    #             self.pointers.append(value)
    #         return self.pointers.index(value)+self._BASE_PTR+self.initial_dir
    #     else:
    #         raise Exception("Type not supported")

    def get_value(self, dir):
        if self._BASE_INT <= dir-self.initial_dir < self._BASE_FLOAT:
            return self.integers.get(dir)
        elif self._BASE_FLOAT <= dir-self.initial_dir < self._BASE_STRING:
            return self.floats.get(dir)
        elif self._BASE_STRING <= dir-self.initial_dir < self._BASE_BOOL:
            return self.strings.get(dir)
        elif self._BASE_BOOL <= dir-self.initial_dir < self._BASE_PTR:
            return self.bools.get(dir)
        elif self._BASE_PTR <= dir-self.initial_dir:
            return self.pointers.get(dir)

    def load_value(self, value, dir):
        if self._BASE_INT <= dir-self.initial_dir < self._BASE_FLOAT:
            self.integers[dir] = value
        elif self._BASE_FLOAT <= dir-self.initial_dir < self._BASE_STRING:
            self.floats[dir] = value
        elif self._BASE_STRING <= dir-self.initial_dir < self._BASE_BOOL:
            self.strings[dir] = value
        elif self._BASE_BOOL <= dir-self.initial_dir < self._BASE_PTR:
            self.bools[dir] = value
        elif self._BASE_PTR <= dir-self.initial_dir:
            self.pointers[dir] = value

    def check_type(self, dir):
        if self._BASE_INT <= dir-self.initial_dir < self._BASE_FLOAT:
            return 'int'
        elif self._BASE_FLOAT <= dir-self.initial_dir < self._BASE_STRING:
            return 'float'
        elif self._BASE_STRING <= dir-self.initial_dir < self._BASE_BOOL:
            return 'string'
        elif self._BASE_BOOL <= dir-self.initial_dir < self._BASE_PTR:
            return 'bool'
        elif self._BASE_PTR <= dir-self.initial_dir:
            return 'ptr'

    def count_content(self):
        counter = 0
        counter+= len(self.integers)
        counter+= len(self.floats)
        counter+= len(self.strings)
        counter+= len(self.bools)
        counter+= len(self.pointers)
        return counter
