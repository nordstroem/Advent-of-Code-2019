import itertools
from functools import wraps
from collections import deque, defaultdict

def mode(modes, i):
    return modes[-(i + 1)] if i < len(modes) else 0

def two_argument_assignment(func):
    @wraps(func)
    def wrapped(self, src1, src2, dst, modes):
        a = self.read_value(src1, modes, 0)
        b = self.read_value(src2, modes, 1)
        func(self, a, b, dst)
        return True
    return wrapped

def zero_argument_assignment(func):
    @wraps(func)
    def wrapped(self, dst, _):
        func(self, dst)
        return True
    return wrapped

def two_argument_conditional(func):
    @wraps(func)
    def wrapped(self, src1, src2, modes):
        a = self.read_value(src1, modes, 0)
        b = self.read_value(src2, modes, 1)
        return func(self, a, b)
    return wrapped

def one_argument_read(func):
    @wraps(func)
    def wrapped(self, src, modes):
        a = self.read_value(src, modes, 0)
        func(self, a)
        return True
    return wrapped

class Computer:
    def __init__(self, memory, input_queue, output_queue, verbose=False):
        self.memory = defaultdict(lambda: 0, {i: val for i, val in enumerate(memory)})
        self.pc = 0
        self.output_log = []
        self.verbose = verbose
        self.input_queue = input_queue
        self.output_queue = output_queue
        self.relative_base = 0

    def operations(self, opcode):
        ops = {
            1: self.add,
            2: self.mul,
            3: self.get_input,
            4: self.write_output,
            5: self.jump_if_true,
            6: self.jump_if_false,
            7: self.less_than,
            8: self.equals,
            9: self.adjust_relative_base
        }
        return ops[opcode]

    parameter_counts = { 1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3, 9: 1 }

    def run(self):
        while self.memory[self.pc] != 99:
            instruction = str(self.memory[self.pc])
            opcode = int(instruction[-2:])
            modes = [int(c) for c in instruction[:-2]] 
            parameters = [self.memory[self.pc + i] for i in range(1, self.parameter_counts[opcode] + 1)]
            update_pc = self.operations(opcode)(*parameters, modes)
    
            if (update_pc):
                self.pc = self.pc + self.parameter_counts[opcode] + 1

    def read_value(self, src, modes, i):
        return self.memory[src] if mode(modes, i) == 0 else src

    @two_argument_assignment
    def add(self, a, b, dst):
        self.memory[dst] = a + b

    @two_argument_assignment
    def mul(self, a, b, dst):
        self.memory[dst] = a * b

    @two_argument_assignment
    def equals(self, a, b, dst):
        self.memory[dst] = 1 if a == b else 0

    @two_argument_assignment
    def less_than(self, a, b, dst):
        self.memory[dst] = 1 if a < b else 0

    @zero_argument_assignment
    def get_input(self, dst):
        self.memory[dst] = self.input_queue.get()

    @one_argument_read
    def write_output(self, a):
        if(self.verbose):
            print(a)
        self.output_queue.put(a)
        self.output_log.append(a)

    @two_argument_conditional
    def jump_if_true(self, a, b):
        if a != 0:
            self.pc = b
            return False
        return True

    @two_argument_conditional
    def jump_if_false(self, a, b):
        if a == 0:
            self.pc = b
            return False
        return True

    @one_argument_read
    def adjust_relative_base(self, a):
        self.relative_base = a
