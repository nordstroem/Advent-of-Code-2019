from aocutil import read_file
from computer import Computer
import itertools

memory = [int(x) for x in read_file("input7.txt").split(',')]

max_value = 0
for (a, b, c, d, e) in itertools.permutations([0, 1, 2, 3, 4]):
    A = Computer(memory.copy(), [a, 0])
    A.run()
    B = Computer(memory.copy(), [b, A.output_log[0]])
    B.run()
    C = Computer(memory.copy(), [c, B.output_log[0]])
    C.run()
    D = Computer(memory.copy(), [d, C.output_log[0]])
    D.run()
    E = Computer(memory.copy(), [e, D.output_log[0]])
    E.run()
    max_value = max(E.output_log[0], max_value)

print(max_value)