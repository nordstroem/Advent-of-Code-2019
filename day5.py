from aocutil import *
import itertools

memory = [int(x) for x in read_file("input5.txt").split(',')]
pc = 0
mode_or_zero = lambda i: modes[-(i + 1)] if i < len(modes) else 0

def add(src1, src2, dst, modes):
    a = memory[src1] if mode_or_zero(0) == 0 else src1
    b = memory[src2] if mode_or_zero(1) == 0 else src2
    memory[dst] = a + b
    return True

def mul(src1, src2, dst, modes):
    a = memory[src1] if mode_or_zero(0) == 0 else src1
    b = memory[src2] if mode_or_zero(1) == 0 else src2
    memory[dst] = a * b
    return True

def get_input(src, _):
    memory[src] = int(input("Enter input value: "))
    return True

def write_output(src, modes):
    value = memory[src] if mode_or_zero(0) == 0 else src
    print(value)
    return True

def equals(src1, src2, dst, modes):
    a = memory[src1] if mode_or_zero(0) == 0 else src1
    b = memory[src2] if mode_or_zero(1) == 0 else src2
    memory[dst] = 1 if a == b else 0
    return True

def less_than(src1, src2, dst, modes):
    a = memory[src1] if mode_or_zero(0) == 0 else src1
    b = memory[src2] if mode_or_zero(1) == 0 else src2
    memory[dst] = 1 if a < b else 0
    return True

def jump_if_true(src1, src2, modes):
    global pc
    a = memory[src1] if mode_or_zero(0) == 0 else src1
    b = memory[src2] if mode_or_zero(1) == 0 else src2
    if a != 0:
        pc = b
        return False
    return True

def jump_if_false(src1, src2, modes):
    global pc
    a = memory[src1] if mode_or_zero(0) == 0 else src1
    b = memory[src2] if mode_or_zero(1) == 0 else src2
    if a == 0:
        pc = b
        return False
    return True

operations = {
    1: add,
    2: mul,
    3: get_input,
    4: write_output,
    5: jump_if_true,
    6: jump_if_false,
    7: less_than,
    8: equals
}

parameter_counts = {
    1: 3,
    2: 3,
    3: 1,
    4: 1,
    5: 2,
    6: 2,
    7: 3,
    8: 3
}

while memory[pc] != 99:
    instruction = str(memory[pc])
    opcode = int(instruction[-2:])
    modes = [int(c) for c in instruction[:-2]] 
    parameters = [memory[pc + i] for i in range(1, parameter_counts[opcode] + 1)]
    update_pc = operations[opcode](*parameters, modes)
    
    if (update_pc):
        pc = pc + parameter_counts[opcode] + 1
