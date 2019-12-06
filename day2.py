from aocutil import *
from operator import *
import itertools

operations = {
    1: add,
    2: mul
}

initial_memory = [int(x) for x in read_file("input2.txt").split(',')]

for tup in itertools.product(range(1, 99), range(1, 99)):
    memory = initial_memory.copy()
    memory[1] = tup[0]
    memory[2] = tup[1]

    index = 0
    while memory[index] != 99:
        opcode = memory[index]
        src1 = memory[index + 1]
        src2 = memory[index + 2]
        dst = memory[index + 3] 
        memory[dst] = operations[opcode](memory[src1], memory[src2])
        index = index + 4

    if memory[0] == 19690720:
        print(100 * tup[0] + tup[1]) 
        break
        