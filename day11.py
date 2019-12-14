from aocutil import read_file
from computer import Computer
from queue import Queue 
from threading import Thread
from collections import defaultdict

memory = [int(x) for x in read_file("input11.txt").split(',')]
input_queue = Queue()
output_queue = Queue()

C = Computer(memory, input_queue, output_queue, verbose=False)

input_queue.put(0)
thread = Thread(target=C.run)
thread.start()

position = (0, 0)
direction = 0

def get_new_position(position, direction):
    (x, y) = position
    if direction == 0:
        return (x, y + 1)
    if direction == 1:
        return (x + 1, y)
    if direction == 2:
        return (x, y - 1)
    return (x - 1, y)

tiles = defaultdict(int)
while True:
    try:
        new_color = output_queue.get(timeout=1)
        turn = output_queue.get(timeout=1)
        direction = (direction + (1 if turn else -1)) % 4
        tiles[position] = new_color
        position = get_new_position(position, direction)
        input_queue.put(tiles[position])
    except: 
        break

thread.join()

print(len(tiles))