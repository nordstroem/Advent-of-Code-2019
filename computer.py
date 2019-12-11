import itertools
from functools import wraps
from collections import deque, defaultdict
from inspect import getfullargspec

def two_argument_assignment(func):
    @wraps(func)
    def wrapped(self, src1, src2, dst, mode1=0, mode2=0, mode3=0):
        a = self.read_value(src1, mode1)
        b = self.read_value(src2, mode2)
        c = self.read_address(dst, mode3)
        func(self, a, b, c)
        self.pc += 4
    return wrapped

def zero_argument_assignment(func):
    @wraps(func)
    def wrapped(self, dst, mode=0):
        a = self.read_address(dst, mode)
        func(self, a)
        self.pc += 2
    return wrapped

def two_argument_jump_conditional(func):
    @wraps(func)
    def wrapped(self, src1, src2, mode1=0, mode2=0):
        a = self.read_value(src1, mode1)
        b = self.read_value(src2, mode2)
        self.pc = b if func(self, a) else self.pc + 3
    return wrapped

def one_argument_read(func):
    @wraps(func)
    def wrapped(self, src, mode=0):
        a = self.read_value(src, mode)
        func(self, a)
        self.pc += 2
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

    def run(self):
        while self.memory[self.pc] != 99:
            instruction = str(self.memory[self.pc])
            opcode = int(instruction[-2:])
            modes = [int(c) for c in instruction[-3::-1]] 
            operation = self.operations(opcode)
            num_parameters = len(getfullargspec(operation).args) - len(getfullargspec(operation).defaults) 
            parameters = [self.memory[self.pc + i] for i in range(1, num_parameters)]
            operation(*parameters, *modes)

    def read_value(self, src, mode):
        values = {0: self.memory[src], 1: src, 2: self.memory[self.relative_base + src]}
        return values[mode]

    def read_address(self, dst, mode):
        return dst if mode == 0 else self.relative_base + dst

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
        if (self.verbose):
            print(a)
        self.output_queue.put(a)
        self.output_log.append(a)

    @two_argument_jump_conditional
    def jump_if_true(self, a):
        return a != 0

    @two_argument_jump_conditional
    def jump_if_false(self, a):
        return a == 0

    @one_argument_read
    def adjust_relative_base(self, a):
        self.relative_base += a
