from aocutil import read_file
from computer import Computer
from queue import Queue
from threading import Thread
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt
import time
import random
import time
import json
import copy

memory = [int(x) for x in read_file("input15.txt").split(',')]

input_queue = Queue()
output_queue = Queue()

C = Computer(memory, input_queue, output_queue)
thread = Thread(target=C.run)
thread.daemon = True
thread.start()

visited = {}
unvisited = {}
distances = defaultdict(lambda: float("Inf"))
distances[0, 0] = 0
all_neighbors = {}
current_node = (0, 0)
last_status = -1
prev = {}
reverse_keys = {1: 2, 2: 1, 3: 4, 4: 3}
deltas = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}
key_path = []    

def goto_unvisited():
    next_node = None
    next_key = None
    check_node = current_node
    while not next_node:
        unvisited_neighbors = [nb for nb in all_neighbors[check_node] if nb[1] not in visited]
        if unvisited_neighbors:
            # If we have an unvisited neighbor, go to that one.
            next_key, next_node = min(unvisited_neighbors, key=lambda nb: distances[nb])
        else:
            # Otherwise, backtrack our taken path and search for an unvisited neighbor.
            if not key_path:
                return None
            reverse_key = reverse_keys[key_path.pop()]
            input_queue.put(reverse_key)
            new_status = output_queue.get()
            assert new_status != 0
            delta = deltas[reverse_key]
            check_node = (check_node[0] + delta[0], check_node[1] + delta[1])

    input_queue.put(next_key)
    new_status = output_queue.get()
    assert new_status != 0
    key_path.append(next_key)
    return next_node

grid = {"(0, 0)": 0}
while True:
    # Find the neighbors of this node
    neighbors = []
    itms = list(deltas.items())
    random.shuffle(itms)
    for key, delta in itms:
        input_queue.put(key)
        last_status = output_queue.get()
        ng_node = (current_node[0] + delta[0], current_node[1] + delta[1])
        if last_status == 0:
            grid[str(ng_node)] = 1
        elif last_status == 1:
            grid[str(ng_node)] = 0
        else:
            print(distances[current_node] + 1)
            grid[str(ng_node)] = 2

        if last_status != 0:
            neighbors.append((key, ng_node))
            input_queue.put(reverse_keys[key])
            le = output_queue.get()
        
    all_neighbors[current_node] = neighbors

    for key, n in neighbors:
        new_distance = distances[current_node] + 1
        if new_distance < distances[n]:
            distances[n] = new_distance
            prev[n] = current_node

    visited[current_node] = True

    current_node = goto_unvisited()
    if not current_node:
        break


'''with open('day14_map.json', 'w') as fp:
    json.dump(grid, fp)


grid = {}
with open('day14_map.json', 'r') as fp:
    grid = json.load(fp)
'''

### Part 2
def str_to_int_tuple(key):
    a, b = tuple(key.replace('(','').replace(')','').replace(' ', '').split(','))
    return int(a), int(b)

grid = {str_to_int_tuple(key): item for key, item in grid.items()}
has_updated = True
iterations = 0
deltas = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}
while has_updated:
    updated_grid = copy.copy(grid)
    has_updated = False
    for node, key in grid.items():
        if key == 2:
            for delta in deltas.values():
                ng_node = (node[0] + delta[0], node[1] + delta[1])
                if grid[ng_node] == 0:
                    updated_grid[ng_node] = 2
                    has_updated = True
    
    grid = updated_grid
    iterations += 1

print(iterations - 1)
