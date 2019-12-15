from aocutil import read_lines
from functools import reduce
from itertools import combinations
import re

class Planet:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def __repr__(self):
        return "pos=<x={}, y={}, z={}> vel=<x={}, y={}, z={}>".format(*self.position, *self.velocity)

    def energy(self):
        pot = reduce(lambda a, b: a + abs(b), self.position, 0)
        kin = reduce(lambda a, b: a + abs(b), self.velocity, 0)
        return pot * kin

    def step(self):
        self.position = [p + v for (p, v) in zip(self.position, self.velocity)]

def sign(a):
    if a > 0:
        return 1
    if a < 0:
        return -1
    return 0

planets = []
for line in read_lines("input12.txt"):
    position = list(map(int, re.findall(r'-*\d+', line)))
    planets.append(Planet(position, [0, 0, 0]))

for i in range(1000):
    for p1, p2 in combinations(planets, 2):
        gravity = [sign(v1 - v2) for (v1, v2) in zip(p1.position, p2.position)]
        for i in range(3):
            p2.velocity[i] += gravity[i]
            p1.velocity[i] -= gravity[i]

    for p in planets:
        p.step()

print(reduce(lambda a, b: a + b.energy(), planets, 0))