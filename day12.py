#from aocutil import read_lines
from functools import reduce
from itertools import combinations
import re
import numpy as np
<<<<<<< HEAD
import math
=======
import time
>>>>>>> Day 13 part1 working.

def read_lines(path, fun=lambda x: x):
    with open(path,'r') as inp:
        lines = inp.readlines()
        return [fun(l.strip()) for l in lines]

class Planet:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def __repr__(self):
        return "pos=<x={}, y={}, z={}> vel=<x={}, y={}, z={}>".format(*self.position, *self.velocity)

    def energy(self):
        return np.sum(np.abs(self.position)) * np.sum(np.abs(self.velocity))

planets = [Planet(np.fromiter(re.findall(r'-?\d+', line), int), np.zeros(3, int)) for line in read_lines("input12.txt")]

get_hash = lambda i: tuple(reduce(lambda a, b: a + [b.position[i], b.velocity[i]], planets, []))
seen = [{}, {}, {}]
result = [0, 0, 0]
steps = 0
while not all(result):
    for j in range(3):
        hsh = get_hash(j)
        if hsh in seen[j] and not result[j]:
            result[j] = steps
        else:
            seen[j][hsh] = steps

<<<<<<< HEAD
    for p1, p2 in combinations(planets, 2):
=======
get_hash = lambda: tuple(reduce(lambda a, b: a + list(b.position) + list(b.velocity), planets, []))
'''hsh = (planets[0].position[0], planets[0].position[1], planets[0].position[2], \
       planets[0].velocity[0], planets[0].velocity[1], planets[0].velocity[2], \
       planets[1].position[0], planets[1].position[1], planets[1].position[2], \
       planets[1].velocity[0], planets[1].velocity[1], planets[1].velocity[2], \
       planets[2].position[0], planets[2].position[1], planets[2].position[2], \
       planets[2].velocity[0], planets[2].velocity[1], planets[2].velocity[2], \
       planets[3].position[0], planets[3].position[1], planets[3].position[2], \
       planets[3].velocity[0], planets[3].velocity[1], planets[3].velocity[2])
'''
seen = {get_hash(): True}

pairs = combinations(planets, 2)
times = []

#positions = np.zeros(4, 3)
#velocities = np.zeros(4, 3)

#for r, c in np.ndindex(positions.shape):
  #  positions[r, c] = planets[r].position[c]

i = 0
while 1:
    for p1, p2 in pairs:
>>>>>>> Day 13 part1 working.
        gravity = np.sign(p2.position - p1.position)
        p1.velocity += gravity
        p2.velocity -= gravity

    for p in planets:
        p.position += p.velocity

<<<<<<< HEAD
    steps += 1
lcm = lambda *args: reduce(lambda a, b: a * b // math.gcd(a, b), *args)
print(lcm(result))

#print(reduce(lambda a, b: a + b.energy(), planets, 0))
=======
    if get_hash() in seen:
        print(i + 1)
    else:
        seen[get_hash()] = True
    i += 1

#print(np.mean(times) * 1000)
#print(reduce(lambda a, b: a + b.energy(), planets, 0))
>>>>>>> Day 13 part1 working.
