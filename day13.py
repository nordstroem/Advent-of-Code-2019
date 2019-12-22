from aocutil import read_file
from computer import Computer
from queue import Queue
from threading import Thread
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt
import time

def draw_screen(screen, score):
    symbols = {
        0: " ",
        1: "|",
        2: "#",
        3: "#",
        4: "o"
    }
    max_x = max(screen.keys(), key=lambda x: x[0])[0]
    max_y = max(screen.keys(), key=lambda x: x[1])[1]
    for y in range(max_y + 1):
        line = ""
        for x in range(max_x + 1):
            line += symbols[screen[x, y]]
        print(line)
    print("----------------------------------------")
    print("Score: " + str(score))

memory = [int(x) for x in read_file("input13.txt").split(',')]
memory[0] = 2

input_queue = Queue()
output_queue = Queue()

C = Computer(memory, input_queue, output_queue, verbose=False)
thread = Thread(target=C.run)
thread.daemon = True
thread.start()
screen = defaultdict(int)
scores = []
score = 0

added_inputs = []
while C.is_running:
    if output_queue.empty():
        input_queue.put(1)
    else:
        x, y, block = [output_queue.get() for _ in range(3)]
        if x == -1 and y == 0:
            score = block
            scores.append(score)
            print(score)
        else:
            screen[x, y] = block
    #draw_screen(screen, score)

print(score)

# Part 2 solution: Put self.memory[392] = self.memory[388] in each iteration in computer.
