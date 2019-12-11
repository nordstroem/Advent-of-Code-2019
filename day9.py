from aocutil import read_file
from computer import Computer
from queue import Queue 


memory = [int(x) for x in read_file("input9.txt").split(',')]
input_queue = Queue()
output_queue = Queue()
input_queue.put(1)

C = Computer(memory.copy(), input_queue, output_queue, verbose=True)
C.run()