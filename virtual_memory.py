class VirtualMemorySegment:
    def __init__(self, dir):
        self.initial_dir = dir
        self.integers = []
        self.floats = []
        self.strings = []
        self.bools = []
        self.pointers = []

        # Offset for each data type
        self._BASE_INT = 0
        self._BASE_FLOAT = 2000
        self._BASE_STRING = 4000
        self._BASE_BOOL = 6000
        self._BASE_PTR = 8000

    def output(self):
        out = []
        for index, val in enumerate(self.integers):
            out.append({'address' : index+self._BASE_INT+self.initial_dir,
            'value' : val})
        for index, val in enumerate(self.floats):
            out.append({'address' : index+self._BASE_FLOAT+self.initial_dir,
            'value' : val})
        for index, val in enumerate(self.strings):
            out.append({'address' : index+self._BASE_STRING+self.initial_dir,
            'value' : val})
        for index, val in enumerate(self.bools):
            out.append({'address' : index+self._BASE_BOOL+self.initial_dir,
            'value' : val})
        for index, val in enumerate(self.pointers):
            out.append({'address' : index+self._BASE_PTR+self.initial_dir,
            'value' : val})
        return out

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
    def add_value(self, value, type):
        if type == 'int':
            if len(self.integers) == 2000:
                raise Exception('StackOverflow: too many values of type integer')
            if value not in self.integers:
                self.integers.append(value)
            return self.integers.index(value)+self._BASE_INT+self.initial_dir
        elif type == 'float':
            if len(self.floats) == 2000:
                raise Exception('StackOverflow: too many values of type float')
            if value not in self.floats:
                self.floats.append(value)
            return self.floats.index(value)+self._BASE_FLOAT+self.initial_dir
        elif type == 'string':
            if len(self.strings) == 2000:
                raise Exception('StackOverflow: too many values of type string')
            if value not in self.strings:
                self.strings.append(value)
            return self.strings.index(value)+self._BASE_STRING+self.initial_dir
        elif type == 'bool':
            if len(self.bools) == 2000:
                raise Exception('StackOverflow: too many values of type bool')
            if value not in self.bools:
                self.bools.append(value)
            return self.bools.index(value)+self._BASE_BOOL+self.initial_dir
        elif type == 'ptr':
            if len(self.pointers) == 2000:
                raise Exception('StackOverflow: too many values of type pointer')
            if value not in self.pointers:
                self.pointers.append(value)
            return self.pointers.index(value)+self._BASE_PTR+self.initial_dir
        else:
            raise TypeError("Type not supported")

    def get_value(self, dir):
        if self._BASE_INT <= dir-self.initial_dir < self._BASE_FLOAT:
            return self.integers[dir-self.initial_dir-self._BASE_INT]
        elif self._BASE_FLOAT <= dir-self.initial_dir < self._BASE_STRING:
            return self.floats[dir-self.initial_dir-self._BASE_FLOAT]
        elif self._BASE_STRING <= dir-self.initial_dir < self._BASE_BOOL:
            return self.strings[dir-self.initial_dir-self._BASE_STRING]
        elif self._BASE_BOOL <= dir-self.initial_dir < self._BASE_PTR:
            return self.bools[dir-self.initial_dir-self._BASE_BOOL]
        elif self._BASE_PTR <= dir-self.initial_dir:
            return self.pointers[dir-self.initial_dir-self._BASE_PTR]

    # def load_value(self, value, dir):
    #     print('se agrego '+ str(value) + ' a ' + str(dir))
    #     if self._BASE_INT <= dir-self.initial_dir < self._BASE_FLOAT:
    #         if dir-self.initial_dir-self._BASE_INT >= len(self.integers):
    #             self.integers.append(value)
    #         else:
    #             self.integers[dir-self.initial_dir-self._BASE_INT] = value
    #     elif self._BASE_FLOAT <= dir-self.initial_dir < self._BASE_STRING:
    #         if dir-self.initial_dir-self._BASE_FLOAT >= len(self.floats):
    #             self.floats.append(value)
    #         else:
    #             self.floats[dir-self.initial_dir-self._BASE_FLOAT] = value
    #     elif self._BASE_STRING <= dir-self.initial_dir < self._BASE_BOOL:
    #         if dir-self.initial_dir-self._BASE_STRING >= len(self.strings):
    #             self.strings.append(value)
    #         else:
    #             self.strings[dir-self.initial_dir-self._BASE_STRING] = value
    #     elif self._BASE_BOOL <= dir-self.initial_dir < self._BASE_PTR:
    #         if dir-self.initial_dir-self._BASE_BOOL >= len(self.bools):
    #             self.bools.append(value)
    #         else:
    #             self.bools[dir-self.initial_dir-self._BASE_BOOL] = value
    #     elif self._BASE_PTR <= dir-self.initial_dir:
    #         if dir-self.initial_dir-self._BASE_PTR >= len(self.pointers):
    #             self.pointers.append(value)
    #         else:
    #             self.pointers[dir-self.initial_dir-self._BASE_PTR] = value

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
