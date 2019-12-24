from aocutil import read_lines
import re
import math
from collections import defaultdict
import time

reactions = {}

for line in read_lines("input14.txt"):
    group = [(int(f), name) for (f, name) in map(lambda l: tuple(l.strip().split()), re.split(r'=>|,', line))]
    result = group[-1][1]
    units = group[-1][0]
    reactions[result] = (units, group[:-1])

def minimum_ore(waste, chemical, units):
    if chemical == "ORE":
        return units

    needed = units - waste[chemical]
    minimum_produced, inputs = reactions[chemical]
    n = math.ceil(max(0, needed) / minimum_produced)
    waste[chemical] = n * minimum_produced - needed
    
    ore = 0
    for amount, input_chemical in inputs:
        ore += minimum_ore(waste, input_chemical, n * amount)

    return ore

# Inverse problem.
#print(minimum_ore("FUEL", 333333333333))

lower_bound = 0
upper_bound = 1000000000000
current_fuel = (upper_bound + lower_bound) // 2
current_ore = 0

i = 0
while lower_bound < upper_bound:
    current_ore = minimum_ore(defaultdict(int), "FUEL", current_fuel)
    if (current_ore < 1000000000000):
        lower_bound = current_fuel + 1
    else:
        upper_bound = current_fuel - 1
    current_fuel = (upper_bound + lower_bound) // 2

print(current_fuel)