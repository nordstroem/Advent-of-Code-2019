from aocutil import read_file
from computer import Computer
from queue import Queue
from threading import Thread
from collections import defaultdict
from functools import reduce


def part1(graph):
    def intersection(x, y):
        deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        if not graph[x, y] == '#':
            return False
        for dx, dy in deltas:
            neighbor = (x + dx, y + dy)
            if neighbor not in graph or graph[neighbor] != '#':
                return False
        return True

    results = []
    for x, y in graph.keys():
        if intersection(x, y):
            results.append((x,y))

    print(reduce(lambda a, b: a + b[0] * b[1], results, 0))

def setup_graph():
    memory = [int(x) for x in read_file("input17.txt").split(',')]
    output_queue = Queue()
    C = Computer(memory, Queue(), output_queue)
    C.run()
    full_map = reduce(lambda a, b: a + chr(b), output_queue.queue, "")
    graph = {}
    for y, line in enumerate(full_map.split()):
        for x, c in enumerate(line):
            graph[x, y] = c
    return graph
    
graph = setup_graph()
part1(graph)