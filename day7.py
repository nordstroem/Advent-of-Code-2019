from aocutil import read_file
from computer import Computer
import itertools
from queue import Queue 
from threading import Thread 

memory = [int(x) for x in read_file("input7.txt").split(',')]

max_value = 0
for (a, b, c, d, e) in itertools.permutations([5, 6, 7, 8, 9]):
    EA_queue = Queue()
    AB_queue = Queue()
    BC_queue = Queue()
    CD_queue = Queue()
    DE_queue = Queue()

    EA_queue.put(a)
    EA_queue.put(0)
    AB_queue.put(b)
    BC_queue.put(c)
    CD_queue.put(d)
    DE_queue.put(e)

    A = Computer(memory.copy(), EA_queue, AB_queue)
    B = Computer(memory.copy(), AB_queue, BC_queue)
    C = Computer(memory.copy(), BC_queue, CD_queue)
    D = Computer(memory.copy(), CD_queue, DE_queue)
    E = Computer(memory.copy(), DE_queue, EA_queue)

    threads = [Thread(target=A.run), Thread(target=B.run), Thread(target=C.run), Thread(target=D.run), Thread(target=E.run)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    max_value = max(max_value, EA_queue.get())

print(max_value)


