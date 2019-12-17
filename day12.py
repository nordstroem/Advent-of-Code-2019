from aocutil import read_lines
from functools import reduce
from itertools import combinations
import re
import numpy as np
import math


class Planet:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def __repr__(self):
        return "pos=<x={}, y={}, z={}> vel=<x={}, y={}, z={}>".format(*self.position, *self.velocity)

    def energy(self):
        return np.sum(np.abs(self.position)) * np.sum(np.abs(self.velocity))

planets = [Planet(np.fromiter(re.findall(r'-*\d+', line), int), np.zeros(3, int)) for line in read_lines("input12.txt")]

get_hash = lambda i: tuple(reduce(lambda a, b: a + [b.position[i], b.velocity[i]], planets, []))
seen = [{}, {}, {}]
result = [0, 0, 0]
for i in range(1000000000):

    for j in range(3):
        hsh = get_hash(j)
        if hsh in seen[j] and not result[j]:
            result[j] = i
        else:
            seen[j][hsh] = i

    if all(result):
        break

    for p1, p2 in combinations(planets, 2):
        gravity = np.sign(p2.position - p1.position)
        p1.velocity += gravity
        p2.velocity -= gravity

    for p in planets:
        p.position += p.velocity

gcd1 = math.gcd(result[0], result[1])
val1 = result[0] * result[1] // gcd1
gcd2 = math.gcd(val1, result[2])
print(val1 * result[2] // gcd2)

#print(reduce(lambda a, b: a + b.energy(), planets, 0))