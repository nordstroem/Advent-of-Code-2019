from aocutil import read_file
from computer import Computer
from queue import Queue 

memory = [int(x) for x in read_file("input13.txt").split(',')]

input_queue = Queue()
output_queue = Queue()
C = Computer(memory, input_queue, output_queue)
C.run()

commands = list(output_queue.queue)

assert len(commands) % 3 == 0

screen = {}
for i in range(len(commands) // 3):
    x, y, block = commands[3*i:3*(i + 1)]
    screen[(x, y)] = block

print(list(screen.values()).count(2))
