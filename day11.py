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
C = Computer(memory, input_queue, output_queue)
thread = Thread(target=C.run)
thread.start()

position = 0 + 0j
direction =  0 - 1j

tiles = defaultdict(int, {position: 1})
input_queue.put(1)
while C.is_running:
    new_color = output_queue.get()
    turn = output_queue.get()
    direction = direction * (1j if turn else -1j)
    tiles[position] = new_color
    position += direction
    input_queue.put(tiles[position])

thread.join()

(min_x, max_x) = (min(v.real for v in tiles.keys()), max(v.real for v in tiles.keys()))
(min_y, max_y) = (min(v.imag for v in tiles.keys()), max(v.imag for v in tiles.keys()))
img = np.zeros((int(max_y - min_y) + 1, int(max_x - min_x) + 1))
for y, x in np.ndindex(img.shape):
    img[y, x] = tiles[((min_x + x) + (min_y + y)*1j)]

plt.imshow(img)
plt.show()
