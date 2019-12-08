from aocutil import read_file
from computer import Computer

initial_memory = [int(x) for x in read_file("input5.txt").split(',')]
a = Computer(initial_memory, [])
a.run()

assert(a.memory[0] == 1210687)