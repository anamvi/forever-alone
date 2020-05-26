class MemorySegment:
    def __init__(self, dir):
        self.initial_dir = dir
        self.integers = []
        self.floats = []
        self.strings = []
        self.bools = []
        self.pointers = []

        # Offset data types
        self._BASE_INT = 0
        self._BASE_FLOAT = 2000
        self._BASE_STRING = 4000
        self._BASE_BOOL = 6000
        self._BASE_PTR = 8000

    def __str__(self):
        output = '-- Initial Direction: '+ str(self.initial_dir)
        output+= '\n        INTEGERS:'
        output+= '\n        -- start: ' + str(self.initial_dir+self._BASE_INT)
        output+= '\n        -- end: ' + str(self.initial_dir+self._BASE_INT+len(self.integers))
        output+= '\n        -- ' + str(self.integers)
        output+= '\n        FLOATS:'
        output+= '\n        -- start: ' + str(self.initial_dir+self._BASE_FLOAT)
        output+= '\n        -- end: ' + str(self.initial_dir+self._BASE_FLOAT+len(self.floats))
        output+= '\n        -- ' + str(self.floats)
        output+= '\n        STRINGS:'
        output+= '\n        -- start: ' + str(self.initial_dir+self._BASE_STRING)
        output+= '\n        -- end: ' + str(self.initial_dir+self._BASE_STRING+len(self.strings))
        output+= '\n        -- ' + str(self.strings)
        output+= '\n        BOOLS:'
        output+= '\n        -- start: ' + str(self.initial_dir+self._BASE_BOOL)
        output+= '\n        -- end: ' + str(self.initial_dir+self._BASE_BOOL+len(self.bools))
        output+= '\n        -- ' + str(self.bools)
        output+= '\n        POINTERS:'
        output+= '\n        -- start: ' + str(self.initial_dir+self._BASE_PTR)
        output+= '\n        -- end: ' + str(self.initial_dir+self._BASE_PTR+len(self.pointers))
        output+= '\n        -- ' + str(self.pointers)
        output+= '\n\n'
        return output

    def reset_memory():
        self.integers.clear()
        self.floats.clear()
        self.strings.clear()
        self.bools.clear()
        self.pointers.clear()

    # -------------------------- ACCESS VALUES IN MEMORY --------------------------
    def add_value(self, value, type):
        if type == 'int':
            if value not in self.integers:
                self.integers.append(value)
            return self.integers.index(value)+self._BASE_INT+self.initial_dir
        elif type == 'float':
            if value not in self.floats:
                self.floats.append(value)
            return self.floats.index(value)+self._BASE_FLOAT+self.initial_dir
        elif type == 'string':
            if value not in self.strings:
                self.strings.append(value)
            return self.strings.index(value)+self._BASE_STRING+self.initial_dir
        elif type == 'bool':
            if value not in self.bools:
                self.bools.append(value)
            return self.bools.index(value)+self._BASE_BOOL+self.initial_dir
        elif type == 'ptr':
            if value not in self.pointers:
                self.pointers.append(value)
            return self.pointers.index(value)+self._BASE_PTR+self.initial_dir
        else:
            raise Exception("Type not supported")

    def get_value(self, dir):
        if self._BASE_INT <= dir-self.initial_dir < self._BASE_FLOAT:
            return self.pointers[dir-self.initial_dir-self._BASE_INT]
        elif self._BASE_FLOAT <= dir-self.initial_dir < self._BASE_STRING:
            return self.pointers[dir-self.initial_dir-self._BASE_FLOAT]
        elif self._BASE_STRING <= dir-self.initial_dir < self._BASE_BOOL:
            return self.pointers[dir-self.initial_dir-self._BASE_STRING]
        elif self._BASE_BOOL <= dir-self.initial_dir < self._BASE_PTR:
            return self.pointers[dir-self.initial_dir-self._BASE_BOOL]
        elif self._BASE_PTR <= dir-self.initial_dir:
            return self.pointers[dir-self.initial_dir-self._BASE_PTR]

class VirtualMemory:
    def __init__(self):
        self._BASE_GLOBAL = 1000
        self._BASE_GLOBAL_TEMP = 11000
        self._BASE_LOCAL = 21000
        self._BASE_LOCAL_TEMP = 31000
        self._BASE_CONSTANT = 41000
        self.global_ = MemorySegment(self._BASE_GLOBAL)
        self.global_temp = MemorySegment(self._BASE_GLOBAL_TEMP)
        self.local_ = MemorySegment(self._BASE_LOCAL)
        self.local_temp = MemorySegment(self._BASE_LOCAL_TEMP)
        self.constant_ = MemorySegment(self._BASE_CONSTANT)

    def __str__(self):
        output = '---------- GLOBAL MEMORY ---------- \n' + str(self.global_)
        output += '---------- GLOBAL TEMPORALS ---------- \n' + str(self.global_temp)
        output += '---------- LOCAL MEMORY ---------- \n' + str(self.local_)
        output += '---------- LOCAL TEMPORALS ---------- \n' + str(self.local_temp)
        output += '---------- CONSTANTS ---------- \n' + str(self.constant_)
        output+= '\n'
        return output
