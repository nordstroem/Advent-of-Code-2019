from aocutil import read_file
from computer import Computer

memory = [int(x) for x in read_file("input5.txt").split(',')]
a = Computer(memory, [1, 2, 3])
a.run()
