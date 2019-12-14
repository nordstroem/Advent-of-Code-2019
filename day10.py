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
        k = gcd(delta[0], delta[1])
        minimum_delta = delta // k
        visible = True
        for i in range(1, k):
            ind2 = ind + i * minimum_delta
            if asteroid_map[ind2[0], ind2[1]]:
                visible = False
                break
        if visible:
            count += 1
    return count

best = 0
for ind in np.argwhere(asteroid_map):
    best = max(best, visible_count(ind))

print(best)