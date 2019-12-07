from aocutil import *
import itertools

memory = [int(x) for x in read_file("input5.txt").split(',')]
mode_or_zero = lambda i: modes[-(i + 1)] if i < len(modes) else 0

def add(src1, src2, dst, modes):
    a = memory[src1] if mode_or_zero(0) == 0 else src1
    b = memory[src2] if mode_or_zero(1) == 0 else src2
    memory[dst] = a + b

def mul(src1, src2, dst, modes):
    a = memory[src1] if mode_or_zero(0) == 0 else src1
    b = memory[src2] if mode_or_zero(1) == 0 else src2
    memory[dst] = a * b

def get_input(src, _=None):
    memory[src] = int(input("Enter input value: "))

def write_output(src, modes):
    value = memory[src] if mode_or_zero(0) == 0 else src
    print(value)

operations = {
    1: add,
    2: mul,
    3: get_input,
    4: write_output
}

parameter_counts = {
    1: 3,
    2: 3,
    3: 1,
    4: 1
}

pc = 0
while memory[pc] != 99:
    instruction = str(memory[pc])
    opcode = int(instruction[-2:])
    modes = [int(c) for c in instruction[:-2]] 
    parameters = [memory[pc + i] for i in range(1, parameter_counts[opcode] + 1)]
    operations[opcode](*parameters, modes)
    pc = pc + parameter_counts[opcode] + 1
    