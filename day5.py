from aocutil import *
from operator import *
import itertools

operations = {
    1: add,
    2: mul
}

memory = [int(x) for x in read_file("input2.txt").split(',')]

pc = 0
while memory[pc] != 99:
    opcode = memory[pc]
    src1 = memory[pc + 1]
    src2 = memory[pc + 2]
    dst = memory[pc + 3] 
    memory[dst] = operations[opcode](memory[src1], memory[src2])
    pc = pc + 4


print(memory[0])