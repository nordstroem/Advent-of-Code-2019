from aocutil import read_file
from computer import Computer
from queue import Queue 
from threading import Thread
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt

memory = [int(x) for x in read_file("input11.txt").split(',')]
input_queue = Queue()
output_queue = Queue()

C = Computer(memory, input_queue, output_queue, verbose=False)

input_queue.put(1)
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

tiles = defaultdict(int, {(0, 0): 1})
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

(minx, maxx) = (min(x for (x, y) in tiles.keys()), max(x for (x, y) in tiles.keys()))
(miny, maxy) = (min(y for (x, y) in tiles.keys()), max(y for (x, y) in tiles.keys()))

img = np.zeros(((maxy - miny) + 1, (maxx - minx) + 1))

for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        img[img.shape[0]-y-1, x] = tiles[((minx + x), (miny + y))]

plt.imshow(img)
plt.show()
