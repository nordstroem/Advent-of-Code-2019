from aocutil import *
import itertools

total_number = 0

for num in range(273025, 767253 + 1):
    digits = [int(c) for c in str(num)]

    never_decreasing = digits == sorted(digits)
    groups = [list(g) for k, g in itertools.groupby(digits)]
    two_adjacent = any(len(dgs) == 2 for dgs in groups)
    
    if never_decreasing and two_adjacent:
        total_number = total_number + 1

print(total_number)