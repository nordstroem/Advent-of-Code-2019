from aocutil import read_file
import numpy as np
from math import gcd

lines = read_file('input10.txt').replace('\n', '').replace('#', '1').replace('.', '0')
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
    return count

best = max(visible_count(ind) for ind in np.argwhere(asteroid_map))

print(best)