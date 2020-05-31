from virtual_memory import VirtualMemorySegment
from execution_memory import ExecutionMemorySegment

class Memory:
    def __init__(self, mem_type):
        # Declare initial directions of each memory segment.
        # Global and Local have 8000 spaces each (2000 for each data type).
        # Temporal and Constant adds 2000 extra for pointers.
        self._BASE_GLOBAL = 1000
        self._BASE_LOCAL = 9000
        self._BASE_TEMP = 17000
        self._BASE_CONSTANT = 27000
        # Create the four memory segments, depending on the type of memory
        if mem_type == 'virtual':
            self.global_ = VirtualMemorySegment(self._BASE_GLOBAL)
            self.local_ = VirtualMemorySegment(self._BASE_LOCAL)
            self.temp_ = VirtualMemorySegment(self._BASE_TEMP)
            self.constant_ = VirtualMemorySegment(self._BASE_CONSTANT)
        elif mem_type == 'execution':
            self.global_ = ExecutionMemorySegment(self._BASE_GLOBAL)
            self.local_ = ExecutionMemorySegment(self._BASE_LOCAL)
            self.temp_ = ExecutionMemorySegment(self._BASE_TEMP)
            self.constant_ = ExecutionMemorySegment(self._BASE_CONSTANT)

    def __str__(self):
        output = '---------- GLOBAL MEMORY ---------- \n' + str(self.global_)
        output += '---------- LOCAL MEMORY ---------- \n' + str(self.local_)
        output += '---------- TEMPORALS ---------- \n' + str(self.temp_)
        output += '---------- CONSTANTS ---------- \n' + str(self.constant_)
        output+= '\n'
        return output

    def get_value(self, dir):
        if self._BASE_GLOBAL <= dir < self._BASE_LOCAL:
            return self.global_.get_value(dir)
        elif self._BASE_LOCAL <= dir < self._BASE_TEMP:
            return self.local_.get_value(dir)
        elif self._BASE_TEMP <= dir < self._BASE_CONSTANT:
            return self.temp_.get_value(dir)
        elif self._BASE_CONSTANT <= dir:
            return self.constant_.get_value(dir)

    def load_value(self, value, dir):
        if self._BASE_GLOBAL <= dir < self._BASE_LOCAL:
            return self.global_.load_value(value, dir)
        elif self._BASE_LOCAL <= dir < self._BASE_TEMP:
            return self.local_.load_value(value, dir)
        elif self._BASE_TEMP <= dir < self._BASE_CONSTANT:
            return self.temp_.load_value(value, dir)
        elif self._BASE_CONSTANT <= dir:
            return self.constant_.load_value(value, dir)

    def check_type(self, dir):
        if self._BASE_GLOBAL <= dir < self._BASE_LOCAL:
            return self.global_.check_type(dir)
        elif self._BASE_LOCAL <= dir < self._BASE_TEMP:
            return self.local_.check_type(dir)
        elif self._BASE_TEMP <= dir < self._BASE_CONSTANT:
            return self.temp_.check_type(dir)
        elif self._BASE_CONSTANT <= dir:
            return self.constant_.check_type(dir)
