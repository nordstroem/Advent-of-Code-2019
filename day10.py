from aocutil import read_file
import numpy as np
from math import gcd
from collections import defaultdict
from math import atan2

lines = read_file('input10.txt').replace('\n', '').replace('#', '1').replace('.', '0').replace('X', '1')
asteroid_map = np.fromiter(lines, int).reshape(34, 34)

def visible_count(tar_index):
    count = 0
    for ind in np.argwhere(asteroid_map):
        if np.array_equal(ind, tar_index):
            continue
        delta = tar_index - ind
        k = gcd(*delta)
        minimum_delta = delta // k
        test_indices = [ind + i * minimum_delta for i in range(1, k)]
        if not any(asteroid_map[x, y] for (x, y) in test_indices):
            count += 1

    if count == 292:
        print(tar_index)
    return count

# Part 1 
#best = max(visible_count(ind) for ind in np.argwhere(asteroid_map))
# print(best)

# Part 2
def minimum_deltas(tar_index):
    deltas = defaultdict(list)
    for ind in np.argwhere(asteroid_map):
        if np.array_equal(ind, tar_index):
            continue
        delta = tar_index - ind
        k = gcd(*delta)
        angle = (-atan2(delta[1], delta[0])) % (2 * np.pi)
        deltas[angle * 180 / (np.pi)].append((k, ind))
    return deltas

for delta, value in minimum_deltas([20, 20]).items():
    value.sort()

as_list = list(minimum_deltas([20, 20]).items())
as_list.sort()

num_popped = 0
for i in range(300):
    for key, value in as_list:
        if value:
            removed = value.pop()[1]
            num_popped += 1
            if (num_popped == 200):
                print(removed[1] * 100 + removed[0])