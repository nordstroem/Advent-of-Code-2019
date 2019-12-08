from aocutil import *
from computer import *

initial_memory = [int(x) for x in read_file("input5.txt").split(',')]

a = Computer(initial_memory, [])

a.run()

#print(a.memory[0])